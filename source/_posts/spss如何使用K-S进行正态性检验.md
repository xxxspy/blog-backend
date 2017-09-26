---
title: spss如何使用K-S进行正态性检验
date: 2016-09-23 18:03:15
tags: [spss]
author: mlln.cn
---
在对数据进行t检验或者f检验之前需要让数据满足正态性的要求，所以应该对数据进行正态性检验，检验正态性的方法中，K-S检验是最普遍的方法之一，下面我们就来具体的操作一下图和进行K-S检验。
方法/步骤


-  我拿到数据以后，先要在spss中组织数据，如图所示，第一列变量是我们要检验是否为正态的变量，第二列是数据的分组，即他们的组号。有的时候你的数据没有分组，也就是只有一个组，那就没有必要写group列了

{% asset_img c2cec3fdfc0392458db6a68a8794a4c27d1e2537.jpg spss如何使用K-S进行正态性检验 %}

- 为了分别检验每个分组的数据是否符合正态分布，我们要先将各个组分离（如果你的数据只有一个组那就没必要进行这一步了），如图所示在菜单栏上执行：data---split file

{% asset_img 71cf3bc79f3df8dc8133c814cd11728b4710282c.jpg spss如何使用K-S进行正态性检验 %}

- 勾选【organize output by groups】，它的意思是分组呈现变量结果，将分组情况这个变量添加到group based on中，点击ok按钮

{% asset_img d000baa1cd11728b1323cba7c8fcc3cec3fd2c2c.jpg spss如何使用K-S进行正态性检验 %}

- 接着要对正太性进行检验了，我们在菜单栏上执行：analyze--nonparametric---one sample

{% asset_img 80cb39dbb6fd5266ba287b91ab18972bd4073637.jpg spss如何使用K-S进行正态性检验 %}

- 切换到fileds这个选项，然后将你要检验的变量放到右侧的text fields中

{% asset_img 9345d688d43f8794faf10fabd21b0ef41bd53a2c.jpg spss如何使用K-S进行正态性检验 %}

- 切换到settings选项，然后点击【choose test】，勾选右侧的K-S检验，如图所示。然后点击下方的options

{% asset_img 0ff41bd5ad6eddc434e9f37e39dbb6fd5266332c.jpg spss如何使用K-S进行正态性检验 %}

- 打开如图所示的对话框，我们将normal这个选项勾选，因为没有已知的正太分布的参数，所以选择use sample data，点击ok

{% asset_img dcc451da81cb39dbdece20d3d0160924ab18302c.jpg spss如何使用K-S进行正态性检验 %}

- 切换到text options 设置显著性水平，如图所示，一般为0.05或者0.01

{% asset_img 72f082025aafa40f34c58958ab64034f78f01937.jpg spss如何使用K-S进行正态性检验 %}

- 点击run，你就会看到数据处理的结果了

{% asset_img ac4bd11373f08202279cd6ba4bfbfbedab641b2c.jpg spss如何使用K-S进行正态性检验 %}

- 下面是各个组的检验结果，结果显示的很详细，每个组都没有达到显著水平，接受原假设，即所有的组都是正态分布的。

-  

{% asset_img cefc1e178a82b901dbae84b6738da9773912ef30.jpg spss如何使用K-S进行正态性检验 %}

{% asset_img f703738da97739122525c2e4f8198618367ae230.jpg spss如何使用K-S进行正态性检验 %}

{% asset_img b21bb051f8198618ac44a8014aed2e738bd4e630.jpg spss如何使用K-S进行正态性检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
