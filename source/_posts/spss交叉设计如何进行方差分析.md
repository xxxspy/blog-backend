---
title: spss交叉设计如何进行方差分析
date: 2015-01-05 18:23:15
tags: [spss]
author: mlln.cn
---
交叉设计是自身配对基础上发展的设计方法，是一种特殊的自身对照设计，通常的设计方案为被试分为两组，一组接受实验的顺序是AB，一组接受的实验顺序是BA，这样就形成了对照，这样的设计如何进行方差分析呢？下面是具体的方法：
工具/原料


- spss20.0
方法/步骤


- 首先要明白数据的录入方式，如图所示，stage就是接受条件AB的阶段

{% asset_img f603918fa0ec08faab3c106659ee3d6d55fbda37.jpg spss交叉设计如何进行方差分析 %}

- 在菜单栏上执行：analyse--GLM--univariate，打开方差分析对话框

{% asset_img b8014a90f603738d79ee0fe3b31bb051f919ec4f.jpg spss交叉设计如何进行方差分析 %}

- 将自变量和因变量放入格子的框中，点击model按钮，开始设置模型

{% asset_img e1fe9925bc315c605105682e8db1cb134854775a.jpg spss交叉设计如何进行方差分析 %}

{% asset_img 024f78f0f736afc3b8283da4b319ebc4b64512ce.jpg spss交叉设计如何进行方差分析 %}

- 勾选“custom”，然后将三个变量放入右侧的模型框中

{% asset_img 03087bf40ad162d91cef60dd11dfa9ec8b13cdea.jpg spss交叉设计如何进行方差分析 %}

{% asset_img 63d0f703918fa0ecf0c666cc269759ee3c6ddbea.jpg spss交叉设计如何进行方差分析 %}

- 将type设置为maineffect，意思是没有交互作用，回到主菜单，点击ok

{% asset_img 80cb39dbb6fd526675313ed5ab18972bd50736dc.jpg spss交叉设计如何进行方差分析 %}

{% asset_img 34fae6cd7b899e51a19438d542a7d933c9950ddc.jpg spss交叉设计如何进行方差分析 %}

- 我们看到输出的结果，治疗方案treat边缘显著，但是质量的顺序stage是不显著的，判断标准就是sig值

{% asset_img 7dd98d1001e9390164138fff7bec54e737d196d9.jpg spss交叉设计如何进行方差分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
