---
title: wxpython教程：[4]菜单中的图标
date: 2015-07-23 18:15:11
tags: [python,wxpython]
author: mlln.cn
---
我们看到的菜单中多半是有一个图标的，那么今天我们就来做一个菜单，菜单选项左侧有一个图标。要达到这个目的我们必须手动创建一个选项。下面是今天代码的全部：由于这些大部分代码在之前的文章中有讲解，所以这篇文章就着重讲不同的部分。

- 先创建一个选项：注意第二个参数设定了该选项的id，以后绑定方法的时候可以用id来表示该选项

{% asset_img 0e655ca7d933c895c3031a14d21373f082020024.jpg wxpython教程：[4]菜单中的图标 %}

- 设置选项的图标用到了方法：SetBitmap，该方法需要传入一个Bitmap对象：exit.jpg是我自己做的一个图片

{% asset_img c9d4cf43ad4bd11366b0355d59afa40f4bfb0524.jpg wxpython教程：[4]菜单中的图标 %}

- 将创建好的选项添加到菜单

{% asset_img 72b19c025aafa40f52bb4cb2a864034f78f01924.jpg wxpython教程：[4]菜单中的图标 %}

- 将选项与方法绑定，这样点击该菜单选项就能执行OnQuit动作。注意现在用id来表示跟哪个选项进行的绑定，因为我们在

{% asset_img 55a628d12f2eb9383071f89dd6628535e5dd6f06.jpg wxpython教程：[4]菜单中的图标 %}

- 这是最后做出来的效果图

{% asset_img b25d9901a18b87d61b3c2670040828381f30fd20.jpg wxpython教程：[4]菜单中的图标 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
