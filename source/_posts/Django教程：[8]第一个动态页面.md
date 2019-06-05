---
title: Django教程：[8]第一个动态页面
date: 2015-01-03 18:17:19
tags: [django]
author: mlln.cn
---
今天我们写一个动态页面，让我们理解一下动态页面的原理。其实前面我们写过一篇文章介绍如何构建第一个静态页面，你可以搜索【Django教程：[4]制作第一个网页】，今天的这一篇文章与上一篇仅有一点不同，今天是动态的页面，你每次访问这个页面都是不同的。

- 我们先在view文件中创建一个函数来返回页面，关于view文件，你应该参考下面的参考资料。我们先引入了datetime模块来计算当前的时间，然后增加一个函数ctime，此函数可以计算当前时间，保存在cutime变量中，然后通过HttpResponse返回到页面

{% asset_img ae10eddeb48f8c547927765538292df5e1fe7f91.jpg Django教程：[8]第一个动态页面 %}

- 接下来设置函数ctime与url的映射。先要引入ctime函数，看下面第一个红色方框；然后再建立函数与url模式的映射关系，看下面第二个红色方框

{% asset_img 91ae68c6a7efce1b7afc7bb0ad51f3deb58f65b2.jpg Django教程：[8]第一个动态页面 %}

- 我们在浏览器中输入url既可以看到在相应的url下，打开一个页面，显示当前的日期。

{% asset_img 3b6833f5e0fe99254ff8da2a36a85edf8cb17191.jpg Django教程：[8]第一个动态页面 %}

- 刷新页面，你可以看到不同的时间，这就是动态页面。与动态页面相对，还有动态url，我们下一篇文章介绍如何设置动态的url。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
