---
title: python高级教程：[3]生成器方法send throw clos
date: 2015-07-05 18:17:01
tags: [python]
author: mlln.cn
---
这一篇接着讲Python的生成器，生成器总共有四个方法你可以看一下：next方法已经说过了，接下来说一下其余的三个方法。

- send：用于传递参数，实现与生成器的交互，我们举一个例子，下面的函数dog代表一只狗。当程序运行到food=(yield)的时候就会被挂起，等待生成器调用send方法，这时候我调用d.send(u'骨头')，骨头就会被传递到food这个变量中，然后程序就说"我吃饱了"。仔细看一下下面的输出内容你就会明白。所以，send实际上是把yield变成了一个输入入口。

{% asset_img 2e6fa7389b504fc2fc62bdbae3dde71190ef6d14.jpg python高级教程：[3]生成器方法send throw clos %}

- stop用于停止生成器，如果再stop之后调用next，就会引发StopIteration错误。

{% asset_img b29f8282d158ccbf2069b9851fd8bc3eb035417c.jpg python高级教程：[3]生成器方法send throw clos %}

- throw用于给生成器传递一个error，结合stop，我们可以做一些有意思的事情：

{% asset_img 346bd85c10385343ffbf889e9513b07ecb8088d9.jpg python高级教程：[3]生成器方法send throw clos %}

- 根据上面的例子我们可以知道，实际上stop可以在生成器内部引发一个GeneratorExit错误，我们可以使用try...except GeneratorExit句型捕获该错误，然后做一些善后的事情。

- 注意，在捕获GeneratorExit错误以后，你需要raise StopIteration错误，否则程序就没有终止的时候了。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
