---
title: python 线性代数：[18]线性规划求最优解
date: 2016-02-01 18:11:15
tags: [python]
author: mlln.cn
---
 现在有个需要解决的问题：我找到了一份实习工作，于是想租一个房子，最好离工作近点，但是还没毕业，学校时不时有事，还不能离学校远了；而且有时候还要去女朋友那里，她希望我就住在她附近，于是，我怎么选择房子的地址？假定：公司、学校、女盆友的在地图上的坐标分别是：（1,1），（4,6），（9,2），求我的房子的坐标？

- 我们解决的方法是用scipy提供的一个scipy.optimize.minimize 方法，首先要写出一个计算距离的方程：

{% asset_img 61183b2dd42a28343bbf204358b5c9ea15cebf19.jpg python 线性代数：[18]线性规划求最优解 %}

{% asset_img cc506c8b4710b9124cece0b6c0fdfc039245220d.jpg python 线性代数：[18]线性规划求最优解 %}

- 分别把三个地点的横坐标和纵坐标都保存在两个列向量里

{% asset_img c9bdddcec3fdfc031a55f5f0d73f8794a4c2260d.jpg python 线性代数：[18]线性规划求最优解 %}

- 找一个起始点：

{% asset_img 9c57e3faaf51f3def9aeaf2c97eef01f3a29791e.jpg python 线性代数：[18]线性规划求最优解 %}

- 看一下，随便选择的这个住址到三个地点的距离的平方和
求得这个值很大：6224

{% asset_img d35a10f41bd5ad6e4fd472a282cb39dbb6fd3c0d.jpg python 线性代数：[18]线性规划求最优解 %}

- 求最优解

{% asset_img 5f9e93b1cb1349545502fe2c554e9258d1094a1e.jpg python 线性代数：[18]线性规划求最优解 %}

- 求得最优解
输出为：

- [ 4.66666667  3.        ]

- 46.6666666667

{% asset_img ca5257540923dd54086fb120d209b3de9c82481e.jpg python 线性代数：[18]线性规划求最优解 %}

- 将地图绘制出来
求得我的地址就标在地图上（house的地方）

{% asset_img 7ac880510fb30f24e1b7fa4bcb95d143ad4b030d.jpg python 线性代数：[18]线性规划求最优解 %}

{% asset_img 948bcfc8a786c917081f4471ca3d70cf3bc7571e.jpg python 线性代数：[18]线性规划求最优解 %}

- 有的人还说了，假如我的预算有限，只能租得起五环边上的房子，那么问题也很简单，就是设定我的房子的坐标是(x,y)，假如五环到市中心（0,0）的距离为r=10，那么我的房子在五环边上，就可以用等式x**2+y**2-100=0来表示。可以写到我的代码里：

{% asset_img 91138622720e0cf32f5c5cb10946f21fbf09aa96.jpg python 线性代数：[18]线性规划求最优解 %}

- 在求最优解得时候，我们加上一个参数constraints

{% asset_img 0db2c9ca7bcb0a46098999736863f6246a60af96.jpg python 线性代数：[18]线性规划求最优解 %}

- 最后我们将五环也绘制在图上，看看我的房子是不是在五环上：

{% asset_img cdfe7281800a19d8df3f994f30fa828ba61e4678.jpg python 线性代数：[18]线性规划求最优解 %}

- 最后求得的结果绘图如下：蓝色线就表示五环

{% asset_img 54baacfb43166d22bfdc07de452309f79152d296.jpg python 线性代数：[18]线性规划求最优解 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
