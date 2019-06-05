---
title: Python教程：[61]创建文件夹 目录
date: 2016-10-03 18:05:23
tags: [python]
author: mlln.cn
---
python如何创建文件夹，用到了mkdir和makedirs两个方法，前者创建一层目录，后者创建多层目录，下面我们来看看具体是怎么用的。

- 先要引入os模块

{% asset_img ac754782b2b7d0a2c2fbb31dc9ef76094a369ac5.jpg Python教程：[61]创建文件夹 目录 %}

- 使用mkdir方法创建一个tt文件夹，参数是文件夹的路径：

{% asset_img caae68094b36acaffad2217c7ed98d1000e99cc5.jpg Python教程：[61]创建文件夹 目录 %}

- 假如我们使用mkdir方法创建多层文件夹，也就是说，文件夹f:/tt1和文件夹f:/tt1/tt1都是不存在的，这时候就会出现错误

{% asset_img 7d98931001e93901fb303abe79ec54e737d196c5.jpg Python教程：[61]创建文件夹 目录 %}

- 我们可以使用makedirs方法来创建多层目录：

{% asset_img 8697397f9e2f07085e689d80eb24b899a801f286.jpg Python教程：[61]创建文件夹 目录 %}

- 写完这篇文章，你可能想知道，如何删除目录呢，幸好我前几天已经写完了一篇如何删除文件夹的文章，具体见：http://jingyan.baidu.com/article/39810a23e80384b636fda639.html

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
