---
title: pandas教程：[1]DataFrame入门
date: 2015-10-23 18:19:05
tags: [pandas]
author: mlln.cn
---
pandas是python环境下最有名的数据统计包，而DataFrame翻译为数据框，是一种数据组织方式，这么说你可能无法从感性上认识它，举个例子，你大概用过Excel，而它也是一种数据组织和呈现的方式，简单说就是表格，而在在pandas中用DataFrame组织数据，如果你不print DataFrame，你看不到这些数据，下面我们来看看DataFrame是如何使用的。

- 首先是引入pandas和numpy，这是经常配合使用的两个包，pandas依赖于numpy，引入以后我们可以直接使用np/pd来表示这个两个模块

{% asset_img 0ef2112442a7d9335e64e347ae4bd11372f001f2.jpg pandas教程：[1]DataFrame入门 %}

- 先创建一个时间索引，所谓的索引（index)就是每一行数据的id，可以标识每一行的唯一值

{% asset_img 21e5582309f7905271fa410a0ff3d7ca7acbd5da.jpg pandas教程：[1]DataFrame入门 %}

- 为了快速入门，我们看一下如何创建一个6X4的数据：randn函数用于创建随机数，参数表示行数和列数，dates是上一步创建的索引列

{% asset_img c9d4cf43ad4bd113e90db00659afa40f4afb0586.jpg pandas教程：[1]DataFrame入门 %}

- 我们还可以使用字典来创建数据框，例如创建一个列名为A的数据框，索引是自动创建的整数

{% asset_img aa251d4f78f0f7360b324b350955b319eac413f2.jpg pandas教程：[1]DataFrame入门 %}

- 这又是一个字典创建DataFrame的例子

{% asset_img ea85a94543a98226630d2c138982b9014b90ebf3.jpg pandas教程：[1]DataFrame入门 %}

- 假如字典内的数据长度不同，以最长的数据为准，比如B列有4行：

{% asset_img b8405490f603738d1a8a0b16b01bb051f919ec87.jpg pandas教程：[1]DataFrame入门 %}

- 可以使用dtypes来查看各行的数据格式

{% asset_img b110e6198618367a604978e92d738bd4b21ce587.jpg pandas教程：[1]DataFrame入门 %}

- 接着看一下如何查看数据框中的数据，看一下所有的数据

{% asset_img e865a699a9014c08a5f72f91097b02087af4f4f3.jpg pandas教程：[1]DataFrame入门 %}

- 使用head查看前几行数据（默认是前5行），不过你可以指定前几行

{% asset_img b25d9901a18b87d6e58eac2b040828381e30fdf3.jpg pandas教程：[1]DataFrame入门 %}

- 查看前三行数据

{% asset_img 6f4703950a7b0208b40538d561d9f2d3562cc8f3.jpg pandas教程：[1]DataFrame入门 %}

- 使用tail查看后5行数据

{% asset_img 1cd4147b02087bf4da2050ddf1d3572c10dfcff3.jpg pandas教程：[1]DataFrame入门 %}

- 查看数据框的索引

{% asset_img 6398ecd3572c11df7c1db817602762d0f603c2f3.jpg pandas教程：[1]DataFrame入门 %}

- 查看列名用columns

{% asset_img 8b527d2762d0f7034b7e92e80bfa513d2797c5f3.jpg pandas教程：[1]DataFrame入门 %}

- 查看数据值，用values

{% asset_img 507c389759ee3d6db40a80ff40166d224e4adef3.jpg pandas教程：[1]DataFrame入门 %}

- 查看描述性统计，用describe

{% asset_img b3ba5d166d224f4ac65574270af790529922d1f3.jpg pandas教程：[1]DataFrame入门 %}

- 使用type看一下输出的描述性统计是什么样的数据类型——DataFrame数据

{% asset_img 08b68e529822720ee002e5ce78cb0a46f31fabf3.jpg pandas教程：[1]DataFrame入门 %}

- 使用T来转置数据，也就是行列转换

{% asset_img 0db2c9ca7bcb0a4602ee8c0d6863f6246a60aff3.jpg pandas教程：[1]DataFrame入门 %}

- 对数据进行排序，用到了sort，参数可以指定根据哪一列数据进行排序。

{% asset_img 0d729944ebf81a4ca8feebfdd42a6059242da6f3.jpg pandas教程：[1]DataFrame入门 %}

- 好了，这篇入门教程到这里，后面还有很多，希望有志同道合的朋友一起交流学习，有什么说的不对的地方，请批评指正。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
