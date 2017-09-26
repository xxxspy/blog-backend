---
title: Python教程：[68]字典排序方法大全
date: 2016-05-19 18:17:23
tags: [python]
author: mlln.cn
---
怎样对字典进行排序？其实和列表有点类似，方法差不多，但是有细微的差别。鉴于前几篇文章都写的是列表排序，所以有些内容不不详细讲了，不知道的可以翻看前几篇文章。我在文章中也会提示哪篇文章可以看。

- 先创建一个字典a，字典a有三个元素

{% asset_img 346bd85c103853437ba670a19113b07ecb808882.jpg Python教程：[68]字典排序方法大全 %}

- 我们使用key进行排序，注意这是第一个参数用的是a.items，而列表排序的时候用的是列表本身，不是其元素。我们看这种方法返回了一个列表b，而不再是字典了。列表排序这篇文章详细讲解了key的用法【http://jingyan.baidu.com/article/90808022a546b8fd90c80f48.html】

{% asset_img b13fd48065380cd71677556da344ad3458828182.jpg Python教程：[68]字典排序方法大全 %}

- 注意看下面这个方法，有略微的区别，但是返回的b都是一样的

{% asset_img 0db2c9ca7bcb0a4693957cb96963f6246a60afb8.jpg Python教程：[68]字典排序方法大全 %}

- 我们也可以使用更加高效也更加简洁的方法：引入itemgetter

{% asset_img 30ecd5ef76094b363ffbec6da1cc7cd98c109d82.jpg Python教程：[68]字典排序方法大全 %}

- 假如我们想要使用字典的值进行排序，就写参数key=itemgetter(1)

{% asset_img 00a82701213fb80ee7b8965734d12f2eb8389482.jpg Python教程：[68]字典排序方法大全 %}

- 假如要用字典的键进行排序，可以使用itemgetter(0)

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
