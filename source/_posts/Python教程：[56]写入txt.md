---
title: Python教程：[56]写入txt
date: 2016-02-15 18:23:03
tags: [python]
author: mlln.cn
---
今天写一个系列，记录一下如何用python来操作txt文件，包括写入txt、读取txt等，我们今天作为入门先来看看比较简单的创建和写入txt，下面来看看具体的例子：

- 使用open方法打开一个txt文件，句柄保存在f中。注意第二个参数w，表明是可写模式，只有这种模式你才可以写入文字。第一个参数大家都知道，就是文件路径，如果文件不存在，那么会自动创建一个该目录下的txt文件。

{% asset_img c9bdddcec3fdfc03a129af38d63f8794a5c22699.jpg Python教程：[56]写入txt %}

{% asset_img d7c9ca3f8794a4c24572abab0cf41bd5ac6e3999.jpg Python教程：[56]写入txt %}

- 写入文字，用write

{% asset_img bd7faf3533fa828bb02ed263ff1f4134960a5ae5.jpg Python教程：[56]写入txt %}

- 如果你一次有多行要写入，你可以用一个列表作为参数：

{% asset_img fd428c45d688d43fb2c4de727f1ed21b0ff43b85.jpg Python教程：[56]写入txt %}

- 如果写入完毕，我们需要关闭文件，用到的close方法。

{% asset_img 1cd4147b02087bf483e71869f0d3572c10dfcfec.jpg Python教程：[56]写入txt %}

- 最后看一下，已经写入到tt记事本了。

{% asset_img dc854fda81cb39dbf79d2bd6d2160924aa183095.jpg Python教程：[56]写入txt %}

- open(path,'w')：w模式下，写入内容会覆盖掉原来的内容，所以我们还有另一个模式叫做追加模式，就是a模式。下一篇介绍。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
