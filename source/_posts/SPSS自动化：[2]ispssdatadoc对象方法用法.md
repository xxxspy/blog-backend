---
title: SPSS自动化：[2]ispssdatadoc对象方法用法
date: 2016-06-01 18:01:05
tags: [spss]
author: mlln.cn
---
   ispssdatadoc对象从属于document对象，其方法有很多，今天我们来一一介绍，包括他的功能和用法，可能有不太详尽的地方，大家多提意见，欢迎有志于spss自动化的网友交流。

- 1>clear方法：清除数据。

- 使用方法：objdatadoc.selectcells（"a","b",19,29)

- Objdatadoc.clear

- 2>copy方法：复制数据。

- 使用方法：

- objdatadoc.copy

- 3>cut方法：

- 剪贴对象到剪贴板。使用方法：

- objoutputdoc.selectalltables

- Objoutputdoc.cut

- 4>delete方法：删除选定的数据。

- 使用方法：

- objoutputdoc.selectlastutput

- Objoutputdoc.remove

- 5>deletemenuitem方法：删除菜单项

- 使用方法：

- Objdatadoc.deletemenuitem("edit")

- 6>deletemenuitemfromall方法：从所有数据窗中中删除菜单项，用法同上。

- 7>getbannertext方法：获取标题文本

- 使用方法：

- Banner=objoutputdoc.getbannertext

- 8>getdocumentpath方法：获取文档路径

- 使用方法：

- Path=objoutputdoc.getdocumentpath

- 9>getfiltervariable方法：获取变量名或者带有标签的变量名

- 使用方法：

- Objdatadoc.getfiltervariable(false)   'false表示只获得变量名不要标签

- 10>getnumberofcases方法：获取case数量

- 使用方法：

- Num=objdatadoc.getnumberofcases

- 11>gettextdata方法：获取范围内文本格式的数据

- 使用方法：

- array=objdatadoc.gettextdata("a列","b列",12,14)

- 12>getvariables方法：返回一个一维变量数组，可以选择接收变量还变量标签。功能是获得变量名或者带标签的变量名。

- 使用方法：

- Variablelist=objdatadoc.getvariables(boolean)           'boolean取1为获取变量名和标签，取0为仅获取变量名

- 13>getweightingvariable方法：获取加权变量。

- 使用方法：string=objdatadoc.getweightingvariable(boolean)          'boolean是1则返回变量名和标签

- 14>invokedialogandexcutesyntax方法：激活一个对话框并运行命令。

- 使用方法：

- Objdatadoc.invokedialogandexecutesyntax(strpath,spsswindoparent,true)     'strpath是菜单路径，例如"analyze>survival>lifetables"；spsswindoparent是父对话框，可取1或者0；true指的是同步，也就是运行命令以后立刻获得控制权。

- 15>invokedialogandreturnsyntax方法：返回一个syntax命令。

- 使用方法：

- String=objdatadoc.invokedialogandreturnssyntax(strpath,spsswindoparent)

- 16>paste方法：粘贴

- 使用方法：

- Objdatadoc.selectcells('a列','b列',20,23)    '选择区域粘贴

- Objdatadoc.paste

- 17>printdoc方法：打印

- 使用方法：

- Objdatadoc.printdoc     '使用ispssprintoptions和printrange确定打印内容和方法。

- 18>saveas方法：另存为

- 使用方法：objdatadoc.saveas("d:\fuck.sav")

- 19>selectcases方法：选择case

- 使用方法：objdatadoc.selectcases(1,100)     '选择1到100的case

- 20>selectcells方法：选择单元格

- 使用方法：

- Objdatadoc.selectcells('a列','b列',1,100)

- 21>selectvariables方法：选择一定范围内的变量

- 使用方法：

- Objdatadoc.selectvariables('a列','b列')

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
