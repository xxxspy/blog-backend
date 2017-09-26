---
title: Python统计分析：[9]2因素卡方检验
date: 2016-05-03 18:05:03
tags: [python]
author: mlln.cn
---
2因素卡方检验主要是检验两个因素之间是否存在关联，或者叫相互影响，我们举一个例子，学习成绩和性别有没有关系，我们首先想到的可能是方差分析来检验平均数的差异，但是如果我们拿到的数据是计数数据，比如成绩分为高分组和低分组，这样只能用卡方检验了。

- 引入相关模块，这里介绍一下Counter这个对象，它用于生成一个迭代器，关于迭代器你们百度一下；list可以生成一列表
我们可以看到迭代器是一个itertools.chain
那么这个迭代器生成的这个列表就是：

{% asset_img b3508d13b07eca802d23f285922397dda144836b.jpg Python统计分析：[9]2因素卡方检验 %}

{% asset_img d1e312f431adcbef2212b564afaf2edda3cc9f6b.jpg Python统计分析：[9]2因素卡方检验 %}

{% asset_img 207ea60e7bec54e757cad17cba389b504fc26a6b.jpg Python统计分析：[9]2因素卡方检验 %}

- 了解了迭代器，我们下面就用Couter来生成我们需要的分类数据

{% asset_img 72ccb7773912b31b5a6d064b8518367adab4e115.jpg Python统计分析：[9]2因素卡方检验 %}

- 打印一下结果，看看具体的数据是啥样子的
这是数据

{% asset_img 647912d7912397dded5f53665a82b2b7d0a2876b.jpg Python统计分析：[9]2因素卡方检验 %}

{% asset_img 29790130e924b899543db25a6d061d950a7bf615.jpg Python统计分析：[9]2因素卡方检验 %}

- 最后运行卡方检验

{% asset_img dbf554ed2e738bd441207953a28b87d6277ff915.jpg Python统计分析：[9]2因素卡方检验 %}

- 首先输出的结果还是描述统计，括号内的数字表示期望值（根据虚无假设计算的值）

{% asset_img e865a699a9014c08913ae3c7097b02087bf4f415.jpg Python统计分析：[9]2因素卡方检验 %}

- 接着是卡方检验

{% asset_img b9d8b7014c086e061da8f42901087bf40ad1cb15.jpg Python统计分析：[9]2因素卡方检验 %}

- 这是最后得到的统计量

{% asset_img e49cf91190ef76c6cbf430499e16fdfaaf51676b.jpg Python统计分析：[9]2因素卡方检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
