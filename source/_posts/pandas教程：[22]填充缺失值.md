---
title: pandas教程：[22]填充缺失值
date: 2015-01-01 18:15:23
tags: [pandas]
author: mlln.cn
---
当数据中存在NaN缺失值时，我们可以用其他数值替代NaN，主要用到了DataFrame.fillna()方法，下面我们来看看具体的用法：

- 先来创建一个带有缺失值的数据框
具体数据内容为：

{% asset_img 570f8c58d109b3debac78e6fcfbf6c81800a4c79.jpg pandas教程：[22]填充缺失值 %}

{% asset_img b29f8282d158ccbf45c4df3d1ad8bc3eb1354179.jpg pandas教程：[22]填充缺失值 %}

- 使用0替代缺失值（当然你可以用任意一个数字代替NaN）
输出结果为：

{% asset_img 814b07d8bc3eb1351dbfddbca51ea8d3fd1f4479.jpg pandas教程：[22]填充缺失值 %}

{% asset_img 48151723dd54564eb1728e3eb0de9c82d1584f66.jpg pandas教程：[22]填充缺失值 %}

- 用一个字符串代替缺失值
输出结果为：

{% asset_img a75fb6d3fd1f4134a34f6f79261f95cad1c85e79.jpg pandas教程：[22]填充缺失值 %}

{% asset_img 6dc09e0a19d8bc3e9c1f6ccd818ba61ea8d34566.jpg pandas教程：[22]填充缺失值 %}

- 用前一个数据代替NaN：method='pad'
输出结果为：

{% asset_img f99dcf00baa1cd1137ce1827ba12c8fcc3ce2d79.jpg pandas教程：[22]填充缺失值 %}

{% asset_img 4651a712c8fcc3ce89b8a3349145d688d43f2079.jpg pandas教程：[22]填充缺失值 %}

- 与pad相反，bfill表示用后一个数据代替NaN。这里我们增加一个知识点，用limit限制每列可以替代NaN的数目，下面我们限制每列只能替代一个NaN
输出结果为：

{% asset_img 9304c888d43f8794f4872229d11b0ef41bd53a79.jpg pandas教程：[22]填充缺失值 %}

{% asset_img b7bc4c66d0160924f55dc81cd70735fae6cd3479.jpg pandas教程：[22]填充缺失值 %}

- 除了上面用一个具体的值来代替NaN之外，还可以使用平均数或者其他描述性统计量来代替NaN
输出结果为：

{% asset_img 0865b518972bd40754bfb9fa78899e510fb30979.jpg pandas教程：[22]填充缺失值 %}

{% asset_img 34bbf8cd7b899e516af6501341a7d933c8950d79.jpg pandas教程：[22]填充缺失值 %}

- 另外，我们还可以选择哪一列进行缺失值的处理
输出结果为：

{% asset_img c9d4cf43ad4bd1131eb5dd3559afa40f4bfb0579.jpg pandas教程：[22]填充缺失值 %}

{% asset_img 808a27dbb6fd52668c3c5613a818972bd4073666.jpg pandas教程：[22]填充缺失值 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
