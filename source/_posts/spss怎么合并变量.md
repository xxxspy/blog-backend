---
title: spss怎么合并变量
date: 2015-05-11 18:11:03
tags: [spss]
author: mlln.cn
---
合并变量是合并数据的一种方法，比如我今天给被试测量几个变量，过几天再测了几个变量，这些数据合并在一起就是合并变量，这不是将case合并，这是关键，下面我来演示一下这个过程。
方法/步骤


- 打开spss以后，先要打开第一个要合并的数据，然后合并变量如图所示，在菜单栏上执行：data--merge file--addvariable

{% asset_img 8ad4b31c8701a18bcec8ecc29e2f07082838fe18.jpg spss怎么合并变量 %}

- 打开合并变量对话框，点击浏览选项，找到要合并的第二个文件

{% asset_img a08b87d6277f9e2f4b16e3851f30e924b899f318.jpg spss怎么合并变量 %}

- 找到要合并的第二个文件，然后点击open

{% asset_img d8f9d72a6059252d5212e389349b033b5bb5b932.jpg spss怎么合并变量 %}

- 回到合并变量对话框，点击continue按钮，进行下一步设置

{% asset_img 9f2f070828381f30a63a7324a9014c086e06f018.jpg spss怎么合并变量 %}

- 在这里，我们先看到右边的列表指的是合并变量以后的数据，左侧的列表显示的是被排除的变量，这些变量之所以被排除是因为两个数据表出现了相同的变量。

{% asset_img 1e30e924b899a9011e16a5bb1d950a7b0208f518.jpg spss怎么合并变量 %}

- 要想合并变量必须制定关键变量，也就是key variables，因为我们的关键变量是id，这个id在new active dataset中，先选中id，然后点击如图所示的按钮，让id变为排除变量

{% asset_img a8014c086e061d955f65c9b57bf40ad162d9ca18.jpg spss怎么合并变量 %}

- 接着在排除变量中，选中id，点击如图所示的按钮，将其添加到关键变量中

{% asset_img 1c950a7b02087bf452cfa964f2d3572c11dfcf18.jpg spss怎么合并变量 %}

- 点击ok按钮，开始合并变量，一般会弹出警告框，点击ok即可。

-  

{% asset_img 3bf33a87e950352a5264db855343fbf2b2118b32.jpg spss怎么合并变量 %}

{% asset_img 63d9f2d3572c11dff4f241ae632762d0f703c218.jpg spss怎么合并变量 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
