---
title: spss中如何利用直方图看出残差的正态性
date: 2016-03-17 18:15:17
tags: [spss]
author: mlln.cn
---
直方图是粗略检验正态性的一个好方法，通过对数据的大概形态的了解我们可以粗略的看出数据是正太还是偏态，好吧，下面是具体的方法：
工具/原料


- spss20.0
方法/步骤


- 先打开线性回归的对话框，如图所示，打开linear菜单

{% asset_img f11f3a292df5e0feaabed9c55c6034a85fdf724b.jpg spss中如何利用直方图看出残差的正态性 %}

- 将GDP作为因变量，将其他变量作为自变量，放入各自的框中，点击plot按钮，设置输出的图标

{% asset_img eac4b74543a9822655637be38a82b9014b90eb50.jpg spss中如何利用直方图看出残差的正态性 %}

{% asset_img faf2b2119313b07eca8803cc0cd7912397dd8c38.jpg spss中如何利用直方图看出残差的正态性 %}

- 在该对话框中，注意XY轴分别是什么变量，这里X轴是标准化的残差，而Y轴是概率，设置输出的图为直方图，如图所示，然后点击continue按钮

{% asset_img 8ad4b31c8701a18b282b428b9e2f07082938fe36.jpg spss中如何利用直方图看出残差的正态性 %}

- 点击ok按钮，开始处理数据并输出结果

{% asset_img 91529822720e0cf30d8b1d3f0a46f21fbf09aaf2.jpg spss中如何利用直方图看出残差的正态性 %}

- 在结果界面，找到直方图，如果直方图的形态符合正太分布，我们就可以大体上认为数据的残差是符合正太分布的。

{% asset_img 91ef76c6a7efce1bbad19b0eaf51f3deb58f657f.jpg spss中如何利用直方图看出残差的正态性 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
