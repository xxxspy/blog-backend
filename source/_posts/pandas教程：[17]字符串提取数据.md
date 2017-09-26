---
title: pandas教程：[17]字符串提取数据
date: 2015-04-23 18:03:23
tags: [pandas]
author: mlln.cn
---
很多时候数据都是以字符串的形式保存的，比如多选题的答案，很多人都是用‘ABCD’这种形式保存数据，那么我们怎样将这样的数据提取出来，转换成可以统计的数据呢？pandas的extract可以做到这些。

- 先来创建一个数据序列
查看一下数据内容

{% asset_img 9a1151c2d56285351b988f2593ef76c6a7ef637f.jpg pandas教程：[17]字符串提取数据 %}

{% asset_img 4e83cb628535e5dd1865f8db75c6a7efce1b622e.jpg pandas教程：[17]字符串提取数据 %}

- 使用extract方法提取数字：它的第一个参数是正则表达式，括号表示要提取的部分
输出内容为：（注意无法匹配的内容用NaN表示）

{% asset_img e49cf91190ef76c6a59aa62f9e16fdfaaf51672e.jpg pandas教程：[17]字符串提取数据 %}

{% asset_img 91ae68c6a7efce1b996395ceac51f3deb48f652e.jpg pandas教程：[17]字符串提取数据 %}

- 假如我们要提取多个数据，可以使用多个括号
输出内容为：

{% asset_img 9864a2315c6034a84d99e585c81349540923767f.jpg pandas教程：[17]字符串提取数据 %}

{% asset_img f29faa8f8c5494eefb6a521d2ef5e0fe99257e2e.jpg pandas教程：[17]字符串提取数据 %}

- 你要灵活使用问号，它表示可有可无，下面的方式可以匹配字符“c”
输出内容为：

{% asset_img 95afee1f3a292df5ee8bf111bf315c6034a8732e.jpg pandas教程：[17]字符串提取数据 %}

{% asset_img 9864a2315c6034a84daae585c81349540923762e.jpg pandas教程：[17]字符串提取数据 %}

- 如果我们想要让输出的结果包含变量名（列名），我们可以使用下面的写法：
输出结果为：

{% asset_img 9319cf09b3de9c82cf1ea48b6f81800a19d8437f.jpg pandas教程：[17]字符串提取数据 %}

{% asset_img 814b07d8bc3eb13516bceabfa51ea8d3fd1f447f.jpg pandas教程：[17]字符串提取数据 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
