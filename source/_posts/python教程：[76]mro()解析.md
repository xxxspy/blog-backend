---
title: python教程：[76]mro()解析
date: 2015-08-11 18:03:17
tags: [python]
author: mlln.cn
---
今天在看django-xadmin源码的时候看到的一个mro方法，我这种小白还不太懂python里比较深入的内容，所以百度了很多文章来看，现在总结一下。

- 这个方法用于返回某个类的基类以及基类的基类，我们举一个简单的例子：创建一个类A，然后调用mro，它返回了一个列表，列表元素是类A本身和它的基类

{% asset_img d002b34bd11373f04c42a5a4a70f4bfbfbed0449.jpg python教程：[76]mro()解析 %}

- 假如我们再创建一个类B，继承于A，然后调用mro，现在列表里多了内容，看到了吧，mro总是返回类本身和其基类的列表

{% asset_img ac2fc3c451da81cb80aa49f65166d0160924317a.jpg python教程：[76]mro()解析 %}

- 假如把类的继承关系弄的复杂一些，类C和类B都继承自A，D继承B和C，这时候调用D.mro，我们看到这时候列表的顺序为：D-B-C-A

{% asset_img d048adde9c82d158444d938a830a19d8bd3e42fb.jpg python教程：[76]mro()解析 %}

- 在负责一些，增加类E继承类A，F继承自E和D，然后调用F.mro，这时候你就可以看到类A总是列表的最后一个元素，列表的顺序是：F-E-D-B-C-A

{% asset_img 814b07d8bc3eb135be7d8287a51ea8d3fd1f4410.jpg python教程：[76]mro()解析 %}

- 记住这个列表的顺序很有用，因为以后再复制的类调用的时候，可能会考虑到初始化类的顺序，它们遵循的就是mro的顺序

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
