---
title: SPSS实例：[10]分割数据的方法
date: 2016-07-23 18:05:19
tags: [spss]
author: mlln.cn
---
我手上有一批数据，我们要分别计算本科生和专科生的性别、年级、年龄等变量的频率，我们可以将数据按照学历来分组，然后再进行描述性统计就能得到两个平行结果，一个是本科的一个是专科的。当然，如果我们做方差分析、回归分析，先将数据分组也一样可以得到不同人群的同样的结果。我们来看看具体的方法：

- 首先我们打开数据，在菜单中执行：data--splitfile，进行数据分割

{% asset_img 0d729944ebf81a4c9674bcdbd52a6059252da61b.jpg SPSS实例：[10]分割数据的方法 %}

- 然后我们选择compare groups，这样可以对比两组人群（本科和专科）

{% asset_img 4a77b2af2edda3cc8f6ce83203e93901203f92dd.jpg SPSS实例：[10]分割数据的方法 %}

- 将学历这个变量发那个如分组列表里

{% asset_img a28d62d98d1001e9cfb4441dba0e7bec55e797dd.jpg SPSS实例：[10]分割数据的方法 %}

- 点击ok，运行分组命令

{% asset_img 00a82701213fb80e825931c534d12f2eb83894dd.jpg SPSS实例：[10]分割数据的方法 %}

- 接着我们做一个描述性统计来看看结果

{% asset_img c8ab0bce36d3d539637b5fd13887e950352ab01b.jpg SPSS实例：[10]分割数据的方法 %}

- 这是是得到的结果，我们看到数据结果分为两行，第一行是本科生，第二行是专科生。

{% asset_img fab3ac119313b07e2bfb001a0ed7912397dd8c1b.jpg SPSS实例：[10]分割数据的方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
