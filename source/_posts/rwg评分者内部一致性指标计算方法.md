---
title: 评分者内部一致性Rwg和Intraclass相关系数ICC指标计算方法
date: 2023-02-14 10:17:23
tags: [多层线性模型]
mathjax: true
---

这篇文章列出了James开发的`$r_{wg}$` ( the inter-rater agreement index) 这个指标的计算方法，
$r_{wg}$是用于评估评分者内部一致性(inter-rater agreement index)的指标，

然后，我们给出了ICC （ intraclass correlation coefficients ） 的计算公式及其解释， 
Intraclass相关系数（ICC）：这是一种用于评估评分者内部一致性的常用指标，可以考虑到评分者与评分者之间的关系。

我们会先列出公式， 然后解释公式， 最后给出计算的工具。

<!-- more -->

### 什么是评分者内部一致性

评分者内部一致性（Inter-rater reliability）是指评分者对于相同的评分标准和评分对象，他们给出的评分的相似程度的度量。这是评估评分系统的有效性的重要因素，因为它表明评分是否是稳定和一致的。如果评分者内部一致性高，则可以更确信地依赖评分结果，而如果评分者内部一致性低，则说明评分结果可能不够稳定和一致。

### 有哪些统计指标可以计算评分者内部一致性

有许多统计指标可以计算评分者内部一致性，其中一些常用的指标包括：

- Kappa系数：这是一种常用的评分者内部一致性指标，它考虑了随机误差，并且可以应用于多个评分者和多个评分类别。
- Pearson相关系数：这是一种常用的相关系数，可以度量评分者间的线性关系。
- 均方根误差：这是一种常用的评分者内部一致性指标，可以表示评分者对于同一评分标准的评分结果的离散程度。
- Fleiss' Kappa系数：这是一种用于多评分者和多评分类别情况的评分者内部一致性指标。
- Intraclass相关系数（ICC）：这是一种用于评估评分者内部一致性的常用指标，可以考虑到评分者与评分者之间的关系。
- James' `$r_{wg}$`

请注意，选择的统计指标取决于评分者的数量、评分的性质和评分结果的分布情况。

### `$r_{wg}$` 计算公式

`$$
r_{wg} = 1 - (S^2/t_E^2)
$$`

- `$S^2$`代表方差
- `$t_E^2$`代表期望方差（评分者完全随机情况下的方差）

`$t_E^2$`的计算公式如下(假定均匀分布)：

`$$
t_E^2 = (A^2 - 1) / 12
$$`

- A代表评分等级，比如5级计分， A=5

这个公式的原理是， 方差代表了评分者的不一致程度，
但是如何评分者完全随机的评分， 这个不一致的程度会更大，代表了方差的最大值，
因此， 当`$S^2$`趋近于`$t_E^2$`时， `$r_{wg}$`接近于0；
当`$S^2$`趋近于0时，评分者的评分完全一致， `$r_{wg}$`接近于1；


### ICC 组内相关系数 计算公式

Intraclass Correlation Coefficient (ICC) 公式可以表示如下：

ICC = (MSB - MSW) / (MSB + (k-1) * MSW)

其中：

MSB：组间均方 (between-group mean square）
MSW：组内均方( within-group mean square）
k：表示评分者数量
具体计算方法如下：

- 对于每个评分者，计算该评分者给出的所有评分的平均值。
- 对所有评分者的平均评分求平均值，得到所有评分的总平均值。
- 对每个评分者的平均评分，计算该评分与所有评分的总平均值的差的平方。
- 将每个评分者的差的平方相加，得到MSB。
- 对于每个评分，计算该评分与该评分者的平均评分的差的平方。
- 将每个评分者的差的平方相加，除以评分数量，得到MSW。
- 用MSB和MSW计算ICC，公式如上。

### 使用Excel计算评分者一致性`$r_{wg}$`

我们使用Excel计算的目的是让你对计算公式有一个深入的理解。

#### 数据

<img src="9.png">

这是从论文中摘录的数据， 我们可以看到， 表格中是一个评定者对10个评定对象的打分情况。
如何计算该评定者的一致性。

#### 录入数据

<img src="8.png">

#### 计算方差

使用Excel中的var函数，可以计算一组数据的方差：

<img src="10.png">


#### 计算理想方差

上面已经列出理想方差的计算方法， 我们的评分等级是5， 我们套用公式可以知道， Excel中的公式是：

<img src="11.png">


#### 计算`$r_{wg}$`

<img src="12.png">

### 使用Excel计算组内相关系数ICC

#### 数据

<img src="1.png">


#### ANOVA分析

在Excel中有一个数据分析的插件， 它是Excel自带的， 但是需要你自己设置才能显示出来：

<img src="2.png">

选中数据，也就是“A1:E11”这个区域：

<img src="3.png">

打开excel中的“数据”标签， 找到下面的“数据分析”选项：

<img src="4.png">

在打开的对话框中， 选择“Anova: Two-Factor Without Replication ”， 点击“ok”， 你就会看到下面的对话框：

<img src="5.png">

点击“ok”， 你就可以计算得到ANOVA的结果：

<img src="6.png">

最关键的一步就是根据公式计算ICC， 图中公式的颜色可以告诉你它的地址：

<img src="7.png">

#### 解读公式

根据Excel的“ Two Factor ANOVA without Replication”算法， 我们知道：

- MSRow = 25.7
- MSCol = 1.6
- MSE = 1.68

而ICC的定义是组间均方比总均方， 也就是：

`$$
ICC = {var(\beta) \over {var(\alpha) + var(\beta) + var(e)}}
$$`

我们可以分别计算三个var：

  var(β) = (MSRow – MSE)/k = (25.7 – 1.68)/4 

  var(ε) = MSE = 1.68

  var(α) = (MSCol – MSE)/n = (1.6– 1.68)/10

至此， 我们应该讲清楚了具体的计算过程。

### 参考文献

- L.R. James, R.G. Demaree, G. Wolf, Estimating within-group interrater reliability
with and without response bias, J. Appl. Psychol. 69 (1) (1984) 85–98.

- P.D. Bliese, Within-Group Agreement, Non-independence, and reliability: implications for data aggregation and analysis, in: K.J. Klein, S.W.J. Kozlowski (Eds.),
Multilevel Theory, Research, and Methods in Organizations, Jossey-Bass, San
Francisco, 2000, pp. 349–381

- https://wenku.baidu.com/view/19f1871833687e21ae45a91b.html?_wkts_=1675644378774&bdQuery=the+inter-rater+agreement+index

- https://real-statistics.com/reliability/interrater-reliability/intraclass-correlation/