---
title: numpy函数：[4]reshape用法
date: 2016-01-19 18:11:17
tags: [numpy]
author: mlln.cn
---
今天我们学习一个新函数reshape，顾名思义，它就是用于该表数组的形状的，它是数组对象中的方法，我们还是来看具体的例子吧：

- 同样要引入numpy，名称为np

{% asset_img c9bdddcec3fdfc03c787811fd63f8794a5c2265e.jpg numpy函数：[4]reshape用法 %}

- 我们先来创建一个数组a，你们可以看到这是一个一维的数组

{% asset_img 5af4d7ea15ce36d33419ee9738f33a87e950b13d.jpg numpy函数：[4]reshape用法 %}

- 我们使用reshape()方法来更改数组的形状，我们看看数组d成为了一个二维数组

{% asset_img 509b9fcb39dbb6fd36a487810b24ab18962b375e.jpg numpy函数：[4]reshape用法 %}

- 当然我们还可以得到一个三维数组f

{% asset_img 0e655ca7d933c895a3b6f5dcd31373f083020009.jpg numpy函数：[4]reshape用法 %}

- 形状变化的原则是数组元素不能发生改变，比如这样写就是错误的，因为数组元素发生了变化。

{% asset_img d1571724ab18972bbdc5626de4cd7b899f510a5e.jpg numpy函数：[4]reshape用法 %}

- 通过reshape生成的新数组和原始数组公用一个内存，也就是说，假如更改一个数组的元素，另一个数组也将发生改变。看看下面的例子：

{% asset_img 647912d7912397dd5264f5a35b82b2b7d0a2873d.jpg numpy函数：[4]reshape用法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
