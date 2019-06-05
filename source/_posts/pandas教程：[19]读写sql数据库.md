---
title: pandas教程：[19]读写sql数据库
date: 2015-02-17 18:11:17
tags: [pandas]
author: mlln.cn
---
如何从数据库中读取数据到DataFrame中？pandas提供这这样的接口完成此工作——read_sql()。下面我们用离子来说明这个方法。

- 我们要从sqlite数据库中读取数据，引入相关模块

{% asset_img 5beeba0f4bfbfbed3468307a7bf0f736afc31f46.jpg pandas教程：[19]读写sql数据库 %}

- read_sql接受两个参数，一个是sql语句，这个你可能需要单独学习；一个是con（数据库连接）、read_sql直接返回一个DataFrame对象
打印一下，可以看到已经成功的读取了数据

{% asset_img d019d2bf6c81800a41348e0bb23533fa838b47a6.jpg pandas教程：[19]读写sql数据库 %}

{% asset_img f7426d8da977391207178364fb198618367ae247.jpg pandas教程：[19]读写sql数据库 %}

- 我们还可以使用index_col参数来规定将那一列数据设置为index
结果输出为：

{% asset_img 79b1e936afc37931af59802ce8c4b74543a91146.jpg pandas教程：[19]读写sql数据库 %}

{% asset_img b110e6198618367a63b879d82d738bd4b31ce547.jpg pandas教程：[19]读写sql数据库 %}

- 当然，我们可以设置多个index，只要将index_col的值设置为列表
输出结果为：

{% asset_img b258f5c4b74543a9282afcc91d178a82b9011446.jpg pandas教程：[19]读写sql数据库 %}

{% asset_img 718e25c79f3df8dcbeec8894ce11728b461028a6.jpg pandas教程：[19]读写sql数据库 %}

- 写入数据库也很简单，下面第二句用于删除数据库中已有的表"weather_2012"，然后将df保存到数据库中的"weather_2012"表

{% asset_img 83cab81ea8d3fd1f21d8a53f334e251f94ca5fa6.jpg pandas教程：[19]读写sql数据库 %}

- 假如我们使用的是mysql数据库也没问题，我们只需要建立与mysql的连接即可，用下面的con代替上面的con可以达到的效果相同。

{% asset_img cebd00178a82b901e59cc536708da9773912ef47.jpg pandas教程：[19]读写sql数据库 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
