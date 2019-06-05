---
title: Python教程：[36]如何替换字符串
date: 2015-02-19 18:17:15
tags: [python]
author: mlln.cn
---
今天要从网页采集url，但是出现了一个问题，需要用到替换字符串来纠正，我们先在就来看看如何替换字符串，用到了正则表达式，下面是具体的过程。

- 给txt赋值，注意看http：后面的“\/”，我们要把它替换成“/”

{% asset_img 734f12f3d7ca7bcb22a40838bc096b63f724a88f.jpg Python教程：[36]如何替换字符串 %}

- 引入正则表达式的模块

{% asset_img bf487563f6246b6022d17d63e9f81a4c500fa28f.jpg Python教程：[36]如何替换字符串 %}

- 我们使用subn方法来替换字符串，其返回两个值，一个是替换以后的结果，一个是替换的次数

{% asset_img d68b65cb0a46f21f94dd9144f4246b600d33aef9.jpg Python教程：[36]如何替换字符串 %}

- 我们看一下替换以后的结果，URL显示就正常了。

{% asset_img 0d729944ebf81a4c63ed23ded52a6059242da68f.jpg Python教程：[36]如何替换字符串 %}

- 当然，我们可以不使用正则表达式对象

{% asset_img 72b19c025aafa40f9dee00caa964034f78f019ba.jpg Python教程：[36]如何替换字符串 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
