---
title: python 线性代数：[22]习题1.10求逆矩阵
date: 2016-05-11 18:05:23
tags: [python]
author: mlln.cn
---
接着以前的文章，我们继续学习用Python解线性代数的问题。今天我们要练习一下《线性代数.同济大学出版.第一章习题10》,演示一下如何求矩阵的逆矩阵和验证结果是否正确。

- 这是今天我们要做的习题：只做前三题

{% asset_img 0b14ad19ebc4b745eef1ac06cbfc1e178a82157d.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

- 将这三个矩阵录入到excel当中

{% asset_img 8bc3a7014a90f603c6d587573d12b31bb051ed7e.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

- 开始写代码，先引入这两个库

{% asset_img 8474fbdde71190ef4ce989cfca1b9d16fdfa6054.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

- 先来计算第一个矩阵的逆矩阵，用np.linalg.inv来计算arr矩阵的逆矩阵，如果你看不太懂代码，应该去翻看我前两篇文章，里面讲得很详细
这是输出的结果：

{% asset_img 3b6833f5e0fe9925f51e724030a85edf8db17154.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

{% asset_img 30ecd5ef76094b3688b401fda7cc7cd98d109db8.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

- 现在计算第第二个矩阵，我们发现这个矩阵是带有符号的，所以我们用sympy这个库中的Matrix对象来进行计算。我们可以使用Matrix.inv来计算逆矩阵，默认情况下，它使用高斯消去法，如果传入参数LU，它

- 这是输出的两个矩阵：

{% asset_img d048adde9c82d158949042a1840a19d8bc3e4254.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

{% asset_img ae8267310a55b31941a3986547a98226cffc170c.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

- 最后一题，和第一题一样，都是数字，但是现在我想验证一下计算结果，让两个矩阵点乘，如果结果是一个单位矩阵，那么久可以证明两个矩阵互为逆矩阵
输出结果为：

{% asset_img 8b527d2762d0f7034cd78ecc0cfa513d2697c57e.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

{% asset_img 29752a9b033b5bb5ca4e24ee32d3d539b700bcc1.jpg python 线性代数：[22]习题1.10求逆矩阵 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
