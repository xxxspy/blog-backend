---
title: SPSS实例：[25]列联表相关
date: 2015-02-23 18:03:17
tags: [spss]
author: mlln.cn
---
如何求两个二分类数据的相关系数？或者两个变量不都是二分类，可能还有三分类、四分类，我们怎么求他们的相关呢？这种数据有一个特点就是，这两个变量都是名义变量，他们的数据没有大小之分，只有类别的不同，比如性别就是一个名义变量，我们定义男生为1，女生为2，不能说明女生大于男生。今天我们就来学习一下如何使用spss求列联表相关，而列联表相关就是用来求解分类数据（不连续数据）的相关的。

- 数据的录入形式：如图所示，年龄组取值分别为0和1，图书顺序取值分别为1和2

{% asset_img 29752a9b033b5bb53d7f579534d3d539b700bcf6.jpg SPSS实例：[25]列联表相关 %}

- 打开交叉表分析对话框，如图所示，找到菜单

{% asset_img 54baacfb43166d2299df62ff442309f79152d2f6.jpg SPSS实例：[25]列联表相关 %}

- 我们将这两个变量分别放入行和列框中，这就是我们要求相关的两个变量

{% asset_img 08b68e529822720ed166959179cb0a46f31fabf6.jpg SPSS实例：[25]列联表相关 %}

- 点击statistics，设置要输出的参数

{% asset_img 4e83cb628535e5ddc1c1d2b474c6a7efcf1b62a8.jpg SPSS实例：[25]列联表相关 %}

- 在这里，我们用到了contingency coefficient（列联系数），点击continue按钮

{% asset_img 8474fbdde71190ef5e16e5b4cc1b9d16fcfa60a8.jpg SPSS实例：[25]列联表相关 %}

- 回到主对话框，我们点击ok即可开始处理数据

{% asset_img 9c57e3faaf51f3de9b5fce0f96eef01f3b2979a8.jpg SPSS实例：[25]列联表相关 %}

- 在结果中，我们主要看到列联系数的值和近似sig值，显然，相关系数很小，也不显著，说明两个变量不相关。

{% asset_img d56b3634349b033ba8208bb117ce36d3d439bdf6.jpg SPSS实例：[25]列联表相关 %}

- 如果觉得这篇文章写的还可以，记得分享给你的小伙伴！！

{% asset_img b74124f33a87e950ae5a650712385343faf2b4c9.jpg SPSS实例：[25]列联表相关 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
