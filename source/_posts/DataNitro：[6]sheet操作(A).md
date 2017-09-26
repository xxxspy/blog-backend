---
title: DataNitro：[6]sheet操作(A)
date: 2016-09-19 18:19:05
tags: [datanitro]
author: mlln.cn
---
今天继续我们的datanitro，讲一讲对sheet的操作，sheet就是工作表（擦！你以为我们不知道啊！），因为内容比较多，我们分为A篇和B篇，看完A篇（A篇听起来很性感），觉得好看再看B篇。

- active_sheet：返回当前活动工作表（当前活动的也就是你正在操作的，鼠标点一下某个sheet就会激活这个sheet）。如果你不传入任何参数，他会返回活动sheet的名称，如果你传入一个sheet名称，就会激活该sheet：

{% asset_img d5462bfae6cd7b8986cda4d00c2442a7d8330e84.jpg DataNitro：[6]sheet操作(A) %}

- display_sheet：展示某个工作表：它的用法和上面一样，传不传参数，它的功能不同，其实datanitro的很多方法都是这样的，你畜类旁通一下，因为很多时候我是不会重复的说这个事情的。

{% asset_img d5462bfae6cd7b898914a3d00c2442a7d9330e2d.jpg DataNitro：[6]sheet操作(A) %}

- clear_row和clear_col：清空某行或者某列：他们可以使用整数、列表、Cell对象CellRange对象作为参数。当使用Cell或者CellRange的时候，他们清空的是这些单元格所在的行或者列

{% asset_img cdfe7281800a19d863fd1d5630fa828ba71e46ac.jpg DataNitro：[6]sheet操作(A) %}

- del_row/del_col用法也是同上，顾名思义，删除行或者列。

- hide_row/hide_col用法稍微不同，顾名思义，隐藏行或者列。可以传入整数、列表，还可以指定隐藏某个特定的工作表中的行。

{% asset_img d66b7e59252dd42aadde98f8003b5bb5c8eab84b.jpg DataNitro：[6]sheet操作(A) %}

- row_is_hidded/col_is_hidden：判断某行/列是否被隐藏，如果被隐藏，返回True，否则返回False。只能接受整数作为参数，而是否指定某个工作表是可选的，如果不指定，那么就指的是当前活动的工作表

{% asset_img 86d5bac27d1ed21b0824b7b6ae6eddc450da3fb0.jpg DataNitro：[6]sheet操作(A) %}

- insert_row/insert_col：这两个方法你应该亲手测试一下，传入不同的参数看看效果，它可以接受的参数有整数，Cell对象，列表；还可以指定某个工作表。

{% asset_img c8ab0bce36d3d5393bea96903987e950342ab04b.jpg DataNitro：[6]sheet操作(A) %}

- aotofit：设置自动列宽，它有两个可选参数：工作表和CellRange地址

{% asset_img c71d0e385343fbf224fb3f70b37eca8064388f4b.jpg DataNitro：[6]sheet操作(A) %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
