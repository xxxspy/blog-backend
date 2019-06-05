---
title: numpy函数：[8]logspace()创建等比数列数组
date: 2016-10-17 18:23:19
tags: [numpy]
author: mlln.cn
---
上一篇介绍了numpy.linspace用于创建等差数列，现在介绍logspace用于创建等比数列。其实用法差不多，但是有一个特殊的地方需要注意。

- 先来看一个例子，我们让开始点位0，结束点为0，元素个数为10，看看输出结果。为什么是酱紫呢？难道不都是0么？

{% asset_img a992e31f4134970ad07f90b297cad1c8a6865de4.jpg numpy函数：[8]logspace()创建等比数列数组 %}

- 因为logspace中，开始点和结束点是10的幂，0代表10的0次方，9代表10的9次方。我们看看下面的例子。
】

{% asset_img 964b2e4e251f95ca32f9122bcb177f3e660952e4.jpg numpy函数：[8]logspace()创建等比数列数组 %}

- 假如，我们想要改变基数，不让它以10为底数，我们可以改变base参数，将其设置为2试试

{% asset_img d089b986c9177f3e80387c9072cf3bc79e3d56e4.jpg numpy函数：[8]logspace()创建等比数列数组 %}

- 假如我们想要不包含结束点，可以设置endpoint为0

{% asset_img c87c6ecf3bc79f3d14ed64adb8a1cd11738b29e4.jpg numpy函数：[8]logspace()创建等比数列数组 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
