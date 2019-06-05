---
title: spss如何筛选部分case
date: 2016-05-11 18:23:15
tags: [spss]
author: mlln.cn
---
有时候我们需要对部分数据进行处理，这时候需要对满足条件的数据进行筛选，选择出符合要求的数据，select cases命令就是用来处理这种问题的。
方法/步骤


- 打开spss ，执行file --open--data，打开数据文件

{% asset_img 95eef01f3a292df55ef04098bc315c6034a87308.jpg spss如何筛选部分case %}

- 在菜单栏上执行：data-select cases，打开case选择对话框

{% asset_img f11f3a292df5e0fe262b658c5c6034a85edf7208.jpg spss如何筛选部分case %}

- 我们看到这里有很多删选的方法，我们一一进行尝试，首先根据条件筛选，选择if condition is satisfied，点击if按钮，打开设置

{% asset_img e1fe9925bc315c60f6a687628db1cb1349547708.jpg spss如何筛选部分case %}

{% asset_img d009b3de9c82d1580397b53c800a19d8bc3e4222.jpg spss如何筛选部分case %}

- 假如我们要筛选id小于45的case，那么我们先选择id，点击添加按钮，然后输入公式条件id<45

{% asset_img 5fdf8db1cb134954ce2d04e9564e9258d1094a08.jpg spss如何筛选部分case %}

- 条件输入以后，点击continue按钮。这样就完成了按照条件筛选

- 、

{% asset_img d009b3de9c82d15803b1b53c800a19d8bc3e4208.jpg spss如何筛选部分case %}

- 假如我们要使用随机选择case的方法，我们就选择random sample of cases，然后点击sample

{% asset_img 4034970a304e251f4be20875a786c9177f3e5322.jpg spss如何筛选部分case %}

- 我们看到这个对话框有两个选项，第一个选择是选择百分比，也就是从所有的case中选择百分之多少的case；第二个选项是从前多少个case中选择多少个case

{% asset_img 810a19d8bc3eb135e6f45b36a61ea8d3fd1f4408.jpg spss如何筛选部分case %}

- 回到select cases 对话框，勾选基于时间或者case范围，看到下面这个对话框，输入case的范围是从第五十个到第100个，点击continue

{% asset_img 241f95cad1c8a786283fa6836709c93d70cf5022.jpg spss如何筛选部分case %}

- 最后一个filter variables，也就是过滤变量，这个选项的功能是如果变量中有缺省值，那么这个case就被删除或者排除在外了。

{% asset_img a686c9177f3e67092d15a9723bc79f3df8dc5522.jpg spss如何筛选部分case %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
