---
title: numpy函数：[5]dtype数组元素类型
date: 2015-05-23 18:03:01
tags: [numpy]
author: mlln.cn
---
数组元素的类型可以通过dtype属性获得。下面我们创建几个数组，然后看看她们的元素类型是什么。然后我们看看dtype作为参数创建特定类型的数组的方法。

- 引入numpy ，创建一个列表a

{% asset_img 0b07ec1fbe096b63bec1b5cc0e338744eaf8ac17.jpg numpy函数：[5]dtype数组元素类型 %}

- 用列表a创建一个数组c

{% asset_img f76575600c338744a71dc4e0530fd9f9d62aa017.jpg numpy函数：[5]dtype数组元素类型 %}

- 我们看看数组c的元素的数据类型，是int32

{% asset_img e1bf8725bc315c60a96a80738fb1cb1348547774.jpg numpy函数：[5]dtype数组元素类型 %}

- 假如我们要创建一个其他类型的数组，可以设置dtype参数，如图所示，我们创建一个浮点型数据数组

{% asset_img 9864a2315c6034a8c01d531dc913495408237674.jpg numpy函数：[5]dtype数组元素类型 %}

- 我们再创建一个complex类型数组

{% asset_img d66b7e59252dd42a7cd1ea37013b5bb5c8eab817.jpg numpy函数：[5]dtype数组元素类型 %}

- 当然，每一种数据类型都有几种字符串表达形式，我们可以使用typeDict字典来查询某种字符串所代表的数据类型，比如'd'和‘double’都表示float64数据类型

{% asset_img 48151723dd54564e379a0fa5b1de9c82d0584f74.jpg numpy函数：[5]dtype数组元素类型 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
