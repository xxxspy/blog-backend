---
title: python 线性代数：[9]求矩阵的秩
date: 2015-01-05 18:15:23
tags: [python]
author: mlln.cn
---
矩阵的秩，课本上是这么定义的：

- 先引入numpy模块

{% asset_img 834344afa40f4bfba7e0dda3014f78f0f63618d1.jpg python 线性代数：[9]求矩阵的秩 %}

- 创建一个单位矩阵i

{% asset_img 020e66f0f736afc31b3c7c92b119ebc4b64512d1.jpg python 线性代数：[9]求矩阵的秩 %}

- 计算单位矩阵i的秩

{% asset_img a84052086e061d95802574cf79f40ad163d9caa3.jpg python 线性代数：[9]求矩阵的秩 %}

- 改变一下i右下角元素的值，设置为0

{% asset_img 1cd4147b02087bf4878f141ef0d3572c10dfcfa3.jpg python 线性代数：[9]求矩阵的秩 %}

- 重新计算矩阵的秩，得到3

{% asset_img f392492c11dfa9ec194d15e060d0f703908fc1a3.jpg python 线性代数：[9]求矩阵的秩 %}

- 以下是我们用到的所有代码：

- >>> import numpy

- >>> i=numpy.eye(4)

- >>> i

- array([[ 1.,  0.,  0.,  0.],

-        [ 0.,  1.,  0.,  0.],

-        [ 0.,  0.,  1.,  0.],

-        [ 0.,  0.,  0.,  1.]])

- >>> 

- >>> 

- >>> 

- >>> numpy.matrix_rank(i)

- Traceback (most recent call last):

-   File "<pyshell#6>", line 1, in <module>

-     numpy.matrix_rank(i)

- AttributeError: 'module' object has no attribute 'matrix_rank'

- >>> numpy.linalg.matrix_rank(i)

- 4

- >>> i[-1,-1]=0

- >>> i

- array([[ 1.,  0.,  0.,  0.],

-        [ 0.,  1.,  0.,  0.],

-        [ 0.,  0.,  1.,  0.],

-        [ 0.,  0.,  0.,  0.]])

- >>> i[1,1]

- 1.0

- >>> 

- >>> 

- >>> 

- >>> numpy.linalg.matrix_rank(i)

- 3

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
