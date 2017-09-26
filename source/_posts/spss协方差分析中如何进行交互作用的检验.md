---
title: spss协方差分析中如何进行交互作用的检验
date: 2016-03-17 18:01:05
tags: [spss]
author: mlln.cn
---
协方差分析前必须进行交互作用的检验，为的是满足协方差分析的平行性假设，存在交互作用就无法进行协方差分析了。下面是具体的过程：
工具/原料


- spss20.0
方法/步骤


- 打开数据，在菜单栏上点击analyse--GML--univariate，打开协方差的对话框

{% asset_img d31b0ef41bd5ad6e9d14c72981cb39dbb7fd3c07.jpg spss协方差分析中如何进行交互作用的检验 %}

- 在打开的这个对话框中，我们要将因变量、固定因素、斜变量放入各自的框中，点击model按钮，设置模型

{% asset_img e824b899a9014c08e9518a660a7b02087af4f48f.jpg spss协方差分析中如何进行交互作用的检验 %}

{% asset_img d439b6003af33a872fcea2d9c65c10385243b556.jpg spss协方差分析中如何进行交互作用的检验 %}

- 在这，需要将两个自变量和他们的交互项放入到模型框中，点击continue按钮

{% asset_img f636afc379310a55d0bc7c37b74543a98326105c.jpg spss协方差分析中如何进行交互作用的检验 %}

- 回到主对话框，点击ok按钮开始处理数据，等待几分钟才能出现图，因为绘图需要一些时间

{% asset_img 91529822720e0cf37e00ec380a46f21fbf09aa7a.jpg spss协方差分析中如何进行交互作用的检验 %}

- 我们看到这两个变量的交互作用并不显著，这说明协方差分析是可行的

{% asset_img 4ec2d5628535e5dd16df071c76c6a7efcf1b6206.jpg spss协方差分析中如何进行交互作用的检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
