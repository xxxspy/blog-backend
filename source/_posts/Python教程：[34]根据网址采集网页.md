---
title: Python教程：[34]根据网址采集网页
date: 2015-02-15 18:15:19
tags: [python]
author: mlln.cn
---
做数据分析的工作，大部分时间不是在处理数据而是在收集数据，使用python可以手机网页数据，今天我们就教给大家如何使用python的urllib2来获取网页源码，这是最简单的获取网页源码的方法，以后我们会逐步加大难度。

- 引入模块urllib2

{% asset_img d7c9ca3f8794a4c2634a413c0cf41bd5ad6e3978.jpg Python教程：[34]根据网址采集网页 %}

- 设置要采集的地址

{% asset_img 0fb505d5ad6eddc4758e12ec3bdbb6fd52663378.jpg Python教程：[34]根据网址采集网页 %}

- 使用urlopen方法来返回网页文件

{% asset_img 509b9fcb39dbb6fd7a3243310b24ab18972b3778.jpg Python教程：[34]根据网址采集网页 %}

- 只能使用read方法来获得网页文件的内容

{% asset_img ac0acf1373f0820266b9372849fbfbedab641bba.jpg Python教程：[34]根据网址采集网页 %}

- 看一下f的长度就知道是否真的返回了网页

{% asset_img a54e55fbfbedab644259ebd7f536afc379311eba.jpg Python教程：[34]根据网址采集网页 %}

- 避免这样去看f的内容，你会疯掉的。

{% asset_img d5462bfae6cd7b89af059c940d2442a7d9330e78.jpg Python教程：[34]根据网址采集网页 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
