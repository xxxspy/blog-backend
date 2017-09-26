---
title: Django教程：[5]URLpattern的语法
date: 2015-03-01 18:23:03
tags: [django]
author: mlln.cn
---
前一篇文章我们使用Django制作了第一个网页，针对其中的一些问题，我们补充一点知识，这是关于urls.py文件中的URLpattern的，

- 我们在写url的时候实际上写的是正则表达式，尖号（^）和美元符号（$）都是正则表达式符号，分别表示字符串的开头和结尾。上面添加的url（'^hello/$'）表示url以hello/开头，也以hello/结尾，只有满足这两个条件的url才可以调用hello函数。

{% asset_img fab3ac119313b07ef63b6f720ed7912396dd8c82.jpg Django教程：[5]URLpattern的语法 %}

- 假如我们写成 ^hello/ ，没有$结尾，表示任何以hello/开头的url都是可以调用hello方法的，比如浏览器中访问http://127.0.0.1:8001/hello/dfdf也可以调用hello方法。

- 假如我们写成 hello/$，没有尖号（^）开头，那么任何以hello/结尾的url都可以调用hello方法。比如http://127.0.0.1:8001/dfdfdf/hello/

- 那么，只写 hello/ ，没有尖号和美元符号，那么只要url中包含字符 hello/都可以调用方法 hello 。

- 学习python的正则表达式可以帮助你更好的理解这些内容，下面的参考资料里有python的正则表达式的学习教程。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
