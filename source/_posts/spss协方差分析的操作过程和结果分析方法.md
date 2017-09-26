---
title: spss协方差分析的操作过程和结果分析方法
date: 2015-04-11 18:23:01
tags: [spss]
author: mlln.cn
---
 协方差分析就是当研究中出现一个变量不是我们想要研究的变量，但是却会影响到我们的研究结果，我们不得不对其进行控制，这时候就可以用协方差分析的方法来控制，协方差分析一个最重要的假设是斜率同质假设，下面就要先检验斜率同质假设，然后才能进行协方差分析。
方法/步骤


- 协方差分析之前，要先检验一下数据是否满足斜率同质假设，也就是检验自变量和斜变量之间有木有交互作用，如图所示，在菜单栏上执行：analyze--general linear model--univariate

{% asset_img 9e3df8dcd100baa1d766d84c4710b912c9fc2efa.jpg spss协方差分析的操作过程和结果分析方法 %}

- 在打开的对话框中，将因变量、自变量、斜变量都放到各自的位置，如图所示，评定得分为因变量，培训方式为自变量，家庭指数为斜变量，点击options按钮，进入子对话框

{% asset_img b219ebc4b74543a9d684653b1e178a82b80114ad.jpg spss协方差分析的操作过程和结果分析方法 %}

{% asset_img d31b0ef41bd5ad6ef1fafb1d81cb39dbb7fd3cc1.jpg spss协方差分析的操作过程和结果分析方法 %}

- 在这里将培训方式，也就是自变量移动到display means for中，并且勾选描述统计和方差齐性检验，点击continue按钮继续

{% asset_img dcc451da81cb39db86c3f8a1d0160924aa1830c1.jpg spss协方差分析的操作过程和结果分析方法 %}

- 点击model按钮，选择模型

{% asset_img 4b90f603738da97764b019dcb051f8198718e3ae.jpg spss协方差分析的操作过程和结果分析方法 %}

- 刚打开这个对话框的时候，默认是full factorial模式，但是我们要检验交互作用，所以要选中custom

{% asset_img f703738da9773912edb91a96f8198618377ae2ae.jpg spss协方差分析的操作过程和结果分析方法 %}

- 将培训方式和家庭指数都放到model里

{% asset_img 34fae6cd7b899e51348da5e342a7d933c9950dc1.jpg spss协方差分析的操作过程和结果分析方法 %}

- 同时选中培训方式和家庭指数，将type设置为interaction，点击添加按钮，添加到model中，点击continue按钮

{% asset_img 0b46f21fbe096b636ab9c1a70c338744eaf8aca1.jpg spss协方差分析的操作过程和结果分析方法 %}

{% asset_img 34fae6cd7b899e5134c4a5e342a7d933c9950dfa.jpg spss协方差分析的操作过程和结果分析方法 %}

- 点击ok按钮，开始处理数据

{% asset_img faedab64034f78f0bb08050479310a55b2191cc1.jpg spss协方差分析的操作过程和结果分析方法 %}

- 在出来的结果中，我们主要是看自变量和斜变量的交互作用，如图所示，sig值大于0.05，所以交互作用不显著，这就满足了斜率同质性假设

{% asset_img 8601a18b87d6277ff28dadcf28381f30e824fcae.jpg spss协方差分析的操作过程和结果分析方法 %}

- 接着我们来进行协方差分析，在菜单栏上执行：analyse--general linear model--univariate

{% asset_img 6159252dd42a28349d06a9fc5bb5c9ea14cebfa1.jpg spss协方差分析的操作过程和结果分析方法 %}

- 将各个变量都放到各自的位置，和上面的步骤一样，点击options按钮

{% asset_img 1f178a82b9014a90ac3dd94aa9773912b21beec2.jpg spss协方差分析的操作过程和结果分析方法 %}

- 将培训方式移动到display means for列表里，勾选描述统计、方差齐性、效应值，点击continue继续

{% asset_img 5ab5c9ea15ce36d37aa41cc73af33a87e850b1a1.jpg spss协方差分析的操作过程和结果分析方法 %}

- 点击model，选择模型

{% asset_img a8773912b31bb05198272cdf367adab44bede0c2.jpg spss协方差分析的操作过程和结果分析方法 %}

- 选择full factorial，点击continue

{% asset_img eac4b74543a982269a8bb4d08a82b9014b90ebfb.jpg spss协方差分析的操作过程和结果分析方法 %}

- 点击ok按钮，开始处理数据

{% asset_img 03087bf40ad162d98971fdeb11dfa9ec8b13cdae.jpg spss协方差分析的操作过程和结果分析方法 %}

- 最后看分析的结果培训方式的效应显著，这说明不同的培训方式会影响到学生最后的分数

-  

-  

{% asset_img 10dfa9ec8a1363271dc75bc4918fa0ec08fac71b.jpg spss协方差分析的操作过程和结果分析方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
