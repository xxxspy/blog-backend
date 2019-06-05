---
title: Python教程：[40]列表与字符串相互转换
date: 2015-09-23 18:11:23
tags: [python]
author: mlln.cn
---
以前玩vb没有体会到python这么强大的功能，列表与字符串可以直接的相互转换，非常方便，我们就好好的来享受一把吧！

- 首先我们来初始化一个list（列表）

{% asset_img 11794d43fbf2b211f7135056c88065380cd78eae.jpg Python教程：[40]列表与字符串相互转换 %}

- 使用join方法来转换列表，将列表转换成字符串，注意join是字符串的方法，前面必须是字符串，我用的是“;”,也就是分号，然后连接成的字符串就是用分号来进行元素的分割的。

{% asset_img 9252ae7eca80653864d7710b95dda144ad3482ae.jpg Python教程：[40]列表与字符串相互转换 %}

- 我们再试试其他的字符串，你感受一下

{% asset_img 4bd1e803738da97731d76c33b251f8198718e3eb.jpg Python教程：[40]列表与字符串相互转换 %}

- 当然，我们还有能力将字符串转换回去，看下面，设置叹号为分隔符，然后对字符串进行切割，得到列表

{% asset_img a8362712b31bb051f3dc5930347adab44bede0eb.jpg Python教程：[40]列表与字符串相互转换 %}

- split函数还有第二个参数，你猜猜这是干什么用的，对了，它指的是分割的次数

{% asset_img b110e6198618367ad47195c52c738bd4b21ce5eb.jpg Python教程：[40]列表与字符串相互转换 %}

- 假如我们分割两次呢，你看看效果。

{% asset_img 30ecd5ef76094b36d9afcef5a1cc7cd98d109dae.jpg Python教程：[40]列表与字符串相互转换 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
