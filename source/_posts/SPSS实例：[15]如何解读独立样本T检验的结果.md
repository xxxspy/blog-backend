---
title: SPSS实例：[15]如何解读独立样本T检验的结果
date: 2016-08-23 18:19:11
tags: [spss]
author: mlln.cn
---
下面这幅图是从网页上搜索得到的一个结果，我们就拿这个结果来解读一下如何分析独立样本T检验的结果。

- 第一个看第一个sig值，它是对方差齐性的假设的检验，假如sig<0.05，说明不满足方差齐性，我们认为方差是不齐的

{% asset_img 3bb22487e950352af27a1b1f5143fbf2b2118b4a.jpg SPSS实例：[15]如何解读独立样本T检验的结果 %}

- 这种情况下，我们只能看第二行数据，也就是看下图所示的sig值来判断是否有组间差异。第二个sig值说明，差异不显著，因为它大于了.05。我们得出的结论是没有差异。

{% asset_img 734f12f3d7ca7bcb1d6af938bc096b63f624a850.jpg SPSS实例：[15]如何解读独立样本T检验的结果 %}

- 我们看第二行数据，sig值>0.05，说明方差是齐性的。

{% asset_img 4651a712c8fcc3ce5c58f7249045d688d53f20c9.jpg SPSS实例：[15]如何解读独立样本T检验的结果 %}

- 这时候，我们需要看另一个sig值，这个值仍然是没有达到显著水平（0.05)，我们认为两组是没有差异的。

{% asset_img 5af4d7ea15ce36d3fb95bd2738f33a87e850b1d0.jpg SPSS实例：[15]如何解读独立样本T检验的结果 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
