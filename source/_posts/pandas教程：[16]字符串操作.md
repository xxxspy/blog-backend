---
title: pandas教程：[16]字符串操作
date: 2015-09-01 18:05:01
tags: [pandas]
author: mlln.cn
---
有些时候我们的数据是字符串形式的，pandas也能方便的处理，今天我们就举几个例子来操作字符串。

- 先来创建一个Series
查看下其中的内容

{% asset_img 58c3acb7d0a20cf4dce6a8db75094b36acaf9905.jpg pandas教程：[16]字符串操作 %}

{% asset_img b29f8282d158ccbf49e5e33e1ad8bc3eb135411d.jpg pandas教程：[16]字符串操作 %}

- 将数据转换为小写
查看下是不是转换为了小写

{% asset_img adee30dda3cc7cd9785b62dd3a01213fb80e9105.jpg pandas教程：[16]字符串操作 %}

{% asset_img 6dc09e0a19d8bc3e985150ce818ba61ea8d3451d.jpg pandas教程：[16]字符串操作 %}

- 转换为大写

{% asset_img 1899a23eb13533faa9efc52aabd3fd1f41345b1d.jpg pandas教程：[16]字符串操作 %}

{% asset_img 38403f3fb80e7becafac55e52c2eb9389b506b05.jpg pandas教程：[16]字符串操作 %}

- 获取字符串的长度，使用len
现在所有的字符串转换为了数字，也就是字符串的长度

{% asset_img a75fb6d3fd1f4134a76e537a261f95cad1c85e1d.jpg pandas教程：[16]字符串操作 %}

{% asset_img a992e31f4134970a012a462b96cad1c8a7865d1d.jpg pandas教程：[16]字符串操作 %}

- 我们还可以切割字符串，将字符串转换为list
查看list构成的数据列

{% asset_img e49cf91190ef76c6a0a3ad2f9e16fdfaaf516705.jpg pandas教程：[16]字符串操作 %}

{% asset_img c856613e6709c93d4aab58f39c3df8dcd100541d.jpg pandas教程：[16]字符串操作 %}

- 如果list构成的数据列比较怪，我们可以使用get方法获得列中的某个元素
结果为：

{% asset_img 3a86813df8dcd10085c5ae25718b4710b9122f1d.jpg pandas教程：[16]字符串操作 %}

{% asset_img 73ca5910b912c8fc86aaa0c9ff039245d688211d.jpg pandas教程：[16]字符串操作 %}

- 替换字符串，使用replace，replace的第一个参数是正则表达式，第二个参数是要替换成的字符串。
输出：

{% asset_img c28fddfdfc0392459fecb70b8494a4c27d1e251d.jpg pandas教程：[16]字符串操作 %}

{% asset_img d57e9994a4c27d1e9c7f6dc018d5ad6eddc4381d.jpg pandas教程：[16]字符串操作 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
