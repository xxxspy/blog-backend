---
title: wxpython教程：[3]菜单栏
date: 2016-09-11 18:03:03
tags: [python,wxpython]
author: mlln.cn
---
窗口中通常有菜单栏，菜单栏中包括很多菜单，每一个菜单中包括很多选项，比如一个简单的记事本：里面菜单有：文件、编辑、格式等等。下面我们就来亲手制作一个菜单栏——以便让我们退出程序。

- 先看一下我们所有的代码

{% asset_img 9319cf09b3de9c82072a7ce06f81800a18d843d7.jpg wxpython教程：[3]菜单栏 %}

- 重点要说的首先是这句：创建菜单栏
这就是菜单栏：

{% asset_img 9dc3cf58ccbf6c815978a987bf3eb13532fa40d7.jpg wxpython教程：[3]菜单栏 %}

{% asset_img a75fb6d3fd1f413474788011261f95cad0c85ed7.jpg wxpython教程：[3]菜单栏 %}

- 创建一个菜单
这是一个菜单：

{% asset_img dbf554ed2e738bd4f348375ea28b87d6277ff931.jpg wxpython教程：[3]菜单栏 %}

{% asset_img 948bcfc8a786c917954cd756ca3d70cf3ac757d7.jpg wxpython教程：[3]菜单栏 %}

- 向菜单中添加一个选项：
也就是这个选项：

{% asset_img 1e71f724b899a901005cde591e950a7b0208f531.jpg wxpython教程：[3]菜单栏 %}

{% asset_img 72ccb7773912b31b880548468518367adab4e131.jpg wxpython教程：[3]菜单栏 %}

- 现在我们将创建好的菜单添加到菜单栏

{% asset_img d57e9994a4c27d1ed368beab18d5ad6edcc438d7.jpg wxpython教程：[3]菜单栏 %}

- 最后，我们将设置好的菜单栏添加到窗口：
将菜单中的选项与命令绑定，这样才能在点击选项的时候执行某个动作：
到此我们的菜单栏就做好了，运行程序可以看到效果

{% asset_img 0fb505d5ad6eddc457a931943adbb6fd536633d7.jpg wxpython教程：[3]菜单栏 %}

{% asset_img dc854fda81cb39dbbf8ee239d3160924aa1830d7.jpg wxpython教程：[3]菜单栏 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
