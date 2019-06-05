---
title: spss20.0如何进行反向计分
date: 2015-04-11 18:15:15
tags: [spss]
author: mlln.cn
---
 在心理学中经常使用反向计分的问卷，这种问卷获得数据在处理以前，要先进行重新编码。重新编码的目的就是要将反向计分的数据转换成正向计分，下面图是我分享的一个案例，他可以帮助你更好的理解什么是反向计分。
方法/步骤


- 我们导入要转换的数据，在菜单栏上执行transform--recode into same variables，这个操作的意思你懂啦，就是将原有的数据转换，但是并不生成新的变量，而是替换掉原有的变量

{% asset_img f11f3a292df5e0feb7b4d6845c6034a85fdf7282.jpg spss20.0如何进行反向计分 %}

- 打开了如图所示的对话框，我们将要转换的变量选中，然后点击添加按钮

{% asset_img 5243fbf2b21193134b03a03565380cd790238df7.jpg spss20.0如何进行反向计分 %}

- 接着要设置转换的方法 ，点击old and new values

{% asset_img b3119313b07eca8098456662912397dda04483f7.jpg spss20.0如何进行反向计分 %}

- 打开如图所示的对话框，我们在value这里填写1，在new value这里写5，意思是将1分转换为5分，然后点击add按钮

{% asset_img b17eca8065380cd76e5efd68a144ad34588281f7.jpg spss20.0如何进行反向计分 %}

- 同样的方法，我们将其他的数据转换方法都添加到这个列表里，然后点击继续按钮

{% asset_img d1a20cf431adcbef7f772183acaf2edda2cc9ff7.jpg spss20.0如何进行反向计分 %}

- 返回到了选择变量的对话框，点击ok按钮开始进行数据的转换。到此，反向计分就完成了。下面是介绍如何在反向计分的时候保留原始数据，生成新的变量。

{% asset_img b2de9c82d158ccbf5310eabf19d8bc3eb0354182.jpg spss20.0如何进行反向计分 %}

- 如何在反向计分的时候保留原始数据，生成新的变量，在导入数据以后，我们在菜单栏上执行：transform--recode into different variables

- 、

{% asset_img 0df431adcbef76094148c61a2edda3cc7dd99ef7.jpg spss20.0如何进行反向计分 %}

- 打开如图所示的对话框，我们选择要转换的数据，然后点击添加按钮

{% asset_img cdbf6c81800a19d8feafdb8033fa828ba71e4682.jpg spss20.0如何进行反向计分 %}

- 从中间的列表里选择一个变量，然后在右侧的name栏中输入新的变量的名字，然后点击change按钮

{% asset_img 2fdda3cc7cd98d10119753b4213fb80e7aec90f7.jpg spss20.0如何进行反向计分 %}

- 同样的方法给所有的变量重新命名以后，点击old and new values，添加转换数据的规则

{% asset_img 32fa828ba61ea8d3b58e2b81970a304e241f5882.jpg spss20.0如何进行反向计分 %}

- 和上面使用的方法一样的，我们左侧填写原始数据的值，有的填写转换成的值，然后点击add按钮

{% asset_img b90e7bec54e736d13850d38d9b504fc2d46269f7.jpg spss20.0如何进行反向计分 %}

- 将所有的转换规则都添加进去以后，我们点击continue按钮，好了数据转换完成。

{% asset_img 960a304e251f95ca9f59cd33c9177f3e66095282.jpg spss20.0如何进行反向计分 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
