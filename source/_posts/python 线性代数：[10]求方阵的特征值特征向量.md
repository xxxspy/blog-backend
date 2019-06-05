---
title: python 线性代数：[10]求方阵的特征值特征向量
date: 2015-05-03 18:19:05
tags: [python]
author: mlln.cn
---
求方阵（矩阵）的特征值和特征向量用的是python中的numpy.linagl.eig方法，它需要一个二维数组作为参数，输出一个一位数组（元素为特征值）和一个二维数组（特征向量组），我们还是在例子中学习一哈：

- 先引入numpy模块

{% asset_img a1ad16fa513d2697caee42aa57fbb2fb4216d8cd.jpg python 线性代数：[10]求方阵的特征值特征向量 %}

- 创建一个对角矩阵，关于diag的用法可以看我前几篇文章

{% asset_img 29752a9b033b5bb57ea46a0934d3d539b700bc93.jpg python 线性代数：[10]求方阵的特征值特征向量 %}

- 求矩阵x的特征值和特征向量，特征值保存在a中，特征向量保存在b中

{% asset_img b3ba5d166d224f4abaa439e40bf790529922d1cd.jpg python 线性代数：[10]求方阵的特征值特征向量 %}

- 使用循环的方法，我们来验证一下特征值和特征向量，验证的方法是特征值和特征向量的定义法：

- 设A为n阶矩阵，若存在常数λ及非零的n维向量x，使得

- Ax=λx，

- 则称λ是矩阵A的特征值，x是A属于特征值λ的特征向量。

{% asset_img 5202e5f2b21193137630b54767380cd790238d93.jpg python 线性代数：[10]求方阵的特征值特征向量 %}

- 这是我今天犯的错误：

{% asset_img 6a22e8246b600c332d44943f184c510fd8f9a1cd.jpg python 线性代数：[10]求方阵的特征值特征向量 %}

- 这是今天用到的所有代码：

- >>> import numpy

- >>> x=numpy.diag((1,2,3))

- >>> x

- array([[1, 0, 0],

-        [0, 2, 0],

-        [0, 0, 3]])

- >>> a,b=numpy.linalg.eig(x)

- >>> a

- array([ 1.,  2.,  3.])

- >>> b

- array([[ 1.,  0.,  0.],

-        [ 0.,  1.,  0.],

-        [ 0.,  0.,  1.]])

- >>> 

- >>> 

- >>> for i in range(3):

- if numpy.dot(x,b[:][i])==a[i]*b[:][i]:

- print '正确'

- else:print '错误‘

- SyntaxError: EOL while scanning string literal

- >>> for i in range(3):

- if numpy.dot(x,b[:][i])==a[i]*b[:][i]:

- print '正确'

- else:print '错误'

- Traceback (most recent call last):

-   File "<pyshell#38>", line 2, in <module>

-     if numpy.dot(x,b[:][i])==a[i]*b[:][i]:

- ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

- >>> for i in range(3):

- if (numpy.dot(x,b[:][i])==a[i]*b[:][i]).all():

- print '正确'

- else:print '错误'

- 正确

- 正确

- 正确

- >>> 

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
