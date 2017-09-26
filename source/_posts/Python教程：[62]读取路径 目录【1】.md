---
title: Python教程：[62]读取路径 目录【1】
date: 2015-06-11 18:23:03
tags: [python]
author: mlln.cn
---
已知一个路径，我们怎么知道文件的类型，文件存放的文件夹，根目录呢？今天这篇文章主要就是解决这个问题——根据路径提取有用信息：

- 引用path模块，然后我们创建一个路径filepath

{% asset_img 8697397f9e2f07085a0c9980eb24b899a801f2e2.jpg Python教程：[62]读取路径 目录【1】 %}

- 用dirname提取文件夹的路径：

{% asset_img 29790130e924b899df35cab86c061d950b7bf6e2.jpg Python教程：[62]读取路径 目录【1】 %}

- 用basename提取文件名称：

{% asset_img 91138622720e0cf34da7fd7b0846f21fbf09aa9b.jpg Python教程：[62]读取路径 目录【1】 %}

- 用splitdrive分割根目录和其他目录

{% asset_img 29790130e924b899df77cab86c061d950b7bf6ac.jpg Python教程：[62]读取路径 目录【1】 %}

- 用split方法分割文件名及其目录

{% asset_img 6a2112338744ebf8bf78d7bfdbf9d72a6159a7e2.jpg Python教程：[62]读取路径 目录【1】 %}

- 用splitext，注意它的拼写，用于分割后缀名和其他路径：

{% asset_img a005b3345982b2b719e58a4433adcbef77099bfd.jpg Python教程：[62]读取路径 目录【1】 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
