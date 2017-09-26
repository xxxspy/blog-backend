---
title: Python教程：[41]判断抓取的网页的编码方式
date: 2016-05-15 18:05:03
tags: [python]
author: mlln.cn
---
在抓取网页的时候经常遇到网页编码问题，我们需要将抓取的网页进行解码以后才能正确得到网页上的 内容，那么怎么获取网页的编码方式呢？很多人还在手动去查看网页源码，然后找到charset吗？下面是百度经验的编辑器页面的编码方式。

- 引入两个模块，urllib2用于获取源码，chardet用于检测编码方式

{% asset_img 507c389759ee3d6d7a8957d741166d224f4ade24.jpg Python教程：[41]判断抓取的网页的编码方式 %}

- 先获取网页，存放于f中

{% asset_img 8367d1fc1e178a824434afbcf403738da977e860.jpg Python教程：[41]判断抓取的网页的编码方式 %}

- 读取网页的内容，存放在txt中

{% asset_img f7426d8da9773912b02d557dfa198618367ae260.jpg Python教程：[41]判断抓取的网页的编码方式 %}

- 使用detect方法来获得网页的编码方式

{% asset_img eab9044c510fd9f99e588575272dd42a2834a424.jpg Python教程：[41]判断抓取的网页的编码方式 %}

- 我们读取一下网页编码方式：

{% asset_img 8697397f9e2f07083b0efa1ceb24b899a901f260.jpg Python教程：[41]判断抓取的网页的编码方式 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
