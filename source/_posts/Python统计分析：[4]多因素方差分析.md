---
title: Python统计分析：[4]多因素方差分析
date: 2016-05-01 18:19:03
tags: [python]
author: mlln.cn
---
上一篇文章介绍了Python做统计中如何实现单因素方差分析，这篇文章介绍一下如何做多因素方差分析以及当主效应显著时如何做多重比较。

- 引入相关模块

{% asset_img 509b9fcb39dbb6fdbb2901510a24ab18972b371c.jpg Python统计分析：[4]多因素方差分析 %}

- 读取数据（如果你需要我案例中的数据，可以联系我索要）

{% asset_img d1571724ab18972b3a48e4bde5cd7b899e510a1c.jpg Python统计分析：[4]多因素方差分析 %}

- 删除空值并打印数据
我们可以看到数据是酱紫的：

{% asset_img c9d4cf43ad4bd1138f0e524559afa40f4afb0543.jpg Python统计分析：[4]多因素方差分析 %}

{% asset_img 43e6c733c895d1435404005470f082025aaf071c.jpg Python统计分析：[4]多因素方差分析 %}

- 用statsmodels中的anova_lm，注意公式formula的写法
这是随即设计的两因素方差分析的结果：结果显示fetus的主效应显著

{% asset_img 734f12f3d7ca7bcb5a362358bd096b63f624a83d.jpg Python统计分析：[4]多因素方差分析 %}

{% asset_img d0526df082025aaf5a409abcf8edab64034f1a1c.jpg Python统计分析：[4]多因素方差分析 %}

- 阴虚fetus的主效应显著，所以有必要进行事后简单，使用tukey方法进行多重比较的方法及结果：
输出的结果显示，三个水平均均值均呈现显著差异（reject==Ture）

{% asset_img f35ea0096b63f6243e10dd748444ebf81a4ca33d.jpg Python统计分析：[4]多因素方差分析 %}

{% asset_img 834344afa40f4bfbfbbd7a23004f78f0f736181c.jpg Python统计分析：[4]多因素方差分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
