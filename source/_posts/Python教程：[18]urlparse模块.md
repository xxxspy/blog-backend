---
title: Python教程：[18]urlparse模块
date: 2015-01-11 18:03:23
tags: [python]
author: mlln.cn
---
使用urlparse模块可以对url进行分析，最主要的操作就是拆分和合并url的各个部件，那么url有哪些部件呢？下图列出了所有的部件。你可能不太理解，不要着急，我们在例子中看看每个部分都代表着什么。

- 引入urlparse模块，这里只引入了urlparse方法，如果你想要用所有的方法，你需要import urlparse

{% asset_img d7c9ca3f8794a4c23abdb8070cf41bd5ac6e39c4.jpg Python教程：[18]urlparse模块 %}

- 我们将下面的url地址进行拆解，将拆解的结果存放到parsed中

{% asset_img f7426d8da9773912cd4fda4dfa198618367ae276.jpg Python教程：[18]urlparse模块 %}

- 之后，我们通过parsed的各个属性来访问不同的部分

{% asset_img d5462bfae6cd7b89c4f265af0d2442a7d8330ec4.jpg Python教程：[18]urlparse模块 %}

- 我们看最后输出的结果：通过这样的方法我们可以快速的对url进行操作

{% asset_img 834344afa40f4bfb934ec178014f78f0f63618c4.jpg Python教程：[18]urlparse模块 %}

- 所有的源码都写在下面：

- from urlparse import urlparse

- parsed = urlparse('url地址')

- print 'scheme  :'+ parsed.scheme   #网络协议

- print 'netloc  :'+ parsed.netloc   #服务器位置（也可呢能有用户信息）

- print 'path    :'+ parsed.path     #网页文件在服务器中存放的位置

- print 'params  :'+ parsed.params   #可选参数

- print 'query   :'+ parsed.query    #连接符（&）连接键值对

- print 'fragment:'+ parsed.fragment #拆分文档中的特殊猫

- print 'username:'+ parsed.username #用户名

- print 'password:'+ parsed.password #密码

- print 'hostname:'+ parsed.hostname #服务器名称或者地址

- print 'port    :', parsed.port     #端口（默认是80

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
