---
title: pandas教程：[7]筛选计数统计
date: 2016-03-03 18:01:03
tags: [pandas]
author: mlln.cn
---
上一篇我们讲了pandas实现的一个简单的计数统计，今天我们还是针对同样的数据，统计一下各个专业高考成绩在520以上的学生个数和百分比。下面看看具体的实现过程：

- 先引入pandas，然后读取csv数据

{% asset_img f7426d8da9773912f48c1072fb198618367ae238.jpg pandas教程：[7]筛选计数统计 %}

- 我们先筛选出高考成绩在520以上的学生

{% asset_img 8759287adab44aed60e42bf7b01c8701a18bfb38.jpg pandas教程：[7]筛选计数统计 %}

- print打印数据的前三行为：

{% asset_img 4d4970061d950a7b629fdbd709d162d9f2d3c938.jpg pandas教程：[7]筛选计数统计 %}

- 然后根据得到的good数据，统计各个专业学生的人数

{% asset_img dbf554ed2e738bd4e38b2722a28b87d6277ff938.jpg pandas教程：[7]筛选计数统计 %}

- 利用print来查看结果

{% asset_img 0b3a1c087bf40ad1014e52f0542c11dfa9ecce38.jpg pandas教程：[7]筛选计数统计 %}

- 计算总体中各个专业的人数

{% asset_img 8640bf8b87d6277fcbb8a72b2b381f30e924fc38.jpg pandas教程：[7]筛选计数统计 %}

- 利用print查看统计结果

{% asset_img 34bbf8cd7b899e512b0eaf0741a7d933c9950de5.jpg pandas教程：[7]筛选计数统计 %}

- 最后，我们需要计算百分比，直接利用矩阵的除法即可

{% asset_img 389aa8fd5266d01615990b3b942bd40734fa35e5.jpg pandas教程：[7]筛选计数统计 %}

- 利用print输出结果

{% asset_img 109eb7ec8a13632708475720928fa0ec08fac738.jpg pandas教程：[7]筛选计数统计 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
