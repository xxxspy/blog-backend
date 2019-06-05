---
title: pandas教程：[14]按月分组
date: 2015-10-17 18:17:11
tags: [pandas]
author: mlln.cn
---
我们经常处理的数据是不规范的，尤其是包含日期的数据，通常需要做一些转换，今天我们就做一个按月分组的实例，具体过程如下：

- 引入相关模块

{% asset_img 0865b518972bd4075882b5eb78899e510fb3091b.jpg pandas教程：[14]按月分组 %}

- 创建一个DataFrame对象，索引为日期
查看一下数据的前5行

{% asset_img 7ac880510fb30f2431df8a15cb95d143ad4b031b.jpg pandas教程：[14]按月分组 %}

{% asset_img b5ce925494eef01f1b827ed3e3fe9925bd317dd6.jpg pandas教程：[14]按月分组 %}

- 假如索引为日期Series，按月分组很简单，用到了一个lambda函数
分组后的情况：

{% asset_img 4abae5edab64034ff988a410acc379310a551d1b.jpg pandas教程：[14]按月分组 %}

{% asset_img 3b6833f5e0fe9925999a0f4637a85edf8cb171d6.jpg pandas教程：[14]按月分组 %}

- 但是有时候，索引不是日期，但是有一列数据为日期格式，因此，我们同样可以使用一个lambda函数来进行分组：
分组结果为：

{% asset_img b258f5c4b74543a9085e9cda1d178a82b901141b.jpg pandas教程：[14]按月分组 %}

{% asset_img 8367d1fc1e178a82377919b6f503738da977e824.jpg pandas教程：[14]按月分组 %}

- 但实际上，我们还可以将日期数据列设置为索引就可以使用上一种方法啦：
输出结果：

{% asset_img b8405490f603738d3b0f6a34b01bb051f819ec24.jpg pandas教程：[14]按月分组 %}

{% asset_img 0862c354564e9258e1a2e0f89f82d158cdbf4ed6.jpg pandas教程：[14]按月分组 %}

- 假如，我们的日期数据是以字符串的形式存储的，也不必着急，我们可以轻松的将其转换为Date
数据结果为：

{% asset_img d048adde9c82d158f8143fa7830a19d8bd3e42d6.jpg pandas教程：[14]按月分组 %}

{% asset_img 9dc3cf58ccbf6c81b6a14afebf3eb13532fa40d6.jpg pandas教程：[14]按月分组 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
