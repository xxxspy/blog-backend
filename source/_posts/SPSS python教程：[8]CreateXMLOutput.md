---
title: SPSS python教程：[8]CreateXMLOutput
date: 2016-01-15 18:03:23
tags: [python,spss]
author: mlln.cn
---
上一篇文章我们介绍了如何使用OMS（结果输出系统）来获取某个变量的平均数，今天我们接着这个话题，讲一讲上一篇文章中用到的spssaux.CreateXMLOutput。

- 通常，如果你想学习一个模块，你只要用help（）方法即可

{% asset_img 1cd4147b02087bf403379869f0d3572c10dfcf1c.jpg SPSS python教程：[8]CreateXMLOutput %}

- 我们看到CreateXMLOutput有四个参数，除了cmd，其他都是可选的，我们来介绍一下这几个参数

{% asset_img 0b907cd9f2d3572c1c39535c8813632763d0c31c.jpg SPSS python教程：[8]CreateXMLOutput %}

- cmd是syntax命令，比如下面计算平均数的一个syntax

{% asset_img fab3ac119313b07e81649e880ed7912396dd8c12.jpg SPSS python教程：[8]CreateXMLOutput %}

- omsid翻译为命令标识符：命令标识符可用于所有统计和绘图过程，以及在查看器的概要窗格中生成包含自己的可识别标题的输出区的任何其他命令。这些标识符通常（但不总是）与菜单上的过程名称和对话框标题相同或类似，这些名称和标题通常（但不总是）与基础命令名称相同。怎样查看一个输出表格的omsid呢，我们看一下截图：

{% asset_img a84052086e061d950e4efeb879f40ad163d9cae3.jpg SPSS python教程：[8]CreateXMLOutput %}

- subtype：表子类型是可以生成的枢轴表的不同类型。某些子类型仅由一个命令生成；其他子类型可由多个命令生成（尽管表看上去并不相同）。虽然表子类型名称通常是描述性的，但也可以选择其他名称（尤其是选择了大量命令时）；并且，两个子类型的名称可以非常类似。我们也可以查看一个表的子类型：

{% asset_img 2f9cbdcc7cd98d105f4bc5b1233fb80e7aec9050.jpg SPSS python教程：[8]CreateXMLOutput %}

- 最后是visible属性，也就是可见属性，默认情况下，我们是不能看到输出结果的，但是visible设置为1就可以在结果视图中看到输出结果。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
