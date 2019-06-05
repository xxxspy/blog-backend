---
title: Python教程：[58]写入并关闭txt
date: 2015-09-05 18:03:01
tags: [python]
author: mlln.cn
---
上面介绍的方法写入txt，需要三个过程：open-write-close，实际上我们大可不必这么麻烦，我们可以用一句话就能完成这个过程：

- 我们来用一句代码完成这三句代码的工作：

{% asset_img 9dc3cf58ccbf6c818e756568be3eb13532fa40b4.jpg Python教程：[58]写入并关闭txt %}

- 就只额这样一句，它写入内容后，自动关闭

{% asset_img d019d2bf6c81800a16a7c08eb33533fa838b47b4.jpg Python教程：[58]写入并关闭txt %}

- 看一下内容

{% asset_img 8cf0d51349540923d8362afe9058d109b2de4997.jpg Python教程：[58]写入并关闭txt %}

- 以写入模式这样操作也是可以的：

{% asset_img d089b986c9177f3e4776b58d72cf3bc79e3d56b4.jpg Python教程：[58]写入并关闭txt %}

- 写入后，覆盖了原先的内容

{% asset_img fc5e5f34970a304e3f60e97ad3c8a786c8175cb4.jpg Python教程：[58]写入并关闭txt %}

- 假如，输入的路径文件不存在，同样也是创建一个新的文件，然后写入内容，然后关闭文件，看一下，深入一个不存在的文件路径：

{% asset_img a75fb6d3fd1f41348f684cfe271f95cad0c85e97.jpg Python教程：[58]写入并关闭txt %}

{% asset_img 6dc09e0a19d8bc3ea0574f4a808ba61ea9d34597.jpg Python教程：[58]写入并关闭txt %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
