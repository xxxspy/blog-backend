---
title: psychopy教程1-入门认识psychopy
date: 2017-09-29 16:56:24
tags: [psychopy, eprime/e-prime]
---

本篇文章开始正式进入psychopy的教程，先给大家介绍一下psychopy软件的两个基本视图，然后在不同的视图下实现同一个程序。如果你还没有安装psychopy，在[这里](http://mlln.cn/2017/09/27/psychopy%E4%B8%AD%E6%96%87%E7%89%88%E5%AE%89%E8%A3%85-%E9%99%84%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80/)可以下载和安装。

### 两种视图

Psychopy本质上是一个桌面软件，有两个视图：Builder视图和Coder视图，顾名思义，Builder视图基于一个友好的用户界面，用户不需要专业的编程知识，只需要鼠标点击和拖拽就能完成一个简单的实验程序；Coder视图只提供了一个代码编辑器，你需要编写代码来完成一个实验程序。两个视图各有优劣，因为我是开发软件的，所以我个人的建议是从一开始就使用Coder编写你的实验程序，一方面，编程能力是这个时代对每个人的基本要求，另一方面，Coder的工作效率非常高，尤其是当你需要经常编写实验程序的时候。如果你有编程经验，学习使用Builder和Coder的时间成本几乎是一样的。但是，如果你并没用编程经验，并且以后没有计划再次使用psychopy，Builder也许是你唯一的选择。

<!--more-->
##### coder视图
{% asset_img coder.jpg coder视图 %}
##### builder视图
{% asset_img builder.jpg builder视图 %}

### Builder, Hello World

在学习一门编程语言的第一件事就是写一个程序打印出"Hello World"， 现在我们同样使用Builder来建立一个刺激呈现程序，程序很简单，就是呈现在屏幕上一个"Hello World"。

下面的教程中，你不必关心你不懂的按钮/选项等, 先做出来一个能运行的程序来给自己一点成就感。这才是"Hello World"的意义。

- 首先点击文本控件，打开文本控件设置对话框

{% asset_img builder01.jpg builder视图 %}

- 然后设置Text内容为"Hello World"， 其他设置不用更改，保持默认值

{% asset_img builder02.jpg builder视图 %}

- 点击确定即可添加一个文本

{% asset_img builder03.jpg builder视图 %}

- 最后点击运行按钮，开始试验

{% asset_img builder04.jpg builder视图 %}

- 你会在屏幕上看到这样的刺激

{% asset_img builder05.jpg builder视图 %}


### Coder, Hello World

如果你没有Python的编程经验，建议你跳过这部分，除非你非常感兴趣。其实Python程序非常简单，是接触到的这么多编程语言里，最简单的。我几乎向所有从事科学研究的朋友推荐Python, 而实际他们也采纳了我的建议。

- 打开Coder视图，把以下代码粘贴到编辑框里。

```python
#encoding:utf8
# 引入需要用到的模块
from psychopy import visual, core

# 创建一个刺激呈现窗口，它就是所有刺激的展示舞台
win = visual.Window()

# 创建一个文本刺激，但是它还没有显示在舞台上
msg1 = visual.TextStim(win, text=u"Hello world!")  # default position = centered

# 把文本绘制到隐藏的缓存中（我们还没看到文本呢1)
msg1.draw()

# 调用win的flip方法，会将所有缓存区绘制的刺激展现到舞台
win.flip()

# 等待3秒，否则你都看不到文本，实验就结束了
core.wait(3)
win.close()
```

{% asset_img coder01.jpg coder视图 %}

- 同样点击运行按钮，你会看到类似的刺激

### 总结

好了，通过这篇文章，那你大概就了解了psychopy的基本界面和使用方法，接下来我会持续更新这个系列的教程，大家可以关注我的博客[DataScience](http://mlln.cn)或者[心理学技术博客](http://psychopy.com)如果大家有什么问题可以直接评论留言，或者加入心理学技术群：475179613，申请信息注明psychopy。