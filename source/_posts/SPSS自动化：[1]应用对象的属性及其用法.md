---
title: SPSS自动化：[1]应用对象的属性及其用法
date: 2016-04-05 18:17:17
tags: [spss]
author: mlln.cn
---
在上一篇经验《vba控制spss处理数据》中，我们介绍了vba使用spss对象来控制spss，下面我们接着来讲如何使用spss对象的属性，因为spss对象的属性有十几个（见下图），下面的列表呈现了spss对象所具有的属性，可能不全，希望指正。我们来一一介绍这些属性的用法和功能。

- alerts属性：语法格式为spss.alerts=boolean。boolean值可以是1或者0，如果值为1，则spss程序允许弹出警告窗口，如果值为0，则spss程序不会弹出警告窗口。该属性可读可写，下面是我在vba中调用alerts属性的方法。

{% asset_img b9d8b7014c086e06f3031b7e00087bf40ad1cb19.jpg SPSS自动化：[1]应用对象的属性及其用法 %}

- currentdirectory属性：设置文件存放目录。该属性可读可写，下面是在vba中读取当前目录的代码。当然你可以使用该属性来设置当前目录。

{% asset_img 7e7f7909c93d70cfb61c8d38fadcd100bba12be5.jpg SPSS自动化：[1]应用对象的属性及其用法 %}

- options属性：利用该属性可以获取options对象，它提供了与spss选项设置的链接，选项设置我们并不陌生，以后我们会详细的介绍使用options对spss进行设置，现在你只要知道读取options属性的方法，下面是代码实例：首先要把变量opt声明为选项对象，然后在读取选项对象。

{% asset_img 9252ae7eca8065383c2f892695dda144ac3482fa.jpg SPSS自动化：[1]应用对象的属性及其用法 %}

- spssifo属性：这个属性可以获得当前spss打开的数据文件中的变量信息。示例代码如下：

{% asset_img 8a95ad1c8701a18b5dc43d7a9c2f07082838fe9d.jpg SPSS自动化：[1]应用对象的属性及其用法 %}

- 还有很多属性，未完待续。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
