---
title: python 线性代数：[17]线性组合的协方差
date: 2016-07-11 18:23:01
tags: [python]
author: mlln.cn
---
我们先来看这个练习题：

- 先来创建这个X矩阵

{% asset_img 425773224f4a20a490994a8593529822730ed0aa.jpg python 线性代数：[17]线性组合的协方差 %}

- 创建两个系数向量

{% asset_img 6c63514a20a44623de4dd3209b22720e0df3d7aa.jpg python 线性代数：[17]线性组合的协方差 %}

- 先计算X的协方差矩阵
结果为：

{% asset_img 54baacfb43166d229b9163d6452309f79152d24b.jpg python 线性代数：[17]线性组合的协方差 %}

{% asset_img fab3ac119313b07ec83b264a0fd7912396dd8caa.jpg python 线性代数：[17]线性组合的协方差 %}

- 计算X的均值向量，注意设置axis为0
求得结果为：

{% asset_img f35ea0096b63f62488da4f418444ebf81b4ca3aa.jpg python 线性代数：[17]线性组合的协方差 %}

{% asset_img 3792cb39b6003af3c25caa22362ac65c1138b64b.jpg python 线性代数：[17]线性组合的协方差 %}

- 求得两个线性组合的均值：
结果为：

{% asset_img 6a2112338744ebf8fdf6127ddaf9d72a6159a7aa.jpg python 线性代数：[17]线性组合的协方差 %}

{% asset_img 3bb22487e950352a3d87534a5043fbf2b3118b4b.jpg python 线性代数：[17]线性组合的协方差 %}

- 求两个线性组合的方差
结果为：

{% asset_img 734f12f3d7ca7bcbd49db16dbd096b63f724a84b.jpg python 线性代数：[17]线性组合的协方差 %}

{% asset_img fab3ac119313b07ec85c264a0fd7912396dd8c4b.jpg python 线性代数：[17]线性组合的协方差 %}

- 求两个线性组合的协方差：
结果为：

{% asset_img 504ec7f9d72a6059c9f697582b34349b023bba4b.jpg python 线性代数：[17]线性组合的协方差 %}

{% asset_img 0d968f2397dda144a5e81af0b1b7d0a20df4864b.jpg python 线性代数：[17]线性组合的协方差 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
