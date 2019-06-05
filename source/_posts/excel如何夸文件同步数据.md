---
title: excel如何夸文件同步数据
date: 2015-10-23 18:23:17
tags: [excel]
author: mlln.cn
---
在一个excel的单元格里如何显示另一个excel文件单元格里的数据我们可以使用文件引用，很简单，下面是具体的过程：

- 我们看到我现在有几个excel文件，现在想要在A.xlsx中显示B1.xlsx中的数据，打开A.xlsx

{% asset_img 3b6833f5e0fe99250d3e9b2837a85edf8db1715d.jpg excel如何夸文件同步数据 %}

- 随便找一个单元格输入公式：='F:\数据分析存档\excel\[b1.xlsx]Sheet1'!A1 

- 这个公式的意思是：文件的路径+[文件名称]+工作表名！单元格地址

{% asset_img 9864a2315c6034a8ead04af9c81349540923765d.jpg excel如何夸文件同步数据 %}

{% asset_img d1e312f431adcbeffac58d7eafaf2edda2cc9f92.jpg excel如何夸文件同步数据 %}

- 这样在这个单元格里已经显示了另一个excel的内容，下面我们增加一个功能

{% asset_img d1e312f431adcbeffac58d7eafaf2edda2cc9f92.jpg excel如何夸文件同步数据 %}

- 增加一个超链接，点击超链接就可以打开所引用的文件，右键单击单元格，选择【超链接】

{% asset_img 570f8c58d109b3de228d1610cfbf6c81800a4c5d.jpg excel如何夸文件同步数据 %}

- 在打开的对话框中选择你所引用的文件夹，点击确定即可

{% asset_img 00a82701213fb80eec2092af35d12f2eb8389492.jpg excel如何夸文件同步数据 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
