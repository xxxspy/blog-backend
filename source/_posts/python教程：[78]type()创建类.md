---
title: python教程：[78]type()创建类
date: 2015-06-19 18:11:03
tags: [python]
author: mlln.cn
---
今天我算是长知识了，我是一个python菜鸟，以前一直认为type（A）可以返回A的类型，但是不知道type还可以用于创建class，这篇经验就是介绍一下如何用type（）创建一个类，以及如何设置该类的属性。

- 我们使用type创建一个空类：只有一个名字，其他什么都没有，它的参数格式是：type(class_name,bases,dic)

{% asset_img c8ab0bce36d3d53974894de33987e950352ab01f.jpg python教程：[78]type()创建类 %}

- 我们用type来查看一下我们创建的cls的类型：

{% asset_img 906289dda144ad348c25c5a7d3a20cf431ad853d.jpg python教程：[78]type()创建类 %}

- 查看cls的名称

{% asset_img 0db52fadcbef76099791dbbf2ddda3cc7cd99e3d.jpg python教程：[78]type()创建类 %}

- 假如我们用比较熟悉的继承的方式来创建一个类，它跟cls是一样的：

{% asset_img 7d98931001e93901c598cf1e78ec54e736d1963d.jpg python教程：[78]type()创建类 %}

- 当然，我们可以通过参数dic来设置其他任何类的属性，比如：

{% asset_img 207ea60e7bec54e7de76583eba389b504fc26a3d.jpg python教程：[78]type()创建类 %}

- 现在cls2比cls多了属性__doc__,__module__

{% asset_img 2e6fa7389b504fc238c5f225e6dde71190ef6d3d.jpg python教程：[78]type()创建类 %}

{% asset_img d4239b35e5dde711614801d6a4efce1b9d16613d.jpg python教程：[78]type()创建类 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
