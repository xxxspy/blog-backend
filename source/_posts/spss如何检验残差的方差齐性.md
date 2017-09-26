---
title: spss如何检验残差的方差齐性
date: 2015-09-19 18:23:17
tags: [spss]
author: mlln.cn
---
残差的方差齐性是回归分析要满足的一个条件， 通常我们要用散点图来检验残差的方差齐性，根据散点图可以看到标准化的残差随着估计值的变化趋势，下面是具体的分析方法：
工具/原料


- spss20.0
方法/步骤


- 打开线性回归的对话框：analyse--regression--linear

{% asset_img 35a85edf8db1cb137eac61d7dd54564e93584b28.jpg spss如何检验残差的方差齐性 %}

- 在回归分析中， 将GDP作为因变量，其他的变量可以作为自变量，将这些变量放入各自的框中

{% asset_img f11f3a292df5e0feb66ad5c55c6034a85fdf7287.jpg spss如何检验残差的方差齐性 %}

- 点击plot按钮，打开图标的设置对话框

{% asset_img 34fae6cd7b899e5173eb66d042a7d933c9950d88.jpg spss如何检验残差的方差齐性 %}

- 将如图所示的选项勾选，这是散点图，我们可以看到残差随着估计值的变化趋势

{% asset_img 3b87e950352ac65ce7413ab7fbf2b21192138aaa.jpg spss如何检验残差的方差齐性 %}

- 我们看到这就是需要的散点图，纵坐标是标准化的参差值，横坐标是估计值，如果散点图拟合的直线平行于横坐标，那么就可以认为残差是齐性的。

{% asset_img 9922720e0cf3d7caa34f63b2f21fbe096a63a9bd.jpg spss如何检验残差的方差齐性 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
