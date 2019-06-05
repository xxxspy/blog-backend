---
title: pandas教程：[12]transformation标准化数据
date: 2015-02-11 18:11:01
tags: [pandas]
author: mlln.cn
---
假如有一列数据需要转换为以1为标准差以0为平均数的标准分数，如何用pandas实现？今天我们一边介绍数据的标准化，一边感受一下transformation的用法。要知道transformation不仅仅可以实现数据的标准化，它可以实现任何你能想到的数据转换。

- 引入相关模块

{% asset_img 8a95ad1c8701a18b1c5a7f599d2f07082838fe30.jpg pandas教程：[12]transformation标准化数据 %}

- 创建一个series对象
可以查看一下数据的前五行：

{% asset_img 263e802f07082838bfbcb102bb99a9014c08f130.jpg pandas教程：[12]transformation标准化数据 %}

{% asset_img 72b19c025aafa40f33cda3cba864034f78f01959.jpg pandas教程：[12]transformation标准化数据 %}

- 我们使用两个lambda函数key和zscore，其中zscore是transform的参数，key是groupby的参数

{% asset_img 4abae5edab64034f04c6af10acc379310a551d59.jpg pandas教程：[12]transformation标准化数据 %}

- 经过这样的转换，每个月的数据已经转换为标准分数（每月数据平均数为0标准差为1），查看一下得到的结果的数据类型，它还是一个series对象

{% asset_img 0b907cd9f2d3572cbf53f1ca8913632762d0c330.jpg pandas教程：[12]transformation标准化数据 %}

- 验证一下结果是否正确，我们先按照月分组数据，然后再计算标准差和平均数

{% asset_img f392492c11dfa9ec3a9f3b0161d0f703918fc130.jpg pandas教程：[12]transformation标准化数据 %}

- 输出的结果很明显：已经完成了数据的转换。

{% asset_img 0b14ad19ebc4b745c79fda00ccfc1e178a821559.jpg pandas教程：[12]transformation标准化数据 %}

- 欢迎有志于数据分析的人一起交流学习。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
