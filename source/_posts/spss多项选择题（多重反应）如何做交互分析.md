---
title: spss多项选择题（多重反应）如何做交互分析
date: 2016-08-17 18:11:05
tags: [spss]
author: mlln.cn
---
我们经常做的是单项选择题的交互分析，现在有一个多项选择题，怎么知道别的变量对这个变量有影响呢？那就需要使用下面这个方法，对多重反应做交互分析，下面的一个例子就是分析性别对信息来源的选择有没有影响，信息来源就是一个多重选择题。
方法/步骤


- 在做交互分析以前先要做数据集，如图所示，在菜单栏上执行：analyze--multiple response--define

{% asset_img aa64034f78f0f736690748f10a55b319eac41340.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 将所有选项构成的变量都放到变量集列表中

{% asset_img e61190ef76c6a7ef941cafd6fdfaaf51f3de6603.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 设定这些题中有几个分类，如果是是否型的勾选【dichotomies】

{% asset_img f2deb48f8c5494ee921808e92df5e0fe99257e03.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 填写数据集的名称和标签，点击添加按钮，数据集定义完成

{% asset_img 5d6034a85edf8db1a7147b940923dd54564e7403.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 在菜单栏上执行：analyze--multiple response--crosstable

{% asset_img 8ad4b31c8701a18b641216bf9e2f07082938fe41.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 将刚才定义好的数据集放到row列表，将性别变量放到column列表

{% asset_img cdbf6c81800a19d8c63983f533fa828ba61e4603.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 选中性别，定义一下这个变量，点击define ranges

{% asset_img a8014c086e061d95e5bf33c87bf40ad163d9ca41.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 因为性别变量就是1和2，所以输入最大值和最小值，然后点击continue按钮

{% asset_img a8ec8a13632762d00cc7a04fa0ec08fa503dc641.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 回到这个对话框，点击options按钮，定义输出结果

{% asset_img 91529822720e0cf3d80f4a0b0a46f21fbf09aa41.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 这里需要勾选输出列变量的百分比，所以选中column，点击continue按钮

{% asset_img 730e0cf3d7ca7bcb1b83c3dfbe096b63f724a841.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 回到这个对话框，点击ok按钮，开始输出结果

{% asset_img a5c27d1ed21b0ef4b9d29faeddc451da81cb3e03.jpg spss多项选择题（多重反应）如何做交互分析 %}

- 分析这个结果，我们看到男女比例基本上没有太大的差别，所以性别和信息来源这两个变量没有交互作用

-  

{% asset_img 6a600c338744ebf8008960cfd9f9d72a6159a741.jpg spss多项选择题（多重反应）如何做交互分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
