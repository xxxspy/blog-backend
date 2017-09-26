---
title: SPSS实例：[30]kappa系数怎么计算
date: 2016-01-23 18:01:23
tags: [spss]
author: mlln.cn
---
假如有两个评分者针对一批作文进行分级，分为好中差三级，分级结果见下表。你怎么判定这两个评分者的评分结果是否一致呢？这时候就要计算卡帕系数了。

- 好中差分别用123来表示，将数据录入到spss中

{% asset_img fab3ac119313b07ea149be440ed7912396dd8c43.jpg SPSS实例：[30]kappa系数怎么计算 %}

- 接着，我们再给数据加权，用频数作为加权变量，不会的可以参考我上一篇文章，这里不再重复。http://jingyan.baidu.com/article/9f7e7ec050c3c36f28155434.html

{% asset_img b25aae51f8198618261306c848ed2e738ad4e6e3.jpg SPSS实例：[30]kappa系数怎么计算 %}

- 接着，打开菜单：分析--描述统计-交叉表，将两个变量分别放入行和列变量

{% asset_img 2f3295d4b31c8701b6e25baa257f9e2f0608ffe3.jpg SPSS实例：[30]kappa系数怎么计算 %}

- 设置输出的描述性统计，这里就是输出kappa系数的地方

{% asset_img fd428c45d688d43f541278be7f1ed21b0ff43b80.jpg SPSS实例：[30]kappa系数怎么计算 %}

- 勾选kappa系数，然后点击继续按钮

{% asset_img 29790130e924b899896890746c061d950b7bf6e3.jpg SPSS实例：[30]kappa系数怎么计算 %}

- 回到了主菜单，我们点击ok按钮

{% asset_img 4d4970061d950a7b2761a78808d162d9f3d3c9e3.jpg SPSS实例：[30]kappa系数怎么计算 %}

- 评分者一致性系数就到此计算出来了。

{% asset_img 1cd4147b02087bf42db8bea5f0d3572c10dfcfe3.jpg SPSS实例：[30]kappa系数怎么计算 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
