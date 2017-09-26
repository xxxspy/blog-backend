---
title: DataNitro：[8]workbook对象
date: 2015-09-17 18:23:05
tags: [datanitro]
author: mlln.cn
---
想一想，datanitro的内容还是挺少挺简单的，现在就讲到了workbook了，也就快讲完了。workbook对象也就是工作簿，也就是一个excel文件（擦！说的太直白了）。有些工作需要生成大量的工作簿，所以会用到它，下面来看看它有哪些可以用的属性和方法。

- save：保存工作簿，参数的可选的：

{% asset_img 8605f5f81a4c510f995d3b496359252dd52aa58d.jpg DataNitro：[8]workbook对象 %}

- save_copy：保存副本，参数也是可选的。通常我们要用这个方法来备份一下工作进程。

{% asset_img d7c9ca3f8794a4c2b9593e780df41bd5ad6e3928.jpg DataNitro：[8]workbook对象 %}

- recalc_wkbk/recalc_mode：重新计算工作簿，适合有公式需要刷新的时候。你还可以通过recalc_mode来设置公式是自动计算还是手动计算。

{% asset_img 1a94b36eddc451da4a8cd5b8b5fd5266d0163228.jpg DataNitro：[8]workbook对象 %}

- pivot_refresh：数据透视表的刷新。如果原始数据修改了，数据透视表需要刷新一下才能显示正确的结果。

{% asset_img e8112b2ac65c103807e71791b1119313b17e898d.jpg DataNitro：[8]workbook对象 %}

- active_wkbk:如果打开了多个工作簿，你可能要设定某个工作簿为激活状态，就用到了它。

{% asset_img 11794d43fbf2b211c4b75c1dc98065380dd78e8d.jpg DataNitro：[8]workbook对象 %}

- open_wkbk/close_wkbk：打开工作簿

{% asset_img 9252ae7eca80653857737d4094dda144ac34828d.jpg DataNitro：[8]workbook对象 %}

- new_wkbk：新建工作簿

{% asset_img 0d968f2397dda144f290b5e1b1b7d0a20df4868d.jpg DataNitro：[8]workbook对象 %}

- all_wkbk返回打开的所有工作簿：

{% asset_img 0b14ad19ebc4b745b3ee6e45ccfc1e178a821528.jpg DataNitro：[8]workbook对象 %}

- copy_sheet：复制工作表到特定的工作簿。

{% asset_img 0db52fadcbef76092c9240cc2ddda3cc7dd99e8d.jpg DataNitro：[8]workbook对象 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
