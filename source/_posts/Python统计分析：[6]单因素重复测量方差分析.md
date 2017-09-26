---
title: Python统计分析：[6]单因素重复测量方差分析
date: 2016-08-11 18:23:23
tags: [python]
author: mlln.cn
---
单因素重复测量方差分析:[repeated measuers anova in python]

- 引入相关模块

{% asset_img c71d0e385343fbf211710c5fb37eca8065388f2a.jpg Python统计分析：[6]单因素重复测量方差分析 %}

- 读取数据，并打印查看数据
数据在整理前是这样的：这是重复测量方差分析标准的数据格式，scoreA和scoreB分别是前测和后测成绩，ID表示被试的编号，group在今天的教程中没用，忽略他

{% asset_img fab3ac119313b07e6ce0fa740fd7912397dd8c2a.jpg Python统计分析：[6]单因素重复测量方差分析 %}

{% asset_img 83cab81ea8d3fd1fb2ba0846334e251f94ca5fd8.jpg Python统计分析：[6]单因素重复测量方差分析 %}

- 整理数据很关键，我们用到了pandas.concat来合并两个数据框
最终得到的数据如下：一个因变量score和两个自变量（ID和group）

{% asset_img dc15484e9258d109565003ced258ccbf6d814dd8.jpg Python统计分析：[6]单因素重复测量方差分析 %}

{% asset_img 4075890a304e251f62444e84a486c9177e3e53d8.jpg Python统计分析：[6]单因素重复测量方差分析 %}

- 回忆上一篇的知识，我们需要写一个公式定义模型，然后进行拟合

{% asset_img 814b07d8bc3eb135dd741dc7a51ea8d3fc1f44d8.jpg Python统计分析：[6]单因素重复测量方差分析 %}

- 最后得到的重复测量的方差分析结果，ID是被试差异造成的影响，可以不看；group就是实验处理效应，它是不显著的。

{% asset_img 245e8bcad1c8a7863399e0726409c93d71cf50d8.jpg Python统计分析：[6]单因素重复测量方差分析 %}

- 假如我们用spss进行重复测量的方差分析，得到的结果是：和上面的结果是一样的。至此我们就实现了单因素重复测量的方差分析，下一节继续介绍多因素混合设计方差分析。

{% asset_img 38403f3fb80e7becea64969d2c2eb9389a506bd5.jpg Python统计分析：[6]单因素重复测量方差分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
