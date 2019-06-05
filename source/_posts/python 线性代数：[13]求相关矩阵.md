---
title: python 线性代数：[13]求相关矩阵
date: 2015-08-19 18:19:05
tags: [python]
author: mlln.cn
---
求n个变量之间的相关系数，我们直接求这几个变量之间的相关矩阵即可。上一篇讲了求身高体重之间的协方差，我们现在就来求他们之间的相关系数矩阵。

- 引入numpy模块

{% asset_img 0d729944ebf81a4ccb294b3ed52a6059242da6eb.jpg python 线性代数：[13]求相关矩阵 %}

- 身高用s表示，体重用t表示，采集了三个人的数据，如下

{% asset_img 29752a9b033b5bb56dcc870934d3d539b700bceb.jpg python 线性代数：[13]求相关矩阵 %}

- 创建矩阵y

{% asset_img 346bd85c103853434bd420d69113b07ecb8088eb.jpg python 线性代数：[13]求相关矩阵 %}

- 我们使用numpy.corrcoef方法求相关矩阵，左下角或者右上角就是身高与体重的相关系数，而对角线上元素是t与t或者s与s的相关系数

{% asset_img adee30dda3cc7cd94a36932e3b01213fb90e91eb.jpg python 线性代数：[13]求相关矩阵 %}

- 再增加一个变量

{% asset_img dc15484e9258d10940a80e45d358ccbf6d814dbb.jpg python 线性代数：[13]求相关矩阵 %}

- 求相关矩阵：

{% asset_img 2e6fa7389b504fc2064417f2e7dde71191ef6deb.jpg python 线性代数：[13]求相关矩阵 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
