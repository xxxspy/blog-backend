---
title: Python教程：[17]UDP客户端程序
date: 2015-06-15 18:19:05
tags: [python]
author: mlln.cn
---
python可以快速的写成一个udp客户端程序，前面的文章中我们介绍了如何写udp服务器，服务器其实和客户端的程序时非常类似的，你看了下面的代码就知道了。

- 先引入socket模块

{% asset_img 9e7ce6dcd100baa195843e974510b912c8fc2e36.jpg Python教程：[17]UDP客户端程序 %}

- 设置几个参数：host主机地址，Port端口，bufsiz缓存大小

{% asset_img e1bf8725bc315c601b4e12c38fb1cb1348547787.jpg Python教程：[17]UDP客户端程序 %}

- 创建一个udp套接字类型，如图所示，关键参数是第二个SOCK_DGRAM

{% asset_img c28fddfdfc039245b71d98238594a4c27d1e2536.jpg Python教程：[17]UDP客户端程序 %}

- 下面的代码用于向服务器发送数据，并接受服务器传来的数据

{% asset_img 9319cf09b3de9c82eabe80a36e81800a18d84387.jpg Python教程：[17]UDP客户端程序 %}

- 下面是完整的代码。

- from socket import *

- host='localhost'  #本地服务器地址

- port=12345  #客户端端口(确保和服务器的端口一致

- bufsiz=2048 #缓存大小

- addc=(host, port) #地址+端口

- udpclisock=socket(AF_INET,SOCK_DGRAM)  #创建UDP的套接字类型。

- while True:

-     udpclisock.sendto(b'hello', addc)

-     data,adds=udpclisock.recvfrom(bufsiz)

-     if not data:

-         break

-     print(data)

- udpclisock.close()

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
