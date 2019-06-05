---
title: Python教程：[29]读取
date: 2015-08-11 18:19:11
tags: [python]
author: mlln.cn
---
我们用python搞数据挖掘，通常要从Excel里读取数据，这就用到了xlrd，下面我们来系统的看一下xlrd的使用方法。（下面的方法介绍了为什么从Excel读取的数据是乱码，其实就是编码的问题。）

- 先导入xlrd模块

{% asset_img 476217f7905298223eebded5d5ca7bcb0b46d489.jpg Python教程：[29]读取 %}

- 打开指定路径的Excel文件，Excel这个变量存放的是Excel文件的路径

{% asset_img 99636c0e0cf3d7ca342ed860f01fbe096a63a989.jpg Python教程：[29]读取 %}

- 介绍两种获取sheet对象的方法，第一个俄式通过索引获取第一个sheet

{% asset_img 7a8a1446f21fbe093886240269600c338644ad89.jpg Python教程：[29]读取 %}

- 通过sheet的名称获取

{% asset_img 6a22e8246b600c33d0a139de184c510fd8f9a189.jpg Python教程：[29]读取 %}

- 根据坐标来获取单元格的值，我们看到cv在python当中的编码，但是打印出来的话就是正常显示的了。

{% asset_img ae10eddeb48f8c543551223938292df5e1fe7fe3.jpg Python教程：[29]读取 %}

- 我们还可以读取整行的数据

{% asset_img bd70426034a85edf260e19354b540923dc5475e3.jpg Python教程：[29]读取 %}

- 从读取整整行数据中获得第一个值

{% asset_img cbc17b380cd79123ef387362af345982b3b78089.jpg Python教程：[29]读取 %}

- 当然，我们还可以获取sheet中有多少行和多少列。

{% asset_img d1e312f431adcbeff7ec9910aeaf2edda2cc9f89.jpg Python教程：[29]读取 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
