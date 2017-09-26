---
title: spss两因素（有一个连续变量）如何进行方差分析
date: 2015-01-01 18:17:17
tags: [spss]
author: mlln.cn
---
假如两因素的设计，其中一个变量是连续型变量，那么通常的方差分析就没有办法了，必须使用协方差分析，下面是具体的方法。
工具/原料


- spss20.0
方法/步骤


- 确保数据满足平行性假设的前提下，我们用协方差分析进行检验， 在菜单栏上执行：analyse--GLM--univariate

{% asset_img 562c11dfa9ec8a13f2aafb23f703918fa1ecc045.jpg spss两因素（有一个连续变量）如何进行方差分析 %}

- 将变量放入各自的框中，从上到下依次是：因变量、固定因素、斜变量（连续变量）

{% asset_img 0df431adcbef76099086355c2edda3cc7dd99e60.jpg spss两因素（有一个连续变量）如何进行方差分析 %}

- 点击model按钮，进入model对话框，在custom模式下，设置type为main effect，将两个变量放入模型

{% asset_img c2fdfc039245d688e1d61e67a4c27d1ed31b2418.jpg spss两因素（有一个连续变量）如何进行方差分析 %}

- 点击options按钮，设置输出的参数，下面第二幅图是设置的参数，如图所示

{% asset_img bd315c6034a85edf8ee151e049540923dc547587.jpg spss两因素（有一个连续变量）如何进行方差分析 %}

{% asset_img 37d3d539b6003af3f8d573a3352ac65c1138b682.jpg spss两因素（有一个连续变量）如何进行方差分析 %}

- 点击ok开始处理数据，并输出结果

{% asset_img 50da81cb39dbb6fd109849e50924ab18962b3735.jpg spss两因素（有一个连续变量）如何进行方差分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
