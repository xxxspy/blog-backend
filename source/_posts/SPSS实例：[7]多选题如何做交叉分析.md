---
title: SPSS实例：[7]多选题如何做交叉分析
date: 2015-04-23 18:11:01
tags: [spss]
author: mlln.cn
---
多项选择题做统计分析的时候经常用到两种数据录入方式，一种是二分法；另一种是分类法。其实两种方法都能完成所有的分析，所以我们没有必要跟大家介绍两种方法，今天我们就是用分类法来进行分析，下面是具体的步骤：
工具/原料


- spss20.0
方法/步骤


- 我们先来看数据录入的方式，下面第一幅图是问卷，该题有8个选项，是多选题，被试最多可以选择8个选项。下面第二幅图是数据录入的格式，我们看到有8列变量每列变量中的值可以是1-8的任意一个

{% asset_img cefc1e178a82b901e1bda005718da9773912eff0.jpg SPSS实例：[7]多选题如何做交叉分析 %}

{% asset_img 91529822720e0cf33feb2dcd0846f21fbe09aaec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 将保存在Excel中的数据直接拖动到spss界面，这样就在spss中打开了Excel文件。

{% asset_img 024f78f0f736afc3d9aa5c53b119ebc4b7451265.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 第一步是要设置变量集，因为8个变量都是一个题，所以8个变量要组合成一个变量集，在菜单中找到：analyse--multiple response--define variable sets

{% asset_img f31fbe096b63f62484415a358544ebf81a4ca3ec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 将这8个变量选中，然后放入到右侧的变量集框中

{% asset_img 3b292df5e0fe9925fd0d0a6636a85edf8db17186.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 选择数据录入的方法，我们使用的分类法，选择第二种方法，然后输入最大值和最小值分别是8和1

{% asset_img 500fd9f9d72a6059dd0c822c2a34349b033bbaec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 输入变量集的名称和标签，这个你自己定名字，然后添加到右侧的列表中

{% asset_img 9358d109b3de9c829e649ab96e81800a19d84386.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 当你看到这个列表中成功添加了一个变量集以后，你就可以关闭这个窗口了。

{% asset_img 2934349b033b5bb537cb43c834d3d539b600bcec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 接着我们来做频率统计，在菜单栏中找到：analyse--multiple response--frequency，将刚才生成的变量集放入右侧的列表中，点击ok，输出结果

{% asset_img 14ce36d3d539b60039d16c81eb50352ac65cb7ec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

{% asset_img 3bf33a87e950352ac17e463e5143fbf2b2118bec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 多选题百分比要看最后一列

{% asset_img c75c10385343fbf2b933c515b27eca8065388fec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 交叉分析可以使用analyse--multiple  response--crosstabs

- 假如我们要看不同性别和不同年级的人的频率，我们将性别这个变量放入行变量，将年级放入列变量，然后需要设置每个变量的取值范围

{% asset_img 960a304e251f95cab1f4f180cb177f3e67095286.jpg SPSS实例：[7]多选题如何做交叉分析 %}

{% asset_img 902397dda144ad344ca0e4b1d2a20cf431ad85ec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

- 点击ok我们就可以看到分析的结果了。

{% asset_img 9e3df8dcd100baa1a12d248d4510b912c8fc2e86.jpg SPSS实例：[7]多选题如何做交叉分析 %}

{% asset_img 77094b36acaf2eddbcee2adf8f1001e9390193ec.jpg SPSS实例：[7]多选题如何做交叉分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
