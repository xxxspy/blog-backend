---
title: spss中如何检验残差的相互独立性
date: 2015-05-17 18:11:15
tags: [spss]
author: mlln.cn
---
在做线性回归的时候要检验残差的独立性，这里交给大家一个方法可以在做回归的时候用到的，可以方便的看出残差之间是否独立，下面是具体的方法：
工具/原料


- spss20.0
方法/步骤


- 首先要早spss中准备好数据，如图所示，每一列数据作为一个变量

{% asset_img 962bd40735fae6cdf93affa50fb30f2443a70f63.jpg spss中如何检验残差的相互独立性 %}

- 在菜单栏上执行：analyse--regression--linear，打开线性回归对话框

{% asset_img 83025aafa40f4bfb6bdac990034f78f0f63618ef.jpg spss中如何检验残差的相互独立性 %}

- 在对话框中，将因变量和自变量放入各自的框中，如图所示上面的是因变量，注意因变量和自变量都是连续性变量，点击statistic按钮，设置输出的参数

{% asset_img 29381f30e924b89913a02efc6e061d950b7bf652.jpg spss中如何检验残差的相互独立性 %}

{% asset_img 7aec54e736d12f2e9993f9a44fc2d5628435685b.jpg spss中如何检验残差的相互独立性 %}

- 勾选独立性检验的参数DW，如图所示，然后点击continue按钮，返回到主菜单

{% asset_img 2934349b033b5bb53d44773a36d3d539b700bc67.jpg spss中如何检验残差的相互独立性 %}

- 点击ok开始输出数据，在下面第二幅图的表格中显示了DW值，如图所示，

- –当DW值愈接近2时，残差项间愈无相关

- –当DW值愈接近0时，残差项间正相关愈强

{% asset_img 9a504fc2d5628535c06e85e590ef76c6a6ef6363.jpg spss中如何检验残差的相互独立性 %}

{% asset_img 4d086e061d950a7bbd9419000ad162d9f3d3c955.jpg spss中如何检验残差的相互独立性 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
