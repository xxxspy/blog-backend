---
title: pandas教程：[13]agg分组多种计算
date: 2015-02-01 18:05:15
tags: [pandas]
author: mlln.cn
---
有时候aggregate不能满足需求，因为我们要对分组数据进行多种计算，比如要同时计算各组数据的平均数、标准差、总数等等，这时候用agg()就比较好了。

- 先引入必要的变量，并且创建一个DataFrame
我们可以看一下DataFrame包含哪些数据

{% asset_img 246cca2a2834349b2ee45d93caea15ce37d3be82.jpg pandas教程：[13]agg分组多种计算 %}

{% asset_img 2f9cbdcc7cd98d1052363f27223fb80e7aec9082.jpg pandas教程：[13]agg分组多种计算 %}

- 按照颜色将数据分组：

{% asset_img 77485536acaf2eddecc67bff8e1001e9390193b5.jpg pandas教程：[13]agg分组多种计算 %}

- 计算各组数据的总数、平均数、标准差
计算结果为：

{% asset_img 027a45b5c9ea15ce070cd31fb5003af33b87b282.jpg pandas教程：[13]agg分组多种计算 %}

{% asset_img 00a82701213fb80e2c3352c135d12f2eb8389482.jpg pandas教程：[13]agg分组多种计算 %}

- 假如我们只需要对a列数据进行计算，可以选择a列：
计算结果为：

{% asset_img 3792cb39b6003af30f58ef76362ac65c1138b682.jpg pandas教程：[13]agg分组多种计算 %}

{% asset_img ae10eddeb48f8c54ffe4f73939292df5e0fe7fb5.jpg pandas教程：[13]agg分组多种计算 %}

- 假如我们需要定制显示的标题，也可以如此设置：
输出结果为：

{% asset_img c71d0e385343fbf28ece9535b37eca8064388f82.jpg pandas教程：[13]agg分组多种计算 %}

{% asset_img 9a1151c2d56285358502e13793ef76c6a6ef6382.jpg pandas教程：[13]agg分组多种计算 %}

- 另外，我们还可以通过lambda匿名函数来进行特殊的计算：
计算各组数据的绝对值的平均数（离均差）：

{% asset_img b87985504fc2d562db3fe2fbe41190ef76c66cb5.jpg pandas教程：[13]agg分组多种计算 %}

{% asset_img e49cf91190ef76c6c330c83d9e16fdfaae516782.jpg pandas教程：[13]agg分组多种计算 %}

- 我们还可以使用字符串作为一个function，要正确使用字符串，必须先学习groupby对象有哪些可用的方法。这种方式可以实现一些更高级的功能，比如定制计算方法，不建议新手使用。
计算结果为：

{% asset_img ac754782b2b7d0a2452b378bc8ef76094a369a82.jpg pandas教程：[13]agg分组多种计算 %}

{% asset_img 9319cf09b3de9c82ae52cb996f81800a19d843b5.jpg pandas教程：[13]agg分组多种计算 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
