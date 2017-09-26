---
title: pandas教程：[8]数据分组
date: 2016-05-19 18:01:19
tags: [pandas]
author: mlln.cn
---
使用groupby()可以给数据分组，数据分组的好处是你可以一次性计算得到所有分组中的统计量，比如想计算男女学生的平均成绩分别是多少，可以先按照男女分组，然后计算平均数，我们不用计算完女生然后在计算男生，实际上是一次性完成的，这就是分组的好处。

- 先引入模块，并创建一个DataFrame

{% asset_img 6398ecd3572c11dfa2e57637602762d0f703c2ab.jpg pandas教程：[8]数据分组 %}

- 打印出DataFrame来查看一下结果

{% asset_img 109eb7ec8a1363276cd90b27928fa0ec08fac7ab.jpg pandas教程：[8]数据分组 %}

- 我们可以以A列进行分组，使用groupby

{% asset_img 504ec7f9d72a605911f62f0e2b34349b023bba85.jpg pandas教程：[8]数据分组 %}

- 打印出来的grouped.first()为每一组的第一行数据

{% asset_img 90cebeec08fa513d329ea5ca3e6d55fbb2fbd9ab.jpg pandas教程：[8]数据分组 %}

- 我们还可以以两列以上进行分组，groupby参数为一个列表

{% asset_img 3c2c4bfbb2fb4316772bb36e23a4462309f7d3ab.jpg pandas教程：[8]数据分组 %}

- 打印出来的是这样的情况，last表示每一组的最后一行数据

{% asset_img 734f12f3d7ca7bcb2f4f0e3bbd096b63f624a8ab.jpg pandas教程：[8]数据分组 %}

- 我们还可以根据列来分组，先创建一个get_type函数，如果列名为abem中之一，就分为组别vowel，反之为consonant

{% asset_img 346bd85c10385343bd2949359013b07ecb808885.jpg pandas教程：[8]数据分组 %}

- 打印第一组看看分组情况。

{% asset_img 6a2112338744ebf83445ad2bdaf9d72a6059a7ab.jpg pandas教程：[8]数据分组 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
