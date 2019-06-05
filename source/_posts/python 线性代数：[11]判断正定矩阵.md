---
title: python 线性代数：[11]判断正定矩阵
date: 2015-10-01 18:05:19
tags: [python]
author: mlln.cn
---
正定矩阵的定义是：设M是n阶方阵，如果对任何非零向量z，都有 z'Mz > 0，其中z' 表示z的转置，就称M正定矩阵。这个定义你先搞懂，不懂的看课本去，我这里就直接用python来检验某个方阵是不是正定矩阵（用二维数组表示矩阵）。

- 我们用到的一个重要性质是：判定定理1：对称阵A为正定的充分必要条件是：A的特征值全为正。所以我们只要求得对称阵A的所有特征值即可。

- 引入numpy模块

{% asset_img d7c9ca3f8794a4c2561254dc0cf41bd5ac6e39d0.jpg python 线性代数：[11]判断正定矩阵 %}

- 创建一个方阵A

{% asset_img b5ce925494eef01fcac0a832e2fe9925bd317d36.jpg python 线性代数：[11]判断正定矩阵 %}

{% asset_img 1a94b36eddc451dab3c7bf1cb4fd5266d11632d0.jpg python 线性代数：[11]判断正定矩阵 %}

- 将方阵转换成对称阵的方法是：

{% asset_img fab3ac119313b07e75a3e2ff0ed7912396dd8ce8.jpg python 线性代数：[11]判断正定矩阵 %}

- 求对称阵A的特征值

{% asset_img 00a82701213fb80eac8fd32034d12f2eb83894a8.jpg python 线性代数：[11]判断正定矩阵 %}

- 判断是不是所有的特征值都大于0，用到了all函数，显然对称阵A不是正定的

{% asset_img 389aa8fd5266d0163e282ddf952bd40734fa35d0.jpg python 线性代数：[11]判断正定矩阵 %}

- 我们来创建一个单位矩阵，它肯定是对称的，同样的方法检验是不是正定矩阵

{% asset_img 9dc3cf58ccbf6c8185e09c1fbe3eb13532fa4036.jpg python 线性代数：[11]判断正定矩阵 %}

- 网上查到更简便的方法是对对称阵进行cholesky分解，如果像这样没有提示出错，就说明它是正定的

{% asset_img aa59892bd40735fadac1fd4e9c510fb30e2408d0.jpg python 线性代数：[11]判断正定矩阵 %}

- 如果提示出错，就说明它不是正定矩阵，你可以使用try函数捕获错误值

{% asset_img a992e31f4134970a20a4a0d897cad1c8a6865d36.jpg python 线性代数：[11]判断正定矩阵 %}

- 以下是今天用到的部分代码：

- >>> import numpy

- >>> 

- >>> 

- >>> A=range(16)

- >>> A

- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

- >>> A=numpy.array(A).reshape(4,4)

- >>> A

- array([[ 0,  1,  2,  3],

-        [ 4,  5,  6,  7],

-        [ 8,  9, 10, 11],

-        [12, 13, 14, 15]])

- >>> A=A+A.T

- >>> A

- array([[ 0,  5, 10, 15],

-        [ 5, 10, 15, 20],

-        [10, 15, 20, 25],

-        [15, 20, 25, 30]])

- >>> 

- >>> 

- >>> B=numpy.linalg.eigvals(A)

- >>> B

- array([  6.74165739e+01 +0.00000000e+00j,

-         -7.41657387e+00 +0.00000000e+00j,

-         -8.88285420e-17 +1.82759332e-15j,  -8.88285420e-17 -1.82759332e-15j])

- >>> if numpy.all(B>0):print '是正定矩阵'

- >>> C=numpy.linalg.cholesky(A)

- Traceback (most recent call last):

-   File "<pyshell#41>", line 1, in <module>

-     C=numpy.linalg.cholesky(A)

-   File "D:Python27libsite-packages
umpy-1.8.0-py2.7-win-amd64.egg
umpylinalglinalg.py", line 603, in cholesky

-     return wrap(gufunc(a, signature=signature, extobj=extobj).astype(result_t))

-   File "D:Python27libsite-packages
umpy-1.8.0-py2.7-win-amd64.egg
umpylinalglinalg.py", line 93, in _raise_linalgerror_nonposdef

-     raise LinAlgError("Matrix is not positive definite")

- LinAlgError: Matrix is not positive definite

- >>> A=numpy.eye(4)

- >>> A

- array([[ 1.,  0.,  0.,  0.],

-        [ 0.,  1.,  0.,  0.],

-        [ 0.,  0.,  1.,  0.],

-        [ 0.,  0.,  0.,  1.]])

- >>> 

- >>> B=numpy.linalg.eigvals(A)

- >>> B

- array([ 1.,  1.,  1.,  1.])

- >>> if numpy.all(B>0):print '是正定矩阵'

- 是正定矩阵

- >>> 

- >>> 

- >>> C=numpy.linalg.cholesky(A)

- >>> C

- array([[ 1.,  0.,  0.,  0.],

-        [ 0.,  1.,  0.,  0.],

-        [ 0.,  0.,  1.,  0.],

-        [ 0.,  0.,  0.,  1.]])

- >>> 

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
