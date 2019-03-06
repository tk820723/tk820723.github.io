# -*- coding: utf-8 -*-

#这个脚本用来自动化打包hexo的文章变成网页，并且push到github上面
#githubpush目录对应网页的源码

import os
import time
os.chdir('./Personal_Website_Control')
os.system('hexo cl && hexo g')
os.chdir('..')
os.system('cp -R ./Personal_Website_Control/public/* ./githubpush')
os.chdir('./githubpush')
os.system('git add .;git commit -m "Publish New Articles";git push origin master')
