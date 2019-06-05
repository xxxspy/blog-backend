---
title: spss如何分组进行运算并生成新的变量
date: 2015-09-17 18:15:17
tags: [spss]
author: mlln.cn
---
 spss中如果要给原始的分数加上相应的分数需要使用compute，我们看一个例子，下面是不同的班级的不同的分数，因为某些原因，我们要给1班的学生的分数加上三分，给二班的学生分数加上两分，这该怎么做呢？下面是具体的方法。
方法/步骤


-  拿到数据以后，我们在菜单栏上执行：transform--compute variables

{% asset_img 09fa513d269759ee4a1de947b2fb43166c22dfe9.jpg spss如何分组进行运算并生成新的变量 %}

- 打开一个对话框，我们在目标变量中输入新的变量的名称，我们这里输入新成绩

{% asset_img c75c10385343fbf215422fafb07eca8064388fd4.jpg spss如何分组进行运算并生成新的变量 %}

- 接着，因为不同的班级要加上不同的分数，所以我们需要添加条件，点击左下角的if按钮

{% asset_img a044ad345982b2b763f1b04831adcbef77099bd4.jpg spss如何分组进行运算并生成新的变量 %}

- 在这里，选择班级这个变量，添加到右侧的条件框中，记得要先勾选【include if case satisfies condition】。然后输入=1，也就是班级=1.最后点击continue按钮

{% asset_img 7acb0a46f21fbe09e2134a986b600c338644ade9.jpg spss如何分组进行运算并生成新的变量 %}

- 回到数据转换对话框，将成绩这个变量添加到右侧的公式中，输入+3，这样我们基本完成了一个任务，就是当班级为1的时候，成绩加上1就形成了新成绩。但是，当班级为2的时候怎么办呢？

{% asset_img adaf2edda3cc7cd93043bd553901213fb90e91d4.jpg spss如何分组进行运算并生成新的变量 %}

{% asset_img d8f9d72a6059252d415a9488349b033b5ab5b9e9.jpg spss如何分组进行运算并生成新的变量 %}

- 我们点击paste按钮，打开syntax窗口

{% asset_img e4dde71190ef76c668bc72a79d16fdfaae5167d4.jpg spss如何分组进行运算并生成新的变量 %}

- 这是我们看到的代码，模仿第二行的代码，我们写当班级为2的时候，新成绩等于成绩加上2.

{% asset_img 2cf5e0fe9925bc31823388145edf8db1ca1370d4.jpg spss如何分组进行运算并生成新的变量 %}

- 这是我们写好的代码。

{% asset_img b90e7bec54e736d1ea5e05849b504fc2d46269e9.jpg spss如何分组进行运算并生成新的变量 %}

- 在菜单栏上执行：run--all，运行命令

{% asset_img ca1349540923dd54b01d2ee4d109b3de9d8248d4.jpg spss如何分组进行运算并生成新的变量 %}

- 这是最后的结果，你看到了，这里生成了新的变量。

-  

-  

{% asset_img 8c1001e93901213f797ec75054e736d12e2e95e9.jpg spss如何分组进行运算并生成新的变量 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
