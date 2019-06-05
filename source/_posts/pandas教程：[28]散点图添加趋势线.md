---
title: pandas教程：[28]散点图添加趋势线
date: 2016-07-05 18:15:15
tags: [pandas]
author: mlln.cn
---
上一篇文章我们介绍了绘制散点图的过程，现在我们要给散点图添加一个趋势线，从而直观的看到数据的变化趋势，下面来看看具体的过程：

- 引入相关的模块

{% asset_img d7c9ca3f8794a4c20871e95a0df41bd5ad6e3935.jpg pandas教程：[28]散点图添加趋势线 %}

- 读取数据，并打印出来前五行数据
这是我们看到的数据

{% asset_img aa251d4f78f0f73634cb42700955b319ebc4134e.jpg pandas教程：[28]散点图添加趋势线 %}

{% asset_img 389aa8fd5266d016884b9059942bd40735fa3535.jpg pandas教程：[28]散点图添加趋势线 %}

- 使用ols进行回归拟合，实际上是建立了parent为自变量的线性回归方程

{% asset_img 8367d1fc1e178a821f0971d1f503738da977e84f.jpg pandas教程：[28]散点图添加趋势线 %}

- 先绘制一个简单的散点图

{% asset_img 734f12f3d7ca7bcbec4ec95ebd096b63f624a84f.jpg pandas教程：[28]散点图添加趋势线 %}

- 接着绘制拟合直线

{% asset_img d872d695d143ad4b417c48b181025aafa40f0635.jpg pandas教程：[28]散点图添加趋势线 %}

- 查看绘制出来的图

{% asset_img 1b0d4f0fd9f9d72a93511e6cd72a2834349bbb4f.jpg pandas教程：[28]散点图添加趋势线 %}

- 上面第六步用到了lm.fittedvalues，他其实是一个Series（根据回归方程得到的预测值），我们来查看一下它的数据和类型。

{% asset_img d66b7e59252dd42ade3c0fda003b5bb5c9eab84f.jpg pandas教程：[28]散点图添加趋势线 %}

{% asset_img c8ab0bce36d3d539480801b23987e950352ab04f.jpg pandas教程：[28]散点图添加趋势线 %}

- 最后绘制得到的散点图（带趋势线）是酱紫的。

{% asset_img 11794d43fbf2b2119b1a8b3fc98065380cd78e4f.jpg pandas教程：[28]散点图添加趋势线 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
