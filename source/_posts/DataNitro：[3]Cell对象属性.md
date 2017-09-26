---
title: DataNitro：[3]Cell对象属性
date: 2016-05-19 18:03:01
tags: [datanitro]
author: mlln.cn
---
datanitro的Cell对象也就是单元格对象，我们今天学习一下Cell对象所具有的一些属性：

- name:我现在打开datanitro的Shell，下面的截图欧式在shell中的。创建一个Cell对象很简单，就是输入Cell的两个参数，也就是它的地址就可以创建该对象，如果我们直接print该对象，就会输出它的name属性

- 我们还可以将Cell的地址写成字符串形式：‘A1’

{% asset_img 7787b9efce1b9d160e23d533f0deb48f8d5464b9.jpg DataNitro：[3]Cell对象属性 %}

{% asset_img b5ce925494eef01fc0f05797e3fe9925bd317db9.jpg DataNitro：[3]Cell对象属性 %}

- value:Cell的值，它可以自动识别Cell的数据类型，如果是日期，就会返回date数据

{% asset_img 79b1e936afc3793154c5c97be8c4b74542a911f7.jpg DataNitro：[3]Cell对象属性 %}

{% asset_img 78701455b319ebc4d6d539cb8126cffc1f1716f7.jpg DataNitro：[3]Cell对象属性 %}

- vertical/horizontal：他们用于批量赋值，或者获取多个Cell组成的range对象。我们将一个列表赋值给Cell.vertical，就会在该cell的下方依次将列表中的元素赋值给多个单元格
例如Cell('E1').vertical=[2,2,2,2,1]的效果是：
print Cell('E1').vertical会输出单元格E1以下非空单元格的值

{% asset_img 9252ae7eca806538c074ea4194dda144ac348283.jpg DataNitro：[3]Cell对象属性 %}

{% asset_img 5d212aa85edf8db1c8c933360a23dd54574e74b9.jpg DataNitro：[3]Cell对象属性 %}

- cellrange:代码多个单元格构成的区域：CellRange('B1:B5').value=[1,2,3,4,5]可以给这个区域赋值

- Table：它代表一个二维表，Cell('A10').table代表以A10为左上角，以向右第一个不为空的单元格为有边界，以向下第一个不为空的单元格为下边界的矩形区域。

{% asset_img d56b3634349b033be351b58816ce36d3d439bd4c.jpg DataNitro：[3]Cell对象属性 %}

- formula：我们还可以直接向单元格输入公式

{% asset_img d872d695d143ad4b9f650e9281025aafa50f06dd.jpg DataNitro：[3]Cell对象属性 %}

- comment：Cell('A17').comment=u'这是注释'，它的效果如下：

{% asset_img 54baacfb43166d22d5c25dc6452309f79152d2e8.jpg DataNitro：[3]Cell对象属性 %}

- hyperlink（超链接）：Cell('A18').hyperlink='http://baidu.com'，效果如下：

{% asset_img b3ba5d166d224f4abb5a3b410af790529922d166.jpg DataNitro：[3]Cell对象属性 %}

- color：单元格颜色：例如：Cell('A20').color='red' #还可以用black, white, red, blue, green, yellow, purple, gray, silver, maroon, olive, lime, teal, aqua, navy, and fuchsia等颜色词

- font：字体：例如：

- #font

- Cell('A21').value=u'字体'

- Cell('A21').font.size=9

- Cell('A21').font.color='blue'

- 以下属性可以使用True or False

- Cell('A21').font.bold=True #粗体

- Cell('A21').font.italic=True #斜体

- #Cell('A21').underline=True #下划线

- #Cell('A21').strikethrough=True

- #Cell('A21').subscript=True

- #Cell('A21').superscript=True

- 最后也是最重要的一个属性：df，它可以让我们将pandas的DataFrame对象直接输入到excel，例如：

- #df

- import pandas as pd

- df=pd.DataFrame([[1,2,3],[4,5,6]])

- Cell('A19').df=df

- 下一篇介绍一下datanitro的一些方法

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
