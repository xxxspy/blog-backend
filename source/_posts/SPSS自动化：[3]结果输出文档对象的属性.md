---
title: SPSS自动化：[3]结果输出文档对象的属性
date: 2016-01-15 18:01:11
tags: [spss]
author: mlln.cn
---

- 1>designated属性

- 2>height 和width属性

- 3>items属性

- 用法：

- Dim objoutputdoc as ispssoutputdoc

- Set objoutputdoc=objspssapp.getgesignatedoutputdoc           '声明变量并获取指定的输出文档。

- Dim objoutputitems as ispssitems

- Dim objoutputitem as ispssitem

- Set objoutputitems=objoutputdoc.items         '声明并获取项目对象

- Dim intcount as integer

- Dim strtype() as string

- Intcount=objoutputitems.count

- Redim strtype(intcount)

- For i=0 to count-1

- Objoutputitem=objoutputitems.getitem(i)

- Strtype(i)=objoutputitem.spsstype

- Next I

- 4>label属性：返回或者设置某个输出项的标签

- 用法：

- Dim objoutputdoc as ispssoutputdoc

- Set objoutputdoc=objspssapp.openoutputdoc("c:\out.spo")

- Dim objoutputitems as ispssitems

- Dim objoutputitem as ispssitem

- Set objoutputitems=objoutputdoc.items

- Dim intcount as integer

- Intcount=objoutputitems.count

- For i=0 to intcount-1

- Set objoutputitem=objoutputitems.getitem(i)

- If objoutputitem.label='notes' then

- Objoutputitem.selected=true

- Exit for

- End if

- Next i

- 5>left和top属性：设置输出文档对象的位置

- 7>outliningtoolbarvisible属性：在输出浏览器窗口中显示或者隐藏外观工具条。

- 用法：objoutputdoc.outliningtoolbarvisible=true

- 8>printoptions属性：返回打印选项对象。

- 用法：

- Setobjprintoptions=objoutputdoc.printoptions

- Objprintoptions.headertext="str"

- Objprintoptions.papersize=4

- Objprintoptions.papersource=1

- Objprintoptions.startingpagenumber=10  '从第十页开始打印

- Objoutputdoc.printdoc

- 8>splitterpositon属性：返回或者设置分割线的位置。

- 用法：

- objoutputdoc.splitterposition=objoutputdoc.width/2

- 9>standardtoolbarvisible属性：返回或者设置标准工具条的可见性。

- 用法：

- Objoutputdoc.standardtoolbarvisible=true

- 10>visible属性：可见性。

- 11>windowstate属性：窗口状态属性。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
