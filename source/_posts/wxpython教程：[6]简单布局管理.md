---
title: wxpython教程：[6]简单布局管理
date: 2015-05-15 18:17:03
tags: [python,wxpython]
author: mlln.cn
---
一个软件的界面又很多控件，这些控件是如何布局的？今天我们先来看一下简单的布局方式，之后我们再来看看一些复杂的布局（利用sizer）实现的布局。

- 接着用之前写的代码，我们看一下代码：
很多内容都是之前的文章里介绍的，这里只是添加了两行代码：

-         panel=wx.Panel(self,-1)#创建一个面板对象

-         wx.TextCtrl(panel,pos=(3,3),size=(250,250))#添加一个文本框，并设置它的位置和大小

{% asset_img 3a86813df8dcd100a92c4274718b4710b8122ff7.jpg wxpython教程：[6]简单布局管理 %}

- Panel是窗口的容器，通常其大小与Frame一样，在其上放置各种控件，比如放置按钮、文本框等。

- 创建文本框的时候，我们传入pos和size参数，顾名思义，就是位置和大小，这段代码：wx.TextCtrl(panel,pos=(3,3),size=(250,250))就是设置文本框的位置是x=3，y=3；大小是长宽都是250的正方形。

- 这就是我们看到的界面：
改变界面大小，文本框控件的位置和大小是不变的

{% asset_img 3bb22487e950352a687e805d5043fbf2b2118b0d.jpg wxpython教程：[6]简单布局管理 %}

{% asset_img 346bd85c103853434ad022749013b07eca80880d.jpg wxpython教程：[6]简单布局管理 %}

- 我们一眼就能看出这种方式布局的局限性，于是，也许下面这种方式更加简便与灵活：我们直接将文本框嫁接到Frame上，而不是利用Panel：

{% asset_img 4e83cb628535e5dd30b3008a75c6a7efcf1b628d.jpg wxpython教程：[6]简单布局管理 %}

- 如此一来，文本框铺满整个Frame，大小与Fram相同，改变Frame大小，文本框也跟着变化：

{% asset_img 0862c354564e9258228323bb9f82d158cdbf4ef5.jpg wxpython教程：[6]简单布局管理 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
