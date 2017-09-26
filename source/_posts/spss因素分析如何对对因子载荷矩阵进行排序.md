---
title: spss因素分析如何对对因子载荷矩阵进行排序
date: 2015-08-23 18:01:17
tags: [spss]
author: mlln.cn
---
在确定因子意义的时候需要看变量和因子的关系，如果比如某个因子在某个变量上的载荷为0.9，我们可以认为这个变量和因子的关系很紧密，可以用这个变量来解释这个因子，对载荷进行排序就可以帮助我们一眼看到因子之间的不同。
方法/步骤


- 在spss中准备好数据，然后在菜单栏上执行analyse--dimension reduction--factor，打开factor analyse对话框

{% asset_img 024f78f0f736afc3d61343b1b319ebc4b64512c2.jpg spss因素分析如何对对因子载荷矩阵进行排序 %}

- 将所有需要分析的变量放到variables框中，点击箭头按钮可以添加变量

{% asset_img 838ba61ea8d3fd1f2b45deee304e251f94ca5f91.jpg spss因素分析如何对对因子载荷矩阵进行排序 %}

- 点击option按钮，打开选项对话框

{% asset_img 0df3d7ca7bcb0a460845f7ed6b63f6246a60affb.jpg spss因素分析如何对对因子载荷矩阵进行排序 %}

- 在选项对话框中，找到coefficient display format，勾选下面的sorted by size，这样设置就是为了让输出的因素载荷矩阵按照因素载荷的大小进行排序，方便我们查看结果

{% asset_img bd315c6034a85edfd9ca82f749540923dc54759b.jpg spss因素分析如何对对因子载荷矩阵进行排序 %}

- 我们看到下面的两个表格，都是旋转因子以后的载荷矩阵，他们的区别是，第二个表格中的载荷已经经过了排序，我们可以直观的看到不同的变量在各个因子上的载荷，并将变量分类。

{% asset_img b999a9014c086e06cb72439f02087bf40bd1cb08.jpg spss因素分析如何对对因子载荷矩阵进行排序 %}

{% asset_img 1c950a7b02087bf4d0362b3df2d3572c10dfcf08.jpg spss因素分析如何对对因子载荷矩阵进行排序 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
