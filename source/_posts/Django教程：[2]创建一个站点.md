---
title: Django教程：[2]创建一个站点
date: 2015-01-19 18:15:17
tags: [django]
author: mlln.cn
---
上一篇文章我们安装了django，并测试成功；今天我们就要使用django创建一个站点，创建完成以后你就发现，一个最简单的网站已经制作完毕，我们接下来的任务就是在这个站点的基础上进行开发。下面是创建站点（工程）的具体方法：

- 按下快捷键win+r，打开运行窗口，输入cmd，按下回车键，打开命令窗口

{% asset_img 3792cb39b6003af3717c1819372ac65c1138b642.jpg Django教程：[2]创建一个站点 %}

- 我们将当前目录定位到你想要存放网站的目录，比如我想要放到D盘下的website文件夹中，我们输入命令：cd /d d:\website

{% asset_img 718e25c79f3df8dc612a48e8cf11728b47102871.jpg Django教程：[2]创建一个站点 %}

- 在该目录下，我们输入命令来创建站点：django-admin.py startproject djangoweb；其中最后一个参数djangoweb就是我给我的站点起的名字，该命令将在当前目录下创建一个文件夹，该文件夹命名为django；我的命令出现了错误，因为我之前已经创建好了一个站点

{% asset_img b853d6fcc3cec3fd4529600cd488d43f87942771.jpg Django教程：[2]创建一个站点 %}

- 我们可以看到这个文件夹已经创建了，我们打开文件夹看看有什么内容

{% asset_img 389aa8fd5266d016c20e5951952bd40735fa3571.jpg Django教程：[2]创建一个站点 %}

- 有一个py文件和一个文件夹，继续打开文件夹

{% asset_img 0b14ad19ebc4b745a86c706fcdfc1e178b821594.jpg Django教程：[2]创建一个站点 %}

- 在这个文件夹内有四个文件，如图所示。这么简单的几个文件实际上已经构成了一个站点，下一篇文章我们介绍如何启动服务器，让你在浏览器看到自己的站点。

{% asset_img ac0acf1373f082028785564649fbfbedab641b71.jpg Django教程：[2]创建一个站点 %}

- 下面的参考资料可能会对你学习django有用

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
