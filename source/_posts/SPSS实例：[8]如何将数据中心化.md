---
title: SPSS实例：[8]如何将数据中心化
date: 2016-06-15 18:05:19
tags: [spss]
author: mlln.cn
---
将数据进行中心化和标准化不同，中心化就是将原始数据减去平均数，而标准化是将原始数据减去平均数然后再除以标准差，得到的数据是以0为平均数以1为标准差的数据，数据中心化的目的是将不同的变量的数据的尺度统一化，有的人在使用amos的时候先进行中心化，单其实没有必要，因为amos自己会做这个工作的，你只是重复劳动，好了，废话不多说，我们开始操作。

- 打开数据，在菜单中执行：analyse--descriptive statistics--descriptives

{% asset_img d57e9994a4c27d1eaf793bec19d5ad6eddc4387f.jpg SPSS实例：[8]如何将数据中心化 %}

- 打开一个对话框，在这里找到你要正太化的变量，比如我们用age这个变量，点击添加按钮

{% asset_img fd428c45d688d43ffdef91da7f1ed21b0ef43b10.jpg SPSS实例：[8]如何将数据中心化 %}

- 记得勾选保存项，如图所示

{% asset_img 9304c888d43f8794dfb94806d01b0ef41bd53a10.jpg SPSS实例：[8]如何将数据中心化 %}

- 点击ok按钮，开始运行

{% asset_img 7c5fcc1b0ef41bd52d0ce8dc53da81cb39db3d7f.jpg SPSS实例：[8]如何将数据中心化 %}

- 运行结果需要你看变量视图，你会看到多了一个变量zage，实际上是在原变量名的前面增加了一个Z

{% asset_img d35a10f41bd5ad6e5ca664c283cb39dbb6fd3c7f.jpg SPSS实例：[8]如何将数据中心化 %}

{% asset_img 7c5fcc1b0ef41bd52d15e8dc53da81cb39db3d10.jpg SPSS实例：[8]如何将数据中心化 %}

- 我们看到，新增加的这列变量是以0为中心，1为标准差的

{% asset_img dc854fda81cb39db339f677ed2160924ab18307f.jpg SPSS实例：[8]如何将数据中心化 %}

- 如果使用sytax，我们需要输入如下的命令，然后运行即可。

{% asset_img 1a94b36eddc451da02b00cc3b4fd5266d0163210.jpg SPSS实例：[8]如何将数据中心化 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
