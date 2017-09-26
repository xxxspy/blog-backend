---
title: SPSS实例：[24]卡方检验百分比是否相同
date: 2016-10-03 18:01:19
tags: [spss]
author: mlln.cn
---
今天我处理的数据是一个百分比数据（一看就知道是卡方检验啊！），一个题有三个选项，现在我想要知道被试选择这三个选项的概率是否相同？被试是不是偏爱选择某一个选项呢？这是一个很常见的检验百分比是否均等的问题，我们看看下面具体的教程吧。

- 首先，我们看看数据结构，先来看第二次选择的时候，有三个选项，被试是不是喜欢选择某一个或者某两个选项呢？用卡方来检验以下

{% asset_img 3b6833f5e0fe99258b361e3736a85edf8db1715b.jpg SPSS实例：[24]卡方检验百分比是否相同 %}

- 在菜单中依次打开：analyse-nonparametric texts-legacy dialogs-chisquare

{% asset_img b8405490f603738d0d707b45b11bb051f819ec64.jpg SPSS实例：[24]卡方检验百分比是否相同 %}

- 将要检验的变量放入testvariablelist，点击添加按钮

{% asset_img c9d4cf43ad4bd113f8e8c05558afa40f4bfb0574.jpg SPSS实例：[24]卡方检验百分比是否相同 %}

- 我们要检验的是这三个选项被选择的概率是否相同，虚无假设肯定就是三个选项概率相同，所以我们需要选择【all categories equal】

{% asset_img 6c63514a20a44623d0f0d2059a22720e0cf3d764.jpg SPSS实例：[24]卡方检验百分比是否相同 %}

- 如果你不需要其他的检验，你可以点击ok按钮，这时候你就会看到卡方检验的结果了

{% asset_img 30ecd5ef76094b36bfa76c8aa1cc7cd98d109d64.jpg SPSS实例：[24]卡方检验百分比是否相同 %}

- 先看第一个表格，第一列是观察到的数字，第二列是期望数字，也就是虚无假设

{% asset_img d56b3634349b033ba8ad8bbd17ce36d3d539bd75.jpg SPSS实例：[24]卡方检验百分比是否相同 %}

- 第二个表格就是卡方检验的结果，卡方值为32，概率是0，所以拒绝虚无假设。

{% asset_img 9c57e3faaf51f3de9b87ce0396eef01f3a297964.jpg SPSS实例：[24]卡方检验百分比是否相同 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
