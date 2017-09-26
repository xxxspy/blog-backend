---
title: spss协方差分析如何进行事后两两比较
date: 2015-08-03 18:23:19
tags: [spss]
author: mlln.cn
---
 在进行两两比较之前，我们最后先做一个协方差分析，在前面的文章讲了如何进行协方差分析，如果写反差分析显示出来了显著的结果，然后再进行两两的事后检验，下面是具体的过程：
方法/步骤


- 先进行协方差分析，结果如果达到了显著水平，在进行两两比较，在菜单栏上执行analyze--general linear model--univariate

{% asset_img 377adab44aed2e73568980d58701a18b86d6fae3.jpg spss协方差分析如何进行事后两两比较 %}

- 将自变量、因变量、斜变量都放到相应的位置，这里评定得分是因变量，培训方式是自变量、家庭指数是斜变量

{% asset_img 37d12f2eb9389b501ecbe6ab8535e5dde7116e16.jpg spss协方差分析如何进行事后两两比较 %}

- 点击options按钮，进入子对话框

{% asset_img f2deb48f8c5494ee911609e02df5e0fe99257e16.jpg spss协方差分析如何进行事后两两比较 %}

- 将培训方式，也就是自变量放到右侧的列表里，勾选下面的描述统计和方差齐性检验，点击继续按钮

{% asset_img dc54564e9258d109c1d7af4bd158ccbf6c814d16.jpg spss协方差分析如何进行事后两两比较 %}

- 点击model按钮，选择模型

{% asset_img a71ea8d3fd1f413416030387251f95cad1c85e16.jpg spss协方差分析如何进行事后两两比较 %}

- 选择full factorial，然后点击continue按钮，返回主对话框

{% asset_img c83d70cf3bc79f3d76d5e2c9baa1cd11728b2916.jpg spss协方差分析如何进行事后两两比较 %}

- 点击paste按钮，进入命令编辑窗口

{% asset_img b3119313b07eca8051663f1e912397dda04483e3.jpg spss协方差分析如何进行事后两两比较 %}

- 在这里你会看到很多代码，我们留下前三行，如图所示，然后删除其他的行

{% asset_img b7fd5266d01609240011a4e2d40735fae6cd3416.jpg spss协方差分析如何进行事后两两比较 %}

- 编辑下面的六行代码，使用的是lmatrix命令，我们知道培训方式有三个水平，所以要进行三次两两比较才能将所有的水平进行比较。

{% asset_img d50735fae6cd7b892f583c7a0f2442a7d9330e16.jpg spss协方差分析如何进行事后两两比较 %}

- 点击运行按钮，开始处理数据

{% asset_img 9a504fc2d5628535b183d4d890ef76c6a6ef63e3.jpg spss协方差分析如何进行事后两两比较 %}

- 在出来的结果中，我们主要看的是定制假设检验，因为上面的命令中用了三次LMATRIX，所以会有三个定制假设检验，我们主要看下面的sig值，如图所示，这个值小于0.05就可以认为是有差异的

-  

{% asset_img 5bafa40f4bfbfbed6b6d308678f0f736afc31f16.jpg spss协方差分析如何进行事后两两比较 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
