---
title: python高级教程：[3]yield生成器
date: 2015-09-23 18:11:15
tags: [python]
author: mlln.cn
---
基于yield这个指令，Python可以挂起一个程序并返回中间结果，被挂起的程序会保持自己的执行环境，在必要的时候再重启它。

- 先看看yield的简单用法：yield_example表示一个2的n次方的无穷数列，我们想要它输出前10项，就用[ye.next() for a in range(10)]

{% asset_img 9864a2315c6034a8fd2d583fcd13495408237606.jpg python高级教程：[3]yield生成器 %}

- 一个生成器的next()方法可以让程序运行，并输出yield的值，然后再次被挂起，直到下一个next被调用。这句I是一个生成器。我们经常使用生成器来表示一个无穷数列，下面看一个复杂的例子。

- 用yield写一个分组数列，分组数列的定义是：

{% asset_img 034965f40ad162d9db928fa217dfa9ec8b13cdd5.jpg python高级教程：[3]yield生成器 %}

{% asset_img 43e6c733c895d1435df9069d75f082025baf0746.jpg python高级教程：[3]yield生成器 %}

- 实现分组数列的代码：

{% asset_img 570f8c58d109b3de377306d6cabf6c81810a4c05.jpg python高级教程：[3]yield生成器 %}

- 为什么使用字典作为sublist函数的参数，这是因为在传参的时候，如果参数是字典，那么传递的是一个指针，而不是字典的数据，因此当sublist改变了字典的数据的时候，位于fenqunlist函数中的kwargs字典的数据也会发生改变，这是我所希望的。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
