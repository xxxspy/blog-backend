---
title: python教程：[79]赋值运算中的条件语句
date: 2015-03-01 18:15:17
tags: [python]
author: mlln.cn
---
在python中，我们经常用一些逻辑运算来实现复杂的赋值运算。在一些赋值语句，也就是包含等号的python语句中，通常附带一些条件语句，以便用更少的代码写更复杂的命令，并且增加了代码的可读性，因为这些语句往往看起来就像一个英文句子，读起来还朗朗上口，下面是一个简单的赋值，后面的代码都用到了这些值。

- 在赋值中使用if语句，如果b等于c，返回a，否则返回c

{% asset_img 2e6fa7389b504fc2a6947426e6dde71191ef6d8f.jpg python教程：[79]赋值运算中的条件语句 %}

- and符号表示如果a为零则返回a，否则返回b，也就是and总是返回第一个为零的数，当然，如果都不为零，则返回最后一个数

{% asset_img 9f1011b30f2442a70ffc3986d243ad4bd01302e0.jpg python教程：[79]赋值运算中的条件语句 %}

- 如果我们交换ab，返回的仍然是d=0

{% asset_img 8474fbdde71190ef0e3056fccd1b9d16fcfa608f.jpg python教程：[79]赋值运算中的条件语句 %}

- 如果换成两个不为零的数，总是返回后者

{% asset_img e6508eef76c6a7efb4ed6c05fefaaf51f2de668f.jpg python教程：[79]赋值运算中的条件语句 %}

- 返回后者

{% asset_img d002b34bd11373f05ecdabbca70f4bfbfaed04e0.jpg python教程：[79]赋值运算中的条件语句 %}

- or语句总是返回第一个不为零的数，下面返回的是a

{% asset_img d0526df082025aaf7ac0bae8f8edab64024f1ae0.jpg python教程：[79]赋值运算中的条件语句 %}

- 下面返回的还是a（两个不为零的数）

{% asset_img 7787b9efce1b9d16810c5e42f0deb48f8d54648f.jpg python教程：[79]赋值运算中的条件语句 %}

- 如果交换这两个数，则返回c

{% asset_img ae10eddeb48f8c541518010c39292df5e1fe7f8f.jpg python教程：[79]赋值运算中的条件语句 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
