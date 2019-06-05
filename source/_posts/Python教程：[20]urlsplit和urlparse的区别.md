---
title: Python教程：[20]urlsplit和urlparse的区别
date: 2016-06-23 18:05:01
tags: [python]
author: mlln.cn
---
urlsplit和urlparse非常相像，用法基本一致，但是他们有略微的不同，split函数在分割的时候，path和params属性是在一起的，我们看下面的例子。

- 先用urlparse函数来分割url

{% asset_img 55a628d12f2eb938980b2fdfd7628535e5dd6f7d.jpg Python教程：[20]urlsplit和urlparse的区别 %}

{% asset_img d4239b35e5dde71199b416dba5efce1b9d16617d.jpg Python教程：[20]urlsplit和urlparse的区别 %}

- 将结果打印出来

{% asset_img cf5a8316fdfaaf51e385d4928e5494eef01f7a7d.jpg Python教程：[20]urlsplit和urlparse的区别 %}

- 我们看到输出的结果，有params这一项

{% asset_img ae10eddeb48f8c5487b5900238292df5e0fe7f7d.jpg Python教程：[20]urlsplit和urlparse的区别 %}

- 接着使用urlsplit函数，可选参数不能输出，所以只能再前面加了以井号

{% asset_img a75fb6d3fd1f4134a32e5053271f95cad1c85e46.jpg Python教程：[20]urlsplit和urlparse的区别 %}

- 我们比较一下两个结果

- urlparse函数

- urlsplit函数

{% asset_img 310f3b1f95cad1c89ea2a90a7d3e6709c93d5146.jpg Python教程：[20]urlsplit和urlparse的区别 %}

{% asset_img 7e7f7909c93d70cf04e3ff20fadcd100baa12b46.jpg Python教程：[20]urlsplit和urlparse的区别 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
