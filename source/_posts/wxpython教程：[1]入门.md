---
title: wxpython教程：[1]入门
date: 2015-04-17 18:23:17
tags: [python,wxpython]
author: mlln.cn
---
我们今天来学习Python的一个界面开发包wxpython，我最近要做一些Python统计分析的软件界面，所以用到了wxpython，很久以前用过这个包，现在跟大家一起回顾一下。这篇文章是入门，讲的比较简单，以后逐渐增加新的知识。
工具/原料

方法/步骤


- 先来看一下如下代码，这是一个简单的界面，我们接下来逐句解释

{% asset_img 8326cffc1e178a82e60ceacff503738da977e8a9.jpg wxpython教程：[1]入门 %}

- 首先是两行注释，用#号打头表示注释，不执行。而coding表示编码方式，开始透明coding表示该文件使用utf8编码，因为Python文件中有中文，必须声明一个支持中文的编码

{% asset_img 203fb80e7bec54e7ebf08f71ba389b504fc26a45.jpg wxpython教程：[1]入门 %}

- 接下来实例化一个app，任何一个应用程序都是一个app

{% asset_img 3801213fb80e7bec88c6968e2c2eb9389b506b45.jpg wxpython教程：[1]入门 %}

{% asset_img 7aec54e736d12f2e66193b0f4cc2d56285356845.jpg wxpython教程：[1]入门 %}

- 这两句表示创建了一个Frame，Frame就是框架，是一个容器，内部可以包含多个容器或者其他组件，如果我们的Frame的第一个参数使用None表示它是顶层的容器，它包含了应用程序的所有组件。‘入门'表示Frame的标题，一会你就看到标题在哪里。最后，任何Frame窗口想要显示，必须用show(),但是你现在还看不到窗口，因为程序没有运行呢

- frame=wx.Frame(None,-1,u'入门')

- frame.Show()

{% asset_img 5882b2b7d0a20cf4ffed6bb075094b36acaf9964.jpg wxpython教程：[1]入门 %}

- 实际上，我们是用app.mainLoop来启动程序的

{% asset_img 37d12f2eb9389b50aee3753d8635e5dde7116e45.jpg wxpython教程：[1]入门 %}

- 这样我们就看到了一个最简单的界面了。

{% asset_img d4628535e5dde71176ced699a4efce1b9d166145.jpg wxpython教程：[1]入门 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
