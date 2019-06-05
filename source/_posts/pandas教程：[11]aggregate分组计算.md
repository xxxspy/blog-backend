---
title: pandas教程：[11]aggregate分组计算
date: 2015-05-03 18:15:17
tags: [pandas]
author: mlln.cn
---
一旦对数据分组，接下来一定是对各组数据进行计算，这是通过groupby.aggregate()实现的，我们来看一下今天的例子：

- 先引入必要的模块，然后创建一个DataFrame对象，如果你看了前几篇文章，应该已经知道这个DataFrame了。
这是内部数据：

{% asset_img bf487563f6246b602a038662e8f81a4c510fa253.jpg pandas教程：[11]aggregate分组计算 %}

{% asset_img 9e7ce6dcd100baa16f0973ad4410b912c8fc2ebb.jpg pandas教程：[11]aggregate分组计算 %}

- 根据两个索引color、food进行分组

{% asset_img f76575600c338744c3c81b6a520fd9f9d72aa053.jpg pandas教程：[11]aggregate分组计算 %}

- 计算各组总和：
计算结果为：

{% asset_img 310f3b1f95cad1c8309ec8317c3e6709c93d51bb.jpg pandas教程：[11]aggregate分组计算 %}

{% asset_img b853d6fcc3cec3fd551b9363d588d43f879427bb.jpg pandas教程：[11]aggregate分组计算 %}

- 计算结果默认使用了两个分组索引color和food作为新的DataFrame的索引（注意计算结果为一个DataFrame对象），可以使用reset_index()来将两个索引转化为列变量
结果为：

{% asset_img d66b7e59252dd42a180435bd003b5bb5c9eab853.jpg pandas教程：[11]aggregate分组计算 %}

{% asset_img 3bb22487e950352afb6c111e5043fbf2b2118b53.jpg pandas教程：[11]aggregate分组计算 %}

- 在分组是也可以使用as_index参数达到reset_index()的效果：
计算结果为：

{% asset_img fd428c45d688d43f2a8ca5e47e1ed21b0ef43bbb.jpg pandas教程：[11]aggregate分组计算 %}

{% asset_img 1a94b36eddc451da37d338fdb5fd5266d01632bb.jpg pandas教程：[11]aggregate分组计算 %}

- 另外我们经常用到的一个方法为size()返回各组数据量
结果为：

{% asset_img dc854fda81cb39db0ee55340d3160924ab1830bb.jpg pandas教程：[11]aggregate分组计算 %}

{% asset_img aa59892bd40735fa26d57aaf9d510fb30f2408bb.jpg pandas教程：[11]aggregate分组计算 %}

- 最后，还有一个经常用到的方法为describe()，对各组数据进行描述性统计：
计算结果为：

{% asset_img 34bbf8cd7b899e51ccab0e0241a7d933c8950dbb.jpg pandas教程：[11]aggregate分组计算 %}

{% asset_img d872d695d143ad4b1b0b72d681025aafa40f06bb.jpg pandas教程：[11]aggregate分组计算 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
