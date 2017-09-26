---
title: spss多重共线性的诊断方法
date: 2016-07-01 18:17:11
tags: [spss]
author: mlln.cn
---
spss诊断多重共线性是在多重线性回归的时候容易出现的一个问题，他指的是多个变量可能高相关，造成了模型方程的不稳定，一般是在方程求出来以后，发现方程的问题，然后进行的方程的诊断，下面是诊断多重共线性的步骤: 
方法/步骤


- 多重共线性的诊断是在回归中进行的，所以先打开回归的对话框：analyse--regression--linear，打开线性回归对话框

{% asset_img d1160924ab18972b3fb4c029e6cd7b899f510a43.jpg spss多重共线性的诊断方法 %}

- 将自变量因变量都放到各自的位置，然后点击statistic

{% asset_img d000baa1cd11728b96f14cc1c8fcc3cec2fd2c71.jpg spss多重共线性的诊断方法 %}

- 在该对话框中，有一个多重共线性诊断的选项，勾选他，如图所示，点击continue按钮，返回主对话框

{% asset_img 63d0f703918fa0ec326ca4ee269759ee3c6ddbae.jpg spss多重共线性的诊断方法 %}

- 点击ok按钮，开始输出诊断结果

{% asset_img b812c8fcc3cec3fd2ae26796d688d43f86942771.jpg spss多重共线性的诊断方法 %}

- 我们先来看这两个参数，特征根（Eigenvalue）：多个维度特征根约为0证明存在多重共线性；条件指数（Condition Index）：大于10时提示我们可能存在多重共线性

{% asset_img 279759ee3d6d55fbf26db6c56d224f4a21a4ddae.jpg spss多重共线性的诊断方法 %}

- 接着来看相关系数矩阵，找到数值接近1的相关，这也提示出可能存在多重共线性。

-  

{% asset_img 7c1ed21b0ef41bd54d8f281751da81cb38db3d71.jpg spss多重共线性的诊断方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
