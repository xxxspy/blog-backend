---
title: Python教程：[64]判断文件 文件夹
date: 2015-01-17 18:01:05
tags: [python]
author: mlln.cn
---
如何判断某个路径是不是存在、是不是文件夹、是不是文件？我们今天就来介绍一下判断文件、文件夹，同样也是用到了os.path模块，下面看看具体的例子：

- 装载一下os模块，然后我们写一个路径，这个路径是真是存在的

{% asset_img 5f9e93b1cb134954fcd956e4544e9258d0094a28.jpg Python教程：[64]判断文件 文件夹 %}

- 判断一下这个目录是不是文件夹，用isdir

{% asset_img c87c6ecf3bc79f3dede45db0b8a1cd11738b29ed.jpg Python教程：[64]判断文件 文件夹 %}

- 判断该路径是不是指向一个文件，用isfile

{% asset_img 9e7ce6dcd100baa1d529fe3b4510b912c9fc2eed.jpg Python教程：[64]判断文件 文件夹 %}

- 判断一下该路径是不是绝对路径：用isabs

{% asset_img b29f8282d158ccbf927b0bba1bd8bc3eb0354128.jpg Python教程：[64]判断文件 文件夹 %}

- 判断一下，该路径是否存在：用exists

{% asset_img cdfe7281800a19d8bdc53a8531fa828ba71e4628.jpg Python教程：[64]判断文件 文件夹 %}

- 总结一下，os.path模块下的五个判断函数：

{% asset_img d7c9ca3f8794a4c258265eab0cf41bd5ac6e39ed.jpg Python教程：[64]判断文件 文件夹 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
