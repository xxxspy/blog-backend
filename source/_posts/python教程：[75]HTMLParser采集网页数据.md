---
title: python教程：[75]HTMLParser采集网页数据
date: 2016-06-19 18:03:05
tags: [python]
author: mlln.cn
---
HTMLParser是python自带的处理html文件的模块，用起来非常简单，但很有实用价值，下面我们通过一个简单的例子来说明它的工作机制，然后对它所包含的所有方法进行一个说明。

- 先看一个简单的例子，我们先引入HTMLParser，然后声明一个类，继承自HTMLPaerser，然后定义了一个方法，这个方法继承自HTMLParser

{% asset_img 5beeba0f4bfbfbedc8be6c497bf0f736aec31fe5.jpg python教程：[75]HTMLParser采集网页数据 %}

- 这一段代码的运行结果是：从结果中我们可以看到feed方法是将要处理的html字符串传递给HTMLParser，处理的过程是从前到后逐个处理html文件的标签，当遇到一个标签的时候，就调用handle_starttag方法，我们写的这个方法就是将tag名打印出来，所以就出现了下面这个结果：

{% asset_img 718e25c79f3df8dce066caa7ce11728b47102869.jpg python教程：[75]HTMLParser采集网页数据 %}

- feed()和handle_starttag()已经说了，这里不再重复

- handle_endtag()：处理结束标签，比如</a>就是一个结束标签，当遇到结束标签的时候调用该方法

- handle_data():处理数据，比如<a>这是数据</a>，“这是数据”就是data，当遇到data的时候调用该方法。

- handle_entityref()：处理“&gt;”“&#62;”“&#x3E;”这样的字符串，他们各有自己指代的字符，处理的方法是使用name2codepoint将其转换，就可以知道gt原来是>的意思

{% asset_img b25aae51f81986184ee3a9b249ed2e738bd4e625.jpg python教程：[75]HTMLParser采集网页数据 %}

{% asset_img 29790130e924b89921983f0e6d061d950a7bf625.jpg python教程：[75]HTMLParser采集网页数据 %}

- handle_charref()处理十进制或十六进制“&#x3E;”这样的字符串，可以将其转换为&gt

- handle_comment()处理<!--comment-->内的内容

- handle_decl()处理html文档类型声明，例如<!coctype html>

- 大部分方法都列在上面了，还有一些不常用就没有写，这些相信已经够你用了。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
