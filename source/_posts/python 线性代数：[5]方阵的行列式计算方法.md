---
title: python 线性代数：[5]方阵的行列式计算方法
date: 2016-09-11 18:23:19
tags: [python]
author: mlln.cn
---
如何计算方阵的行列式，用到的是numpy模块的linalg.det方法，关于行列式的定义你应该懂，但是其实也不用记住，以后直接用numpy计算就可以了。下面我们看看如何使用numpy计算矩阵的行列式吧：

- 行列式的算法：这是二阶方阵行列式

{% asset_img a992e31f4134970ab41e34dd97cad1c8a6865d97.jpg python 线性代数：[5]方阵的行列式计算方法 %}

- 行列式的算法：这是三阶行列式

{% asset_img 0db52fadcbef76090899bd6d2cdda3cc7dd99e76.jpg python 线性代数：[5]方阵的行列式计算方法 %}

- 先引入numpy模块

{% asset_img b3f6cea20cf431ad986a89c84936acaf2fdd984c.jpg python 线性代数：[5]方阵的行列式计算方法 %}

- 创建两个方阵

{% asset_img 1f569482b9014a9013248c4cab773912b21beeef.jpg python 线性代数：[5]方阵的行列式计算方法 %}

- 使用det方法求得方阵E和方阵F的行列式

{% asset_img 3853ad1bb051f8196a3fc9bbd8b44aed2f73e7ef.jpg python 线性代数：[5]方阵的行列式计算方法 %}

{% asset_img 373bc4b44aed2e737af34cdd8501a18b86d6faef.jpg python 线性代数：[5]方阵的行列式计算方法 %}

- 这是今天用到的所有代码

- >>> E

- array([[1, 2, 3],

-        [4, 5, 6],

-        [7, 8, 9]])

- >>> F

- array([[-1,  0,  1],

-        [ 2,  3,  4],

-        [ 5,  6,  7]])

- >>> 

- >>> 

- >>> 

- >>> np.linalg.det(E)

- 6.6613381477509402e-16

- >>> 

- >>> np.linalg.det(F)

- 2.664535259100367e-15

- >>> 

- >>> 

- >>> C

- array([[1, 2],

-        [1, 3]])

- >>> 

- >>> np.linalg.det(C)

- 1.0

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
