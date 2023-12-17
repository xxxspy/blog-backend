---
title: 关于 Dijkstra 的信度系数ρ_A定义和用法
date: 2023-12-05 18:23:19
tags: [spss,smartpls,结构方程,amos,mplus]
author: mlln.cn
mathjax: true
---

rho_A 的英文名称是 reliability coefficient rhoA (Dijkstra, 2014; Dijkstra & Henseler, 2015), 也是信度的一种, 与组合信度CR(rhoc)和内部一致性信度(alpha)具有一定的关系,
所以数值上 rho_a 位于rho_c和alpha之间. 意义与他们不同, rho_a 衡量的是测量指标之间的相关性, 或者他们的共同变异占总变异的比率. 

<!--more-->

### 计算公式

`$$
\rho_A = \sqrt{\frac{\sum_{i=1}^p \sum_{j=1}^p \rho_{ij}}{p(p-1)}}
$$`

- `$\rho_A$`是可靠性系数
- p 是指标变量的数量
- `$\rho_{ij}$`是指标变量 i 和 j 之间的相关系数

从公式中也可以看出, 它类似于求各个指标之间相关系数的平均值.

rho_A 的值范围为 0 到 1。值越高，可靠性越好。一般来说，rho_A 值高于 0.7 表示复合构造具有良好的可靠性。

### 与组合信度rho_c的区别

Both composite reliability rho_c and reliability coefficient rho_A are internal consistency measures used in Structural Equation Modeling (SEM) and Partial Least Squares Structural Equation Modeling (PLS-SEM) to assess the reliability of a composite construct. However, they differ in their assumptions and calculations:
组合信度rho_c和信度系数rho_A都是用来衡量潜变量的内部一致性的, 通常在结构方程模型或者最小二乘法的结构方程模型中使用.

#### 组合信度 Composite Reliability (rho_c):

- 一维性: 假定所有的测量指标都属于个潜变量,是一维的
- 计算方法:
    - 通过平均方差提取量Average Variance Extracted (AVE): ρ_c = (AVE^2) / [(AVE^2) + (1 - AVE)].
    - 通过观测指标的方差协方差矩阵 Individual item variances and covariances: ρ_c = (Σvariances)^2 / [(Σvariances)^2 + 2Σcovariances)].
    - 解释: 代表了观测指标的变异被潜变量解释的比率.
    - 优势Advantages: 好用好理解, 是衡量内部一致性的指标
    - 劣势: 假定构念的一维性, 缺乏适用性

#### 信度系数 Reliability Coefficient (rho_A):

- 没有一维性假定: 当潜变量不是严格的一维时,也可以使用
- 计算: 基于观测指标之间的相关性(e.g., rho_A by Dijkstra, rho_A by Cronbach, etc.).
- 解释: 代表了观测指标之间的相关大小, 是衡量指标之间共同变异的
- 优势: 当潜变量不是单维度时也可以使用, 并且可以衡量观测指标之间的相关性
- 难以计算难以理解: More complex to interpret and calculate, may not be directly comparable to rho_c.

#### 总结:

如果你有强烈的证据认为构念(潜变量)是一维的, 你可以使用rho_c, 如果你不是很确定, 你可以使用 rho_A . 最好的选择往往是基于你的实际研究情景和模型假设. 不过, 很多情况下研究者都是汇报两种信度指标, 以便对结果有更全面的衡量.



### 参考文献

Dijkstra, T. K. (2014). PLS’ Janus face–response to professor Rigdon’s ‘rethinking partial least squares modeling: In praise of simple methods. Long Range Planning, 47(3), 146–153.

Dijkstra, T. K., & Henseler, J. (2015). Consistent partial least squares path modeling. MIS Quarterly, 39(2), 297–316.
