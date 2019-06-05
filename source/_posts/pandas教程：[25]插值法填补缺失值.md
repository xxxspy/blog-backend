---
title: pandas教程：[25]插值法填补缺失值
date: 2015-05-15 18:11:15
tags: [pandas]
author: mlln.cn
---
使用插值法可以计算缺失值的估计值，所谓的插值法就是通过两点（x0，y0），（x1，y1）估计中间点的值，假设y=f(x)是一条直线，通过已知的两点来计算函数f(x),然后只要知道x就能求出y，以此方法来估计缺失值。当然我们也可以假设f（x)不是直线，二是其他函数。

- 引入相关模块并创建一个数据框
数据框的内容为：
‘

{% asset_img 62667cd0f703918f03ed62cd523d269759eec4be.jpg pandas教程：[25]插值法填补缺失值 %}

{% asset_img 0865b518972bd40763af8cfa78899e510fb30909.jpg pandas教程：[25]插值法填补缺失值 %}

- 使用插值法估计缺失值
输出结果为：

{% asset_img b13fd48065380cd74f81fdeaa244ad34588281df.jpg pandas教程：[25]插值法填补缺失值 %}

{% asset_img 99636c0e0cf3d7cacdca6071f11fbe096b63a9be.jpg pandas教程：[25]插值法填补缺失值 %}

- 我们可以计算一下缺失值实际上上前一个值和后一个值得平均数，因为interpolate（）假设函数是直线形式

- 假如index是数字，我们还可以根据数字来进行插值，用到参数method='values'
比较一下插值的结果与上一个结果的不同之处这时候索引的数值实际上就是用于估计y的x值

{% asset_img dc854fda81cb39dbf9a83851d3160924ab183009.jpg pandas教程：[25]插值法填补缺失值 %}

{% asset_img 7a8a1446f21fbe09d1629c1368600c338744adbe.jpg pandas教程：[25]插值法填补缺失值 %}

- 同样道理，如果index是时间，我们可以用method=time来达到同样的效果
输出结果为：

{% asset_img 54baacfb43166d22e24b4a93452309f79052d2be.jpg pandas教程：[25]插值法填补缺失值 %}

{% asset_img f35ea0096b63f624d76166048444ebf81a4ca3be.jpg pandas教程：[25]插值法填补缺失值 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
