---
title: numpy函数：[2]tile函数用法
date: 2016-10-19 18:17:15
tags: [numpy]
author: mlln.cn
---
tile函数位于python模块 numpy.lib.shape_base中，他的功能是重复某个数组。比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组，我们还是使用具体的例子来说明问题：

- 先来引入numpy下的所有方法

{% asset_img f677b1c379310a5583d241f8b54543a98326108c.jpg numpy函数：[2]tile函数用法 %}

- 我们创建一个a，如图下图，使用tile来创建b，注意看b的数据结构

{% asset_img 43e6c733c895d1438c637b2f71f082025aaf0761.jpg numpy函数：[2]tile函数用法 %}

- 假如我们输入一个元组(1,2)，我们会得到一样的结果，与上面相同的b

{% asset_img d57e9994a4c27d1eda87a4c819d5ad6edcc438dd.jpg numpy函数：[2]tile函数用法 %}

- 当然，我们想要a变为一个二维数组，就要换一种重复的方式了。

{% asset_img 0fb505d5ad6eddc45c462bf73bdbb6fd536633dd.jpg numpy函数：[2]tile函数用法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
