---
title: Python教程：[54]matplotlib引用错误
date: 2015-10-23 18:23:15
tags: [python]
author: mlln.cn
---
安装好了matplotlib，但是引入的时候出现问题，无法引用，提示引用错误：ImportError: matplotlib requires pyparsing。然后通过安装pyparsing模块解决了这个问题，为了让大家都解决这个问题，我把我遇到问题描述在这里：

- 首先，我用的是exe文件装的matplotlib模块：

{% asset_img 54baacfb43166d2221538a0e442309f79152d2c1.jpg Python教程：[54]matplotlib引用错误 %}

- 安装过程没有任何提示错误，但是引用的时候出现问题：提示错误

- Traceback (most recent call last):

-   File "<pyshell#0>", line 1, in <module>

-     import matplotlib

-   File "D:\Python27\lib\site-packages\matplotlib\__init__.py", line 125, in <module>

-     raise ImportError("matplotlib requires pyparsing")

- ImportError: matplotlib requires pyparsing

- 解决问题的方法是安装pyparsing，用到setuptools，如果你没有安装setuptools，你可以在这里安装：http://jingyan.baidu.com/article/b907e627dd80df46e7891c2c.html

- 接着我们打开命令窗口，输入命令easy_install pyparsing

{% asset_img fc5e5f34970a304ec9993f60d3c8a786c8175cb6.jpg Python教程：[54]matplotlib引用错误 %}

- 接着，我们引入matplotlib，就成功了

{% asset_img c9bdddcec3fdfc03902a7c22d63f8794a5c2269e.jpg Python教程：[54]matplotlib引用错误 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
