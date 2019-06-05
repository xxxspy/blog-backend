---
title: DataNitro：[4]CellRange对象
date: 2016-07-01 18:01:03
tags: [datanitro]
author: mlln.cn
---
CellRange在之前介绍过，我们大概也知道CellRange就是几个单元格组成的区域，今天来系统地看一下CellRange有哪些方法和属性。

- 创建或者获取一个CellRange，我们可以用这些写法：注意print只是我为了输出这些CellRange的名字，与今天的学习内容无关。下面三种写法意义相同。

{% asset_img b94f65ec54e736d1fb7b355a98504fc2d562693d.jpg DataNitro：[4]CellRange对象 %}

- 上一种写法代表了一个连续区域，下面的写法代表不连续区域：

{% asset_img 7d98931001e93901eee5346c78ec54e737d196ba.jpg DataNitro：[4]CellRange对象 %}

- 通过名称获取一个区域：

{% asset_img 9f6e190828381f30856335fbaa014c086e06f02f.jpg DataNitro：[4]CellRange对象 %}

- 我们还可以指明区域所在的sheet

{% asset_img 5327ce160924ab18a639596536fae6cd7b890b71.jpg DataNitro：[4]CellRange对象 %}

- 迭代的方式输出所有单元格：

{% asset_img a75fb6d3fd1f41349197bd2c261f95cad0c85e84.jpg DataNitro：[4]CellRange对象 %}

- 一个区域内包含多少单元格：可以用len()

{% asset_img 27d647ee3d6d55fb3563ce746e224f4a21a4ddf8.jpg DataNitro：[4]CellRange对象 %}

- 像列表一样，我们可以使用索引来得到区域内任意一个单元格：

{% asset_img b29f8282d158ccbf97200d681ad8bc3eb0354181.jpg DataNitro：[4]CellRange对象 %}

- 这篇文章略去的属性有：

- value,formula,color,hyperlink,comment,font，row,col,position,name,sheet，table，这些与Cell属性相同，参考上一篇文章

- 合并两个区域，用加号就好了

{% asset_img 6a22e8246b600c331d16659a194c510fd9f9a132.jpg DataNitro：[4]CellRange对象 %}

- 将Cell添加进CellRange

{% asset_img cf5a8316fdfaaf51128b3aed8f5494eef01f7a3d.jpg DataNitro：[4]CellRange对象 %}

- 将Cell从CellRange中删除：

{% asset_img 72ccb7773912b31beaca767b8518367adbb4e1fb.jpg DataNitro：[4]CellRange对象 %}

- 其他方法：

- 如：claer,copy_from,copy_format_from,is_empty,set_name等

- #可以参考Cell的方法

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
