---
title: Python教程：[69]strip()函数详解
date: 2015-02-11 18:19:03
tags: [python]
author: mlln.cn
---
strip()用于裁剪字符串首尾的某些字符，是一个用处非常多的函数，今天我们来通过例子来探讨一下它的基本用法：

- 假如有一个这样的字符串

{% asset_img fab3ac119313b07ede4d57890ed7912396dd8c7b.jpg Python教程：[69]strip()函数详解 %}

- strip()不带任何参数，可以删除首位的空格

{% asset_img 906289dda144ad34424f8006d2a20cf430ad857b.jpg Python教程：[69]strip()函数详解 %}

- 但是strip（）无法删除位于字符串中间的空格

{% asset_img a005b3345982b2b7cd6f3e4533adcbef77099b7b.jpg Python教程：[69]strip()函数详解 %}

- 除了删除首位空格，任何不显示的的字符都会被删除

{% asset_img caae68094b36acaf0a10917d7ed98d1000e99c7b.jpg Python教程：[69]strip()函数详解 %}

- 如果我们想要删除位于首位的其他字符，我们可以使用参数strip（string），它将删除所有包含在string中的字符，当然只删除位于首位的字符

{% asset_img a28d62d98d1001e910cc138eba0e7bec55e7977b.jpg Python教程：[69]strip()函数详解 %}

- 如果首位有空格，就无法删除这些字符了，道理是一样的。

{% asset_img 38403f3fb80e7bec792a04602d2eb9389a506b7b.jpg Python教程：[69]strip()函数详解 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
