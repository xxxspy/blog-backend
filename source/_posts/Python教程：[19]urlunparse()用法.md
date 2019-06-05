---
title: Python教程：[19]urlunparse()用法
date: 2015-06-11 18:15:05
tags: [python]
author: mlln.cn
---
前一篇文章我们讲了urlparse函数，我在这里补充一点，在python的新版本中，urlparse模块已经不能用了，想要使用rulparse函数只能是在低版本中使用，我这里示范的代码是在python2.7中测试的，这也是目前比较稳定的版本。其实从前面的文章中看到urlparse函数，你就知道urlunparse函数的用法，下面是具体的例子。

- 先引入两个方法，urlparse和urlunparse

{% asset_img 29752a9b033b5bb51e9f4ad334d3d539b600bc10.jpg Python教程：[19]urlunparse()用法 %}

- 我们将一个url分割成不同的部分，用的是urlparse，然后将不同的部分在合并成url，用的是urlunparse方法。

{% asset_img 7787b9efce1b9d16f269f04cf1deb48f8c546435.jpg Python教程：[19]urlunparse()用法 %}

- 我们看到分割后的parsed，他被分成不同的部分，这个上一篇文章就讲过

{% asset_img d478a8003af33a8737256a37c45c10385343b510.jpg Python教程：[19]urlunparse()用法 %}

- 使用urlparse分割过的可以用urlunparse来合并，重新形成url

{% asset_img 3bc6f750352ac65cf14d0c5ef9f2b21193138a10.jpg Python教程：[19]urlunparse()用法 %}

- 所有的代码如下：

- from urlparse import urlparse

- from urlparse import urlunparse

- parsed=urlparse('http://user:pass@NetLoc:80/path;parameters?query=argument#fragment')

- url=urlunparse(parsed)

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
