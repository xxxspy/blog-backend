---
title: SPSS自动化：[4]
date: 2015-08-11 18:17:15
tags: [spss]
author: mlln.cn
---
syntax是spss中的命令，在spss有syntax文档对象，这个对象有哪些属性呢？

- 1>designated属性：为当前输出文档、语法文档或草稿文档返回或设置指定的窗口状态。指定的窗口（designatedwindow）是spss传送输出、粘贴或运行语法命令的窗口。当一个新的输出窗口打开以后它就成为了指定窗口。

- 用法：

- Intcount=objdocuments.outputdoccount

- Set objoutputdoc=objdocuments.getoutputdoc(intcount-1)

- Objoutputdoc.designated=true

- '本实例将最后一个输出文档设置成指定文档接收新的输出。

- 2>height和width属性、left和top属性、modified属性在前面其他对象中有介绍，这里省略。

- 3>papersource属性：设置打印时候纸张的来源，它有四个值：

- 1    Upper

- 2    Lower

- 3    Middle

- 4    envelop

- 用法：

- Setobjprintoptions=objoutputdoc.printoptions

- '设置打印选项

- Printoptions.papersource-2

- 4>rtftext属性：返回或设置语法窗口中的格式化文本，或rich文本框中的rtf文本编辑器。

- 用法：

- String=objsyntaxdoc.text

- Objsyntaxdoc.rtftext=string

- Objsyntaxdoc.run

- 5>text属性：在语法窗口或者激活的rtf文本编辑器中返回或设置文本，可以使用该属性写成或接收未格式化的文本。

- 用法：

- Dim syntaxcommands as string

- Syntaxcommands=objdatadoc.invokedialogandreturnsyntax("analyze>compare means>paired-samples t test",1)

- '获取了syntax命令

- Dim objsyntaxdoc as ispsssyntaxdoc

- Set objsyntaxdoc=objspssapp.newsyntaxdoc

- Objsyntaxdoc.text=syntaxcommands

- 6>toolbarvisible属性、visible属性、windowstate属性略去。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
