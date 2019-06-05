---
title: Python教程：[70]enumerate遍历列表
date: 2015-02-05 18:19:03
tags: [python]
author: mlln.cn
---
怎样遍历列表可能大家很少用enumerate，其实它的用处还挺大的，今天我们来举几个例子说明一下它跟别的遍历list方法有什么不同：

- 创建一个列表，然后遍历它

{% asset_img d048adde9c82d158f9203f33820a19d8bd3e4256.jpg Python教程：[70]enumerate遍历列表 %}

- 我们可以使用这样的方式遍历一个列表，但是缺点是无法读取索引index

{% asset_img bd7faf3533fa828b9bc7fb61ff1f4134960a5a08.jpg Python教程：[70]enumerate遍历列表 %}

- 也可以使用索引的方法遍历，但写起来比较麻烦

{% asset_img a992e31f4134970a729776ad97cad1c8a6865d08.jpg Python教程：[70]enumerate遍历列表 %}

- 使用enumerate就可以了，写法稍微简单了些

{% asset_img 32bb9c8ba61ea8d3c2801286950a304e241f5856.jpg Python教程：[70]enumerate遍历列表 %}

- 实际上enumerate返回的是一个enumerate对象

{% asset_img 948bcfc8a786c91737e734bbcb3d70cf3ac75708.jpg Python教程：[70]enumerate遍历列表 %}

- 上面的遍历相当于这样的写法

{% asset_img eab9044c510fd9f90d7634eb272dd42a2934a494.jpg Python教程：[70]enumerate遍历列表 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
