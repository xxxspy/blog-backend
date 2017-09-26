---
title: python 线性代数：[15]从协方差阵计算相关阵
date: 2016-08-15 18:11:23
tags: [python]
author: mlln.cn
---
其实Python的numpy包有可以直接计算相关矩阵/协方差矩阵的方法，但是这篇文章是教大家如何理解他俩之间的关系的，所以我们给出协方差矩阵，求相关矩阵。利用公式：

- 引入numpy模块

{% asset_img 90cebeec08fa513d1aee8d9f3e6d55fbb3fbd9e8.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

- 创建一个协方差矩阵
这个矩阵为：

{% asset_img 507c389759ee3d6d6a82668a40166d224e4adee8.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

{% asset_img c87c6ecf3bc79f3d34aa0571b9a1cd11738b29ed.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

- 我们先求得协方差矩阵的尺寸

{% asset_img d019d2bf6c81800aafae684fb23533fa838b47ed.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

- 生成一个与sigma同大小的单位矩阵：e
输出为：

{% asset_img cdfe7281800a19d80b48654430fa828ba71e46ed.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

{% asset_img ac0acf1373f08202a0e7707e48fbfbedab641b3f.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

- 计算方差矩阵，其实就是利用单位矩阵消除协方差矩阵中的非对角线元素

{% asset_img 808a27dbb6fd5266375edd55a818972bd407363f.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

{% asset_img c28fddfdfc0392450efe004e8494a4c27c1e25ed.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

- 求得标准差矩阵

{% asset_img a75fb6d3fd1f4134287ce43f261f95cad0c85eed.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

{% asset_img 020e66f0f736afc37a78de24b019ebc4b745123f.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

- 求得标准差的逆矩阵

{% asset_img e78c65899e510fb3fe6c96d6da33c895d1430c3f.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

{% asset_img ea85a94543a98226c5b5ca668982b9014a90eb38.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

- 根据公式就求得了相关系数矩阵

{% asset_img a6c7d7177f3e6709014ba4be38c79f3df9dc55ed.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

{% asset_img 0fb505d5ad6eddc4b3ac55ba3adbb6fd536633ed.jpg python 线性代数：[15]从协方差阵计算相关阵 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
