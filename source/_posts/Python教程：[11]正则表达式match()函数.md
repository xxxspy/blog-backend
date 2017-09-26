---
title: Python教程：[11]正则表达式match()函数
date: 2015-07-15 18:01:05
tags: [python]
author: mlln.cn
---
如果不创建pattern对象，我们使用match函数可以直接进行正则表达式的匹配，在我看来这种方式更简洁，不过不适合大型程序的编写，后期维护可能会产生困难，不过编写一些小脚本完全可以胜任。

- 先引入re模块

{% asset_img b3ba5d166d224f4a5decda380bf790529822d161.jpg Python教程：[11]正则表达式match()函数 %}

- 使用match函数返回一个match对象

{% asset_img 7d98931001e93901e15e241579ec54e736d1967a.jpg Python教程：[11]正则表达式match()函数 %}

- 使用group方法输出所有匹配的字符串

{% asset_img 99636c0e0cf3d7cafe83965df01fbe096b63a961.jpg Python教程：[11]正则表达式match()函数 %}

- 我们看一下m的数据类型。

{% asset_img 9a1151c2d56285352ebc7b0a92ef76c6a7ef637a.jpg Python教程：[11]正则表达式match()函数 %}

- 我们还可以用简单的写法来获得所有匹配的字符串。

{% asset_img e49cf91190ef76c6686a52009f16fdfaaf516726.jpg Python教程：[11]正则表达式match()函数 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
