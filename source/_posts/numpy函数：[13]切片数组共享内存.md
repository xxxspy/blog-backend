---
title: numpy函数：[13]切片数组共享内存
date: 2015-08-05 18:19:17
tags: [numpy]
author: mlln.cn
---
使用切片的方法获取数组的一部分，并没有创建新的数组，而切片只是原始数组的一种视图，所以改变切片中的数值，也会改变原始数组的元素值，具体通过例子来看一下：

- 先从Numpy中引用所有

{% asset_img 8cf0d513495409233eb9c8e19058d109b2de491a.jpg numpy函数：[13]切片数组共享内存 %}

- 创建一个一位数组a

{% asset_img 6dc09e0a19d8bc3e5f2aac55808ba61ea9d345d4.jpg numpy函数：[13]切片数组共享内存 %}

- 通过切片获取数组b

{% asset_img bd7faf3533fa828b54f3367cff1f4134960a5a1a.jpg numpy函数：[13]切片数组共享内存 %}

- 假如改变数组b中的元素的值

{% asset_img 948bcfc8a786c9178321f8a6cb3d70cf3ac757d4.jpg numpy函数：[13]切片数组共享内存 %}

- 数组a相应的值也会发生变化

{% asset_img 948bcfc8a786c91782d3f9a6cb3d70cf3ac7571a.jpg numpy函数：[13]切片数组共享内存 %}

- 假如把a全部赋值给c，也是一样的效果，还是改变了原数组的值

{% asset_img a28d62d98d1001e984ecbf90ba0e7bec55e7971a.jpg numpy函数：[13]切片数组共享内存 %}

- 想要保证原始数组的值不发生变化，我们最好使用copy方法获取数组c

{% asset_img fcbbb151f3deb48f58b90a41f21f3a292cf5781a.jpg numpy函数：[13]切片数组共享内存 %}

- 现在改变数组c的元素的值，数组a将不放生变化。

{% asset_img 48151723dd54564e76474ea6b1de9c82d0584fd4.jpg numpy函数：[13]切片数组共享内存 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
