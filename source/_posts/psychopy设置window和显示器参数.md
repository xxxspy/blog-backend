---
title: psychopy设置window和显示器参数
date: 2018-03-09 13:10:55
tags: psychopy
---

有时候我们会发现, 做好的程序放到不同的电脑上会有不同的显示效果, 图形的位置和大小会发生变化, 这是因为我们不懂得psychopy对图形的尺寸和位置的控制方式. 通常来说, 换一个电脑你都要设置显示器和窗口属性, 以便刺激能够正确显示.

psychopy的windows(窗口)和monitor(显示器)的设置很重要, 直接关系到你的整个实验的各种刺激尺寸(size). 下面我们用图文的方式介绍一下需要设置的参数以及如何设置他们.

<!--more-->

### 显示器设置

{% asset_img monitorCenter.png 显示器设置中心  %}


- 打开你的显示器设置中心


{% asset_img setMonitor.png 显示器设置中心  %}


- 你需要设置三个参数
    - Screen Distance(cm): 被试眼睛到显示器距离, 单位是厘米
    - Size(pixels): 显示器的像素, 单位是像素
    - Screen Width(cm): 显示器的宽度, 单位是厘米.

设置这三个参数的好处是, 你可以使用任意单位去控制刺激大小, 比如可以用视角(deg).

- 注意设置完以后, 点击保存

### 窗口设置


{% asset_img experiment.png %}

下面我们设置screen/屏幕属性, 可以在`Experiment Settings`中设置. 如上图.

- 首先你可以设置是否以全屏运行程序, 如果不是全屏, 你需要手动填写窗口的大小(单位是像素). 我通常的做法是在程序开发阶段都以窗口形式运行, 当在正式实验阶段就以全屏形式运行.

{% asset_img setScreen.png %}

- color是屏幕的背景色, color space是色域, 通常不用管, 你不是计算机科学家, RGB都够用.

- units是单位, 通常使用norm

其他属性我们暂时不讲, 这篇文章主要是设置尺寸参数以便让刺激大小可控.


