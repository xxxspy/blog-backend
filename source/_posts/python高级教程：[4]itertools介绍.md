---
title: python高级教程：[4]itertools介绍
date: 2016-09-15 18:05:19
tags: [python]
author: mlln.cn
---
itertools是Python提供的用于实现各种生成器的工具包，我们先来看看几个常用的函数的用法。

- 切片itertools.islice

{% asset_img 0b07ec1fbe096b6350ac17ef0a338744eaf8ac9d.jpg python高级教程：[4]itertools介绍 %}

- 切片itertools.islice：有时候我们并不想迭代所有的元素，比如我只想处理d-g这些字母，看下面代码，我们可以使用islice(astr,3,len(astr)-1)

{% asset_img 4e83cb628535e5dd0fbdec6070c6a7efcf1b62b9.jpg python高级教程：[4]itertools介绍 %}

- 生成多个相同的生成器help(itertools.tee)

{% asset_img b3508d13b07eca80a0657258972397dda04483ea.jpg python高级教程：[4]itertools介绍 %}

- 生成多个相同的生成器itertools.tee。

{% asset_img 566d0fdfa9ec8a13ebd91c5ff103918fa1ecc00b.jpg python高级教程：[4]itertools介绍 %}

- tee是很有必要的，假如我们不使用tee，而直接在一个迭代器上进行切片，会产生这种混乱的结果：

{% asset_img 509b9fcb39dbb6fd6b8bae990f24ab18962b3779.jpg python高级教程：[4]itertools介绍 %}

- help(itertools.groupby)

{% asset_img 3c2c4bfbb2fb4316f9b130c526a4462308f7d3a0.jpg python高级教程：[4]itertools介绍 %}

- groupby可以自动将一个序列分组，相同相邻的元素会归为一组，形成一个新的生成器。

{% asset_img b13fd48065380cd757efe852a744ad3458828159.jpg python高级教程：[4]itertools介绍 %}

- 使用groupby可以压缩数据，如下代码，我们使用元组构成的列表来表示一个字符串，而元组的第一个元素表示组中包含的字母，而第二个元素表示这个字符重复的次数。

{% asset_img 0b907cd9f2d3572c9583d6638c13632763d0c3e9.jpg python高级教程：[4]itertools介绍 %}

- 接下来我们将继续介绍itertools中其他有用的函数。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
