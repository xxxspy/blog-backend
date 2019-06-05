---
title: numpy函数：[11]fromfunction以函数式创建数组
date: 2016-10-03 18:11:03
tags: [numpy]
author: mlln.cn
---
给函数绘图的时候经常需要创建一个数组，这时候就用到了fromfunction函数，用以从函数中创建数组，我们下面还是用具体的例子说明一下fromfunction的方法：

- 先从numpy中引入所有

{% asset_img d019d2bf6c81800aec6d2a91b33533fa838b4762.jpg numpy函数：[11]fromfunction以函数式创建数组 %}

- 我们创建一个函数，它是y=i*2的表示形式

{% asset_img 814b07d8bc3eb135cb4f1424a41ea8d3fc1f4462.jpg numpy函数：[11]fromfunction以函数式创建数组 %}

- 我们使用fromfunction函数，创建一个数组a，看a返回的的结果，所以a中存储的就是y的值，而i其实就是数组的索引，数组a反应的是i取值从0到1时，y的值。fromfunction的第二个参数定义了数组的形状，也就是说参数(5,)表示i取值范围是[0,1,2,3,4]

{% asset_img a75fb6d3fd1f413469bfa6e1271f95cad0c85e62.jpg numpy函数：[11]fromfunction以函数式创建数组 %}

- 假如要创建的是二维数组，也就是说函数式有两个自变量，比如y=i*j这个函数，我们在python的表示形式是

{% asset_img a992e31f4134970acffbb3b097cad1c8a6865d62.jpg numpy函数：[11]fromfunction以函数式创建数组 %}

- 以这个函数创建一个数组，我们看结果,参数(10,10)表示i的取值范围和j的取值范围是[0,1,2,3,4,5,6,7,8,9]，数组b中存放的就是函数返回的值

{% asset_img 245e8bcad1c8a786cda1e9916509c93d71cf5062.jpg numpy函数：[11]fromfunction以函数式创建数组 %}

- 换一种取值范围，看看结果

{% asset_img 3853ad1bb051f819d3ffa0d5d8b44aed2f73e71c.jpg numpy函数：[11]fromfunction以函数式创建数组 %}

- 这个很好理解

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
