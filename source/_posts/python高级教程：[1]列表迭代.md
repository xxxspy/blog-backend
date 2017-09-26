---
title: python高级教程：[1]列表迭代
date: 2015-02-23 18:17:23
tags: [python]
author: mlln.cn
---
Python在列表迭代时有许多灵活的用法，如果不用心去设计会让你走很多弯路，比如我们设定一个这样的问题：我们想找到年龄大于30的人的名字，现在有两个列表一个为names，存放着所有人的名字，一个为ages存放有所有人的年龄：

- 我们用菜鸟的方式来解决这个问题：

- 在这里，我们创建了一个空列表oldPeople用来存放那些年龄大于30的人的名字。然后通过循环来获得那些“老人”。

{% asset_img d4239b35e5dde71187a438b3a1efce1b9c1661c5.jpg python高级教程：[1]列表迭代 %}

- 另一种菜鸟的方式也好不到哪里去：

- 我们增加了一个递增变量i,for name in names这种写法就可以不必每次都重新获取name值；

{% asset_img 8640bf8b87d6277f3d33487d2e381f30e924fc17.jpg python高级教程：[1]列表迭代 %}

- 我们首先可以想到enumerate可以即得到索引i，又得到列表元素name，但是这仍然不是最佳的方式

{% asset_img 3853ad1bb051f8191e04790fdcb44aed2e73e717.jpg python高级教程：[1]列表迭代 %}

- 一种极具Python风格的写法，只需要一句代码就可以完成这个任务。

{% asset_img b0742dfa828ba61e97cab36a4734970a304e590b.jpg python高级教程：[1]列表迭代 %}

- 所谓的Python高级教程就是这些，我们提供一些实例来对比菜鸟和Python高手之间的区别，以便于菜鸟能够快速的晋级为高手，如果你觉得这篇文章对你有帮助，请收藏！如果想转载，请注明作者。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
