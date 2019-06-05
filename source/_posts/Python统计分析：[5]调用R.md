---
title: Python统计分析：[5]调用R
date: 2016-06-11 18:03:03
tags: [python]
author: mlln.cn
---
Python做统计还不太成熟，很多需要的统计方法并没有现成的Python模块或者方法，而笔者也不是专门的统计出身，所以并不想自己去开发一些算法，所以我选择调用R来实现部分统计功能，毕竟R包含的统计包更多。今天示范一下如何在Python中调用R来进行一些简单的统计。

- 先引入相关模块，rpy2就是Python中的r接口

{% asset_img 78701455b319ebc4c68329e18126cffc1f17168b.jpg Python统计分析：[5]调用R %}

- 假如我们想要用R中的一些常量，比如pi，可以这样调用
输出结果为：

{% asset_img dc854fda81cb39dbf98d382ed3160924ab18303d.jpg Python统计分析：[5]调用R %}

{% asset_img b6045da98226cffc6b67e0caba014a90f603ea3e.jpg Python统计分析：[5]调用R %}

- 我们还可以将pandas的DataFrame对象转换为R中的data.frame对象或者matrix，下面先读取一个数据，生成DataFrame

{% asset_img 42e89c26cffc1e17fc44d3494990f603728de994.jpg Python统计分析：[5]调用R %}

- 生成r中的dataframe
输出结果为：

{% asset_img 834344afa40f4bfb9c9dc12c004f78f0f736183d.jpg Python统计分析：[5]调用R %}

{% asset_img 8b527d2762d0f7033349caa40bfa513d2797c594.jpg Python统计分析：[5]调用R %}

- 转换为矩阵：

{% asset_img 2f3295d4b31c8701294ded9e247f9e2f0608ff94.jpg Python统计分析：[5]调用R %}

- 当然，我们还可以调用R中的方法来进行绘图，比如绘制一个散点图：
你会看到弹出一个窗口，展示了绘制好的散点图：

{% asset_img a54e55fbfbedab646a3f12b8f436afc379311e3d.jpg Python统计分析：[5]调用R %}

{% asset_img b258f5c4b74543a9f156a5b41d178a82b901143d.jpg Python统计分析：[5]调用R %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
