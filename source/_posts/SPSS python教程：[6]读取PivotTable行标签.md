---
title: SPSS python教程：[6]读取PivotTable行标签
date: 2016-10-03 18:19:01
tags: [python,spss]
author: mlln.cn
---
spss输出的结果文档用到最多的就是数据透视表（pivot table），在spss中，数据透视表被分为三个部分：行标签列表、列标签列表、数据列表。你可能还不理解这些内容。我们从这篇开始介绍数据透视表的行标签，并用python读取行标签，然后输出。看看代码吧：

- 这是在spss结果文档中输出的一个数据透视表，我们要读取它的行标签

{% asset_img 8b527d2762d0f7036208ba450afa513d2797c5b6.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 这就是行标签，但是它并不像我们看到的那么简单，我们试着读取行标签就知道了

{% asset_img 6c63514a20a4462308668afb9a22720e0df3d7bf.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 创建一个python脚本文件：outputTrim.py，下图中你可以看到该文件存放的目录

{% asset_img 48151723dd54564efa5acaa0b1de9c82d1584f28.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 接着先写入代码StartClient和stopclient，所有操作spss的代码都应该放在这两句之间。

{% asset_img dc15484e9258d109d807862bd358ccbf6d814d07.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 我们详细讲解一下代码的意义，先看这两句，假如我们只打开了一个结果文档，我们使用第一句代码可以获取该文档的句柄；第二句获取该文档下所有的输出项目，里面包含但不仅限于数据透视表，outputItems是一个列表

{% asset_img 9864a2315c6034a83fae9618c91349540823769f.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 通过循环，我们可以找到名称为'Descriptive Statistics'的数据透视表。我们看下面的if语句，首先判断输出项是不是PIVOT，然后判断该输出项的标题为'Descriptive Statistics'的PIVOT，获取标题用的是GetDescription

{% asset_img 263e802f07082838c19ff28dba99a9014d08f15e.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 这句代码是将找到的这个输出项转换为数据透视表，这样才能使用数据透视表所具有的类和方法

{% asset_img 814b07d8bc3eb13540169922a41ea8d3fc1f4412.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 这一句就是获取数据透视表的行标签

{% asset_img 9304c888d43f879430a461b7d01b0ef41ad53a94.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 我们用这个循环来输出所有的行标签，看看输出结果是啥样的

{% asset_img 35e940df8db1cb132a38158adf54564e93584b92.jpg SPSS python教程：[6]读取PivotTable行标签 %}

- 这就是输出结果，跟数据透视表对比一下，你就知道行标签到底代表着什么。

{% asset_img 6f4703950a7b02089dae167860d9f2d3562cc881.jpg SPSS python教程：[6]读取PivotTable行标签 %}

{% asset_img 6c63514a20a4462308668afb9a22720e0df3d7bf.jpg SPSS python教程：[6]读取PivotTable行标签 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
