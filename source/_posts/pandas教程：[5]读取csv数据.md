---
title: pandas教程：[5]读取csv数据
date: 2015-06-15 18:17:01
tags: [pandas]
author: mlln.cn
---
很多数据是从网上下载而来，数据的格式可能是csv，那么pandas可以很容易的从csv格式的文件中读取数据，下面我们来看看具体的过程：

- 引入pandas

{% asset_img 7787b9efce1b9d161dd32272f0deb48f8c54644a.jpg pandas教程：[5]读取csv数据 %}

- 使用pandas下的read_csv方法，读取csv文件，参数是文件的路径，这是一个相对路径，是相对于当前工作目录的，那么如何知道当前的工作目录呢？

{% asset_img bd7faf3533fa828ba41825f0fe1f4134970a5aae.jpg pandas教程：[5]读取csv数据 %}

- 使用os.getcwd()方法获取当前工作目录

{% asset_img 1cd4147b02087bf47fe5effaf1d3572c11dfcf5d.jpg pandas教程：[5]读取csv数据 %}

- 读取前三后数据，查看一下是否读取正确，显然都是乱码，这是什么问题呢？

{% asset_img 95afee1f3a292df509d71406bf315c6034a8734a.jpg pandas教程：[5]读取csv数据 %}

- 我们需要设定参数encoding，也就是编码方式，如果你不设定编码方式，默认是utf8，现在csv文件是gbk编码的，所以需要使用encoding='gbk'

{% asset_img 2cb4fefe9925bc31b049b98b5ddf8db1cb13704a.jpg pandas教程：[5]读取csv数据 %}

- 我用的编辑器是eric4，注意，eric4默认是不支持中文的，如果你想要显示中文，前提是设置正确的编码，在preferences中

{% asset_img c87c6ecf3bc79f3debda5c23b9a1cd11728b29ae.jpg pandas教程：[5]读取csv数据 %}

- 设置成utf8即可

{% asset_img d041a4a1cd11728b5f163431cbfcc3cec3fd2cae.jpg pandas教程：[5]读取csv数据 %}

- 回到pandas，我们可以有更多选项来设置打开数据时的操作：

{% asset_img 808a27dbb6fd5266fd228707a818972bd407365c.jpg pandas教程：[5]读取csv数据 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
