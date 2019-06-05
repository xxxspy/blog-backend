---
title: numpy函数：[10]ones和empty创建数组
date: 2016-07-01 18:23:17
tags: [numpy]
author: mlln.cn
---
使用ones可以创建任意维度和元素个数的数组，其元素均为1。empty函数的使用方法一样，只是它创建的是数组所有元素均为空，所以它是速度最快的创建数组的方法。

- 先从numpy中引入所有

{% asset_img d56b3634349b033bff9b584517ce36d3d439bddb.jpg numpy函数：[10]ones和empty创建数组 %}

- 接着，我们使用ones创建一个包含5个元素的一维数组，其元素均为1

{% asset_img f35ea0096b63f624fd6e9d9c8544ebf81a4ca33b.jpg numpy函数：[10]ones和empty创建数组 %}

- ones创建的数组数据类型默认为浮点型，我们可以通过第二个参数来设置其数据类型

{% asset_img 0d729944ebf81a4cca014856d52a6059252da63b.jpg numpy函数：[10]ones和empty创建数组 %}

- 假如我们创建一个2维数组，就要用到列表作为参数。三维数组以此类推

{% asset_img 1b0d4f0fd9f9d72afe57b482d62a2834349bbb3b.jpg numpy函数：[10]ones和empty创建数组 %}

- 多维数组也可以改变数据类型

{% asset_img c8ab0bce36d3d5391f0eab5c3887e950352ab03b.jpg numpy函数：[10]ones和empty创建数组 %}

- 接着我们用empty试试创建数组

{% asset_img 3bc6f750352ac65cbf36c2ecf9f2b21193138a3b.jpg numpy函数：[10]ones和empty创建数组 %}

- 和ones的使用方法是一样的。empty创建的数组中，包含元素均为无意义的数值

{% asset_img 969cbf44ad3459820f99410d0ef431adcaef84db.jpg numpy函数：[10]ones和empty创建数组 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
