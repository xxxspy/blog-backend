---
title: DataNitro：[5]Cell对象方法
date: 2016-01-01 18:05:17
tags: [datanitro]
author: mlln.cn
---
这篇文章介绍一下Datanitro常用的一些方法。我们还是用例子来说明，大家比较容易理解，另外想要学习一门计算机语言，一定要亲手实验你的代码，否则学起来很慢。

- clear()：清空Cell，例如：

- #clear()

- Cell(1,1).clear()

- copy_from():复制单元格：下面的代码将A21单元格的内容和格式复制到了A22

{% asset_img 389aa8fd5266d01634b4d47a942bd40734fa35f7.jpg DataNitro：[5]Cell对象方法 %}

- copy_format_from()：仅仅复制单元格格式

{% asset_img 99636c0e0cf3d7cada757524f11fbe096a63a9a6.jpg DataNitro：[5]Cell对象方法 %}

- is_empty():判断单元格是否为空，如果为空则返回True，否则返回False

{% asset_img 3b6833f5e0fe9925443edc0237a85edf8db17177.jpg DataNitro：[5]Cell对象方法 %}

- offset()：移动：下面的代码将返回A1单元格右边的单元格A2

{% asset_img 6648d73d70cf3bc7801478bed200baa1cd112a08.jpg DataNitro：[5]Cell对象方法 %}

- print,这不是cell的方法，但是使用print可以返回cell的名字，注意Cell的参数，有一个sheet1，它明确的指明了是在sheet1中的单元格A1

{% asset_img dc15484e9258d109b7ce1ce0d258ccbf6c814d77.jpg DataNitro：[5]Cell对象方法 %}

- rename()我们还可以给单元格起一个个性化名字，然后使用改名字就可以调用该单元格

{% asset_img b29f8282d158ccbf649100681ad8bc3eb1354177.jpg DataNitro：[5]Cell对象方法 %}

- active_cell():返回当前活动单元格，如果你输入一个参数，比如：active_cell(Cell('A1'))，就可以设定A1为活动单元格

{% asset_img d7c9ca3f8794a4c24d3752790df41bd5ad6e3908.jpg DataNitro：[5]Cell对象方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
