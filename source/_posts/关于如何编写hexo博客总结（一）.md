---
title: 关于如何编写hexo博客总结（一）
date: 2016-06-16 15:40:33
categories:
- Hexo
tag:

---

Hexo博客也建起来一阵子了，一直没有更新过，现在回来想写点东西，突然发现已经不太记得怎么编写了，所以现在边学习边把编写博客的记录下来。

Hexo用的是markdown语法，我就先从markdown讲起，关于markdown，已经有很不错的教程，所以这里参考转载了简述上Te\_Lee的一篇简书

# Markdown语法

> Markdown 是一种轻量级的「标记语言」，它的优点很多，目前也被越来越多的写作爱好者，撰稿者广泛使用。看到这里请不要被「标记」、「语言」所迷惑，Markdown 的语法十分简单。常用的标记符号也不超过十个，这种相对于更为复杂的 HTML 标记语言来说，Markdown 可谓是十分轻量的，学习成本也不需要太多，且一旦熟悉这种语法规则，会有一劳永逸的效果。

![Ulysses For Mac][image-1]
## Markdown 语法的简要规则
## 标题
![标题][image-2]
标题是每篇文章都需要也是最常用的格式，在 Markdown 中，如果一段文字被定义为标题，只要在这段文字前加 # 号即可。

## 列表

熟悉 HTML 的同学肯定知道有序列表与无序列表的区别，在 Markdown 下，列表的显示只需要在文字前加上 - 或 \* 即可变为无序列表，有序列表则直接在文字前加1. 2. 3. 符号要和文字之间加上一个字符的空格。

![列表][image-3]

## 引用
只需要在文本前加入 `>` 这种尖括号（大于号）即可

> 这里是引用

## 图片与链接

插入链接与插入图片的语法很像，区别在一个 !号

图片为：`![](){ImgCap}{/ImgCap}`

链接为：`[]()`

这两种方法都需要图片云服务的支持，你可以使用七牛或者原博主推荐的围脖图床修复计划 与 CloudApp 的服务，生成URL地址。
小编找了很久，终于找到如何在Hexo里头使用本地图片的方法，参考下面这篇博客：在hexo 中无痛使用本地图片 作者： M-x codefalling，使用：
`![imageName](postname/image.jpg)`方法

推酷地址：http://www.tuicool.com/articles/umEBVfI

补充：使用了两种发式之后，我发现虽然使用本地图片没有上传图片的痛苦了，但是相对传输速度要比专门的图床慢很多，如果不是懒人的话，还是建议使用图床外链url的形式。

## 表格
例子如下：  
`| Tables        | Are           | Cool  |`  
`| ------------- |:-------------:| -----:|`  
`| col 3 is      | right-aligned | $1600 |`  
`| col 2 is      | centered      |   $12 |`  
`| zebra stripes | are neat      |    $1 |`  

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

## 代码

如果你是个程序猿，需要在文章里优雅的引用代码框，在 Markdown下实现也非常简单，只需要用两个 \` 把中间的代码包裹起来。图例：

![代码][image-4]

## 分割线
分割线的语法只需要三个 ｀\*｀ 号，例如：

---- 

`***`

[image-1]:	http://7xt6mv.com1.z0.glb.clouddn.com/image/posts/HexoSummarymarkdown_1_1.jpg
[image-2]:	http://7xt6mv.com1.z0.glb.clouddn.com/image/posts/HexoSummarymarkdown_1_2.jpg
[image-3]:	http://7xt6mv.com1.z0.glb.clouddn.com/image/posts/HexoSummarymarkdown_1_3.jpg
[image-4]:	http://7xt6mv.com1.z0.glb.clouddn.com/image/posts/HexoSummarymarkdown_1_4.jpg