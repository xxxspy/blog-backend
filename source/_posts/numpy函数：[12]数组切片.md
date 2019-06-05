---
title: numpy函数：[12]数组切片
date: 2016-10-19 18:05:11
tags: [numpy]
author: mlln.cn
---
我们可以向使用列表切片一样使用数组切片，如果会使用liest切片，那么这篇文章就是温习一下而已，下面我们来看看具体的数组切片是如何使用的。

- 从numpy中引入所有

{% asset_img c71d0e385343fbf21a8108bcb27eca8064388f45.jpg numpy函数：[12]数组切片 %}

- 创建一个包含10个元素的一位数组

{% asset_img d1571724ab18972bf1a4ae55e4cd7b899f510a57.jpg numpy函数：[12]数组切片 %}

- 我们可以使用一个下标获取数组中相应的值，也可以更改它的值

{% asset_img b3508d13b07eca80c9a89778932397dda0448345.jpg numpy函数：[12]数组切片 %}

- 使用冒号获取连续的几个元素，如获取第四个到第五个元素

{% asset_img 34bbf8cd7b899e512510948b40a7d933c9950d57.jpg numpy函数：[12]数组切片 %}

- 省略冒号前的数字，表示从头开始

{% asset_img 43e6c733c895d1439de84abc71f082025baf0757.jpg numpy函数：[12]数组切片 %}

- 使用负数表示从后往前数，-1表示从后往前数第一个数

{% asset_img 30ecd5ef76094b36163fb572a1cc7cd98c109d45.jpg numpy函数：[12]数组切片 %}

- -2表示从后往前第二个，以此类推

{% asset_img a28d62d98d1001e9f991ba90ba0e7bec55e79745.jpg numpy函数：[12]数组切片 %}

{% asset_img b258f5c4b74543a9c18554531c178a82b8011457.jpg numpy函数：[12]数组切片 %}

- 还可以设置步长来读取数组元素

{% asset_img b6045da98226cffc5bb4112dbb014a90f703ea50.jpg numpy函数：[12]数组切片 %}

- 步长为-1，其他参数不设置，就是将数组进行了倒序排列

{% asset_img 1f569482b9014a90bfa0e822ab773912b21bee50.jpg numpy函数：[12]数组切片 %}

- 使用负数步长需要让第一个下表大于第二个下标

{% asset_img a005b3345982b2b7635e905b33adcbef77099b29.jpg numpy函数：[12]数组切片 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
