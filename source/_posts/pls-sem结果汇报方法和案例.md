---
title: pls-sem结果汇报方法和案例【以SmartPLS为例】
date: 2023-03-27 11:27:59
tags: [sem,spss,smartpls]
---

如何汇报pls-sem （Partial Least Square Structural Equation Modeling）的结果， 很多刚入门的学生都会有疑问，
因为它不像一般的统计方法， 只有一两个指标看需要汇报，
sem的结果有很多，而pls-sem又与cb-sem（Covariance Based Structural Equation Modeling）不同，使得汇报sem的结果比较困难，
也很容易遗漏重要信息。

所以我认为有必要写一篇文章， 总结一下pls-sem的汇报规范， 并且我们提供了案例方便大家效仿。

<!-- more -->

## 通用报告原则

在开始pls-sem的报告之前， 我们需要强调实证研究一些常用的基本原则， 这些原则有助于你的论文顺利通过评审，
并且有助于学科发展，提高研究的可重复性和可批判性。

- 数据样本来自哪里，总体是什么，抽样方法是什么
- 数据分布以及对统计方法的适用性
- 理论模型，以便确定统计方法的适用性
- 统计结果
- 统计软件的名称和版本号

通常sem模型最好的方法是绘制概念图（理论模型），
在图中可以看到每个潜变量的测量指标， 并且可以看到每个潜变量之间的关系（箭头），
绘图的方式可以快速让读者（或者评审）理解你的模型，而且很全面。

## 解释使用PLS的原因

Hair 在 《When to use and how to report the results of PLS-SEM》这篇文章中介绍了使用pls-sem的原因， 
为什么做结构方程的话，采用pls需要解释原因呢，因为pls是有偏估计， 而CB-SEM是无偏估计，所以在大部分时间，
我们都建议使用CB-SEM来做结构方程， 那么什么时候你必须采用PLS方法呢， 下面是几个原因：

<img src="imgs/使用pl-sem的原因.png">

总结和翻译过来， 选择PLS-SEM而不是CB-SEM的原因通常有以下几个：

- 数据的性质：PLS-SEM适用于小样本数据，而CB-SEM更适用于大样本数据。因此，如果数据样本较小，则可以选择PLS-SEM。并且你需要说明为何无法收集更多样本。
- 复杂性：CB-SEM通常比PLS-SEM更复杂，因为它需要指定更多的参数，例如路径和方差。如果你的模型非常复杂，CB-SEM经常无法收敛，则可以选择PLS-SEM。
- 研究目的：PLS-SEM更适用于探索性研究或理论建立，而CB-SEM更适用于验证性研究或检验理论模型。因此，研究目的也是选择PLS-SEM或CB-SEM的重要因素之一。
- 形成性潜变量存在时（formatively measured constructs）只能用PLS
- 当数据分布问题令人担忧时，例如缺乏正态分布特性；
- 当研究用到了潜变量的分数，以便在后续分析中使用时

总之，PLS-SEM和CB-SEM都是有用的统计分析方法，选择哪种方法取决于研究的目的、数据的性质和模型的复杂程度。

## 两阶段汇报原则

基本上结构方程模型（不管是PLS还是CB）的结果汇报包含两部分：
    - 测量模型的结果：测量题目的信效度（或者叫测量模型的信效度）， 变量都是用题目来测量的， 但是你凭什么证明这些题目可以代表某个变量呢， 通常需要做信效度分析的
    - 结构模型的结果：变量之间的关系的检验， 或者说变量之间的路径系数的显著性检验

<img src="imgs/模型图.png">

### 测量模型的结果

#### 反映性指标组合信度和平均方差提取量

下面是一个典型的测量模型的结构效度的结果，主要包含了指标：组合信度（CR）、平均方差提取量（AVE）、相关系数。
有时候这个表格也叫做区分效度， 因为潜变量之间具有区分度是结构效度的一种。 具有区分效度的要求是， AVE的平方根大于变量之间的相关系数，
它的寓意是变量内部的题目之间的共同变异要多于变量之间的共同变异。

<img src="imgs/测量模型信效度检验.png">

有时候这个表格可以简写为下面， 省略了相关系数， 同时这个表格可以添加克隆巴赫alpha系数：

<img src="imgs/平均方差提取量.png">

注意这个表格犯了一个常见错误， 就是CR和AVE都是针对反应性变量的（Reflective Latent Variable）， 
如果变量是形成性的（Formative）， 那么不可以计算CR和AVE， 并且即便算出来了， 通常形成性潜变量的CR和AVE比较低，无法达标，
不过即便达标也是毫无意义。

在上面的表格中，“期刊多樣性”，“期刊期刊屬性”，“期刊易取性”是形成性指标，不要汇报AVE。

有时候我们还会在这个表格中整合均值和标准差：

<img src="imgs/ave-cr-mean-correlation-sd.png">

#### 形成性指标汇报权重

如果你的潜变量是形成性指标， 我们可以汇报权重及其显著性检验统计量：

<img src="imgs/OUTER WEIGHT IN FORMATIVE Indicators.png">

#### 反映性指标汇报因子载荷和交叉因子载荷

这个表格汇报了我们每个潜变量的因子载荷以及交叉因子载荷，
交叉因子载荷指的是每一个题目与每一个潜变量的载荷，
不管题目是否属于某个潜变量， 我们仍然计算了该潜变量在该题目上的因子载荷，
目的是对区分效度做进一步验证， 这个表格的要求是，题目在所属因子上载荷较高，
在非所属因子上载荷较低， 证明因子结构的良好。

<img src="imgs/loadings-and-cross.png">

### 结构模型结果

如前所述，PLS分析的主要重点是方差解释以及确定所有路径估计的显著性。
具体而言，通过内生变量（因变量）的R2值评估结构模型的预测能力。
与OLS回归中的类似，PLS的R2结果表示因变量被模型解释的方差量。、

#### R方和路径系数的显著性

<img src="imgs/r-square.png">

注意这个表格没有显著性检验， 因为pls不可以直接计算显著性， 它是一个非参数估计方法。
在martpls中， 通常是使用bootstraping方法来估计路径系数的置信区间及其显著性。

下面这个表格是对路径系数的显著性进行检验：

<img src="imgs/coefficient-test.png">

#### 效应量f方

f方的计算公式如下:

<img src="imgs/f-formula.png">

它的涵义很简单就是自变量对因变量的方差贡献率， 
从计算公式来看， 在没有该自变量的情况下， R方较小为R2excluded，
在有该自变量的情况下，R方较大为R2included。

下面是汇报f方的表格：

<img src="imgs/effect-size-f.png">

#### q方



#### 中介效应检验

<img src="imgs/MEDIATOR ANALYSIS.png">

#### 总体拟合指标GOF

<img src="imgs/gof拟合指标.png">

“与 CB-SEM 不同，PLS-SEM 并没有优化全局函数。一些学者传统上认为 PLS-SEM 缺乏全局标量函数，导致缺乏全局拟合优度，但很多学者不采取这种立场。使用 PLS-SEM 时，重要的是要认识到术语“拟合”在 CB-SEM 和 PLS-SEM 的上下文中具有不同的含义（Hair、Hollingsworth、Randolph 和 Chong，2017 年；Rigdon、Sarstedt  & Ringle, 2017 ). CB-SEM 的拟合统计量源自实际数据和模型隐含协方差矩阵的差距，而 PLS-SEM 则侧重于因变量的预测效果（Hair, Sarstedt, & Ringle, 2019; Henseler et al., 2014）。虽然研究人员提出了各种模型拟合 PLS-SEM 的测量（Schuberth、Henseler 和 Dijkstra，2018； Tenenhaus 等人，2005），它们识别错误模型的功效非常有限（有关措施及其局限性的讨论，请参见图表 6.2）。 因此，为了判断模型的质量，研究人员使用 PLS-SEM 依赖于评估模型对因变量的预测能力（Shmueli, Ray, Velasquez Estrada, & Chatla, 2016；Shmueli et al., 2019（Hair，2020）。”（Hair 等人，2022 年，第 92-93 页）。

## 补充提问

如果有对本教程有什么疑问可以留言，如果你认为我缺少了某些你需要部分，可以留言告诉我，我会很快补充。


## 参考文献

Hair, J. F., Hult, G. T. M., Ringle, C. M., and Sarstedt, M. (2022). A Primer on Partial Least Squares Structural Equation Modeling (PLS-SEM), 3^rd^ Ed., Sage: Thousand Oaks.

Henseler, J., and Sarstedt, M. (2013). Goodness-of-Fit Indices for Partial Least Squares Path Modeling, Computational Statistics, 28(2), 565-580.

Tenenhaus, M., Amato, S., and Esposito Vinzi, V. (2004). A Global Goodness-of-Fit Index for PLS Structural Equation Modeling, Proceedings of the XLII SIS Scientific Meeting. Padova: CLEUP, 739-742.

> **注意**
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的, 不论什么模型都可以, 只限制于1个研究内. 
> 跟我学统计可以代做分析, 每单几百元不等. 
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pls-sem结果汇报方法和案例.ipynb)
> 可以在微博上@mlln-cn向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
