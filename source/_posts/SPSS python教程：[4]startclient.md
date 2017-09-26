---
title: SPSS python教程：[4]startclient
date: 2015-07-03 18:03:15
tags: [python,spss]
author: mlln.cn
---
使用python控制spss的时候，我们必须在使用spss的任何功能前，先启动spss，这就是用到了StartClient方法。假如我们完成了所有spss的工作，这时候我们就可以使用StopClient方法来结束spss进程。下面看一个例子。

- 首先我们在syntax编辑窗口中运行python，首先应该想到使用BEGIN PROGRAM.和END PROGRAM.来将python代码包括起来。

{% asset_img 42e89c26cffc1e178d6963a64890f603728de910.jpg SPSS python教程：[4]startclient %}

- 然后引入SpssClient模块，这样才能使用它的StartClient方法

{% asset_img ac754782b2b7d0a2786eed0ac9ef76094a369a47.jpg SPSS python教程：[4]startclient %}

- 我们启动spss客户端的方法就是这样了，记住，通常使用完spss以后，要通过StopClient方法来关闭它。

{% asset_img e78c65899e510fb3e5bb9e00db33c895d0430c4c.jpg SPSS python教程：[4]startclient %}

- 真正实现功能的是这两句代码，先不用管它什么意思

{% asset_img 73ca5910b912c8fc0e641f5afe039245d7882157.jpg SPSS python教程：[4]startclient %}

- 运行结果是输出了当前的工作文件夹：

{% asset_img c28fddfdfc039245073608988594a4c27c1e2563.jpg SPSS python教程：[4]startclient %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
