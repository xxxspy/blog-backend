---
title: pandas教程：[3]DataFrame切片操作
date: 2015-04-15 18:03:17
tags: [pandas]
author: mlln.cn
---
DataFrame数据框允许我们使用iloc方法来像操作array（数组）一样对DataFrame进行切片操作，其形式上，跟对数组进行切片是一样的，我们下面来演示一下一些典型的切片操作：

- 先创建一个6行4列的DataFrame数据框

{% asset_img 4e83cb628535e5dd397819eb75c6a7efce1b626b.jpg pandas教程：[3]DataFrame切片操作 %}

- 使用iloc方法，提取第四行数据：

{% asset_img 4abae5edab64034f33d47e32acc379310a551dad.jpg pandas教程：[3]DataFrame切片操作 %}

- 我们可以看一下，这种方法得到的返回值是一个series数据

{% asset_img 79b1e936afc3793145713a1de8c4b74543a911ad.jpg pandas教程：[3]DataFrame切片操作 %}

- 返回4-5行，1-2列数据，用下面的写法，你可以看到跟array的切片操作是一模一样的额

{% asset_img b5ce925494eef01fd140a4f1e3fe9925bc317d6b.jpg pandas教程：[3]DataFrame切片操作 %}

- 我们也可以提取不连续行和列的数

{% asset_img 1f569482b9014a90ac27fa89aa773912b31beeae.jpg pandas教程：[3]DataFrame切片操作 %}

- 想要提取某一样或者某几行的数据，保证所有列都在，可以使用一个冒号来表示所有列

{% asset_img 72ccb7773912b31bef75711d8518367adab4e1ae.jpg pandas教程：[3]DataFrame切片操作 %}

- 当然，所有行，也可以用冒号来表示

{% asset_img b110e6198618367ab990c3e92d738bd4b31ce5ae.jpg pandas教程：[3]DataFrame切片操作 %}

- 提取某一个值，去掉所有冒号，比如取第2行第2列的这个数

{% asset_img d019d2bf6c81800a18b2353ab23533fa828b476b.jpg pandas教程：[3]DataFrame切片操作 %}

- 当然，iat是专门提取某个数的方法，它的效率高更高，因此建议在提取单个数的时候用iat

{% asset_img 8640bf8b87d6277ff20b8e0c2b381f30e924fcae.jpg pandas教程：[3]DataFrame切片操作 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
