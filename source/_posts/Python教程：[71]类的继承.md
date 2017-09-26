---
title: Python教程：[71]类的继承
date: 2015-01-11 18:17:01
tags: [python]
author: mlln.cn
---
类（class），可以继承基类以便形成具有自己独特属性的类，我们在面向对象的编程中，经常用到类及其继承，可以说没有什么不是类的，今天我们就来详细探讨一下在python中，类的继承是如何做的。

- 我们假设有一个类叫做point，顾名思义，point就是一个点，它有横坐标和纵坐标。我们在python中创建一个point类（书上说类名称都要开头字母大写，这是国际惯例）

{% asset_img 0e655ca7d933c895234d75f3d31373f0830200cc.jpg Python教程：[71]类的继承 %}

- 最简单的继承类的方式是这样：只需要在生命类的时候加一个括号和基类

{% asset_img 4e0b3ea4462309f7d403409a700e0cf3d6cad68f.jpg Python教程：[71]类的继承 %}

- 这种方法并没有声明该类的构造器，这样它会隐性调用基类的构造器，所以，在实例化的时候，也要注意基类的构造器需要哪些参数，不要出现这样的错误：这种错误容易发生是因为我们在子类的声明中并没有看到什么参数，在使用的时候就容易忘记基类中需要的参数

- Traceback (most recent call last):

-   File "<pyshell#11>", line 1, in <module>

-     a=point1()

- TypeError: __init__() takes exactly 3 arguments (1 given)

{% asset_img d35a10f41bd5ad6e0302896283cb39dbb7fd3c04.jpg Python教程：[71]类的继承 %}

- 这样来用就没问题了。

{% asset_img a84052086e061d952d27dbb079f40ad163d9ca92.jpg Python教程：[71]类的继承 %}

- 类的继承一般情况下，我们都是要重写类的构造器，然后再调用基类的构造器，不然基类的构造器在这种情况下不会自动调用。应该这样写：类point2比基类增加了一个属性z

{% asset_img a992e31f4134970a8cc0fca797cad1c8a6865d4c.jpg Python教程：[71]类的继承 %}

- 实例化：

{% asset_img 30ecd5ef76094b36d019f765a1cc7cd98c109d74.jpg Python教程：[71]类的继承 %}

- 我们看这样一个写法特别容易出错：你能看出哪里错了吗？
错误代码：

- Traceback (most recent call last):

-   File "<pyshell#50>", line 1, in <module>

-     b=point2(1,2,3)

-   File "<pyshell#45>", line 3, in __init__

-     point.__init__(x,y)

- TypeError: unbound method __init__() must be called with point instance as first argument (got int instance instead)

{% asset_img bd7faf3533fa828b103c726bff1f4134960a5ad8.jpg Python教程：[71]类的继承 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
