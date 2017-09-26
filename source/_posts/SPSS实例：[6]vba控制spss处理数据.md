---
title: SPSS实例：[6]vba控制spss处理数据
date: 2015-04-19 18:15:19
tags: [spss]
author: mlln.cn
---
    使用vba来控制spss处理数据，使得我们可以批量进行spss操作，大大加快我们的工作速度。比如，前两天有网友问我如何进行一万次回归分析，我直接写了一段vba代码，很快就能处理完，并整理成分析报告。这就是vba与spss合作所带来的效果，因为篇幅有限，下面只给大家概述一下如何在vba中调用spss对象，并进行数据处理，想要了解更详细的教程，希望您持续关注我写的教程。转载请注明出处（作者百度ID为：qq675495787）

- 概述spss对象：spss对象是控制spss程序的对象集合。spss对象的指令变换点是ISpssApp对象，它是所有对象的容器，内含所有对象。下面的树形图介绍了spss对象所包含的属性和方法，这些属性和方法会在以后的教程中跟大家介绍。

{% asset_img 9f1011b30f2442a74f8bfa94d343ad4bd113023e.jpg SPSS实例：[6]vba控制spss处理数据 %}

- 引用spss类库：如果你想要写spss脚本，你必然要用到spss对象。在spss脚本中，你可以使用objSPSSApp为全局变量来调用spss对象，在此之前要确保这个对象已经被创建好了（实际上，创建了spss对象就使spss程序开始运行了，只不过你看不到程序界面，说实话，你什么都看不到）。

- 换一种说法，如果你想要在其他编程语言中使用spss，你需要首先创建ISpssApp对象。例如，在微软的VB编辑器中（使用vba），首先你必须在VBA工程中引用spss对象类库（也就是：spsstype library，spss pivot table
type library和spss RTF type library）。操作方法是，在vbe中，点击工具--引用；找到这几个类库，然后勾选他们，点击确定按钮。

{% asset_img 0db52fadcbef76096a269fae2cdda3cc7cd99e96.jpg SPSS实例：[6]vba控制spss处理数据 %}

{% asset_img 4a77b2af2edda3cc59c9be1103e93901213f9296.jpg SPSS实例：[6]vba控制spss处理数据 %}

- 声明spss对象变量：引用了spss类库以后，我们可以在vba中声明spss对象变量了。代码如下：

- Dimspss as object

- Set
spss=createobject("spss.application16")

- 实际上我们更建议使用对象类来声明变量，所以上面的语句应当写成：

- Dimspss as ispssapp

- Set spss=new
spsswinlib.application16

- 这样的写法可以加快你的代码编写速度。

- 设置spss程序可见性：以上两个小代码可以启动spss程序，当你不需要看到这个程序的时候，你应该让其保持隐身，在后台运行，你看不到spss程序。如果你想要看到spss程序，你应该设置spss对象的可见性属性为true。如下图所示，我们打开一个数据文件“卡方检验”，然后设置数据文件的可见性为1，这样就可以看到spss程序了，否则是看不到的，但是即便看不到他们也是运行中的。

{% asset_img 35da1d3b5bb5c9ea117f05d2d739b6003af3b337.jpg SPSS实例：[6]vba控制spss处理数据 %}

- 小试牛刀：我们试试如何读取spss的版本号，输入代码

-         a = spss.GetSPSSVersion

-          MsgBox a

- 这段代码就是用变量a存放spss的版本号，然后用消息框显示a的数值。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
