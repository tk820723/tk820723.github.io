---
title: mac下还原pvr与plist为多个png
date: 2016-04-20 17:06:34
categories:
- cocos2dx
tags:
---
{% img png http://7xt6mv.com2.z0.glb.clouddn.com/png_004.png 1000%}

在网上找了很久，如何把很多网上下载的ipa包中扣出的图片资源（通常为pvr与plist结合格式）还原为png，只找到了一些python写的代码，但是mac下跑不起来，一直没有找到很好的自动化方法，就自己写了一个mac软件，帮助处理自动化切图。需要自己传入相应的png大图路径，plist文件路径，以及输出目录路径

{% codeblock 控制器代码 lang:objc %}

@interface ViewController ()
@property (weak) IBOutlet NSTextField *pngPathField;
@property (weak) IBOutlet NSTextField *plistPathField;
@property (weak) IBOutlet NSTextField *targetPathField;


@end

@implementation ViewController

- (void)viewDidLoad {
[super viewDidLoad];

}
- (IBAction)BtnClicked:(NSButton *)sender {
if (_pngPathField.stringValue.length == 0 || _plistPathField.stringValue.length == 0 || _targetPathField.stringValue.length == 0) {
NSLog(@"输入路径不能为空");
return;
}
//读取所有的文件，转换为数据数组
NSString *pngPath = _pngPathField.stringValue;
NSString *plistPath = _plistPathField.stringValue;
NSString *targetPath = _targetPathField.stringValue;

NSDictionary *plistDic = [NSDictionary dictionaryWithContentsOfFile:plistPath];
NSDictionary *framesDic = [plistDic valueForKey:@"frames"];
NSArray *framesArray = framesDic.allValues;
NSArray *namesArray = framesDic.allKeys;

if (framesArray.count==0||namesArray.count==0) {
NSLog(@"字典文件没有对象");
return;
}
//遍历数组转换plist数据
for (int i = 0; i< namesArray.count; i++) {
NSString *picName = namesArray[i];
NSDictionary *singleImageFrameDic = framesArray[i];
BOOL rotated = [[singleImageFrameDic objectForKey:@"rotated"] boolValue];
NSRect frame = NSRectFromString([singleImageFrameDic valueForKey:@"frame"]);
if (rotated) {
frame = NSMakeRect(frame.origin.x, frame.origin.y, frame.size.height, frame.size.width);
}else{
frame = NSMakeRect(frame.origin.x, frame.origin.y, frame.size.width, frame.size.height);
}

NSImage *image = [[NSImage alloc] initWithContentsOfFile:pngPath];
CGImageRef cutImageRef = [self cutImage:image frame:frame];
[self WriteImageRefToFile:cutImageRef path:targetPath withImageName:picName];
}

NSLog(@"输入图片成功");
}
//根据数据切割图片，返回切割完的图片ref
- (CGImageRef)cutImage: (NSImage *)image frame: (NSRect)frame{

CGImageSourceRef source = CGImageSourceCreateWithData((CFDataRef)[image TIFFRepresentation], NULL);
CGImageRef maskRef =  CGImageSourceCreateImageAtIndex(source, 0, NULL);
CGImageRef finalImgRef = CGImageCreateWithImageInRect(maskRef, frame);

return finalImgRef;
}
//把图片输出到选择的目录
- (void)WriteImageRefToFile: (CGImageRef) image path: (NSString *)path withImageName: (NSString *)imageName
{
NSString *desPath = [NSString stringWithFormat:@"%@/%@",path,imageName];

CFURLRef url = (__bridge CFURLRef)[NSURL fileURLWithPath:desPath];

CGImageDestinationRef destination = CGImageDestinationCreateWithURL(url, kUTTypePNG, 1, NULL);

CGImageDestinationAddImage(destination, image, nil);

if (!CGImageDestinationFinalize(destination)) {
NSLog(@"Failed to write image to %@", path);
}
CFRelease(destination);
}

- (void)setRepresentedObject:(id)representedObject {
[super setRepresentedObject:representedObject];

// Update the view, if already loaded.
}

@end
{% endcodeblock %}