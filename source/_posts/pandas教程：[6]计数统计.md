---
title: pandas教程：[6]计数统计
date: 2015-05-23 18:03:23
tags: [pandas]
author: mlln.cn
---
经过之前的学习，我们现在可以做一个简单的统计了，比如计数，这是最简单的统计，我们现在就使用pandas统计一下数据中各个专业学生的数目：

- 先来引入pandas，并且从csv文件中读取数据

{% asset_img 8640bf8b87d6277fc3b99f2b2b381f30e924fc3f.jpg pandas教程：[6]计数统计 %}

- 查看一下前三行数据，看读取数据是否正确

{% asset_img 29790130e924b899ca97d42b6d061d950a7bf63f.jpg pandas教程：[6]计数统计 %}

{% asset_img 8697397f9e2f070877d28713ea24b899a801f28b.jpg pandas教程：[6]计数统计 %}

- 选择数据：之前也有相关的教程，假如现在我们要统计【专业名称】这一列，那么需要学会选择它：

{% asset_img 6391e903918fa0ec7e27c91e259759ee3c6ddb86.jpg pandas教程：[6]计数统计 %}

- 计数统计我们使用：save_counts()，打印这个结果，查看一下

{% asset_img 09bb4f3d269759ee47b0cdd8b1fb43166c22df86.jpg pandas教程：[6]计数统计 %}

{% asset_img d872d695d143ad4be32dead381025aafa40f0666.jpg pandas教程：[6]计数统计 %}

- 绘制柱形图，使用plot方法，如果想要输出该图，使用get_figure()和savefig()

{% asset_img 27d647ee3d6d55fbce26db356e224f4a21a4dd86.jpg pandas教程：[6]计数统计 %}

- 最后我们可以在D盘下找到plot.png，这就是绘制好的bar图了。

{% asset_img b3ba5d166d224f4aa079de000af790529922d186.jpg pandas教程：[6]计数统计 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
