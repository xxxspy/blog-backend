---
title: python 线性代数：[16]线性组合均值协方差阵
date: 2016-02-03 18:11:15
tags: [python]
author: mlln.cn
---
这里从《实用多元统计分析》（理查德~约翰逊)这本书里摘出一个例子，看题目：

- 引入相关模块

{% asset_img 09bb4f3d269759ee2a25ae8ab1fb43166d22df3f.jpg python 线性代数：[16]线性组合均值协方差阵 %}

- 创建几个符号，代码已知量

{% asset_img 58af236d55fbb2fb595e96534c4a20a44623dc3f.jpg python 线性代数：[16]线性组合均值协方差阵 %}

- sigma代表已知的X矩阵的协方差矩阵
sigma =

{% asset_img e6508eef76c6a7efbffe6767fefaaf51f2de665c.jpg python 线性代数：[16]线性组合均值协方差阵 %}

{% asset_img 61183b2dd42a283403d3f84a58b5c9ea15cebf3f.jpg python 线性代数：[16]线性组合均值协方差阵 %}

- u代表已知的x矩阵的均值向量
这是均值向量

{% asset_img 99636c0e0cf3d7ca5e83f137f11fbe096b63a93f.jpg python 线性代数：[16]线性组合均值协方差阵 %}

{% asset_img 5af4d7ea15ce36d3e8714d7139f33a87e950b13f.jpg python 线性代数：[16]线性组合均值协方差阵 %}

- 、这是线性组合的系数矩阵

{% asset_img f15e24292df5e0fee4c046405f6034a85fdf725c.jpg python 线性代数：[16]线性组合均值协方差阵 %}

{% asset_img 570f8c58d109b3de17672b29cfbf6c81810a4c5c.jpg python 线性代数：[16]线性组合均值协方差阵 %}

- 计算均值向量，利用均值向量的计算公式：
代码为：
求得：

{% asset_img 9304c888d43f8794105b866fd11b0ef41ad53a88.jpg python 线性代数：[16]线性组合均值协方差阵 %}

{% asset_img 1b0d4f0fd9f9d72a5311de5cd72a2834349bbb3f.jpg python 线性代数：[16]线性组合均值协方差阵 %}

{% asset_img cdfe7281800a19d82ddb4b4430fa828ba71e465c.jpg python 线性代数：[16]线性组合均值协方差阵 %}

- 同样，我们利用协方差矩阵的公式：
代码为：

- 求得结果为：

{% asset_img b29f8282d158ccbfe14b7b7b1ad8bc3eb03541b9.jpg python 线性代数：[16]线性组合均值协方差阵 %}

{% asset_img e1bf8725bc315c60b44da4ae8eb1cb134854775c.jpg python 线性代数：[16]线性组合均值协方差阵 %}

{% asset_img b13fd48065380cd7dc6b6caca244ad345982813f.jpg python 线性代数：[16]线性组合均值协方差阵 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
