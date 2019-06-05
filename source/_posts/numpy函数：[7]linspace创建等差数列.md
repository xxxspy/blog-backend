---
title: numpy函数：[7]linspace创建等差数列
date: 2015-03-11 18:03:15
tags: [numpy]
author: mlln.cn
---
numpy.linspace是用于创建一个一位数组，并且是等差数列构成的一位数组，它蕞常用的有三个参数，当然不只有三个参数，我们通过例子来了解一下它是如何使用的：

- 首先，我们看一下第一个例子，用到三个参数，第一个参数表示起始点、第二个参数表示终止点，第三个参数表示数列的个数。

{% asset_img 834344afa40f4bfb989dc4c9014f78f0f636189a.jpg numpy函数：[7]linspace创建等差数列 %}

- 我经常用它创建一个元素全部是1的等差数列，或者你也可以让所有元素为0

{% asset_img 0fb505d5ad6eddc41915ee663bdbb6fd53663379.jpg numpy函数：[7]linspace创建等差数列 %}

- 我们看一下linspace创建的数组的元素的数据格式，当然是浮点型

{% asset_img ae8267310a55b31980f3c7e841a98226cefc17e1.jpg numpy函数：[7]linspace创建等差数列 %}

- 我们还可以使用参数endpoint来决定是否包含终止值，如果不设置这个参数，默认是True。我们看一下例子：注意步长改变了。

{% asset_img c8ab0bce36d3d5397f554b5e3887e950342ab080.jpg numpy函数：[7]linspace创建等差数列 %}

- 我试了试两个参数，也是可以的，但是创建的这个数组，我不太清楚是什么意义，有懂得人可以给我留言

{% asset_img e8112b2ac65c103899088c5fb0119313b17e89fe.jpg numpy函数：[7]linspace创建等差数列 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
