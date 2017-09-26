---
title: python 线性代数：[4]方阵的迹
date: 2016-08-01 18:03:15
tags: [python]
author: mlln.cn
---
怎样求方阵的迹？方阵的迹是什么？方阵的迹就是主对角元素之和，方阵的迹说实话我还不知道它的实际用途，有知道的人麻烦你写在下面的评论里，好了，下面来用numpy计算一下方阵的迹。

- 先引入numpy

{% asset_img d048adde9c82d158417f9740820a19d8bd3e4207.jpg python 线性代数：[4]方阵的迹 %}

- 创建一个方阵（方阵也就是行数等于列数的矩阵）

{% asset_img f29faa8f8c5494ee89a3c1e82ff5e0fe98257e7b.jpg python 线性代数：[4]方阵的迹 %}

- 用trace计算方阵的迹

{% asset_img 8cf0d513495409235be8ad8f9058d109b2de497b.jpg python 线性代数：[4]方阵的迹 %}

- 再创建一个方阵F

{% asset_img b25d9901a18b87d6ddaa65ee050828381e30fd1d.jpg python 线性代数：[4]方阵的迹 %}

- 验证一下方阵的迹等于方阵的转置的迹

{% asset_img 9f6e190828381f3016f14358ab014c086f06f01d.jpg python 线性代数：[4]方阵的迹 %}

- 验证一下方阵的乘积的迹等于

{% asset_img a84052086e061d950fadf9c979f40ad163d9ca1d.jpg python 线性代数：[4]方阵的迹 %}

- 验证一下方阵的和的迹等于方阵的迹的和

{% asset_img 566d0fdfa9ec8a136cf19911f503918fa1ecc01d.jpg python 线性代数：[4]方阵的迹 %}

- 该文章用到的所有代码：

- >>> E=np.array([[1,2,3],[4,5,6],[7,8,9]])

- >>> E

- array([[1, 2, 3],

-        [4, 5, 6],

-        [7, 8, 9]])

- >>> 

- >>> np.trace(E)

- 15

- >>> 

- >>> 

- >>> F=E-2

- >>> F

- array([[-1,  0,  1],

-        [ 2,  3,  4],

-        [ 5,  6,  7]])

- >>> 

- >>> 

- >>> 

- >>> 

- >>> np.trace(E)

- 15

- >>> 

- >>> np.trace(E.T)

- 15

- >>> 

- >>> 

- >>> np.trace(np.dot(E,F))

- 171

- >>> np.trace(np.dot(F,E))

- 171

- >>> 

- >>> 

- >>> 

- >>> np.trace(E+F)

- 24

- >>> 

- >>> np.trace(E)+np.trace(F)

- 24

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
