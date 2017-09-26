---
title: Python教程：[27]字符串时间转换成时间戳
date: 2016-08-19 18:17:05
tags: [python]
author: mlln.cn
---
我们使用time模块来实现数据格式的转换，假如我想要读取现在的时间，我们得到的是一个时间戳，那么如何转换格式，得到你能看懂的时间呢，下面的代码可以帮助你。

- 引入时间模块

{% asset_img 7d98931001e93901ec4a372b79ec54e736d19618.jpg Python教程：[27]字符串时间转换成时间戳 %}

- 使用time.time方法可以生成时间戳，这个时间戳是自1970年以后经过的秒数，精确到小数后3位，也就是微秒。

{% asset_img 2e6fa7389b504fc203170a10e7dde71190ef6d18.jpg Python教程：[27]字符串时间转换成时间戳 %}

- 我们把时间戳赋值给t，然后使用localtime函数来转换成可以读懂的格式时间对象

{% asset_img 6391e903918fa0ec883dde18249759ee3c6ddbea.jpg Python教程：[27]字符串时间转换成时间戳 %}

- 我们设置一下时间格式，然后使用strftime函数来转换，得到字符串。关于时间的格式，下面有详细的讲。

{% asset_img 5d212aa85edf8db12466c6710b23dd54564e7418.jpg Python教程：[27]字符串时间转换成时间戳 %}

- 你怎么知道哪个字符代表的是年月还是日，下面的表格可以告诉你。

{% asset_img c2bce2039245d688ca6117b1a6c27d1ed21b2400.jpg Python教程：[27]字符串时间转换成时间戳 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
