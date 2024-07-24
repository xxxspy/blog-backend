---
title: mplus如何计算组内相关系数ICC
date: 2024-07-17 11:27:40
tags: [mplus, icc]
mathjax: true
---


组内相关系数（ICC）是一个通用的统计量，用于多水平建模、方差分析、心理测量学和其他领域。它衡量的是组内（或类别内）的聚类程度，但它也代表了一个互补的概念，即组间的变异程度。如果我们认为数学成绩`$Y{ij}$`的方差可以分为由于组内个体差异导致的方差`$\sigma^{2}$`（例如，学校内学生的数学乘积的方差）和组间方差`$\tau_{0}^{2}$`（例如，学校平均数学成绩的方差），那么我们可以创建一个由组引起的方差与总方差的比值:

<!-- more -->

`$$
ICC=\rho={\frac{\tau_{0}^{2}}{\sigma^{2}+\tau_{0}^{2}}}
$$`

所得值理论上介于0和1.0之间，因为它是一个方差的比率，较高的值反映了组间变异性的增加。因此，ICC提供了与方差分析类似的信息。尽管可以计算ICC的标准误差、显著性检验和置信区间，但我认为这通常是不相关的，因为在忽略聚类的情况下，一个微不足道的ICC会导致有偏见的标准误差（从而导致第一类错误），而截距的方差显著性检验则提供了关于显著的组间变异性信息。上述公式常用于计算ICC，但也有人提出了其他方法（Bliese, 1988; Shrout & Fleiss, 1979）。尽管如此，ICC是一个有价值的描述性统计量，用作初步步骤以更好地理解由于组差异导致的方差比例。

## ICC 的大小意义

ICC越大代表组间变异程度越大，当ICC=0时，代表组间变量为0，代表数据只存在组内变异，以学校和学生两个层面为例，ICC为0时，学校跟学校相比，校内学生平均成绩没有差异，当ICC为1时，同一个学校内部的学生成绩完全一样，没有变异，不同学校的学生成绩有差异。

以下面的表格为例：

<img src="example.png">

## ICC 如何计算

### SPSS 的方法 

在spss中做多水平回归（混合效应模型）时，构建仅有随机截距的空模型，就可以计算组间和组内方差：

<img src="spss.png">

依据以上公式计算ICC:

`8.614025/(8.614025+39.148322)`

### R 计算方法

```r
> #nlme provides standard deviations of the random effects by default, use VarCorr to obtain variances
> VarCorr(model)
schoolid = pdLogChol(1)
 Variance StdDev
(Intercept) 8.614025 2.934966
Residual 39.148322 6.256862
```

或者，可以使用 psychometric 包的 icc 函数：

```r
> library(psychometric)
> ICC1.lme(mathach,schoolid,data=mydata)[1] 
0.1803518
```

### HLM 结果

<img src="hlm.png">

### Mplus 的方法

在mplus当中，计算ICC的代码如下，下面你需要更改成自己的数据文件、变量名，


```
DATA:
    FILE = datafielname.dat; ! 数据文件
VARIABLE:
    NAMES=class     ! 变量名称
        var1 
        var2;
    USEVAR = var1 var2; ! 需要计算ICC的变量
    CLUSTER =class; ! 集群变量
ANALYSIS:
    TYPE = TWOLEVEL BASIC;
```
