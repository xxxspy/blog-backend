---
title: Python统计分析：[2]相关样本T检验
date: 2016-10-03 18:11:19
tags: [python]
author: mlln.cn
---
上一篇文章介绍了独立样本T检验，现在接着使用Python进行相关样本的T检验，主要用到了scipy.stats.ttest_rel，我们先来看看其基本的用法：

- 引入相关模块，这次我们使用stats的

{% asset_img 8640bf8b87d6277f111a614c2b381f30e924fc7f.jpg Python统计分析：[2]相关样本T检验 %}

- 产生两列随机变量，用到了stats。norm.rvs，参数loc表示平均数，scale表示标准差，size是样本量
这是产生的两个变量的数据的一部分

{% asset_img 1b0d4f0fd9f9d72aa8094369d72a2834349bbb12.jpg Python统计分析：[2]相关样本T检验 %}

{% asset_img 99636c0e0cf3d7cac1fe6c02f11fbe096b63a97f.jpg Python统计分析：[2]相关样本T检验 %}

- ttest_rel的用法：输出t和p值
从p值可以看出，这两列数据是没有差异的。

{% asset_img 29790130e924b8993c342a4c6d061d950a7bf67f.jpg Python统计分析：[2]相关样本T检验 %}

{% asset_img 734f12f3d7ca7bcbb173945bbd096b63f624a87f.jpg Python统计分析：[2]相关样本T检验 %}

- 当然，ttest_rel还可以接受pandas.DataFrame数据，先从excel中读取数据
我们可以看一下数据的基本内容：

{% asset_img d56b3634349b033b95e5afae16ce36d3d539bd12.jpg Python统计分析：[2]相关样本T检验 %}

{% asset_img 969cbf44ad34598255e7b6e60ff431adcbef8412.jpg Python统计分析：[2]相关样本T检验 %}

- 我们可以选择scoreA和ScoreB这两列数据进行T检验
输出的结果可见两列变量均值无差异

{% asset_img 54baacfb43166d22fe7f46e0452309f79052d27f.jpg Python统计分析：[2]相关样本T检验 %}

{% asset_img b3f6cea20cf431ad20bf104d4836acaf2edd9812.jpg Python统计分析：[2]相关样本T检验 %}

- 我们还可以同时对多个变量进行检验，比如：
这是产生的结果可见：第一个array表示t值，两个表示p值，因此我们可以知道p(scoreA)=0.126>0.05

{% asset_img d478a8003af33a873f00536ec55c10385343b512.jpg Python统计分析：[2]相关样本T检验 %}

{% asset_img 0db52fadcbef7609a666caeb2ddda3cc7cd99e12.jpg Python统计分析：[2]相关样本T检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
