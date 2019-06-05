---
title: DataNitro：[11]自动换行
date: 2015-01-11 18:05:15
tags: [datanitro]
author: mlln.cn
---
本篇文章原创于《百度经验》，如果转载此文章，需要注明出处、链接地址和作者名称，否则侵权。

- 我们知道只要点击这里就可以实现自动换行

{% asset_img d4239b35e5dde71132ecb0b4a4efce1b9d166173.jpg DataNitro：[11]自动换行 %}

- 换行后就会实现这个效果：

{% asset_img a992e31f4134970afe44e36d96cad1c8a7865d7a.jpg DataNitro：[11]自动换行 %}

- 但是现在我们需要使用datanitro来实现这个效果，而在datanitro里面没有直接的模块可以用，这时候我们想到用vba，在vbe里面的vba1模块里，写入一个过程：wraptext

{% asset_img 8367d1fc1e178a82a3268de2f503738da977e81f.jpg DataNitro：[11]自动换行 %}

- 接着，我们打开Python shell

{% asset_img ae10eddeb48f8c543f78376d39292df5e1fe7f8e.jpg DataNitro：[11]自动换行 %}

- 写入如下代码，然后按下回车，注意参数是vba过程的名称

{% asset_img 245e8bcad1c8a7861beeb84c6409c93d71cf5069.jpg DataNitro：[11]自动换行 %}

- 这样就实现了自动换行

{% asset_img 245e8bcad1c8a786182cb74c6409c93d70cf502b.jpg DataNitro：[11]自动换行 %}

- 再运行一遍，就可以回到没有自动换行的状态。

{% asset_img 373bc4b44aed2e73acd67b6e8401a18b87d6fa72.jpg DataNitro：[11]自动换行 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
