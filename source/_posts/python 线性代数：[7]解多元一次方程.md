---
title: python 线性代数：[7]解多元一次方程
date: 2015-10-05 18:15:17
tags: [python]
author: mlln.cn
---
用python的numpy包中的linalg.solve()方法解多元一次方程，如果你对矩阵解方程非常熟悉，那么现在只是学习一下这个函数就好了。如果你不是很熟悉用矩阵解方程，你需要看一下线性代数的课本。

- 首先看一下我们要解的方程，将这个方程格式调整好，按照x-y-z-常数项的顺序排列

{% asset_img b8405490f603738d0d597bd5b11bb051f919ecf3.jpg python 线性代数：[7]解多元一次方程 %}

- 将未知数的系数写下来，排列成一个矩阵a，如下

{% asset_img f7426d8da97739121535f296fa198618377ae2f3.jpg python 线性代数：[7]解多元一次方程 %}

- 常数项构成一个一维数组（向量）

{% asset_img 8759287adab44aed835dc913b11c8701a08bfbf3.jpg python 线性代数：[7]解多元一次方程 %}

- 使用linalg.solve方法解方程，参数a指的是系数矩阵，参数b指的是常数项矩阵

{% asset_img d1571724ab18972baa6d773de4cd7b899f510ab6.jpg python 线性代数：[7]解多元一次方程 %}

- 我们得到的解对不对呢？使用点乘的方法可以验证一下，系数乘以未知数可以得到常数项

{% asset_img 8640bf8b87d6277f2a0145cf2a381f30e824fcf3.jpg python 线性代数：[7]解多元一次方程 %}

- 今天用到的所有代码如下

- >>> a=[[1,2,1],[2,-1,3],[3,1,2]]

- >>> a=np.array(a)

- >>> a

- array([[ 1,  2,  1],

-        [ 2, -1,  3],

-        [ 3,  1,  2]])

- >>> 

- >>> 

- >>> b=[7,7,18]

- >>> b=np.array(b)

- >>> b

- array([ 7,  7, 18])

- >>> 

- >>> 

- >>> 

- >>> x=np.solve(a,b)

- Traceback (most recent call last):

-   File "<pyshell#31>", line 1, in <module>

-     x=np.solve(a,b)

- AttributeError: 'module' object has no attribute 'solve'

- >>> x=np.linalg.solve(a,b)

- >>> x

- array([ 7.,  1., -2.])

- >>> 

- >>> 

- >>> 

- >>> 

- >>> np.dot(a,x)

- array([  7.,   7.,  18.])

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
