---
title: Python教程：[72]classmethod装饰器
date: 2016-08-01 18:11:01
tags: [python]
author: mlln.cn
---
classmethod装饰器用于装饰类方法，怎么说呢？通常我们想要调用类中的某个方法时，需要先将其实例化，然后利用实例调用该方法，但是如果我们想要用类（而不是实例）直接调用方法，那就需要使用classmethod装饰器了，下面看看具体的解释：

- 现在我们声明一个类：foo，其中包含两个方法，f1为实例方法，调用时需要先将类实例化；f2为类函数，调用前不需要实例化，注意f2的参数为cls，也就是类本身，而不是self。具体看下面的例子

{% asset_img 1899a23eb13533fa623009eaaad3fd1f40345b35.jpg Python教程：[72]classmethod装饰器 %}

- 加入我们想要调用f1，f1为实例函数，所以需要先将其实例化，foo_sl是foo的一个实例

{% asset_img a75fb6d3fd1f413472b19fba271f95cad0c85e35.jpg Python教程：[72]classmethod装饰器 %}

- 调用f1：

{% asset_img 310f3b1f95cad1c84d3d66e37d3e6709c83d5135.jpg Python教程：[72]classmethod装饰器 %}

- 假如我们使用类直接调用f1，就会提示错误

{% asset_img c87c6ecf3bc79f3d0a677ef4b8a1cd11738b2935.jpg Python教程：[72]classmethod装饰器 %}

- 而类方法就可以直接调用

{% asset_img a75fb6d3fd1f413472d29fba271f95cad3c85eca.jpg Python教程：[72]classmethod装饰器 %}

- 当然，实例也可以直接调用类方法：

{% asset_img a6c7d7177f3e670927e5df3b39c79f3dfadc55ca.jpg Python教程：[72]classmethod装饰器 %}

- 以下为本经验用到的所有的代码：

- >>> class foo(object):

- def f1(self):

- print 'normal'

- @classmethod

- def f2(cls):

- print 'class'

- >>> foo_sl=foo()

- >>> 

- >>> foo_sl.f1()

- normal

- >>> foo_sl.f2()

- class

- >>> 

- >>> 

- >>> foo.f1()

- Traceback (most recent call last):

-   File "<pyshell#42>", line 1, in <module>

-     foo.f1()

- TypeError: unbound method f1() must be called with foo instance as first argument (got nothing instead)

- >>> foo.f2()

- class

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
