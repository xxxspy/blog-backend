---
title: SPSS python教程：[5]SpssClient简介
date: 2015-10-03 18:19:05
tags: [python,spss]
author: mlln.cn
---
SpssClient是用python实现spss操作的必定要引入的一个模块，我们今天就来看一下该模块下有哪些子模块，然后简单说一下我们按照什么顺序来写这一系列教程，重点讲什么，看看你自己是否需要看这篇教程。

- 先来看看SpssClient模块下有哪些类我们可以在python中使用。主要的大类有五个：DataDocList，SyntaxDocsList，OutputDocsList，SpssServerConfList，SpssScriptContext，我们下面分别介绍这五个类别

{% asset_img 4651a712c8fcc3ce50afebab9045d688d53f20ff.jpg SPSS python教程：[5]SpssClient简介 %}

- DataDocList，就是spss的数据文件列表。用它来读取、修改、操作数据，数据文件的后缀名是sav

{% asset_img 509b9fcb39dbb6fdf1a3c8be0b24ab18962b376a.jpg SPSS python教程：[5]SpssClient简介 %}

- SyntaxDocsList，就是spss的syntax文件列表，里面都是syntax代码，或者可能掺杂有python代码，它用于读取、修改、操作syntax代码，syntax文件的后缀名是sps

{% asset_img 0ef2112442a7d9337976c9ebaf4bd11372f00108.jpg SPSS python教程：[5]SpssClient简介 %}

- OutputDocsList，就是spss的统计结果输出文件列表，里面存放着spss的统计结果，我们可以在python中使用该类来修改、操作结果数据，结果输出文件的后缀名比较熟悉，就是spv

{% asset_img d0526df082025aaf1cec5353f9edab64024f1a08.jpg SPSS python教程：[5]SpssClient简介 %}

- SpssServerConfList，该类用于spssserver，由于在我的工作中并没有用到过spss服务器，所以我的教程里不包括spssserver的相关内容

- SpssScriptContext，该类用于返回脚本文件的环境，现在还不涉及，以后用可能用到，但不是现在。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
