---
title: Django教程：[9]如何设置时区
date: 2016-01-17 18:15:03
tags: [django]
author: mlln.cn
---
Django站点的时区和你电脑上的时区必须是一致的，我在北京，所以我们通常设置时区为北京的时区，那么我们怎么具体的设置呢？下面看具体的过程：

- 从下面的参考资料里找到时区代码的链接，打开链接

{% asset_img ac0acf1373f08202182e294549fbfbedaa641bc8.jpg Django教程：[9]如何设置时区 %}

- 在打开的页面中，找到中国的时区，或者找到你自己想要的一个时区

{% asset_img 346bd85c103853434ed43f5b9113b07eca808876.jpg Django教程：[9]如何设置时区 %}

- 接着回到你站点文件夹，打开settings文件，设置时区

{% asset_img d041a4a1cd11728b5b423358cafcc3cec3fd2c19.jpg Django教程：[9]如何设置时区 %}

- 搜索TIME_ZONE，我们看默认的时区是UTC，也就是国际协调时，不是任何的时区，而是一个国际通用时间。

{% asset_img 72ccb7773912b31beffb72538418367adbb4e1f2.jpg Django教程：[9]如何设置时区 %}

- 将其修改为上海时区，就这样就ok了。保存settings文件

{% asset_img c9d4cf43ad4bd11330a2084858afa40f4bfb0519.jpg Django教程：[9]如何设置时区 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
