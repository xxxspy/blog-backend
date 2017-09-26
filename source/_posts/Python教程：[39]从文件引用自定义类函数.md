---
title: Python教程：[39]从文件引用自定义类函数
date: 2016-05-19 18:03:23
tags: [python]
author: mlln.cn
---
python可以将自己编写的类放在py文件中，然后由其他程序调用，很多人都不知道这个该怎么调用，都来问我，这里就给大家讲一下如何在shell中从文件引用自定义类和函数，希望对大家有帮助，下面是具体的过程：

- 第一步将你编写的文件声明编码类型

{% asset_img e49cf91190ef76c6a117ab339f16fdfaae5167a5.jpg Python教程：[39]从文件引用自定义类函数 %}

- 然后将你编写的文件保存为py格式的文件，看好你保存的路径，后面会用到这个路径

{% asset_img 4e83cb628535e5dde4e9f5c774c6a7efcf1b62a5.jpg Python教程：[39]从文件引用自定义类函数 %}

- 引入sys模块，然后向path中添加路径，也就是上一步提到的途径

{% asset_img c9d4cf43ad4bd1131b3de72a58afa40f4afb05f2.jpg Python教程：[39]从文件引用自定义类函数 %}

- 引用的方法是from 文件名 import 类名

{% asset_img cf5a8316fdfaaf51f826d1a78e5494eef11f7aa5.jpg Python教程：[39]从文件引用自定义类函数 %}

- 调用的方法是：这样我们就建立了一个列content

{% asset_img fcbbb151f3deb48f81acf1c6f21f3a292cf578a5.jpg Python教程：[39]从文件引用自定义类函数 %}

- 调用自定义的函数也是同样的方法。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
