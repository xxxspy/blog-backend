---
title: 如何去掉excel保存文件时提示隐私问题警告
date: 2015-05-19 18:17:23
tags: [excel]
author: mlln.cn
---
这几天编辑Excel中的宏的时候,保存的时候总是提示"隐私问题警告:此文档中包含宏、active插件、XML扩展包信息或web组件,其中可能包含个人信息,并且这些信息不能通过“文档检测器”进行删除",这是为了保护用户的隐私才设置的一个安全警告,但是如果是我们经常使用vba,这个警告经常出现,很麻烦。那么怎么关闭警告呢?下面是具体的方法:

- 打开Excel软件,然后在左上角有一个开始按钮,点击开始按钮,打开开始菜单

{% asset_img 35e940df8db1cb131c9c221bdc54564e93584b85.jpg 如何去掉excel保存文件时提示隐私问题警告 %}

- 在开始菜单的右下角有一个Excel选项，打开Excel选项

{% asset_img 8cf0d513495409238af57d769358d109b2de49de.jpg 如何去掉excel保存文件时提示隐私问题警告 %}

- 打开了Excel选项，切换到信任中心，在信任中心找到【信任中心设置】按钮，打开它

{% asset_img 8c511fe93901213f8be850d455e736d12e2e959b.jpg 如何去掉excel保存文件时提示隐私问题警告 %}

- 在设置对话框中，找到最下面的个人信息选项，你会看到这里有一个文件检测器，下面有一个选项“保存时从属性中删除个人信息”，我们取消勾选这个选项，然后点击保存

{% asset_img 5d212aa85edf8db19ff5626c0823dd54574e749b.jpg 如何去掉excel保存文件时提示隐私问题警告 %}

- 如果你是从网上下载下来的文档，你还可以对文档进行检测，这样在你保存文档前就可以确定他的安全性。点击文档检测器

{% asset_img 0ef2112442a7d9335727fa7bac4bd11372f001ef.jpg 如何去掉excel保存文件时提示隐私问题警告 %}

- 这里也有一个文档属性和个人信息的选项，如果你勾选这个选项还是会提示安全警告

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
