---
title: Python教程：[14]快速创建TCP服务器
date: 2016-10-23 18:05:05
tags: [python]
author: mlln.cn
---
这里我不跟大家讲什么是TCP，什么是服务器，相信大家都懂，不懂的话我也没有能力让你懂，所以我就直接上代码了，在代码中解释，然后把所有的代码呈现出现，以后你只要在这个简单的代码上进行修改就可以了。

- 首先我们引入socket的所有属性，引入时间戳函数ctime，后面要用到时间戳

{% asset_img bf487563f6246b6025f2785fe9f81a4c500fa2da.jpg Python教程：[14]快速创建TCP服务器 %}

- 设置主机地址，主机地址为空说明我们可以使用任意可以使用的地址；端口号是我随意写的，只要不超过一定的范围就可以了，你可以搜索一下端口号的范围；ADDR连接地址包括主机地址和端口号。

{% asset_img 4651a712c8fcc3ce685903189045d688d53f20c5.jpg Python教程：[14]快速创建TCP服务器 %}

- 我们使用socket方法来创建一个套接字；使用bind方法绑定到地址上；使用listen设定最多可以连接5个客户端。

{% asset_img 504ec7f9d72a605914ec2b312a34349b023bbada.jpg Python教程：[14]快速创建TCP服务器 %}

- 下面是最重要的部分，我们使用无限循环来保证随时接受链接请求，accept方法可以接受请求，并返回客户端tcpclisock和客户端地址。使用recv方法来接受数据，send方法发送数据。如果一开始接受到了数据，后来数据为空，则跳出循环。

{% asset_img d66b7e59252dd42a1bf5cb80013b5bb5c8eab8da.jpg Python教程：[14]快速创建TCP服务器 %}

- 下面是所有的代码：

- >>> from socket import *   #引入socket的所有

- >>> from time import ctime  #时间戳函数，用于实现服务器的功能

- >>> HOST=''   #主机地址

- >>> PORT=23345   #端口号

- >>> BUFSIZ=2048   #缓存区大小，单位是字节，这里设定了2K的缓冲区

- >>> 

- >>> 

- >>> ADDR=(HOST,PORT)   #链接地址

- >>> 

- >>> tcpSerSock=socket(AF_INET,SOCK_STREAM)   #创建一个TCP套接字

- >>> tcpSerSock.bind(ADDR)    #绑定地址

- >>> tcpSerSock.listen(5)    #最大连接数为5

- >>> while True:   #无限循环

- print('客户端连接。。。')   #显示文字信息

- tcpCliSock,addr=tcpSerSock.accept()          #等待接受连接

- print( '链接成功，客户端地址为：',addr)

- while True:

- data=tcpCliSock.recv(BUFSIZ)    #接收数据,BUFSIZ是缓存区大小

- if not data:   #如果data为空

- break  #则跳出循环

- tcpCliSock.send('[%s] %s'% (ctime(),data))

- >>>     tcpCliSock.close()   #关闭连接

- >>> tcpSerSock.close()   #关闭服务器

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
