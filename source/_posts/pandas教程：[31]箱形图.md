---
title: pandas教程：[31]箱形图
date: 2016-06-19 18:11:23
tags: [pandas]
author: mlln.cn
---
箱形图用于显示数据的一些基本的统计量：中位数、平均数、四分位数等，我们来看一个关于箱形图的介绍：

- 下面我们用Python.pandas来绘制箱形图，先引入相关的模块

{% asset_img 7a8a1446f21fbe09e50f606568600c338744ad2b.jpg pandas教程：[31]箱形图 %}

- 配置画板

{% asset_img 95afee1f3a292df500b70f64bf315c6034a87308.jpg pandas教程：[31]箱形图 %}

- 先绘制一个简单的箱形图，用到了ax参数指定在哪里绘图
生成的plot.png如下图：

{% asset_img 6a2112338744ebf88e20c74edaf9d72a6059a72b.jpg pandas教程：[31]箱形图 %}

{% asset_img 570f8c58d109b3de73cb4719cfbf6c81800a4c08.jpg pandas教程：[31]箱形图 %}

- 有时候我们需要分组显示箱形图，比如数据中有的来自于男性、有的来自于女性，我们先生成一个列表示男女

{% asset_img 5d212aa85edf8db12c5adf150a23dd54564e7408.jpg pandas教程：[31]箱形图 %}

- 以性别进行分组，然后绘制箱形图
生成的plot1.png如下图所示：左边的是a列数据，右边是b列数据

{% asset_img 8cf0d51349540923371dc00f9158d109b3de4908.jpg pandas教程：[31]箱形图 %}

{% asset_img b29f8282d158ccbf9ec8164b1ad8bc3eb1354108.jpg pandas教程：[31]箱形图 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
