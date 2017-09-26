---
title: Python教程：[67]itemgetter对列表排序
date: 2016-04-15 18:03:23
tags: [python]
author: mlln.cn
---
上一篇文章讲了如何对list进行排序【请看传送门http://jingyan.baidu.com/article/90808022a546b8fd90c80f48.html】，今天我们进一步加深学习，使用 itemgetter来加速排序，并且可以减少代码的写作难度，我们来看看具体的例子，如何使用itemgetter：

- 首先装载一下operator模块

{% asset_img eab9044c510fd9f9a7c3dee9272dd42a2934a41f.jpg Python教程：[67]itemgetter对列表排序 %}

- 创建一个列表，列表由元组构成

{% asset_img d8b8c92a6059252da7c39684369b033b5ab5b91f.jpg Python教程：[67]itemgetter对列表排序 %}

- 使用itemgetter来进行排序，使用元组的第二个元素进行排序

{% asset_img 3a86813df8dcd1005f1573a1708b4710b8122f62.jpg Python教程：[67]itemgetter对列表排序 %}

- 使用元组的第一个元素进行排序

{% asset_img 29752a9b033b5bb5b103ab7e34d3d539b700bc1f.jpg Python教程：[67]itemgetter对列表排序 %}

- 甚至我们可以先对元组的第2个元素进行排序，然后对第一个元素进行排序，形成多级排序。

{% asset_img 5af4d7ea15ce36d3aed008b038f33a87e850b11f.jpg Python教程：[67]itemgetter对列表排序 %}

- 当然，我们还可以使用reverse来进行逆序排列

{% asset_img 3bc6f750352ac65c92d1edf3f9f2b21192138a1f.jpg Python教程：[67]itemgetter对列表排序 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
