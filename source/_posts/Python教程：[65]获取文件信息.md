---
title: Python教程：[65]获取文件信息
date: 2016-07-23 18:17:05
tags: [python]
author: mlln.cn
---
怎样获取文件的创建时间、修改时间、大小、路径等信息？我们今天就要通过一个已知路径来获取这些信息，下面是具体的方法：

- 先来一如一个os模块，然后写一个路径，比如fpath

{% asset_img 42e89c26cffc1e17de1a34b14890f603728de94e.jpg Python教程：[65]获取文件信息 %}

- 通过join方法，得到一个txt文件的路径:join

{% asset_img 8bc3a7014a90f6032b1524c73b12b31bb151ed4e.jpg Python教程：[65]获取文件信息 %}

- 看一下，现在这个路径指向一个txt文件

{% asset_img 263e802f07082838734a6494ba99a9014d08f1a8.jpg Python教程：[65]获取文件信息 %}

- 判断一下这个路径是否指向的是文件，而不是我文件夹:isfile

{% asset_img 6f4703950a7b02080e8e876160d9f2d3562cc8a8.jpg Python教程：[65]获取文件信息 %}

- 获取文件的修改时间:getatime

{% asset_img 4bac30738bd4b31ce2992c3b85d6277f9f2ff84e.jpg Python教程：[65]获取文件信息 %}

- 获取文件的创建时间:getctime

{% asset_img 566d0fdfa9ec8a131e5def60f503918fa1ecc0a8.jpg Python教程：[65]获取文件信息 %}

- 获取文件的大小:getsize

{% asset_img 90cebeec08fa513da2edd45e3f6d55fbb3fbd9a8.jpg Python教程：[65]获取文件信息 %}

- 获取文件的绝对路径：abspath

{% asset_img a1ad16fa513d2697dc94b0dd57fbb2fb4216d8a8.jpg Python教程：[65]获取文件信息 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
