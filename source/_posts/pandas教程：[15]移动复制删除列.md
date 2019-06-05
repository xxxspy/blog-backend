---
title: pandas教程：[15]移动复制删除列
date: 2015-01-19 18:01:15
tags: [pandas]
author: mlln.cn
---
pandas的DataFrame非常灵活，我们可以快速的移动、复制、删除列，今天就用案例来说明一下具体的工作是如何完成的。

- 首先我们创建一个dataframe
打印一下：

{% asset_img b74124f33a87e95019c1d76f13385343faf2b49b.jpg pandas教程：[15]移动复制删除列 %}

{% asset_img 62667cd0f703918f5bcc1ac9523d269759eec451.jpg pandas教程：[15]移动复制删除列 %}

- 增加列，我们可以把df当作一个object，给它增加一个属性c，如下：
这是增加c列以后的数据：

{% asset_img 0d729944ebf81a4c482ecbcad42a6059252da651.jpg pandas教程：[15]移动复制删除列 %}

{% asset_img 4a77b2af2edda3cc3a329c2302e93901203f929b.jpg pandas教程：[15]移动复制删除列 %}

- 我们还可以插入一列数据到任意位置：比如插入到第二列
插入后的数据：

{% asset_img 61183b2dd42a283414ba110858b5c9ea15cebf51.jpg pandas教程：[15]移动复制删除列 %}

{% asset_img 148f28d3d539b60012d228b4ea50352ac65cb751.jpg pandas教程：[15]移动复制删除列 %}

- 永久删除一列数据用del，虽然我们不建议你这么武断的删除c列：
删除后的数据：

{% asset_img 3790312eb9389b501d29c4518635e5dde6116e9b.jpg pandas教程：[15]移动复制删除列 %}

{% asset_img cbc17b380cd79123a0fcb377ae345982b2b78051.jpg pandas教程：[15]移动复制删除列 %}

- 更明智的方法是使用drop，它不改变原有的df中的数据，而是返回另一个dataframe来存放删除后的数据
这是df2中的数据：

{% asset_img d4239b35e5dde711c70467f5a4efce1b9c16619b.jpg pandas教程：[15]移动复制删除列 %}

{% asset_img 91ae68c6a7efce1bc6fdecc9ac51f3deb58f659b.jpg pandas教程：[15]移动复制删除列 %}

- 移动列也很简单，假如我们想要将c列移动到第一列，我们可以使用pop来输出并删除b列，然后再将b列插入到第一列，这样就完成了移动
移动后的结果为：

{% asset_img d4239b35e5dde711c6ce64f5a4efce1b9d166151.jpg pandas教程：[15]移动复制删除列 %}

{% asset_img ae10eddeb48f8c54f505e12c39292df5e1fe7f9b.jpg pandas教程：[15]移动复制删除列 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
