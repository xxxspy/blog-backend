---
title: spss做因素分析的时候如何输出因素值并形成变量
date: 2015-09-01 18:03:19
tags: [spss]
author: mlln.cn
---
假如因素分析的时候我们会用到因素的值，比如根据因素的值进行排序，那么我们就需要用到save as variables过程。下面我们就要介绍一下如何使用这个过程。
工具/原料


- spss 20.0
方法/步骤


- 准备好spss中的数据，然后在菜单栏上执行：analyse--dimension reduction--factor

{% asset_img b03533fa828ba61e01a6f5f84134970a314e5998.jpg spss做因素分析的时候如何输出因素值并形成变量 %}

- 将用于因素分析的变量放入variables框中

{% asset_img e824b899a9014c08787915720a7b02087af4f4a2.jpg spss做因素分析的时候如何输出因素值并形成变量 %}

- 点击scores按钮，设置要输出的变量

{% asset_img a686c9177f3e67097c9f78283bc79f3df9dc554d.jpg spss做因素分析的时候如何输出因素值并形成变量 %}

- 打开score对话框，勾选save as variables，就是这个选项用于输出因素分数，点击continue按钮

{% asset_img cf1b9d16fdfaaf517b28bc688c5494eef11f7a19.jpg spss做因素分析的时候如何输出因素值并形成变量 %}

- 点击ok开始输出数据，并在变量视图输出三个新的变量

{% asset_img 0ff41bd5ad6eddc49fda882c39dbb6fd52663323.jpg spss做因素分析的时候如何输出因素值并形成变量 %}

- 如图所示，你会看到三个多出来的变量

{% asset_img 6159252dd42a28347e930adc5bb5c9ea15cebf2b.jpg spss做因素分析的时候如何输出因素值并形成变量 %}

- 通常我们要根据因素的值来对case进行排序，方法是选中一个因素的所有值，然后右键单击，选择sort descending，你会看到数据从大到小的排序

{% asset_img 5ab5c9ea15ce36d38535bfe73af33a87e950b137.jpg spss做因素分析的时候如何输出因素值并形成变量 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
