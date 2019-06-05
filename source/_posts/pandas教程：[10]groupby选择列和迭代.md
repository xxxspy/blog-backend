---
title: pandas教程：[10]groupby选择列和迭代
date: 2015-10-11 18:23:19
tags: [pandas]
author: mlln.cn
---
groupby对象可以按照列选择数据，这种做法可以减少运算量，提高运算速度。而这里讲的迭代就是对各个组进行迭代以便对各个组进行不同的操作，因为进行相同的操作不必使用迭代。

- 引入相关模块

{% asset_img 263e802f070828381bc51d01bb99a9014d08f198.jpg pandas教程：[10]groupby选择列和迭代 %}

- 创建一个DataFrame对象，有两个index和两个column

{% asset_img 064936381f30e924be6c5d244f086e061c95f798.jpg pandas教程：[10]groupby选择列和迭代 %}

- 打印一下，看看DataFrame到底有哪些内容

{% asset_img 29790130e924b899aef4b82d6d061d950b7bf698.jpg pandas教程：[10]groupby选择列和迭代 %}

- 以color index进行分类，然后选择a列数据，分组计算a列数据的总数
计算结果为：

{% asset_img a84052086e061d95018ef62d78f40ad163d9ca98.jpg pandas教程：[10]groupby选择列和迭代 %}

{% asset_img 7ab514d162d9f2d346d9e5faaaec8a136227cc98.jpg pandas教程：[10]groupby选择列和迭代 %}

- 假如我们不选择a列，直接计算总数，可以得到。如果我们不需要b列的数据，那么显然事先选择a列进行计算可以减少无效的运算

{% asset_img 90cebeec08fa513d3db7accb3e6d55fbb2fbd943.jpg pandas教程：[10]groupby选择列和迭代 %}

{% asset_img f392492c11dfa9ec9ee6970261d0f703908fc198.jpg pandas教程：[10]groupby选择列和迭代 %}

- 迭代输出各个组的数据：
输出结果：

{% asset_img 62667cd0f703918fb919fcdf523d269758eec498.jpg pandas教程：[10]groupby选择列和迭代 %}

{% asset_img 54baacfb43166d226d6ad581452309f79052d243.jpg pandas教程：[10]groupby选择列和迭代 %}

- 假如分类索引有两个，分别是color和food
这时候迭代的结果显示，名称变为一个元组：

{% asset_img 27d647ee3d6d55fbaddbb6336e224f4a20a4dd43.jpg pandas教程：[10]groupby选择列和迭代 %}

{% asset_img 3c2c4bfbb2fb43164fd7bb6f23a4462308f7d398.jpg pandas教程：[10]groupby选择列和迭代 %}

- 致力于数据分析的同行，欢迎与我联系交流

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
