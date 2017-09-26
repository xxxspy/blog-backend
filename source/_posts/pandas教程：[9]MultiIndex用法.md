---
title: pandas教程：[9]MultiIndex用法
date: 2015-05-15 18:19:15
tags: [pandas]
author: mlln.cn
---
在pandas的DataFrame中经常使用多个索引，在pandas中成为MultiIndex对象，这篇文章介绍一下MultiIndex创建和使用方法：

- 引入所有需要的模块

{% asset_img 1f569482b9014a90cb5cd5a8aa773912b31bee02.jpg pandas教程：[9]MultiIndex用法 %}

- 创建两个<type 'numpy.ndarray'>对象，分别为colors和foods

{% asset_img 2cb4fefe9925bc318f3c928d5ddf8db1cb137007.jpg pandas教程：[9]MultiIndex用法 %}

- 打印出这两个数组来查看一下，注意tm.choice创建的数组是随机的，你利用同样的代码创建的数组和我的可能不一样

{% asset_img 207ea60e7bec54e78f92890bba389b504fc26a6e.jpg pandas教程：[9]MultiIndex用法 %}

- 创建MultiIndex对象，然后创建DataFrame对象（其中使用index=index参数）

{% asset_img 55a628d12f2eb9382713e9e7d6628535e5dd6f6e.jpg pandas教程：[9]MultiIndex用法 %}

- 打印一下df看看里面的数据：有两个索引color和food

{% asset_img 570f8c58d109b3de43de777dcfbf6c81800a4c07.jpg pandas教程：[9]MultiIndex用法 %}

- 如何利用索引来筛选数据：使用query（）
结果为：

{% asset_img ae10eddeb48f8c5458ad563a39292df5e0fe7f6e.jpg pandas教程：[9]MultiIndex用法 %}

{% asset_img b29f8282d158ccbf8edd262f1ad8bc3eb1354107.jpg pandas教程：[9]MultiIndex用法 %}

- 还可以在分组中使用索引，使用了level参数
打印结果为：

{% asset_img 1899a23eb13533fa6ad7003babd3fd1f41345b07.jpg pandas教程：[9]MultiIndex用法 %}

{% asset_img 4075890a304e251f659677eda486c9177f3e5307.jpg pandas教程：[9]MultiIndex用法 %}

- 删除或者更改索引的名称：如果删除了名称，我们只能使用ilevel_0表示第一个索引
打印结果为：

{% asset_img b29f8282d158ccbf8ec2262f1ad8bc3eb135416e.jpg pandas教程：[9]MultiIndex用法 %}

{% asset_img 7e7f7909c93d70cfc39b3918fbdcd100baa12b07.jpg pandas教程：[9]MultiIndex用法 %}

- 分组中也是一样，删除掉索引名称以后，只能使用数字1表示第二个索引
打印结果为：

{% asset_img 73ca5910b912c8fcc19365d8ff039245d6882107.jpg pandas教程：[9]MultiIndex用法 %}

{% asset_img b853d6fcc3cec3fdf85e3460d588d43f87942707.jpg pandas教程：[9]MultiIndex用法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
