---
title: Python统计分析：[3]单因素方差分析
date: 2015-08-19 18:05:05
tags: [python]
author: mlln.cn
---
Python 实现单因素方差分析用到了scipy.stats.f_oneway()方法，用法很简单，只不过在用之前需要先检验方差齐性，用到了levene test。

- 引入相关模块

{% asset_img ae8267310a55b319747a8c0240a98226cefc1782.jpg Python统计分析：[3]单因素方差分析 %}

- 读取数据，数据保存在text文件中，就是两列数据，列之间用逗号隔开，参数header=None指的是数据头部没有标题，names参数指定列的名称
我们可以看到输出的数据：

{% asset_img b29f8282d158ccbf2159bb4d1ad8bc3eb03541a4.jpg Python统计分析：[3]单因素方差分析 %}

{% asset_img 90cebeec08fa513df32962a93e6d55fbb3fbd983.jpg Python统计分析：[3]单因素方差分析 %}

- 数据分组，因为数据中group列有三个值表示数据来自不同的组

{% asset_img 263e802f07082838a28ed263bb99a9014d08f183.jpg Python统计分析：[3]单因素方差分析 %}

- 将这三个分组后的数据保存到一个列表args里，有变成经验的应该知道*args的作用，不懂的百度 Python *args

{% asset_img e865a699a9014c08acb826d2097b02087af4f483.jpg Python统计分析：[3]单因素方差分析 %}

- 首先进行levene test，如果p小于0.05，就警告方差不齐

{% asset_img 948bcfc8a786c91720e65c4eca3d70cf3ac757a4.jpg Python统计分析：[3]单因素方差分析 %}

- 之后再进行方差分析
方差分析结果：

{% asset_img a583631ed21b0ef4630d9629dec451da80cb3ea4.jpg Python统计分析：[3]单因素方差分析 %}

{% asset_img 6398ecd3572c11df6552b154602762d0f603c283.jpg Python统计分析：[3]单因素方差分析 %}

{% asset_img a583631ed21b0ef4630d9629dec451da80cb3ea4.jpg Python统计分析：[3]单因素方差分析 %}

- 很多时候我们不知道数据分成多少组，需要自动生成不同组的数据，可以用下面的方法：

{% asset_img f99dcf00baa1cd111b537c57ba12c8fcc2ce2da4.jpg Python统计分析：[3]单因素方差分析 %}

- 检验的结果也是一样的。

{% asset_img 734f12f3d7ca7bcbecf8c958bd096b63f724a883.jpg Python统计分析：[3]单因素方差分析 %}

- 如果你熟悉Statsmodels，你可以这么做来输出更优雅的结果：
输出结果为：

{% asset_img cbc17b380cd791239e1fe103ae345982b3b7808e.jpg Python统计分析：[3]单因素方差分析 %}

{% asset_img 3853ad1bb051f8192f14773dd9b44aed2e73e751.jpg Python统计分析：[3]单因素方差分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
