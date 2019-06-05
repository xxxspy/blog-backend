---
title: spss聚类分析如何对分类结果进行检验
date: 2016-03-15 18:03:15
tags: [spss]
author: mlln.cn
---
聚类分析的结果都知道，就是获得几个类别，那么我们怎么知道这些类别是合理的呢？这里提供一个方法，就是利用means方法，检验各个类别在所有变量上的差异，如果差异显著，我们就可以认为分类结果是可靠的。
方法/步骤


- 假设我们现在已经得到了聚类的结果，所有的case都已经分类了，我们看到在数据窗口已经形成了若干个新的变量，显示了case的分类结果，如图所示，这里显示了三个聚类的结果，分别是把数据分为3、4、5类的结果

{% asset_img f7246b600c338744ad481ea9510fd9f9d62aa051.jpg spss聚类分析如何对分类结果进行检验 %}

{% asset_img b7003af33a87e9506ff8c2b910385343faf2b473.jpg spss聚类分析如何对分类结果进行检验 %}

- 在菜单栏上执行：analyse--compare means--means，打开平均数对话框

{% asset_img 6d81800a19d8bc3e18e6371f828ba61ea9d3457c.jpg spss聚类分析如何对分类结果进行检验 %}

- 将指标变量都放入因变量框中，然后将分组变量（聚类分析得到的变量）放入因变量中

{% asset_img b17eca8065380cd7f4db9338a144ad3458828119.jpg spss聚类分析如何对分类结果进行检验 %}

- 点击ok按钮，开始运行数据，并显示结果

{% asset_img 5ab5c9ea15ce36d380dbb2e53af33a87e850b103.jpg spss聚类分析如何对分类结果进行检验 %}

- 我们会看到三种分类结果各自的平均数，下面的三个表格分别是将case分为5、4、3类的结果，当然这种方法只能计算出各组平均数，如何检验平均数的差异就要用到下面的方法

{% asset_img 902397dda144ad3431eab752d0a20cf430ad8589.jpg spss聚类分析如何对分类结果进行检验 %}

{% asset_img 622762d0f703918f89c40d1f513d269758eec4c9.jpg spss聚类分析如何对分类结果进行检验 %}

{% asset_img d53f8794a4c27d1e1f510b111bd5ad6edcc438eb.jpg spss聚类分析如何对分类结果进行检验 %}

- 在菜单栏上执行：analyse--compare means--one way anova

{% asset_img d01373f082025aaf4f5a4e1efbedab64024f1afe.jpg spss聚类分析如何对分类结果进行检验 %}

- 将指标变量放到因变量列表，将分组变量放入factor中，然后点击ok，开始处理数据

{% asset_img b17eca8065380cd7f5a69238a144ad34588281ae.jpg spss聚类分析如何对分类结果进行检验 %}

- 我们看到下面的这个表格就是对平均数的差异的检验了，看sig这一列，除了一个指标，其他指标都达到了显著的水平，这说明这种分类还是比较有效的。

{% asset_img 503d269759ee3d6d7a57b71e43166d224e4ade55.jpg spss聚类分析如何对分类结果进行检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
