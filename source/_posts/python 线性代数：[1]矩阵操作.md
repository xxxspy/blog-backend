---
title: python 线性代数：[1]矩阵操作
date: 2016-05-11 18:11:19
tags: [python]
author: mlln.cn
---
今天是这一个系列入门教程的第一篇，简单介绍一下python中是如何操作maxtrix（矩阵）的，然后我们后面就开始用python中的numpy来解决线性代数的问题，比如解方程等，下面我们开始吧：

- 我先引入numpy，以后的教程中，我们都引用为np作为简写

{% asset_img 3c2c4bfbb2fb431647d6a28a22a4462308f7d332.jpg python 线性代数：[1]矩阵操作 %}

- 使用mat函数创建一个2X3矩阵

{% asset_img aa59892bd40735fa34b98b499c510fb30e2408b2.jpg python 线性代数：[1]矩阵操作 %}

- 使用shape可以获取矩阵的大小

{% asset_img 0e655ca7d933c8950b375d8bd31373f0830200b2.jpg python 线性代数：[1]矩阵操作 %}

- 使用下标读取矩阵中的元素

{% asset_img e49cf91190ef76c6dc473edb9f16fdfaae51676e.jpg python 线性代数：[1]矩阵操作 %}

- 进行行列转换：

{% asset_img 263e802f07082838164519e4ba99a9014d08f1b3.jpg python 线性代数：[1]矩阵操作 %}

- 实际上官方文档建议我们使用二维数组代替矩阵来进行矩阵运算；因为二维数组用得较多，而且基本可取代矩阵。比如：可见矩阵和数组基本上都可以

{% asset_img 0865b518972bd407e5c3170d79899e510eb309ff.jpg python 线性代数：[1]矩阵操作 %}

{% asset_img c9d4cf43ad4bd113afc973c258afa40f4afb05ff.jpg python 线性代数：[1]矩阵操作 %}

- 加减法也是一样的：

{% asset_img 7ab514d162d9f2d3426fe01fabec8a136227cc81.jpg python 线性代数：[1]矩阵操作 %}

- 当然列表是不能这么尽兴加减的：

{% asset_img 99636c0e0cf3d7ca4b83fb86f01fbe096a63a98e.jpg python 线性代数：[1]矩阵操作 %}

- 好啦，我们今天就介绍到这里啦，下一篇继续哈。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
