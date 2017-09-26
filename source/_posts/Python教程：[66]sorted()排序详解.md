---
title: Python教程：[66]sorted()排序详解
date: 2015-01-19 18:15:11
tags: [python]
author: mlln.cn
---
使用python对列表（list）进行排序，说简单也简单，说复杂也复杂，我一开始学的时候也搞不懂在说什么，只能搜索一些英文文章看看讲解，现在积累了一些经验，写在这里跟大家分享，我们通过例子来详细解释一下函数sorted的具体用法：

- 先创建一个列表a

{% asset_img 58af236d55fbb2fb18b1d6924d4a20a44723dc5d.jpg Python教程：[66]sorted()排序详解 %}

- 直接使用sorted方法，返回一个列表b，b就是排序好了的

{% asset_img 72ccb7773912b31b9ec043a98418367adbb4e147.jpg Python教程：[66]sorted()排序详解 %}

- 假如a是一个由元组构成的列表，这时候就麻烦了。

{% asset_img 425773224f4a20a41984b24792529822730ed05d.jpg Python教程：[66]sorted()排序详解 %}

- 我们需要用到参数key，也就是关键词，看下面这句命令，lambda是一个隐函数，是固定写法，不要写成别的单词；a_tuple表示列表中的一个元素，在这里，表示一个元组，a_tuple只是临时起的一个名字，你可以使用任意的名字；a_tuple[0]表示元组里的第一个元素，当然第二个元素就是a_tuple[1]；所以这句命令的意思就是按照列表中元组里的第一个元素进行排序。

{% asset_img 109eb7ec8a13632732414cb3938fa0ec09fac747.jpg Python教程：[66]sorted()排序详解 %}

- 按照元组里的第二个元素排序

{% asset_img 08b68e529822720e68546c7a79cb0a46f31fab5d.jpg Python教程：[66]sorted()排序详解 %}

- 除了key参数可以实现这个功能外，还可以使用cmp参数，注意看，这里不同之处是使用了x和y两个元组，他俩都是临时起的名字，你可以任意更改，我们用x表示列表里第一个元素，y表示列表里第二个元素，x[1]表示第一个元组的第二个元素，同理y[1]也是，而cmp()就是比较函数，也就是说，比较x[1]和y[1]的大小。

{% asset_img 90cebeec08fa513d7006e25e3f6d55fbb3fbd947.jpg Python教程：[66]sorted()排序详解 %}

- 我们还可以使用reverse参数实现倒序排列

{% asset_img 0b07ec1fbe096b639d83d0d00e338744eaf8ac5d.jpg Python教程：[66]sorted()排序详解 %}

- 如果你现在还不能理解，先记住他们的固定写法，写多了自然就懂了。

- 下一篇文章讲更加深入的一个排序方法，在写法上更见简单，请看传送门：http://jingyan.baidu.com/article/f3ad7d0ffe8e1409c2345b48.html

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
