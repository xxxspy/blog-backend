---
title: python 线性代数：[6]逆矩阵 伴随矩阵
date: 2016-09-23 18:19:23
tags: [python]
author: mlln.cn
---
设A是数域上的一个n阶方阵，若在相同数域上存在另一个n阶矩阵B，使得： AB=BA=E。 则我们称B是A的逆矩阵，而A则被称为可逆矩阵。当矩阵A的行列式|A|不等于0时才存在可逆矩阵。而伴随矩阵的定义我 从网上找到了一个：

- 先来求一下矩阵的逆，先引入numpy

{% asset_img 72ccb7773912b31bea8677db8418367adbb4e11f.jpg python 线性代数：[6]逆矩阵 伴随矩阵 %}

- 然后创建一个方阵A

{% asset_img f6428f8fa0ec08fad0a9a9555bee3d6d54fbda5c.jpg python 线性代数：[6]逆矩阵 伴随矩阵 %}

- 使用linalg.det求得方阵的行列式

{% asset_img 09bb4f3d269759eeb9f9da39b0fb43166c22df5c.jpg python 线性代数：[6]逆矩阵 伴随矩阵 %}

- 使用linalg.inv求得方阵A的逆矩阵

{% asset_img b25aae51f81986186bad557648ed2e738ad4e61f.jpg python 线性代数：[6]逆矩阵 伴随矩阵 %}

- 接着我们利用公式：
numpy的计算方法：

{% asset_img 08b68e529822720e9c16580879cb0a46f31fab2d.jpg python 线性代数：[6]逆矩阵 伴随矩阵 %}

{% asset_img f9589818367adab4153aa1b189d4b31c8601e41f.jpg python 线性代数：[6]逆矩阵 伴随矩阵 %}

- 以下是今天用到的所有代码

- >>> import numpy as np

- >>> A=np.array([[1,-2,1],[0,2,-1],[1,1,-2]])

- >>> A

- array([[ 1, -2,  1],

-        [ 0,  2, -1],

-        [ 1,  1, -2]])

- >>> 

- >>> 

- >>> A_abs=np.linalg.det(A)

- >>> A_abs

- -3.0000000000000004

- >>> 

- >>> 

- >>> B=np.linalg.inv(A)

- >>> B

- array([[ 1.        ,  1.        ,  0.        ],

-        [ 0.33333333,  1.        , -0.33333333],

-        [ 0.66666667,  1.        , -0.66666667]])

- >>> 

- >>> 

- >>> A_ni=B*A_abs

- >>> A_ni

- array([[-3., -3., -0.],

-        [-1., -3.,  1.],

-        [-2., -3.,  2.]])

- >>> A_bansui=B*A_abs

- >>> A_bansui

- array([[-3., -3., -0.],

-        [-1., -3.,  1.],

-        [-2., -3.,  2.]])

- >>> 

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
