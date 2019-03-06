---
title: hexo deploy 部署github缓慢解决方法
date: 2016-04-20 16:46:16
categories:
- Hexo
tags:
- Hexo deploy
---
{% img png http://7xt6mv.com2.z0.glb.clouddn.com/png_002.png 1000 %}

不知道出于什么原因，使用hexo deploy部署到github会非常缓慢，有时候一个小时都没反应。查询了一大堆资源都没有找到解决方法，后来结合github部署个人网站原理，其实更改的最主要就是index.html这个静态网页。所以尝试手动push到github，这样部署过程就快很多了。
步骤如下：
    ＊ 新建一个文件夹，cd到这个目录，使用git init初始化git然后git remote add origin <https://github.com/你的用户名/你的用户名.github.io> 给这个目录连接到你的网页
    ＊ git pull origin master 拉下当前目录
    ＊ 然后把hexo在你本地网页目录下生成的public所有东西替换进新建的这个文件夹
    ＊ 然后push一下这个文件夹，整个部署就完成了