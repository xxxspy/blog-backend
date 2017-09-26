---
title: python教程：[77]lambda和filter的神奇
date: 2015-06-19 18:01:19
tags: [python]
author: mlln.cn
---
我们先分别讲一下这两个内置函数的用法，然后看看这两个结合起来产生的效果，以及通常我们用他们来干嘛。

- lambda通常是匿名函数的代名词，我们用到lambda的时候就是创建一个匿名函数：举个简单的例子：x代表了输入，x**2代表计算方法，也代表返回内容，也就是说这个函数输入一个数，返回这个数的平方。但是因为这个函数没有函数名，所以无法在其他地方调用

{% asset_img 4d4970061d950a7bf9f37ef809d162d9f3d3c98d.jpg python教程：[77]lambda和filter的神奇 %}

- 除非我们将这个函数起一个名字：但通常我们不会这么做，匿名函数只是作为匿名使用。

{% asset_img 21e5582309f790528e7674020ff3d7ca7bcbd565.jpg python教程：[77]lambda和filter的神奇 %}

- filter函数用法是：filter(fuction,list)：将list中每一个元素带入到function中，计算返回值，将返回值为True的list中的元素形成一个新的list，当然也可以是tuple。

{% asset_img 8a95ad1c8701a18b6cee2f739d2f07082838fe42.jpg python教程：[77]lambda和filter的神奇 %}

{% asset_img 064936381f30e9244aa1a10d4f086e061d95f742.jpg python教程：[77]lambda和filter的神奇 %}

- 对于上面这个函数，我们可以用lambda来简化：它的意思是，如果alist中的值的平方小于5，就返回这个值，形成一个新的list

{% asset_img 6398ecd3572c11df565a821f602762d0f603c2c0.jpg python教程：[77]lambda和filter的神奇 %}

- 通常，我们使用这两个内置函数的结合来过滤list里的空值：

{% asset_img 32bb9c8ba61ea8d375184838940a304e251f5890.jpg python教程：[77]lambda和filter的神奇 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
