---
title: pandas教程：[30]直方图
date: 2016-05-23 18:17:05
tags: [pandas]
author: mlln.cn
---
上一篇文章介绍了用python.pandas绘制柱形图，今天介绍的直方图与柱形图看起来很像，但是直方图更多用于连续数据而不是分类或者离散数据，下面看看具体的过程：

- 引入相关模块

{% asset_img eab9044c510fd9f903ad3918262dd42a2934a4ce.jpg pandas教程：[30]直方图 %}

- 创建一个数据框，查看一下其中的数据
这是数据：

{% asset_img 504ec7f9d72a6059f3aa8d6b2b34349b023bbace.jpg pandas教程：[30]直方图 %}

{% asset_img 964b2e4e251f95caef69fec7ca177f3e660952e7.jpg pandas教程：[30]直方图 %}

{% asset_img 86d5bac27d1ed21b57554294ae6eddc450da3fe7.jpg pandas教程：[30]直方图 %}

- 假如我们绘制a列数据的直方图，可以直接使用hist()方法

- 这是输出的plot.png图（很多人问我为什么要输出图片，直接show()一下图片不好么？我这么做是有用意的，我倾向于用Python做一些数据分析软件，输出图片后可以将其导入word或者excel中，生成数据分析报告，因此show(）是没用的）

{% asset_img 964b2e4e251f95caef69fec7ca177f3e660952e7.jpg pandas教程：[30]直方图 %}

{% asset_img 55a628d12f2eb93893711583d6628535e5dd6f67.jpg pandas教程：[30]直方图 %}

- 我们可以同时绘制所有列的直方图，得到的是一个numpy.ndarray对象，其元素是matplotlib.axes.AxesSubplot对象
输出的结果：
如果你使用的Python(x,y)这样的集成平台，那么去掉print后（df.hist(color='k', alpha=0.5, bins=50)）可以直接看到有四个图输出，但是如果你是一个程序员我不建议你使用Python（x,y),我也是一样，从来都不用它，所以我们无法直接看到这些图，除非你show或者savefig

{% asset_img c856613e6709c93d346e62869c3df8dcd00054e7.jpg pandas教程：[30]直方图 %}

{% asset_img d35a10f41bd5ad6e8165089b82cb39dbb7fd3ce7.jpg pandas教程：[30]直方图 %}

- 我们经常用到by参数来设定分组

{% asset_img 3bc6f750352ac65cf6bf0a02f8f2b21192138ace.jpg pandas教程：[30]直方图 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
