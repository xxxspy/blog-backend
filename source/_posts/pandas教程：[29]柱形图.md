---
title: pandas教程：[29]柱形图
date: 2015-08-23 18:03:17
tags: [pandas]
author: mlln.cn
---
上一篇文章做了一个散点图以及散点图的趋势线，这篇文章转向柱形图，柱形图一般适用于离散数据，而直方图更多用于连续数据。下面是具体绘制过程：

- 引入相关模块
创建一个10x4的DataFrame

{% asset_img 6dc09e0a19d8bc3e8ed97ebb818ba61ea9d345aa.jpg pandas教程：[29]柱形图 %}

{% asset_img 83cab81ea8d3fd1f04d8da4b334e251f94ca5faa.jpg pandas教程：[29]柱形图 %}

- 绘制一个柱形图很简单，只要在plot里指定kind为bar
这是输出的图plot1.png,有没有发现这个图很难看？

{% asset_img e865a699a9014c08ded650d4097b02087af4f497.jpg pandas教程：[29]柱形图 %}

{% asset_img d7c9ca3f8794a4c21ef29f5a0df41bd5ac6e39aa.jpg pandas教程：[29]柱形图 %}

- 可以如此设置柱形图的样式：
现在这个图变成了这个样式，如果你还是喜欢上一个图，你就设置mpl_style为none即可

{% asset_img 1cd4147b02087bf4bf012f98f1d3572c10dfcf97.jpg pandas教程：[29]柱形图 %}

{% asset_img 0fb505d5ad6eddc43836cc8a3adbb6fd536633aa.jpg pandas教程：[29]柱形图 %}

- 堆积直方图只需要设置stacked=True
绘制出来的堆积柱形图：

{% asset_img 7ab514d162d9f2d3effc5c9eaaec8a136227cc97.jpg pandas教程：[29]柱形图 %}

{% asset_img ac2fc3c451da81cb5237fbbc5166d016082431aa.jpg pandas教程：[29]柱形图 %}

- 很多时候我们的柱形图是延水平方向的，这时候需要设置kind=‘barh’
现在该图变成了水平方向的柱形图

{% asset_img f99dcf00baa1cd1125670a51ba12c8fcc2ce2daa.jpg pandas教程：[29]柱形图 %}

{% asset_img bf487563f6246b60d6e3ca05e8f81a4c500fa297.jpg pandas教程：[29]柱形图 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
