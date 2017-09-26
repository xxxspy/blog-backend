---
title: python 字符串类型错误
date: 2016-02-23 18:17:03
tags: [python]
author: mlln.cn
---
今天调程序发现总出现错误TypeError: 'str' does not support the buffer interface，研究了很久才发现，错误在与python的版本不同，我们来看看如何更改。

- 这是我的源码，是不是和你的挺像？红色方框的位置出现了错误。也就是在sendto函数这里，我们发送一个字符串，但是提示我们类型错误

{% asset_img b6045da98226cffc9fd6d59ebb014a90f703eadb.jpg python 字符串类型错误 %}

- 新版本的python对字符串对象做了很大的更改，使得原先的函数产生了很大的不同，所以我们需要添加一个参数。这个问题就解决了。

{% asset_img 4651a712c8fcc3ce8812a31f9045d688d53f2088.jpg python 字符串类型错误 %}

- 但是，还有一个问题，这种方法发送的字符串发送的结果是b'hello，怎么办呢，我们使用转码函数试试。print(cs.recv(1024).decode('utf-8'))

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
