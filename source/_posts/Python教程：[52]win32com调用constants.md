---
title: Python教程：[52]win32com调用constants
date: 2015-03-23 18:03:17
tags: [python]
author: mlln.cn
---
今天使用python的win32com组间操作Excel的时候发现一个问题，想要使用常数constants.xlUp，但是却总是提示错误：

- Traceback (most recent call last):

-   File "<pyshell#1>", line 1, in <module>

-     c.xlUp

-   File "D:\Python27\lib\site-packages\win32com\client\__init__.py", line 170, in __getattr__

-     raise AttributeError(a)

- AttributeError: xlUp

- 我来介绍一下自己的代码吧，先来引入常量constants

{% asset_img 906289dda144ad34b56cd31dd2a20cf430ad851e.jpg Python教程：[52]win32com调用constants %}

- 接着，我们引入client，这都是操作Excel的时候用到的基本模块

{% asset_img 38403f3fb80e7beca9a4547b2d2eb9389a506beb.jpg Python教程：[52]win32com调用constants %}

- 现在我们启动一下Excel，句柄存在xl中

{% asset_img 2e6fa7389b504fc2d626e79fe7dde71191ef6deb.jpg Python教程：[52]win32com调用constants %}

- 我们尝试调用一下c.xlUp,看到了吧，提示错误

{% asset_img b94f65ec54e736d12fc1d89299504fc2d462691e.jpg Python教程：[52]win32com调用constants %}

- 假如，我现在用另一个方式启动Excel

{% asset_img b87985504fc2d56280da8477e51190ef77c66c1e.jpg Python教程：[52]win32com调用constants %}

- 现在就可以正确读取了

{% asset_img e49cf91190ef76c6ad00afb19f16fdfaae51671e.jpg Python教程：[52]win32com调用constants %}

- 我现在还不知道这两种方式到底有什么区别，只能先写到这里，如果哪位朋友知道为什么，可以在下面留言。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
