---
title: python 线性代数：[2]矩阵乘法
date: 2016-08-23 18:01:17
tags: [python]
author: mlln.cn
---
今天我们来使用Python的numpy包进行矩阵的乘法运算，用到了一些矩阵乘法的基本知识，这里我们就不再说矩阵，我们假设你对矩阵都有一定的了解，下面看我们具体的例子。

- 使用二维数组创建两个矩阵A和B

{% asset_img 43e6c733c895d143723b3dd271f082025baf07b7.jpg python 线性代数：[2]矩阵乘法 %}

- 先来一个矩阵的数乘，其实见识矩阵的每一个元素乘以该数

{% asset_img 9304c888d43f8794605d91dfd01b0ef41ad53a66.jpg python 线性代数：[2]矩阵乘法 %}

- dot函数用于矩阵乘法，对于二维数组，它计算的是矩阵乘积，对于一维数组，它计算的是内积。注意交换矩阵的前后位置会导致不同的结果，看下面的例子

{% asset_img 1a94b36eddc451da4d54d51ab4fd5266d1163266.jpg python 线性代数：[2]矩阵乘法 %}

{% asset_img 964b2e4e251f95ca7c3a4c47cb177f3e66095231.jpg python 线性代数：[2]矩阵乘法 %}

- 再创建一个二维数组

{% asset_img 647912d7912397ddc19e46f55b82b2b7d1a28719.jpg python 线性代数：[2]矩阵乘法 %}

- 我们验证一个矩阵乘法的结合性 （AB)C=A(BC）

{% asset_img a005b3345982b2b7b478e73533adcbef77099b19.jpg python 线性代数：[2]矩阵乘法 %}

- 接着看一下对加法的分配性 （A+B)C=AC+BC，C(A+B）=CA+CB

{% asset_img d041a4a1cd11728bfce252d3cafcc3cec2fd2c31.jpg python 线性代数：[2]矩阵乘法 %}

{% asset_img 4651a712c8fcc3ce7c0f17c29045d688d53f2031.jpg python 线性代数：[2]矩阵乘法 %}

- 数乘的结合性，也一样啦：

{% asset_img 8c511fe93901213fcad4902d56e736d12e2e9519.jpg python 线性代数：[2]矩阵乘法 %}

{% asset_img d7c9ca3f8794a4c2bbec39da0cf41bd5ac6e3931.jpg python 线性代数：[2]矩阵乘法 %}

{% asset_img a005b3345982b2b7b479e73533adcbef77099b1a.jpg python 线性代数：[2]矩阵乘法 %}

- 接着我们用到一个新知识，使用eye创建一个单位矩阵，单位矩阵的定义就是看下面的步骤

{% asset_img adee30dda3cc7cd9e3cbea283b01213fb90e911a.jpg python 线性代数：[2]矩阵乘法 %}

- 我们看一下，一个矩阵A乘以一个单位矩阵，还是它本身

{% asset_img 00a82701213fb80e0837bf2634d12f2eb838941a.jpg python 线性代数：[2]矩阵乘法 %}

- 好了，乘法就到这里了，我们下面接着继续讲矩阵的转置

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
