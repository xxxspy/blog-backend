---
title: Python教程：[7]IF语句基本用法
date: 2016-02-05 18:19:19
tags: [python]
author: mlln.cn
---
python的if语句和其他语言有些不同，它没有用括号来表示代码块，而是使用缩进，现在乍听一下你可能不太明白，用下面的例子来感受一下缩进的写法：

- if的基本语法格式看下面：第一行是条件语句，如果满足条件就会执行第二行，没有括号或者结束语句，比如endif，没有。

{% asset_img adee30dda3cc7cd9c7d80ef23b01213fb90e91e0.jpg Python教程：[7]IF语句基本用法 %}

- 假如第二行没有缩进，就会产生错误。

{% asset_img 8cf0d51349540923ac1e46559058d109b3de4962.jpg Python教程：[7]IF语句基本用法 %}

- 新手容易犯一个错误就是条件语句后面不写冒号，出现这样的错误：

{% asset_img f9589818367adab494973e6889d4b31c8701e413.jpg Python教程：[7]IF语句基本用法 %}

- 我们假如有多个条件，我们可以使用else，当条件不满足的时候执行它下面的语句块。当然else是顶个写，并且后面记得写冒号。

{% asset_img 027a45b5c9ea15ce1e3cc522b4003af33b87b28f.jpg Python教程：[7]IF语句基本用法 %}

- 如果还有更多的条件，我们可以使用elif，同样不要忘记冒号和缩进

{% asset_img dbf554ed2e738bd45301961aa38b87d6277ff9be.jpg Python教程：[7]IF语句基本用法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
