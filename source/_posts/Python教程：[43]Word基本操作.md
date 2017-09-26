---
title: Python教程：[43]Word基本操作
date: 2016-04-01 18:15:11
tags: [python]
author: mlln.cn
---
使用python操作Word用到了win32com模块，我们现在就要介绍一下python对Word的基本操作，文章涉及到如何与Word程序建立连接、如果与Word文档建立连接的，以及对Word文档的基本操作。

- 首先，我们必须要引入win32com，已经Dispatch和constants两个常用的库

{% asset_img 7ac880510fb30f24b3470f0cca95d143ac4b03a5.jpg Python教程：[43]Word基本操作 %}

- 与Word建立连接，这时候如果你已经打开了一个Word，则直接与Word程序建立连接，如果没有打开，则它会打开Word。如果已经开启了一个Word，你可以使用DispatchEx代替下面的Dispatch

{% asset_img ae8267310a55b319ee70617a41a98226cefc17f0.jpg Python教程：[43]Word基本操作 %}

- 设置Word的可见性visible，默认情况下，你看不到Word程序；然后设置Word的警告信息是否出现，默认也是不出现，这样你在使用python控制Word的时候不会弹出Word的警告信息。

{% asset_img f677b1c379310a55b7f83dfbb54543a9832610a5.jpg Python教程：[43]Word基本操作 %}

- 新建一个Word文档用add（），假如你只想打开一个已经存在的Word，你是用下面红色的代码（去掉注释符号#）

{% asset_img a6aed01b9d16fdfa36a325e1b68f8c5495ee7bb7.jpg Python教程：[43]Word基本操作 %}

- 获取已经打开的文档的数目，从下面我们看到我们只打开了一个Word文档

{% asset_img 8759287adab44aed37925debb11c8701a08bfba6.jpg Python教程：[43]Word基本操作 %}

- 想要获取第一个文档的句柄，我们使用Documents集合

{% asset_img 2cb4fefe9925bc31f892e2975cdf8db1ca1370b7.jpg Python教程：[43]Word基本操作 %}

- 假如想要激活特定的文档，我们使用activate()方法，可以其后的操作都在该文档下执行。

{% asset_img 263e802f070828383cd13f1bba99a9014d08f1a6.jpg Python教程：[43]Word基本操作 %}

- 我们还可以打印文档，使用printout方法。

{% asset_img 064936381f30e9249d787f3e4e086e061c95f7a6.jpg Python教程：[43]Word基本操作 %}

- 保存Word，可以使用另存为（saveas）方法或者使用保存（save）方法
  

{% asset_img 5d212aa85edf8db16e1f906b0b23dd54564e7449.jpg Python教程：[43]Word基本操作 %}

{% asset_img d002b34bd11373f0771a8390a60f4bfbfbed045d.jpg Python教程：[43]Word基本操作 %}

- 最后要学的就是Word的退出，使用python控制Word一定要注意退出，否则程序运行越来越慢，尤其是在多次循环的时候。

{% asset_img b94f65ec54e736d1a842630799504fc2d5626929.jpg Python教程：[43]Word基本操作 %}

- 下一篇文章我们讲如何使用python编辑Word中documents对象下的其他子对象。以后python操作Word的文章都发表在系列文章《python操作Word》下，下面的参考资料里有它的链接地址。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
