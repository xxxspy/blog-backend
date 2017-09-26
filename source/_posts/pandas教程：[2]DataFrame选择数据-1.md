---
title: pandas教程：[2]DataFrame选择数据-1
date: 2015-07-11 18:05:23
tags: [pandas]
author: mlln.cn
---
上一篇文章介绍了如何创建和查看DataFrame数据，这篇文章讲一下如何选择DataFrame中的数据，还是用例子来说明问题。

- 先来看一下今天用到的数据框的内容

{% asset_img 509b9fcb39dbb6fdd256ea120a24ab18972b37b1.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 假如我们要选择A列的数据进行操作：df['a']

{% asset_img 966aca0735fae6cdf3b9a4550cb30f2442a70fb1.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 还可以使用数组的切片操作，但是注意了，切片得到的是行数据

{% asset_img d872d695d143ad4b402349f481025aafa40f06b1.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 如果你想使用这个方法得到列，那就会出现错误

{% asset_img 38403f3fb80e7bec70840cd52c2eb9389b506b6c.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 我们还可以使用行标签来指定输出的行

{% asset_img 4e83cb628535e5ddca72aaeb75c6a7efce1b626c.jpg pandas教程：[2]DataFrame选择数据-1 %}

- DataFrame的loc方法是帮助选择数据的，比如选择索引位置为0的一行数据（注意我们是用dates作为索引的）

{% asset_img ae10eddeb48f8c54ac8dca1b39292df5e0fe7f6c.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 选择多列数据的写法

{% asset_img 8640bf8b87d6277f251f3d0c2b381f30e924fcb2.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 假如我们要选择的是一个局部数据，是行和列的交叉区域

{% asset_img 507c389759ee3d6d8ccb88ff40166d224f4adeb2.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 假如我们只选择某一个数据，可以指定行和列：

{% asset_img 08b68e529822720ee8c3edce78cb0a46f21fabb2.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 当然，at方法是专门用于获取某个值的：

{% asset_img 3a86813df8dcd100d2c2f715718b4710b9122f6c.jpg pandas教程：[2]DataFrame选择数据-1 %}

- 选择数据就是用到了切片和loc、at方法，下一篇文章介绍一下iloc方法选择数据，它使你像操作array一样操作DataFrame

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
