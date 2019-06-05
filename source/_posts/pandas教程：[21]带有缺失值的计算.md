---
title: pandas教程：[21]带有缺失值的计算
date: 2016-04-15 18:17:15
tags: [pandas]
author: mlln.cn
---
有时候数据带有缺失值，也就是有些数据为NaN，在运算的时候要时刻警惕是否存在缺失值，在不同的情况下，pandas处理缺失值的方式不同，主要是两种方式，下面介绍一下：

- 先引入相关模块

{% asset_img 8474fbdde71190ef797bfdd8cd1b9d16fcfa60f1.jpg pandas教程：[21]带有缺失值的计算 %}

- 先创建一个带有缺失值的数据框，注意缺失值用np.nan

- 查看一下df1

{% asset_img 90cebeec08fa513d903103d93e6d55fbb3fbd9db.jpg pandas教程：[21]带有缺失值的计算 %}

{% asset_img cdfe7281800a19d88d83eb0230fa828ba71e46f1.jpg pandas教程：[21]带有缺失值的计算 %}

- 创建一个不带有缺失值的数据框
查看df2的数据：

{% asset_img f15e24292df5e0fe8498e6065f6034a85fdf72f1.jpg pandas教程：[21]带有缺失值的计算 %}

{% asset_img 245e8bcad1c8a786f6aa25096409c93d71cf50f1.jpg pandas教程：[21]带有缺失值的计算 %}

- 在简单的运算中，如果遇到缺失值，运算结果在相应的位置也是缺失值
运算结果为：

{% asset_img 425773224f4a20a4f98553c093529822730ed0db.jpg pandas教程：[21]带有缺失值的计算 %}

{% asset_img 5af4d7ea15ce36d30b9fec3739f33a87e850b1db.jpg pandas教程：[21]带有缺失值的计算 %}

- 在描述性统计中，Nan都是作为0进行运算
输出结果为：

{% asset_img 91138622720e0cf3126c21fc0946f21fbf09aadb.jpg pandas教程：[21]带有缺失值的计算 %}

{% asset_img 148f28d3d539b600da5560b0ea50352ac75cb7db.jpg pandas教程：[21]带有缺失值的计算 %}

- 其他的描述性统计也是一样的：
输出结果为：

{% asset_img 570f8c58d109b3deb73f8b6fcfbf6c81810a4cf1.jpg pandas教程：[21]带有缺失值的计算 %}

{% asset_img 7e7f7909c93d70cf7f7ac50afbdcd100bba12bf1.jpg pandas教程：[21]带有缺失值的计算 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
