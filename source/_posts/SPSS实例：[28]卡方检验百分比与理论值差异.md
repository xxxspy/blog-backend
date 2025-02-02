---
title: SPSS实例：[28]卡方检验百分比与理论值差异
date: 2015-04-19 18:05:03
tags: [spss]
author: mlln.cn
---
我们有一个研究检验某种疗法的有效性，统计了实施前后的人数，我们想要比较实施前和实施后人数是否有差异，怎么比较？有两种数据结构，得使用不同的方法，下面将要介绍的是这种数据没有原始数据，只有计数数据，如下图。变量9表示人数，实施前后表示该方法实施前用0表示，实施后用1表示。另外一种数据结构是你有原始数据，而不是计数数据，你可以参考我以前的文章：http://jingyan.baidu.com/article/d8072ac4587f6dec95cefd9a.html

- 首先要给数据加权，我们在data菜单下，选择case加权

{% asset_img c71d0e385343fbf213af316fb27eca8064388fb8.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 将变量9放入频数变量框，点击【ok】，完成加权（如果有原始数据，则不需要加权）

{% asset_img 29790130e924b899f378ee746c061d950b7bf6f3.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 接着我们来做卡方检验，在菜单栏上执行：分析--非参检验--遗留选项--卡方检验

{% asset_img 906289dda144ad34f23c10cbd2a20cf430ad85b8.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 将实施前后变量放入检验变量框。

{% asset_img 0db52fadcbef7609f9880ed32cdda3cc7dd99eb8.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 这里有一个问题，如果你的数据有一个单元格频数小于5，你得使用精确卡方检验，需要点击【exact】进行设置

{% asset_img f99dcf00baa1cd117002e46cbb12c8fcc2ce2d82.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 勾选这个选项，点击继续

{% asset_img c9bdddcec3fdfc039bcc75f4d63f8794a5c22682.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 接着设置这里，我们可以检验不同组人数是否相同，使用【所有分类相同】；

{% asset_img 27d647ee3d6d55fbc02fe06a6f224f4a21a4dd56.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 也可以自己设定频数，比如我设定为2和6，当然今天我们只讲上面的【所有分类相同】的情况。

{% asset_img 1cd4147b02087bf46a59c1a5f0d3572c10dfcf82.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 这里就是检验结果了，sig值大于0.05，结果不显著，说明两组之间没有差异。

{% asset_img 30ecd5ef76094b361f118ca1a1cc7cd98c109db8.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

- 如果你用的是精确检验就会看大有一个精确sig值

{% asset_img 91138622720e0cf3abe7dfb70846f21fbe09aa2f.jpg SPSS实例：[28]卡方检验百分比与理论值差异 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
