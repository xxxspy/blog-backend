---
title: numpy函数：[18]all()和any()比较矩阵
date: 2015-10-11 18:23:23
tags: [numpy]
author: mlln.cn
---
假如我们想要知道矩阵a和矩阵b中所有对应元素是否相等，我们需要使用all方法，假如我们想要知道矩阵a和矩阵b中对应元素是否有一个相等，我们需要使用any方法。下面看几个例子：

- 先引入numpy模块

{% asset_img 8640bf8b87d6277fe7f17acf2a381f30e824fc23.jpg numpy函数：[18]all()和any()比较矩阵 %}

- 创建两个数组，当然，在这里，我通常把数组教程矩阵或者向量，这无关紧要

{% asset_img 9dc3cf58ccbf6c818daf641fbe3eb13532fa4069.jpg numpy函数：[18]all()和any()比较矩阵 %}

- 检测一下是否a和b中所有对应元素均相等，如果均相等，返回true，只要有一个不相等，返回false

{% asset_img b0742dfa828ba61ebc7680d84334970a314e5969.jpg numpy函数：[18]all()和any()比较矩阵 %}

- 创建一个数组c

{% asset_img 0b3a1c087bf40ad1e5078f14552c11dfa8ecce23.jpg numpy函数：[18]all()和any()比较矩阵 %}

- 检测一下是否a和c中所有对应元素均相等，如果均相等，返回true，只要有一个不相等，返回false

{% asset_img 245e8bcad1c8a786d4b202f96509c93d71cf5069.jpg numpy函数：[18]all()和any()比较矩阵 %}

- 但是any相反，只要有一个元素相等就可以返回true

{% asset_img 62667cd0f703918f3132753d533d269758eec423.jpg numpy函数：[18]all()和any()比较矩阵 %}

- 再尝试一次：

{% asset_img 7e7f7909c93d70cf1962e2fafadcd100bba12b69.jpg numpy函数：[18]all()和any()比较矩阵 %}

{% asset_img cc506c8b4710b912e359be09c1fdfc0393452269.jpg numpy函数：[18]all()和any()比较矩阵 %}

- 本篇教程用到的所有代码都呈现在下方：

- >>> import numpy

- >>> a=numpy.array([1,2,3])

- >>> b=a.copy

- >>> a

- array([1, 2, 3])

- >>> b

- <built-in method copy of numpy.ndarray object at 0x0000000002EA41D0>

- >>> b=a.copy()

- >>> b

- array([1, 2, 3])

- >>> 

- >>> 

- >>> 

- >>> (a==b).all()

- True

- >>> 

- >>> 

- >>> c=b.copy()

- >>> c[0]=0

- >>> c

- array([0, 2, 3])

- >>> 

- >>> 

- >>> a

- array([1, 2, 3])

- >>> 

- >>> 

- >>> (a==c).all()

- False

- >>> 

- >>> 

- >>> (a==c).any()

- True

- >>> 

- >>> c[1]=0

- >>> c

- array([0, 0, 3])

- >>> a

- array([1, 2, 3])

- >>> 

- >>> 

- >>> 

- >>> (c==a).any()

- True

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
