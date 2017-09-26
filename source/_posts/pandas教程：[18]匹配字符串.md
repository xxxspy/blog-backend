---
title: pandas教程：[18]匹配字符串
date: 2015-07-05 18:11:01
tags: [pandas]
author: mlln.cn
---
pandas可以检测字符串是否包含某字符模式或者匹配它，这在处理一些字符串数据的时候非常有用，下面我们来用几个例子说明一下。

- 首先，我们创建一个数据序列
查看数据序列：

{% asset_img 5202e5f2b21193133c3f72b466380cd791238d73.jpg pandas教程：[18]匹配字符串 %}

{% asset_img 1e71f724b899a90109ecd9321e950a7b0308f59e.jpg pandas教程：[18]匹配字符串 %}

- 检测数据序列中哪些元素包含一个字母和一个数字的字符模式
匹配结果为：

{% asset_img b13fd48065380cd701622fe9a244ad3459828173.jpg pandas教程：[18]匹配字符串 %}

{% asset_img 7d98931001e93901827e003a78ec54e736d19673.jpg pandas教程：[18]匹配字符串 %}

- 我们可以使用na参数来规定出现NaN数据的时候匹配成True还是False
结果为：

{% asset_img 0d968f2397dda1443e75e1b6b1b7d0a20cf48673.jpg pandas教程：[18]匹配字符串 %}

{% asset_img 0b3a1c087bf40ad12e3d45e7542c11dfa8ecce9e.jpg pandas教程：[18]匹配字符串 %}

- match方法可以严格匹配字符串：
输出结果为：

{% asset_img 8640bf8b87d6277fa0cbb03c2b381f30e824fc9e.jpg pandas教程：[18]匹配字符串 %}

{% asset_img 55a628d12f2eb9383111f7f6d6628535e5dd6f73.jpg pandas教程：[18]匹配字符串 %}

- 还有，我们可以检查字符串开始字符，假设我们想要查找以字母a开头的数据，可以用startswith或者contains，注意contains中第一个参数，不懂得童鞋可以去看Python的正则表达式

- 输出结果：

{% asset_img caae68094b36acafb39c1bf87fd98d1001e99c73.jpg pandas教程：[18]匹配字符串 %}

{% asset_img 4e83cb628535e5dd485028db75c6a7efce1b6273.jpg pandas教程：[18]匹配字符串 %}

- 同样道理，可以检查结束字符串
输出结果为：

{% asset_img 9f6e190828381f30abc00fadaa014c086f06f09e.jpg pandas教程：[18]匹配字符串 %}

{% asset_img a8ad9413632762d0a3e726bba3ec08fa503dc69e.jpg pandas教程：[18]匹配字符串 %}

- 还有很多字符串方法，这里不一一距离，你看一下简介用到的时候再去学

{% asset_img 54baacfb43166d222fae9790452309f79152d29e.jpg pandas教程：[18]匹配字符串 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
