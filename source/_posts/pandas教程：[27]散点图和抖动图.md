---
title: pandas教程：[27]散点图和抖动图
date: 2015-04-19 18:17:23
tags: [pandas]
author: mlln.cn
---
拿到一个数据我们首先想到的是绘制散点图查看数据的基本分布情况，那么在Python.pandas中，如何绘制散点图呢？散点图的缺陷是什么，为什么要绘制抖动图呢？

- 先引入相应的模块

{% asset_img b25d9901a18b87d6333d7e6f040828381f30fd00.jpg pandas教程：[27]散点图和抖动图 %}

- 读取数据到数据框df
打印出前5行数据，可以看到有两列数据，分别是 孩子的身高和父母的身高

{% asset_img 1e71f724b899a901504a8e461e950a7b0208f500.jpg pandas教程：[27]散点图和抖动图 %}

{% asset_img 3790312eb9389b50ccbb35228635e5dde7116e3f.jpg pandas教程：[27]散点图和抖动图 %}

- 先绘制一个散点图，x轴为孩子的身高，y轴为父母的身高，将绘制得到的图片保存在D盘下的plot.png文件

{% asset_img 969cbf44ad345982dfce30e20ff431adcbef843f.jpg pandas教程：[27]散点图和抖动图 %}

- 我们可以看到得到的图片是酱紫的，由于数据点重合在了一起，所以我们看到的散点图很规整，但却隐藏了规律，于是我们想到用到抖动的方法，绘制抖动图

{% asset_img 08b68e529822720e32b1378a78cb0a46f21fab00.jpg pandas教程：[27]散点图和抖动图 %}

- 我们看可以实现抖动的函数：所谓的抖动就是让数据点发生微小的位移，也就是略微改变数据的值，使得数据点不能完全重合，抖动距离的大小用下面函数中的factor参数来决定。

{% asset_img d1e312f431adcbef0470ab76afaf2edda3cc9f3f.jpg pandas教程：[27]散点图和抖动图 %}

- 利用上面的函数对df进行处理

{% asset_img f392492c11dfa9eca251836761d0f703918fc100.jpg pandas教程：[27]散点图和抖动图 %}

- 我们看得到的数据df2是酱紫的：

{% asset_img 27d647ee3d6d55fb86b9a3566e224f4a20a4dd00.jpg pandas教程：[27]散点图和抖动图 %}

- 现在接着绘制一个散点图，生成的就是抖动图了。alpha参数指的是数据点的透明度

{% asset_img 6391e903918fa0ec26b8b17d259759ee3d6ddb00.jpg pandas教程：[27]散点图和抖动图 %}

- 从这个图中我们可以清楚的看到，颜色比较深、数据比较多的点和颜色比较浅、数据比较少的点的位置。

{% asset_img 61183b2dd42a283466d9e37b58b5c9ea15cebf00.jpg pandas教程：[27]散点图和抖动图 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
