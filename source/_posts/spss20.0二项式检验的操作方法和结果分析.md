---
title: spss20.0二项式检验的操作方法和结果分析
date: 2015-06-01 18:03:17
tags: [spss]
author: mlln.cn
---
 只有两个值的变量叫做二分变量，比如性别就是一个二分变量，它只有两个值：男女。为了检验男女的比率是否符合1:1，我们可以使用二项式检验。下面是具体的操作方法和数据结果的分析。
方法/步骤


- 在spss20.0中，要检验二分变量的两个值的比例是否和理论值相左，我们先在菜单栏上执行：analyze-nonparamecric-legacy dialogs-binomial

{% asset_img b64543a98226cffc086a6043b9014a90f703eafb.jpg spss20.0二项式检验的操作方法和结果分析 %}

- 将你要检验的这个二分变量放到test variable list中

{% asset_img 4b90f603738da977246f59dab051f8198718e3fb.jpg spss20.0二项式检验的操作方法和结果分析 %}

- 点击options按钮，设置要输出的参数有哪些

{% asset_img 72f082025aafa40f4ca3112cab64034f79f019dd.jpg spss20.0二项式检验的操作方法和结果分析 %}

- 这里我们勾选descriptive就可以了，可以看到数据的描述性统计结果

{% asset_img 42a98226cffc1e179dda53c04a90f603728de9de.jpg spss20.0二项式检验的操作方法和结果分析 %}

- 设置检验的比率，这个比率是其中一个变量值在所有的变量值中的比例，比如男女比例一概是1:1，所以这里应该填写0.5，这样就可以建议男女比例是不是1:1了

{% asset_img 4d086e061d950a7b357591350ad162d9f3d3c9fb.jpg spss20.0二项式检验的操作方法和结果分析 %}

- 点击ok，开始运行，输出结果

{% asset_img 63d9f2d3572c11df979160d2632762d0f603c2fb.jpg spss20.0二项式检验的操作方法和结果分析 %}

- 第一个图为描述性统计，第二个图是二项式检验结果，我们看到显著性为0.000这说明该数据的比率与理论值有差异，且差异明显。

-  

-  

{% asset_img b151f8198618367af9eca02c2e738bd4b21ce5de.jpg spss20.0二项式检验的操作方法和结果分析 %}

{% asset_img 503d269759ee3d6d1f86583a43166d224e4adefb.jpg spss20.0二项式检验的操作方法和结果分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
