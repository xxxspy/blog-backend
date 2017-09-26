---
title: spss中拉丁方设计如何进行方差分析
date: 2015-09-23 18:15:19
tags: [spss]
author: mlln.cn
---
 
工具/原料


- spss
方法/步骤


- 首先打开spss，以如图所示的方式录入数据，week和day是两个需要控制的变量，music是自变量，score是因变量

{% asset_img 242dd42a2834349b2b1d7744c9ea15ce37d3bed3.jpg spss中拉丁方设计如何进行方差分析 %}

- 数据准备好以后，在菜单栏上执行：analyse--GLM--univariate，打开方差分析对话框

{% asset_img 63d9f2d3572c11df55bba6e2632762d0f603c28d.jpg spss中拉丁方设计如何进行方差分析 %}

- 打开对话框以后，先将自变量和因变量放入各自的位置，如图所示

{% asset_img 6a600c338744ebf805d87dfed9f9d72a6159a741.jpg spss中拉丁方设计如何进行方差分析 %}

- 点击model按钮，设置一下模型

{% asset_img b151f8198618367a3b2e661c2e738bd4b21ce548.jpg spss中拉丁方设计如何进行方差分析 %}

- 系统默认的是full factorial，我们要勾选custom

{% asset_img c2cec3fdfc0392457688f9ce8794a4c27d1e2535.jpg spss中拉丁方设计如何进行方差分析 %}

- 将三个自变量放入右侧的model框中

{% asset_img cdbf6c81800a19d8c3399cc433fa828ba61e463c.jpg spss中拉丁方设计如何进行方差分析 %}

- 将type设置为main effect ，因为我们默认这三个变量是没有交互作用的

{% asset_img a044ad345982b2b792a9210531adcbef76099b38.jpg spss中拉丁方设计如何进行方差分析 %}

- 返回到主菜单，点击ok开始运行数据处理，并输出结果

{% asset_img a8014c086e061d95f9622ff97bf40ad163d9cacf.jpg spss中拉丁方设计如何进行方差分析 %}

- 我们看方差检验的结果，三个变量中，music和day对应的sig值小于0.05，说明这两个变量的效应是显著的。

{% asset_img 63d0f703918fa0ec0a9e7ccc269759ee3c6ddb91.jpg spss中拉丁方设计如何进行方差分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
