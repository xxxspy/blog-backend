---
title: spss如何使用变量的取值模式进行聚类
date: 2016-05-15 18:05:11
tags: [spss]
author: mlln.cn
---
spss聚类分析中，默认的聚类方法是按照变量的取值水平进行聚类，但是有时候，为了符合我们研究的要求，需要按照变量的取值模式进行聚类，这时候就用到了这里提到的一个方法：By case
工具/原料


- spss20.0
方法/步骤


- 先在spss中打开你要处理的数据，然后点击菜单：analyse--classify--hierarchical cluster，打开聚类分析的对话框

{% asset_img bf096b63f6246b604ca28fa1ebf81a4c500fa2b2.jpg spss如何使用变量的取值模式进行聚类 %}

- 将指标变量放入independent列表，然后把地区放入标签栏，因为地区可以作为case的标签

{% asset_img 80cb39dbb6fd526603e700c1ab18972bd5073612.jpg spss如何使用变量的取值模式进行聚类 %}

- 点击method按钮，这就是我们的重头戏，在在方法对话框中，我们需要设置Z分数的计算方法

{% asset_img 77094b36acaf2eddcd37753c8d1001e938019324.jpg spss如何使用变量的取值模式进行聚类 %}

- 如图所示，将standardised设置为Z score，然后勾选by case

{% asset_img c75c10385343fbf2eb1299f6b07eca8065388f2c.jpg spss如何使用变量的取值模式进行聚类 %}

- 点击ok，开始处理数据，等会就输出结果

{% asset_img a71ea8d3fd1f41343caf39ab251f95cad0c85e4e.jpg spss如何使用变量的取值模式进行聚类 %}

- 第一个表格是聚类过程表，从聚类系数可以帮助我们判断将数据分为几类最合适，判断的方法是，相邻的两个数据变化的幅度显著大于前面的系数的变化范围，这时候分类在这里就是最好的

{% asset_img b03533fa828ba61e0fd9f7fa4134970a304e592b.jpg spss如何使用变量的取值模式进行聚类 %}

- 这里叫做层次聚类谱系图，该图也是帮助我们查看聚类过程的，我们看到如图所示，沿着垂直方向画一条线，这条线与图中的水平线交叉点就是分的类别，有几个交叉点就有几个类别。当然，你所画的线可以决定你的数据分成了几类，越往右边，分类数目越少

{% asset_img 7af40ad162d9f2d34b591b3aa9ec8a136227cc9e.jpg spss如何使用变量的取值模式进行聚类 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
