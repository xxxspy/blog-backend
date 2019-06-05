---
title: SPSS二因素完全随机设计的简单效应检验方法
date: 2015-07-01 18:15:01
tags: [spss]
author: mlln.cn
---
spss在做简单效应的时候没有现成的菜单选项，需要你自己编写syntax，所以比较麻烦，在这个教程了，我交给大家一个办法，不用学太多的syntax就能自己做简单效应，下面是具体的方法：
工具/原料


- spss20.0
方法/步骤


- 在菜单栏上执行：analyse--GLM--univariate，打开方差分析对话框

{% asset_img 6a600c338744ebf8b74dcffdd9f9d72a6059a730.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

- 将自变量、因变量放入各自的框中，如图所示，B和Z是两个自变量，他们是完全随机设计，点击ok按钮，开始运行数据

{% asset_img a08b87d6277f9e2f7e17b6ca1f30e924b999f3d6.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

- 我们看到数据的处理效果，交互作用显著，所以我们需要进一步做简单效益的检验

{% asset_img 4d086e061d950a7b8140e5060ad162d9f3d3c9ff.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

- 如图所示，点击菜单栏上的按钮，打开刚才用过的univariate对话框

{% asset_img 4ec2d5628535e5dd0d5d0e1d76c6a7efcf1b62fb.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

{% asset_img 203fb80e7bec54e7d481b1dcb9389b504ec26a87.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

- 点击下面的paste按钮，来到syntax的编辑窗口

{% asset_img f3d3572c11dfa9ec016afdd562d0f703908fc1a8.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

- 在如图所示的位置，添加一个命令：/EMMEANS=TABLES(B*Z)COMPARE(B)ADJ(SIDAK)

- 其中：EMMEANSE是estimated marginal means subcommand的缩写，意思是估计边际平均数  

- ADJ是比较的方法，还可以用lsd ，bonferroni和sidak这三种方法。

- 单击运行按钮，开始处理数据并输出结果

{% asset_img 8694a4c27d1ed21b3fe6b927ad6eddc450da3fc0.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

- 我们看到，简单主效应的分析已经出来，通过这个表格我们就能对自变量B各个水平进行精细比较

{% asset_img 1ad5ad6eddc451dab7dd9b29b6fd5266d11632cc.jpg SPSS二因素完全随机设计的简单效应检验方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
