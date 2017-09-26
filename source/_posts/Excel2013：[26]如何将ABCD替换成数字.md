---
title: Excel2013：[26]如何将ABCD替换成数字
date: 2016-02-05 18:19:17
tags: [excel]
author: mlln.cn
---
经常给别人做数据分析，拿到的数据都是很不规范的，比如下面这个例子，单元格中的数据是ABCD而不是数字1234，这样的数据是无法放入到spss中进行处理的，所以我们需要对这个进行重新编码，在Excel中使用vba是比较快速的方法，这里我跟大家分享一下我的方法：

- 明确目标：把ABCD转换成1234，如图所示，题目1这一列是我转换完成的，题目3这一列是还没有进行转换的。

{% asset_img a8362712b31bb051727be651347adab44aede029.jpg Excel2013：[26]如何将ABCD替换成数字 %}

- 我们使用快捷键alt + F11，打开vbe编辑窗口

{% asset_img 8640bf8b87d6277f084d67412a381f30e924fc29.jpg Excel2013：[26]如何将ABCD替换成数字 %}

- 掺入一个模块：菜单上执行【插入】-【模块】

{% asset_img d1571724ab18972bb45255b3e4cd7b899e510a1b.jpg Excel2013：[26]如何将ABCD替换成数字 %}

- 将这段代码粘贴到模块中：

- Sub 替换abcd()

-     Dim iRng As Range

-     Set iRng = Selection

-     For Each icell In iRng

-         txt = icell.Value

-         Select Case txt

-         Case "A"

-             icell.Value = 1

-         Case "B"

-             icell.Value = 2

-         Case "C"

-             icell.Value = 3

-         Case "D"

-             icell.Value = 4

-         Case "E"

-             icell.Value = 5

-         End Select

-     Next icell

- End Sub

{% asset_img 0b3a1c087bf40ad1c6bb929a552c11dfa9ecce29.jpg Excel2013：[26]如何将ABCD替换成数字 %}

- 保存并关闭vbe窗口，然后按下快捷键alt+F8，打开宏编辑窗口，选中这个唯一的宏，然后点击【选项】按钮

{% asset_img f392492c11dfa9ec2371036e60d0f703918fc129.jpg Excel2013：[26]如何将ABCD替换成数字 %}

- 设置快捷键为Ctrl+q，然后点击确定按钮

{% asset_img 0b14ad19ebc4b7453efce26fcdfc1e178a82151b.jpg Excel2013：[26]如何将ABCD替换成数字 %}

- 下面开始使用这个宏来转化数据，如图，先选中要转换的这一列，然后按下快捷键【Ctrl+q】，你可以看到数据快速得到转换。abcd都变成了1234

{% asset_img 58af236d55fbb2fbf5740d6b4d4a20a44623dc29.jpg Excel2013：[26]如何将ABCD替换成数字 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
