---
title: DataNitro：[7]sheet操作(B)
date: 2016-06-01 18:19:15
tags: [datanitro]
author: mlln.cn
---
接着上一篇的sheet操作（A篇），下面讲不那么性感的B篇。

- clear_sheet：清空工作表，可以清空当前工作簿，也可以指定其他工作表

{% asset_img 9304c888d43f8794a4eed27dd11b0ef41bd53a14.jpg DataNitro：[7]sheet操作(B) %}

- all_sheets：可以返回所有非隐藏sheet，也可以返回包含隐藏的sheet

{% asset_img a992e31f4134970ad5088a7c96cad1c8a7865d2f.jpg DataNitro：[7]sheet操作(B) %}

- new_sheet：新建一个sheet，可以指定新建sheet的名称，也可以不指定，你是自由的

{% asset_img d35a10f41bd5ad6edbe8feb982cb39dbb6fd3c14.jpg DataNitro：[7]sheet操作(B) %}

- remove_sheet：删除sheet，可以删除当前活动sheet也可以选择其他sheet

{% asset_img 948bcfc8a786c9179478c86aca3d70cf3bc7572f.jpg DataNitro：[7]sheet操作(B) %}

- hide_sheet/is_hidden:用法基本也是一样的，你畜类旁通一下

{% asset_img 7e7f7909c93d70cfd481305efbdcd100baa12b2f.jpg DataNitro：[7]sheet操作(B) %}

- recalc_sheet：重新计算sheet，适用于工作表中有公式，需要更新的。

{% asset_img 509b9fcb39dbb6fd594a7f750a24ab18972b3714.jpg DataNitro：[7]sheet操作(B) %}

- rename_sheet:重命名，第一个参数表示被重命名的sheet，第二个参数表示新名称

{% asset_img 389aa8fd5266d0160408047b942bd40735fa3514.jpg DataNitro：[7]sheet操作(B) %}

- all_cells：返回所有非空单元格（CellRange）对象，你可以通过遍历的方式对这些单元格进行操作

{% asset_img aa59892bd40735faf4e1d4ea9d510fb30f240814.jpg DataNitro：[7]sheet操作(B) %}

- merge_cells/unmerge_cells：合并和拆分单元格。

{% asset_img 4651a712c8fcc3ce39bb53609145d688d43f202f.jpg DataNitro：[7]sheet操作(B) %}

- get_merged_range:返回合并单元格的范围

{% asset_img 43e6c733c895d143b6677e7070f082025aaf0714.jpg DataNitro：[7]sheet操作(B) %}

- last_cell_in_col/last_cell_in_row：返回某个列或者行中最后一个非空单元格，这个方法非常有用，经常用来判断一个sheet中的数据有多少行和多少列

{% asset_img 9304c888d43f8794a485d27dd11b0ef41bd53a2f.jpg DataNitro：[7]sheet操作(B) %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
