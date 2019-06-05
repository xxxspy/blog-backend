---
title: spss 2因素嵌套设计数据处理方法
date: 2015-06-01 18:11:15
tags: [spss]
author: mlln.cn
---
所谓的嵌套设计，指的是至少一个因素的水平是分配在另一个因素的水平中的。如果B因素的每个水平仅出现在A因素的一个水平中，B就是嵌套于A的，可写作B（A）。 注意这个写作方式，下面我们详细的讲解如何操作：
工具/原料


- spss20.0
方法/步骤


- 将数据整理成如图所示的样式，这样才可以做嵌套设计，从图中你可以看出来，变量B嵌套于变量A

{% asset_img 0df431adcbef7609a0b3255c2edda3cc7dd99ebd.jpg spss 2因素嵌套设计数据处理方法 %}

- 接着在菜单栏上执行：analyse--GLM---univariate，打开方差分析的对话框

{% asset_img cefc1e178a82b90130207ff0738da9773812ef60.jpg spss 2因素嵌套设计数据处理方法 %}

- 这里很简单，就是将自变量和因变量放入格子的框框，然后点击model来定义模型

{% asset_img d53f8794a4c27d1e9bed87071bd5ad6edcc4382d.jpg spss 2因素嵌套设计数据处理方法 %}

{% asset_img 6c224f4a20a44623bb0919a19822720e0df3d736.jpg spss 2因素嵌套设计数据处理方法 %}

- 勾选“custom”，然后设置type为main effect

{% asset_img d043ad4bd11373f0e601d05ca40f4bfbfbed0432.jpg spss 2因素嵌套设计数据处理方法 %}

- 将两个变量放入模型框中，然后点击continue按钮

{% asset_img 8435e5dde71190ef76e12d1cce1b9d16fcfa60de.jpg spss 2因素嵌套设计数据处理方法 %}

- 回到主菜单以后，我们点击paste按钮，开始编辑syntax

{% asset_img 37d12f2eb9389b50b5e95f918535e5dde6116edb.jpg spss 2因素嵌套设计数据处理方法 %}

- 我们看下面的图，第一幅图是编辑前的design，第二幅图是编辑后的，其实就是增加了一个（a），b（a）就是b嵌套于a的意思

{% asset_img b21bb051f8198618b45550474aed2e738ad4e6e7.jpg spss 2因素嵌套设计数据处理方法 %}

{% asset_img 6609c93d70cf3bc7a908722fd100baa1cc112aec.jpg spss 2因素嵌套设计数据处理方法 %}

- 点击运行按钮，你就会看到运行的结果，我们看输出的表格显示了ab变量的主效应是显著的。

{% asset_img 3c6d55fbb2fb4316c05dc5b920a4462308f7d3b7.jpg spss 2因素嵌套设计数据处理方法 %}

{% asset_img 730e0cf3d7ca7bcbb23978ecbe096b63f724a8b7.jpg spss 2因素嵌套设计数据处理方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
