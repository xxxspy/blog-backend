---
title: Excel2013：[27]RANK函数计算排名
date: 2016-02-19 18:11:05
tags: [excel]
author: mlln.cn
---
经常会遇到排名的问题，我们可以使用排序的方法来得到排名，但是很多时候我们会用到美式排序法，当出现相同分数的时候名次不再连续，下面我们会演示这种情况。

- 首先，先看看原始的数据，想要对这一列数据进行排名，得到名次

{% asset_img 1f569482b9014a90add4fac4ab773912b21beea6.jpg Excel2013：[27]RANK函数计算排名 %}

- 在b2单元格输入公式=rank(a2,a$2:a$19),第一个参数表示求谁的名字；第二个参数表示在那个范围内求名次

{% asset_img 4bd1e803738da97767c53a52b251f8198718e3a6.jpg Excel2013：[27]RANK函数计算排名 %}

- 我们看到这个公式求得的名次

{% asset_img b3508d13b07eca80d811869e932397dda1448370.jpg Excel2013：[27]RANK函数计算排名 %}

- 我们使用快速填充的方法，拖动单元格，将其他单元格填充好

{% asset_img 58c3acb7d0a20cf4f68441a674094b36acaf9970.jpg Excel2013：[27]RANK函数计算排名 %}

- 名次排名就得到了，假如出现第五名是重复的，那么第六名就没有了，从第七名开始了

{% asset_img 6398ecd3572c11dfd63b035a612762d0f603c2a6.jpg Excel2013：[27]RANK函数计算排名 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
