---
title: pandas教程：[24]删除缺失数据
date: 2015-03-03 18:01:19
tags: [pandas]
author: mlln.cn
---
假如数据量比较大或者有冗余，我们可以删掉有缺失值的数据，你可以选择删除行或者删除列，用的都是DataFrame.dropna()，当然Series也有dropna方法，用法相同。

- 引入相关模块

{% asset_img e78c65899e510fb36d342190da33c895d1430c4c.jpg pandas教程：[24]删除缺失数据 %}

- 创建一个带有缺失值的数据框：
查看一下数据内容：

{% asset_img 5af4d7ea15ce36d30012d53739f33a87e950b160.jpg pandas教程：[24]删除缺失数据 %}

{% asset_img 0b907cd9f2d3572cb2cfcadb8913632762d0c34d.jpg pandas教程：[24]删除缺失数据 %}

- 通常情况下，我们选择删除行，使用参数axis=0，这是最常用的方法
删除后的结果为：

{% asset_img a84052086e061d95966b613f78f40ad162d9ca4d.jpg pandas教程：[24]删除缺失数据 %}

{% asset_img 906289dda144ad34b0a9d180d3a20cf431ad8560.jpg pandas教程：[24]删除缺失数据 %}

- 还有可能的是，我们选择删除列，这种情况不多，因为通常我们选择用列表示一个变量或者指标，我们通常不会因为有几个缺失值就删除一个变量
输出结果为：

{% asset_img 0b3a1c087bf40ad1c2c991e4542c11dfa9ecce4d.jpg pandas教程：[24]删除缺失数据 %}

{% asset_img 90cebeec08fa513d8b873ad93e6d55fbb2fbd94d.jpg pandas教程：[24]删除缺失数据 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
