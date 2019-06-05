---
title: pandas教程：[4]Dataframe筛选数据
date: 2016-01-11 18:01:03
tags: [pandas]
author: mlln.cn
---
今天还是用到了DataFrame，如果你用一下它的筛选数据的功能，你会大吃一惊，它非常擅长筛选数据，可以极大提高你的工作效率，废话不多说，下面看看几个进行复杂数据筛选的例子。

- 首先我们创建一个DataFrame，该DataFrame包含的数据如下

{% asset_img 814b07d8bc3eb13550c4a88da51ea8d3fd1f4441.jpg pandas教程：[4]Dataframe筛选数据 %}

- 假如我们想要筛选D列数据中大于0的行

{% asset_img 32bb9c8ba61ea8d39a216b32940a304e251f5841.jpg pandas教程：[4]Dataframe筛选数据 %}

- 使用&符号可以实现多条件筛选，当然是用"|"符号也可以实现多条件，只不过他是或的关系。

{% asset_img 346bd85c10385343eceb98179013b07eca8088a4.jpg pandas教程：[4]Dataframe筛选数据 %}

- 假如我们只需要A和B列数据，而D和C列数据都是用于筛选的，可以这样写：只返回了AB两列数据
‘

{% asset_img d041a4a1cd11728b3c2e9314cbfcc3cec3fd2c41.jpg pandas教程：[4]Dataframe筛选数据 %}

- 我们以上用到的方法都是通过一个布尔索引完成的，我们看一下这样的运算返回的值是什么

{% asset_img 4a77b2af2edda3cc51c0a71602e93901213f92a4.jpg pandas教程：[4]Dataframe筛选数据 %}

- 我们还可以使用insin方法来筛选特定的值，把要筛选的值写到一个列表里，如alist

{% asset_img 38403f3fb80e7bec60fe1cd72c2eb9389b506ba4.jpg pandas教程：[4]Dataframe筛选数据 %}

- 假如选择D列数据中，有alist中的值的行

{% asset_img 2e6fa7389b504fc2ef7baf33e6dde71190ef6da4.jpg pandas教程：[4]Dataframe筛选数据 %}

{% asset_img b7bc4c66d01609243982bc2dd70735fae6cd3425.jpg pandas教程：[4]Dataframe筛选数据 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
