---
title: Python教程：[53]matplotlib安装错误
date: 2015-03-15 18:19:19
tags: [python]
author: mlln.cn
---
引用matplotlib包的时候出现一个问题，百度一下才知道问题再哪里，我们先来看看问题是什么。错误提示为：ImportError: matplotlib requires dateutil

- 我使用二进制安装文件来安装这个包，安装过程没有出现任何问题

{% asset_img 310f3b1f95cad1c855686ebd7d3e6709c83d511e.jpg Python教程：[53]matplotlib安装错误 %}

- 在我使用【import matplotlib】引入该模块的时候，出现了这个错误：

- Traceback (most recent call last):

-   File "<pyshell#0>", line 1, in <module>

-     import matplotlib

-   File "D:\Python27\lib\site-packages\matplotlib\__init__.py", line 111, in <module>

-     raise ImportError("matplotlib requires dateutil")

- ImportError: matplotlib requires dateutil

- 其实就是引入matplotlib模块需要用到dateutil模块，那么我们可以通过easy_install命令来安装：假如你没用过easy_install ，你可以看这篇文章http://jingyan.baidu.com/article/2a1383284db4e2074a134f2c.html假如你没有安装setuptools,我们可以看这篇文章进行安装：http://jingyan.baidu.com/article/b907e627dd80df46e7891c2c.html

- 打开cmd窗口

{% asset_img b8405490f603738d947290b8b11bb051f819ec35.jpg Python教程：[53]matplotlib安装错误 %}

- 输入这个，找不到这个模块

{% asset_img b25aae51f8198618728e721e48ed2e738ad4e624.jpg Python教程：[53]matplotlib安装错误 %}

- 我们得用：easy_install python-dateutil

{% asset_img 8759287adab44aed6876227eb11c8701a18bfb35.jpg Python教程：[53]matplotlib安装错误 %}

{% asset_img 8a95ad1c8701a18bccd38ed59c2f07082838fe35.jpg Python教程：[53]matplotlib安装错误 %}

- 安装好了以后，我们就可以正确引用matplotlib

{% asset_img fc5e5f34970a304ec85d3c60d3c8a786c8175cea.jpg Python教程：[53]matplotlib安装错误 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
