---
title: Python统计分析：[8]单因素卡方检验
date: 2015-04-15 18:19:23
tags: [python]
author: mlln.cn
---
卡方检验主要用于检验计数数据是否符合某种分布，比如男女比率本应该是1:1，但实际采集的样本可能是1:2，那么1:1和1:2之间有没有差异，我们需要用卡方检验来比较。

- 先引入相关模块

{% asset_img 3c2c4bfbb2fb43164eaebc1823a4462308f7d3e4.jpg Python统计分析：[8]单因素卡方检验 %}

- 实例化ChiSqure1way对象

{% asset_img 4e0b3ea4462309f7b8de6b70710e0cf3d6cad6e4.jpg Python统计分析：[8]单因素卡方检验 %}

- 运行卡方检验，如果我们只输入一个参数，表示我们要检验这一列数据分布是否均匀，也就是各组频数是否相等

{% asset_img 834344afa40f4bfb253a5836004f78f0f63618af.jpg Python统计分析：[8]单因素卡方检验 %}

- 基本检验结果首先是数据的描述

{% asset_img bf487563f6246b6038bf7416e8f81a4c500fa2e4.jpg Python统计分析：[8]单因素卡方检验 %}

- 接着是卡方检验结果，根据p值可知两组差异不显著

{% asset_img ae8267310a55b3190c13441740a98226cefc17af.jpg Python统计分析：[8]单因素卡方检验 %}

- 统计量检验

{% asset_img 504ec7f9d72a605919a127782b34349b023bbae4.jpg Python统计分析：[8]单因素卡方检验 %}

- 假如我们输入两个参数，可以指定各组频数的期望值

{% asset_img aa251d4f78f0f7364c148a630955b319eac413af.jpg Python统计分析：[8]单因素卡方检验 %}

- 结果是这样的：

{% asset_img 61183b2dd42a28340b17f06958b5c9ea14cebfe4.jpg Python统计分析：[8]单因素卡方检验 %}

- 对于结果，我们可以使用字典的方式读取个别值，比如卡方：

{% asset_img 020e66f0f736afc39de6f907b019ebc4b64512af.jpg Python统计分析：[8]单因素卡方检验 %}

{% asset_img 35da1d3b5bb5c9ea5642c581d639b6003bf3b3e4.jpg Python统计分析：[8]单因素卡方检验 %}

- 对于其他值，我们可以参考下面的列表：

{% asset_img d0526df082025aaf7febbfa9f8edab64024f1abc.jpg Python统计分析：[8]单因素卡方检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
