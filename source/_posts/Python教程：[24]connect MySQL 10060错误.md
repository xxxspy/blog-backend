---
title: Python教程：[24]connect MySQL 10060错误
date: 2015-10-05 18:17:23
tags: [python,mysql]
author: mlln.cn
---
今天使用python链接mysql数据的时候发现总是提示错误“Can't connect to MySQL server (10060)”经过我反复尝试，发现错误在于python链接数据库的时间过长，链接失效了，所以需要重新连接。我们可以判断返回的错误自动进行连接。不过并不是所有的10060错误都是这个原因。我也罗列了各种问题和解决的方法。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
