---
title: pandas教程：[26]值替换
date: 2015-04-05 18:05:05
tags: [pandas]
author: mlln.cn
---
有时候我们需要将数据中的某些值替换为其他值，replace()方法就是干这个用的，不同的情况下使用replace的方法也不同，下面我们用离子来说明一下：

- 引入相关模块并创建一个Series

{% asset_img 00a82701213fb80ee7b595d035d12f2eb9389416.jpg pandas教程：[26]值替换 %}

- 具体数值的替换，方法很简单：将0替换为6
输出结果为：

{% asset_img 9a1151c2d56285354084262693ef76c6a7ef6316.jpg pandas教程：[26]值替换 %}

{% asset_img 346bd85c103853437bc173269013b07eca808868.jpg pandas教程：[26]值替换 %}

- 列表到列表的替换，这种方法经常用到，有些问卷的题目是反向计分，所以要在处理数据的时候将分数再翻转一下：
输出结果为：

{% asset_img 91ae68c6a7efce1b364f3ccdac51f3deb48f6516.jpg pandas教程：[26]值替换 %}

{% asset_img 5d212aa85edf8db1774a88630a23dd54564e7416.jpg pandas教程：[26]值替换 %}

- 还可以使用字典映射：将1替换为11，将2替换为12
输出结果为：

{% asset_img fcbbb151f3deb48f3c0d55d9f31f3a292df57816.jpg pandas教程：[26]值替换 %}

{% asset_img cbc17b380cd791231fee6073ae345982b2b78068.jpg pandas教程：[26]值替换 %}

- 以上方法同样适用于DataFrame对象
输出结果为：

{% asset_img d66b7e59252dd42a5807f5ac003b5bb5c9eab868.jpg pandas教程：[26]值替换 %}

{% asset_img 570f8c58d109b3de58db106fcfbf6c81800a4c16.jpg pandas教程：[26]值替换 %}

- 假如DataFrame中只有一列数据需要替换数值，我们可以单独操作者一列
输出结果为：

{% asset_img d56b3634349b033b288608dd16ce36d3d539bd68.jpg pandas教程：[26]值替换 %}

{% asset_img adee30dda3cc7cd91a23c0de3a01213fb80e9168.jpg pandas教程：[26]值替换 %}

- 假如有多个列进行相同的替换操作，我们可以同时选择多个列：
输出结果为：

{% asset_img 3792cb39b6003af340b42867362ac65c1038b668.jpg pandas教程：[26]值替换 %}

{% asset_img 814b07d8bc3eb135ffa343bca51ea8d3fd1f4416.jpg pandas教程：[26]值替换 %}

- 若多个列中不同的值都要替换为一个相同的值，可以使用字典的方法表示所有需要被替换的值：
输出结果为：

{% asset_img 3b6833f5e0fe99250b689d5737a85edf8db17116.jpg pandas教程：[26]值替换 %}

{% asset_img 32bb9c8ba61ea8d32d468003940a304e251f5816.jpg pandas教程：[26]值替换 %}

- 插值法同样可以用于替换数值，只要使用参数method即可

{% asset_img b74124f33a87e9504e97046b13385343faf2b4f2.jpg pandas教程：[26]值替换 %}

{% asset_img 346bd85c10385343844f70269013b07ecb8088f2.jpg pandas教程：[26]值替换 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
