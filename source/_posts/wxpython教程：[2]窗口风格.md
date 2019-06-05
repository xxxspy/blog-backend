---
title: wxpython教程：[2]窗口风格
date: 2015-07-01 18:03:11
tags: [python,wxpython]
author: mlln.cn
---
这篇文章接着介绍wxpython.Frame，我们需要设置一下窗口的大小、位置等。下面看一下今天要写的所有代码。

- 代码的前两行就不说了，引入了相关模块并创建了一个app

{% asset_img 0d968f2397dda1440ba4fcddb1b7d0a20df486f5.jpg wxpython教程：[2]窗口风格 %}

- 接着是Frame的设置，我们先来看看style，他有很多可以设置的属性，不同的属性用竖线“|”连接，比如我们想要窗口上有最大化按钮，就设置wx.MAXIMIZE_BOX，如果想要增加最小化按钮，就写成style=wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX ，写一连串属性很麻烦，我们可以用wx.DEFAULT_FRAME_STYLE默认设置，它等于wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN
其他属性的意义我们直接从官网上看就可以，如下图：

{% asset_img 4abae5edab64034f575f5269acc379310b551d8b.jpg wxpython教程：[2]窗口风格 %}

{% asset_img 109eb7ec8a136327064f515c928fa0ec09fac784.jpg wxpython教程：[2]窗口风格 %}

- 接着我们想要设置窗口的大小，用size参数，Frame（...size=(200,250))，这样就将窗口大小设置为200长，250高。

- 使用Move方法可以设置窗口的位置，比如（它表示窗口的左上角在屏幕上的位置）

{% asset_img ac754782b2b7d0a2a66494f2c8ef76094a369af5.jpg wxpython教程：[2]窗口风格 %}

- 如果我们需要将窗口置于屏幕中央，可以使用Center方法

{% asset_img b6045da98226cffc24b82fddba014a90f703ea94.jpg wxpython教程：[2]窗口风格 %}

- 还有其他很多方法设置窗口位置，这里就不演示了：

{% asset_img 4e83cb628535e5dd279737b075c6a7efcf1b62e3.jpg wxpython教程：[2]窗口风格 %}

- 最后就不用解释了，可以看看你创建的一个窗口

{% asset_img 8bc3a7014a90f6034c220c283a12b31bb151ed94.jpg wxpython教程：[2]窗口风格 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
