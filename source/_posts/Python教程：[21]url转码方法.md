---
title: Python教程：[21]url转码方法
date: 2016-09-17 18:11:15
tags: [python]
author: mlln.cn
---
在url中有一些是不能被打印或者不被web服务器作为有效url的字符必须转码以后再能使用，所以我们就用到了quote函数，quote函数的语法如下：quote(urldata,safe+'/')；逗号、下划线、句点斜线和字母数字这类符号是不需要转化的，通常中文是需要转换的。那些被转换的字符前面会加上一个百分号，同时转换成了16进制字符。

- 先引入urllib模块

{% asset_img ac754782b2b7d0a2e49d59b0c9ef76094b369a0c.jpg Python教程：[21]url转码方法 %}

- 假如我们要对下面的url进行转码，注意观察各种字符的变化

{% asset_img 8d158aeef01f3a29239f88e39b25bc315c607c0c.jpg Python教程：[21]url转码方法 %}

- 使用quote方法，进行转码

{% asset_img f15e24292df5e0fe894fd42c5e6034a85edf720c.jpg Python教程：[21]url转码方法 %}

- 我们看看转码得到的结果：

{% asset_img 4abae5edab64034f15769f2badc379310a551d20.jpg Python教程：[21]url转码方法 %}

- 我们想要得到原先的url，可以使用quote的逆函数unquote

{% asset_img 020e66f0f736afc309b76248b119ebc4b7451220.jpg Python教程：[21]url转码方法 %}

- 得到反转码以后的url，我们看到这种方法并没有返回中文字符。

{% asset_img 8cf0d51349540923c43e3e539058d109b3de490c.jpg Python教程：[21]url转码方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
