---
title: spss二分类的logistic回归的操作和分析方法
date: 2015-03-11 18:11:11
tags: [spss]
author: mlln.cn
---
二分类指的是因变量的数据只有两个值，代表事物的两种类别，典型的二分类变量如性别、是否患病等。因变量为二分变量原则上是无法做回归的，在回归方程中的因变量实质上是概率，而不是变量本身。在理解二分类变量以后，我们看看如何做二分类变量的logistic回归。
工具/原料


- spss20.0
方法/步骤


- 打开数据以后，菜单栏上依次点击：analyse--regression--binary logistic，打开二分回归对话框

{% asset_img e850352ac65c1038bd6b882fb2119313b17e89c2.jpg spss二分类的logistic回归的操作和分析方法 %}

- 将因变量和自变量放入格子的列表里，如图所示，上面的是因变量，下面的是自变量，我们看到这里有三个自变量

{% asset_img d788d43f8794a4c22380a1c60ef41bd5ac6e39bf.jpg spss二分类的logistic回归的操作和分析方法 %}

- 设置回归方法，这里选择最简单的方法：enter，它指的是将所有的变量一次纳入到方程。其他方法都是逐步进入的方法，在前面的文章中有介绍，这里就不再熬述。

{% asset_img 2f738bd4b31c8701013bf40b277f9e2f0608ff4a.jpg spss二分类的logistic回归的操作和分析方法 %}

{% asset_img 060828381f30e9241f17dddc4c086e061c95f7a8.jpg spss二分类的logistic回归的操作和分析方法 %}

- 点击ok，开始处理数据并检验回归方程，等待一会就会弹出数据结果窗口

{% asset_img 962bd40735fae6cd1494ea8c0fb30f2442a70f3e.jpg spss二分类的logistic回归的操作和分析方法 %}

- 看到的第一个结果是对case的描述，第一个列表告诉你有多少数据参与的计算，有多少数据是缺省值；第二个列表告诉你因变量的编码方式，得分为1代表患病，得分为0代表没有患病

{% asset_img c75c10385343fbf25d16e7ceb07eca8065388f21.jpg spss二分类的logistic回归的操作和分析方法 %}

- 这个列表告诉你在没有任何自变量进入以前，预测所有的case都是患病的正确率，正确率为%52.6

{% asset_img 9345d688d43f8794f85f09c3d21b0ef41ad53abe.jpg spss二分类的logistic回归的操作和分析方法 %}

- 下面这个列表告诉你在没有任何自变量进入以前，常数项的预测情况。B是没有引入自变量时常数项的估计值，SE它的标准误，Wald是对总体回归系数是否为0进行统计学检验的卡方。

{% asset_img 00e93901213fb80e72b2213a36d12f2eb83894ff.jpg spss二分类的logistic回归的操作和分析方法 %}

- 下面这个表格结果，通过sig值可以知道如果将模型外的各个变量纳入模型，则整个模型的拟合优度改变是否有统计学意义。 sig值小于0.05说明有统计学意义

{% asset_img 9d82d158ccbf6c81b40b6f05bc3eb13533fa401a.jpg spss二分类的logistic回归的操作和分析方法 %}

- 这个表格是对模型的全局检验，为似然比检验，供给出三个结果：同样sig值<0.05表明有统计学意义。

{% asset_img 55e736d12f2eb938968c391fd5628535e4dd6f7d.jpg spss二分类的logistic回归的操作和分析方法 %}

{% asset_img 09fa513d269759ee816d2226b2fb43166d22df1a.jpg spss二分类的logistic回归的操作和分析方法 %}

- 下面的结果展示了-2log似然值和两个伪决定系数。两个伪决定系数反应的是自变量解释了因变量的变异占因变量的总变异的比例。他们俩的值不同因为使用的方法不同。

{% asset_img e7cd7b899e510fb361763a7ad933c895d0430ceb.jpg spss二分类的logistic回归的操作和分析方法 %}

- 分类表，这里展示了使用该回归方程对case进行分类，其准确度为%71.8。

{% asset_img 08f790529822720ecb13af177bcb0a46f31fab7a.jpg spss二分类的logistic回归的操作和分析方法 %}

- 最后是输出回归方程中的各变量的系数和对系数的检验额值，sig值表明该系数是否具有统计学意义。到此，回归方程就求出来了。

{% asset_img d058ccbf6c81800a2bcbc5e3b13533fa828b4734.jpg spss二分类的logistic回归的操作和分析方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
