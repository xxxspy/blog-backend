---
title: numpy函数：[14]数组的列表下标存取方法
date: 2015-02-15 18:03:23
tags: [numpy]
author: mlln.cn
---
除了使用切片存取数组的元素之外，还可以使用整数列表作为下标存取方法。我们来看看具体的用法：

- 先从numpy包引入所有

{% asset_img b87985504fc2d56241674772e51190ef77c66c87.jpg numpy函数：[14]数组的列表下标存取方法 %}

- 创建一个一位数组a

{% asset_img a8ad9413632762d09da13320a2ec08fa503dc657.jpg numpy函数：[14]数组的列表下标存取方法 %}

- 假如要读取下标为2,4,6,8的数组元素，我们可以写用列表[2,4,6,8]作为下标

{% asset_img e6508eef76c6a7ef04493fb9fffaaf51f2de6687.jpg numpy函数：[14]数组的列表下标存取方法 %}

- 换一个试试

{% asset_img 9c57e3faaf51f3de7bdd2efb96eef01f3b297987.jpg numpy函数：[14]数组的列表下标存取方法 %}

- 由于这种方式获取的数组并不与原数组共享内存，所以改变一个数组的元素并不改变另一个数组中对应元素的值。

{% asset_img 8d158aeef01f3a29f9a742519b25bc315d607c87.jpg numpy函数：[14]数组的列表下标存取方法 %}

- 我们还可以通过列表下表进行赋值

{% asset_img 99636c0e0cf3d7ca0469a8e9f01fbe096a63a957.jpg numpy函数：[14]数组的列表下标存取方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
