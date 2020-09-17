
---

title: SPSS的Process插件下载和安装
date: 2019-08-21 12:44:03
tags: [spss, process]
---


SPSS的Process插件由 Andrew F. Hayes, Ph.D 开发, 大家可以免费使用。Process的主要用途就是进行一些路径分析, 比如中介效应/调节效应的检验, 不过, 其实没有这个插件, 我们也能进行这些分析, 有了Process插件的好处就是我们不必重复劳动, 而且提高了工作效率。

今天这篇文章我主要介绍一下Process的下载和安装方法。

<!-- more -->


### Process有两种使用方法

第一种方法是使用作者提供的界面, 你需要安装这个插件才能使用界面; 第二种方法并不需要安装, 只要在syntax中引用process的源码即可, 但是你只能自己写syntax, 下面我们分别介绍两种方法。

### 下载

从下面的网址中下载插件的压缩包:

下载地址:  http://www.afhayes.com/public/processv34.zip

或者从网盘下载: https://pan.baidu.com/s/1SgkgeDq8p_ybeNcLhJQrUw 
(提取码：apx1)

你会得到一个压缩包, 解压以后得到如下文件:

<img src="imgs/01.png">

打开这个文件夹, 我们看到这些文件:

<img src="imgs/02.png">

### 第一种方法: 安装界面

打开spss软件, 然后来到这个菜单(中文版的spss可以按照菜单位置来定位):

<img src="imgs/04.png">

在打开的对话框中选择文件夹`custom dialog builder file`下面的这个文件`process.spd`:

<img src="imgs/05.png">

在打开的这个界面中, 选择install, 然后点"yes":

<img src="imgs/06.png">

接下来基本结束了, 安装成功!

### 无需安装, 直接引用process源码


其实, 如果你熟悉spss的syntax, 你可以直接使用process这个命令, 方法是:

首先你需要新建一个syntax文件, 然后再文件中写入这样一行代码, 它就是引用了`process.sps`, 注意后缀名是sps。

```spss
INCLUDE 'D:\PROCESS v3.4 for SPSS\process.sps'.
```

然后, 你可以使用process命令来进行数据分析, 比如下面的代码就是做了一个简单的中介效应分析:

```
PROCESS 
  y=Q16_2
  /x=Q18_1
  /m=Q20_1
  /plot=1
  /covcoeff=1
  /decimals=F10.4
  /boot=5000
  /conf=95
  /model=4.

```

### 怎么打开Process对话框


当你安装好了process的界面到spss以后, 你可以在这里找到process的入口:

<img src="imgs/07.png">

### 两种方法的联系

其实使用Process的对话框和使用Process的syntax命令本质都是在调用process命令, 所以我们可以对比一下界面和命令的联系在那里, 也就是界面上的各种配置都决定了命令的什么参数, 这样可以帮助我们使用syntax, 因为syntax的效率更高!

<img src="imgs/08.png">

<img src="imgs/09.png">

### 关于Process插件如何进行分析

我会在之后的文章中以案例的方式给大家分享。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](SPSS的Process插件下载和安装.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
