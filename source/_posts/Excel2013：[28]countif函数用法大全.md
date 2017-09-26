---
title: Excel2013：[28]countif函数用法大全
date: 2015-07-23 18:23:23
tags: [excel]
author: mlln.cn
---
countif函数时我们经常用到的函数之一，经过组合它可以求得任何我们想要的计数结果，下面是具体的用法：

- 假如我们要统计男女生的人数，我们可以在E5单元格输入公式=COUNTIF(A2:A21,"男")；公式中A2:A21是我们计数的范围，第二个参数“男”表示对单元格中为男的计数

{% asset_img 61183b2dd42a28344b75b77259b5c9ea14cebfbd.jpg Excel2013：[28]countif函数用法大全 %}

- 同样的，在F5单元格输入公式也可以求得女生人数：=COUNTIF(A2:A21,"女")

{% asset_img d56b3634349b033bda5b7da317ce36d3d439bdbd.jpg Excel2013：[28]countif函数用法大全 %}

- 假如我们要统计成绩大于60的人数

{% asset_img 35da1d3b5bb5c9ea9620829ad739b6003bf3b3bd.jpg Excel2013：[28]countif函数用法大全 %}

- 我们可以在单元格中输入公式=COUNTIF(B2:B21,">=60")

{% asset_img dc15484e9258d10963cf29cbd358ccbf6c814d58.jpg Excel2013：[28]countif函数用法大全 %}

- 假如我们要计算一个区间内的人数，我们可以使用两个countif函数，运用减法就可以算出来，下面是计算成绩在60到65之间的个数

{% asset_img 9dc3cf58ccbf6c81551bac91be3eb13533fa4058.jpg Excel2013：[28]countif函数用法大全 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
