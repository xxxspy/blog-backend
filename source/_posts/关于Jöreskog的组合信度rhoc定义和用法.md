---
title: 关于Jöreskog的组合信度ρ_c定义和用法
date: 2023-12-05 18:23:19
tags: [spss,smartpls,结构方程,amos,mplus]
author: mlln.cn
mathjax: true
---

组合信度(composite reliability )ρ_c 是 Jöreskog’s (1971) 开发的一个指标.
Jöreskog 的 ρ_c 是结构方程模型 (SEM) 和偏最小二乘结构方程模型 (PLS-SEM) 中用于评估构念的可靠性的度量。构念composite是一种潜变量（未观察变量），由多个指标变量（观察变量）来测量。
组合信度有时候被归纳为聚合效度的一种, 因为聚合效度就是指的是测量指标聚合为一个构念的程度, 因此各种名词很多时候都指的是一个意思.

ρ_c表示指标潜变量(也叫构念)的方差被测量指标解释的比率, 最大是1. 值越高（通常高于 0.7）表示可靠性越高.

<!--more-->

### 计算公式

`$$
{\displaystyle \rho _{C}={\frac {\left(\sum _{i=1}^{k}\lambda _{i}\right)^{2}}{\sigma _{X}^{2}}}}
$$`

或者更常用下面的公式:

`$$ {\displaystyle \rho _{C}={\frac {\left(\sum _{i=1}^{k}\lambda _{i}\right)^{2}}{\left(\sum _{i=1}^{k}\lambda _{i}\right)^{2}+\sum _{i=1}^{k}\sigma _{e_{i}}^{2}}}} $$`

### 计算过程

具体的计算方法, 可以看下面这个案例 https://en.wikipedia.org/wiki/Congeneric_reliability

### 衡量标准

ρ_c 没有单一的“完美”值，但一般来说，值高于 0.7 被认为是可接受的，值高于 0.8 是良好的，值高于 0.9 是优秀的。但是，这些只是一般性的指导方针，ρ_c 的可接受值可能因您的研究背景和您要测量的特定构造而有所不同。
具体你可以看下面的参考文献.

### omega系数 `$\omega$ `

 `$\omega$ `实际上就是 ρ_c , `$\omega$ `是基于 McDonald's (1985, 1999) 提出的.

McDonald's (1985, 1999) 声称它是第一个提出 ρ_c 组合信度的人, 的确在 McDonald (1970) 的论文中出现了 ρ_c 的计算公式, 但是用的不同的数学符号. 当时McDonald (1970)是在EFA的情景下讨论的, 并且ρ_c是基于估计的协方差矩阵, 
而McDonald (1970)说的是观察到的协方差矩阵, 他们具有相同的公式但是不同的意义. 并且 Jöreskog (1971) 是真正对用户产生影响的人, 所以更多的人还是将这个系数归功于 Jöreskog (1971) . 

### 参考文献

Jöreskog, K. G. (1971). Simultaneous factor analysis in several populations. Psychometrika, 36(4), 409–426.
