---
title: spss按照3个标准差筛选数据的方法
date: 2015-10-03 18:23:17
tags: [spss]
author: mlln.cn
---
在数据处理的时候，一般来说数据都是正态分布的，按照正态分布的性质，三个标准差以外的数据都，可以被看作是错误的数据从而排除掉，现在跟大家分享一下如何根据标准差来筛选数据。
方法/步骤


- 要想按照标准差筛选数据，必须先要求出每个数据的Z分数，如图所示，在菜单栏上执行analyze--descriptive statistic--descriptive，打开描述统计对话框

{% asset_img a1ec08fa513d26976bba3d8c55fbb2fb4216d8f1.jpg spss按照3个标准差筛选数据的方法 %}

- 将我们要筛选的数据放入到变量对话框中，勾选save standardized values as variables，这样就能输出Z分数了，点击ok按钮，输出结果

{% asset_img cc11728b4710b9120051c32fc3fdfc039345224a.jpg spss按照3个标准差筛选数据的方法 %}

- 我们看到，在数据窗口中多了一列数据，这就是我们求得的z分数，接下来要根据这组数据。来筛选数据

{% asset_img a08b87d6277f9e2f10d528d91f30e924b999f37a.jpg spss按照3个标准差筛选数据的方法 %}

- 在菜单栏上执行data---select cases，打开数据筛选对话框

{% asset_img 43a7d933c895d1434761d0f273f082025baf07cf.jpg spss按照3个标准差筛选数据的方法 %}

- 我们对case按照标准差进行选择，需要根据条件来选择，所以选择if conditions is satisfied，点击if来设置条件

{% asset_img cb8065380cd79123fe93a0a5ad345982b3b780eb.jpg spss按照3个标准差筛选数据的方法 %}

- 在这里我们输入公式Zx2  <= 3 & Zx2  >=  -3 ，这个条件的意思就是选择数值在3和-3之间。点击continue按钮，返回到主对话框

{% asset_img b2de9c82d158ccbfcba582eb19d8bc3eb03541c1.jpg spss按照3个标准差筛选数据的方法 %}

- 在主对话框中，点击ok按钮，开始处理数据

{% asset_img 5ab5c9ea15ce36d38268b4e13af33a87e850b1f6.jpg spss按照3个标准差筛选数据的方法 %}

- 最后我们看一下处理的效果，超过三个标准差的数据在前面都有一个斜杠表示删除了。以后处理数据的时候他们就不参与了

{% asset_img b8389b504fc2d562010ce73ce71190ef77c66cde.jpg spss按照3个标准差筛选数据的方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
