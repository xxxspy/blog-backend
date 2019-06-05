---
title: python教程：[74]列表排序
date: 2015-10-03 18:15:15
tags: [python]
author: mlln.cn
---
列表排序，做数据经常用到的一个方法，在python中想实现排序有时候觉得挺难，比如按照行排序或按照列排序，写起来都不简单，今天在这里总结一下在python中实现排序的所有方法，如有不全，请下面留言。

- 最简单的排序莫过于直接使用sort对一维的列表排序，创建一个列表

{% asset_img 1cd4147b02087bf4bfd92fddf1d3572c11dfcf8a.jpg python教程：[74]列表排序 %}

- 使用sort就地排序（就地排序就是改变了原始list的排序，而sorted不改变原始list数据）

{% asset_img 29790130e924b899073c010c6d061d950a7bf647.jpg python教程：[74]列表排序 %}

- 可以使用reverse参数进行反向排序。

{% asset_img a84052086e061d95b8464f0c78f40ad162d9ca47.jpg python教程：[74]列表排序 %}

- 创建一个二维列表

{% asset_img 425773224f4a20a48a2b44f393529822720ed08a.jpg python教程：[74]列表排序 %}

- 使用operator进行排序，还是sort方法，使用key参数，下面根据第二列数据排序

{% asset_img 8b527d2762d0f7032eb2ede80bfa513d2697c547.jpg python教程：[74]列表排序 %}

- 多维排序，先根据第一列排序，然而第二列，然后第三列

{% asset_img 425773224f4a20a48a1e44f393529822720ed047.jpg python教程：[74]列表排序 %}

- lambda用于写匿名函数，根据第二列数据排序，x表示列表中的元素，x[1]表示元素中的第二个值

{% asset_img eab9044c510fd9f937222d5d262dd42a2834a48a.jpg python教程：[74]列表排序 %}

- 反向排序

{% asset_img d56b3634349b033bbcbd84ee16ce36d3d539bd8a.jpg python教程：[74]列表排序 %}

- 元组排序和list排序一样，当然还可以对object构成的列表排序，下面创建一个元组构成的列表

{% asset_img 3792cb39b6003af3d48fa454362ac65c1038b68a.jpg python教程：[74]列表排序 %}

- 使用operator

{% asset_img 3bc6f750352ac65ce2301e47f8f2b21193138a8a.jpg python教程：[74]列表排序 %}

- 使用lambda

{% asset_img 35da1d3b5bb5c9eafcf37bd7d639b6003af3b347.jpg python教程：[74]列表排序 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
