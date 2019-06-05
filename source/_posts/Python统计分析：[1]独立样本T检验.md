---
title: Python统计分析：[1]独立样本T检验
date: 2016-04-23 18:15:05
tags: [python]
author: mlln.cn
---
这是《Python统计分析》系列文章的第一篇，该系列文章致力于使用Python进行一般的统计分析，比如T检验、方差分析、回归分析、主成分、聚类、等等。Python有很多统计包可以帮助我们实现我们的目的，《Python统计分析》系列文章用到的包包括但不仅限于：pandas、numpy、scipy、Statsmodels。很多人都知道我写过所有这些包的教程，而《Python统计分析》系列文章可以把以前的内容综合运用起来，所以需要你对这些模块有一定的了解，但不需要精通。

- 引入相关的模块，ttest_ind是用于独立样本t检验的（independent samples t test），pandas主要用到它的DataFrame

{% asset_img 5f9e93b1cb1349547392d817554e9258d0094af1.jpg Python统计分析：[1]独立样本T检验 %}

- 读取数据并查看一下数据的前五行
我们可以看到数据包含三列，最后一列group表示不同的组，只有1、2两组

{% asset_img 8367d1fc1e178a8265b04fd3f503738da877e8f2.jpg Python统计分析：[1]独立样本T检验 %}

{% asset_img 8a95ad1c8701a18b6967223c9d2f07082938fef2.jpg Python统计分析：[1]独立样本T检验 %}

- 我们用到了DataFrame的一个筛选数据的功能，比如筛选1组数据
我们可以得到这样的数据

{% asset_img 8b527d2762d0f7039705a6af0bfa513d2797c5ca.jpg Python统计分析：[1]独立样本T检验 %}

{% asset_img 476217f7905298226abc09b0d4ca7bcb0b46d4f2.jpg Python统计分析：[1]独立样本T检验 %}

- 假如现在我们想要比较两组数据在scoreA上是否有差异，我们可以分别筛选得到1组的scoreA和2组的scoreA，然进行t检验
检验的结果得到一个tuple，第一个元素是t值，第二个元素是p值，根据p值就知道两列数据均值差异不显著

{% asset_img 21e5582309f790528ee7744d0ff3d7ca7acbd58d.jpg Python统计分析：[1]独立样本T检验 %}

{% asset_img 27d647ee3d6d55fbbd6946556e224f4a21a4ddd2.jpg Python统计分析：[1]独立样本T检验 %}

- 如果我们想要同时比较scoreA和scoreB也可以，筛选数据的时候加上scoreB即可
结果得到的是tuple构成的tuple，第一个tuple元素表示t值，根据结果我们就知道t（scoreA）=1.366，t（scoreB）=0.601,另一个tuple就不解释了吧

{% asset_img 1f569482b9014a90289276ceaa773912b21beed2.jpg Python统计分析：[1]独立样本T检验 %}

{% asset_img 08b68e529822720e1561d28978cb0a46f31fabd2.jpg Python统计分析：[1]独立样本T检验 %}

- 当然我们还需要注意，ttest_ind默认两组数据方差齐性的，如果想要设置默认方差不齐，可以设置equal_var=False，下面比较一下这两种情况结果的差异

{% asset_img 148f28d3d539b6000f613fc4ea50352ac75cb7d2.jpg Python统计分析：[1]独立样本T检验 %}

{% asset_img c8ab0bce36d3d53982b23fb03987e950342ab0f2.jpg Python统计分析：[1]独立样本T检验 %}

- 那么，问题来了（挖掘机到底哪家强？），我们用什么检验两组数据的方差齐性呢——levene test
检验结果为p>0.05所以，可以认为方差是相等的。

{% asset_img 373bc4b44aed2e736145b65f8401a18b86d6fad2.jpg Python统计分析：[1]独立样本T检验 %}

{% asset_img 0d729944ebf81a4c77bddcbad42a6059242da6f2.jpg Python统计分析：[1]独立样本T检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
