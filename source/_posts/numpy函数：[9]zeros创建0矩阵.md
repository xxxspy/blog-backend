---
title: numpy函数：[9]zeros创建0矩阵
date: 2015-07-05 18:23:01
tags: [numpy]
author: mlln.cn
---
经常用到一些0数组，就是元素均为0的数组。那么怎么在python中创建0数组呢？我们用到了zeros函数，下面看看这个函数的用法：

- 首先要引入一下numpy这个包

{% asset_img 9e7ce6dcd100baa19c4a21244510b912c9fc2e8f.jpg numpy函数：[9]zeros创建0矩阵 %}

- 试着创建一个一维数组，只使用一个参数就可以了

{% asset_img 73ca5910b912c8fc95959052fe039245d788218f.jpg numpy函数：[9]zeros创建0矩阵 %}

- 默认情况下，zeros创建的数组是浮点型的，假如使用其他类型，可以设置dtype参数

{% asset_img d57e9994a4c27d1e8d6d5d5b19d5ad6edcc438a2.jpg numpy函数：[9]zeros创建0矩阵 %}

- 假如我们想要创建一个二维数组，我一开始以为是用下面这个方法，但是会返回错误

{% asset_img a583631ed21b0ef47aa3fec1dfc451da80cb3ea2.jpg numpy函数：[9]zeros创建0矩阵 %}

- 其实是使用一个列表作为参数，这样就返回一个二维数组

{% asset_img ac2fc3c451da81cb5f80e5525066d0160824318f.jpg numpy函数：[9]zeros创建0矩阵 %}

- 同样我们使用第二个参数设置数组的类型

{% asset_img 0865b518972bd4075b8cb56279899e510eb309a2.jpg numpy函数：[9]zeros创建0矩阵 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
