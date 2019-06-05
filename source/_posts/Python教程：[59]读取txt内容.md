---
title: Python教程：[59]读取txt内容
date: 2016-09-23 18:15:19
tags: [python]
author: mlln.cn
---
前三篇文章主要将写入txt，今天我们讲读取txt，读取txt其实就是以r模式打开txt文件，然后读取其内容，下面看一下代码吧：

- 以可读模式打开txt文件：

{% asset_img 55a628d12f2eb9387f1b3072d7628535e4dd6ff9.jpg Python教程：[59]读取txt内容 %}

- 读取第一行内容，保存在line中，然后打印出line

{% asset_img 8474fbdde71190ef9dffd85fcc1b9d16fcfa60ef.jpg Python教程：[59]读取txt内容 %}

- 通过循环就能读出所有行：注意readine每调用一次就会读取下一行

{% asset_img 9c57e3faaf51f3de46b6f3e496eef01f3b2979ef.jpg Python教程：[59]读取txt内容 %}

- 还可以使用这个方法读取所有的行

{% asset_img ae10eddeb48f8c5460d78faf38292df5e1fe7fef.jpg Python教程：[59]读取txt内容 %}

- 速度更快的方法是直接使用多行读取的方法：readlines，参数5表示读取5行

{% asset_img 8d158aeef01f3a29dacc9f4e9b25bc315d607cef.jpg Python教程：[59]读取txt内容 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
