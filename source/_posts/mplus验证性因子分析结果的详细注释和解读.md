---
title: mplus验证性因子分析结果的详细注释和解读
date: 2023-09-18 15:25:50
tags: [mplus, 结构方程, cfa, amos]
---

今天有付费咨询的小伙伴问我“如何解读mplus的输出结果”， 是关于验证性因子分析的。
我相信我在之前的视频中已经讲过如何使用mplus做验证性因子分析， 但是确实缺少了如何解读输出结果。
那么现在我们出一个文章， 详细标注一下mplus输出结果， 方便大家学习。

<!-- more -->

这篇文章使用的mplus的输出结果是使用 mplus 8.3 产生的， 如果输出的文本与你的文本不同， 可能是由于版本不同导致的， 
也可能是由于你设置了特殊的mplus输出结果。

# 版本和日期

mplus输出结果的第一部分如下：

```
Mplus VERSION 8.3
MUTHEN & MUTHEN
08/16/2023   8:56 PM
```

这里很好理解， 介绍了使用软件的版本、 软件作者和结果产生的时间。

# INPUT INSTRUCTIONS 输入的代码

```
INPUT INSTRUCTIONS

  DATA:
      FILE IS data_7.dat;
  VARIABLE:
      MISSING ARE ALL(-999);
      NAMES ARE AL1 AL2 AL3 BL1 BL2 BL3 SQ1 SQ2 SQ3 SQ4
      SQ5 SQ6 SQ7 SQ8 SQ9 SQ10 SQ11 SQ12 SQ13 SQ14 SQ15
      SQ16 SQ17 SQ18 SQ19 SQ20 SQ21 CS1 CS2 CS3 CS4 CS5
      CS6 EL1 EL2 EL3 EL4 EL5 SC1 SC2 SC3 SC4 SC5;
      USEVARIABLES ARE AL1 AL2 AL3 BL1 BL2 BL3 SQ1 SQ2 SQ3 SQ4
      SQ5 SQ6 SQ7 SQ8 SQ9 SQ10 SQ11 SQ12 SQ13 SQ14 SQ15
      SQ16 SQ17 SQ18 SQ19 SQ20 SQ21 CS1 CS2 CS3 CS4 CS5
      CS6 EL1 EL2 EL3 EL4 EL5 SC1 SC2 SC3 SC4 SC5;

  MODEL:
      AL by AL1-AL3;
      BL by BL1-BL3;
      SQA by SQ1-SQ4;
      SQB by SQ6-SQ9;
      SQC by SQ10-SQ12;
      SQD by SQ13-SQ16;
      SQE by SQ17-SQ21;
      SQ by SQA SQB SQC SQD SQE;
      CS by CS1 CS2 CS4-CS6;
      EL by EL1-EL3;
      SC by SC1-SC3 SC5;
      SC2      WITH SC1;
      SQ18     WITH SQ17;
      SC5      WITH SC3;

  OUTPUT: MODINDICES STANDARDIZED;
```

这部分就是我们的原始mplus代码， 这个如果你看了之前的教程， 你应该知道在写什么， 如果你没看我们的视频教程， 
可以看这里：[mplus入门即专家](https://space.bilibili.com/383752637/channel/collectiondetail?sid=1484620) 。

# SUMMARY OF ANALYSIS 

```
SUMMARY OF ANALYSIS

Number of groups                                                 1
Number of observations                                         404

Number of dependent variables                                   43
Number of independent variables                                  0
Number of continuous latent variables                           11

Observed dependent variables

  Continuous
   AL1         AL2         AL3         BL1         BL2         BL3
   SQ1         SQ2         SQ3         SQ4         SQ5         SQ6
   SQ7         SQ8         SQ9         SQ10        SQ11        SQ12
   SQ13        SQ14        SQ15        SQ16        SQ17        SQ18
   SQ19        SQ20        SQ21        CS1         CS2         CS3
   CS4         CS5         CS6         EL1         EL2         EL3
   EL4         EL5         SC1         SC2         SC3         SC4
   SC5

Continuous latent variables
   AL          BL          SQA         SQB         SQC         SQD
   SQE         SQ          CS          EL          SC


Estimator                                                       ML
Information matrix                                        OBSERVED
Maximum number of iterations                                  1000
Convergence criterion                                    0.500D-04
Maximum number of steepest descent iterations                   20
Maximum number of iterations for H1                           2000
Convergence criterion for H1                             0.100D-03

Input data file(s)
  data_7.dat

Input data format  FREE
```

## 注释

### Number of observations.

分析中使用的样本量。

### Number of dependent variables. 

因变量的个数， 注意mplus把潜变量的观测指标分类为因变量， 因为测量指标都是箭头指向的。

###  Observed dependent variables. 

因变量的变量列表。

在我们的模型中使用的所有变量都是连续型变量， 所有都划分在 Continuous 中 。 

### Estimator 

估计器就是估计模型中的参数的时候使用的算法， 比如因子载荷， 都是模型的参数，
在一开始我们不知道这些参数是什么， 就使用估计器对参数进行估计。 默认情况下， 估计器是 ML， 
也就是极大似然方法， 它的本质含义就是， 选定一组参数使得目前这个样本数据出现的概率最大。

mplus还有很多其他的估计器， 但是最常用的是ML， 其他估计器我们在以后的教程中介绍。

# SUMMARY OF DATA

这部分内容非常长， 我们只截取了部分， 省略的部分其实都是 Covariance Coverage 这部分。

```
SUMMARY OF DATA

     Number of missing data patterns             1


COVARIANCE COVERAGE OF DATA

Minimum covariance coverage value   0.100


     PROPORTION OF DATA PRESENT


           Covariance Coverage
              AL1           AL2           AL3           BL1           BL2
              ________      ________      ________      ________      ________
 AL1            1.000
 AL2            1.000         1.000
 AL3            1.000         1.000         1.000
 BL1            1.000         1.000         1.000         1.000
 BL2            1.000         1.000         1.000         1.000         1.000
 BL3            1.000         1.000         1.000         1.000         1.000
 SQ1            1.000         1.000         1.000         1.000         1.000
 SQ2            1.000         1.000         1.000         1.000         1.000
```

## 注释

### Number of missing data patterns.

因为我们的数据是没有确实数据的， 所以 missing data patterns 就是1个， 这1个就是没有缺失这种模式。

但是有时候缺失模式可能不止1个， 比如举例如下：

```
MISSING DATA PATTERNS (x = not missing)
 1 2

 KFT_V1 x x

 KFT_V3 x x

 KFT_Q1 x x

 KFT_Q3 x x

 KFT_N1 x x

 KFT_N3 x
```

这是一个缺失模式为2的数据， 一种模式是所有数据都没有缺失， 第二种模式是只有在KFT_N3这个变量上的缺失， 其他变量无缺失。

所以缺失模式的数量就是缺失数据的种类， 而根据上面的例子， 缺失模型的数量有两种， 因为这个矩阵有2列。 x 代表没有缺失， 空 代表缺失。

### Covariance Coverage.

非缺失数据的比例， 因为我们的数据是没有缺失的， 所以所有的数据都是1（100%）。

那么我们再举一个例子：

```
           Covariance Coveragei
              ITEM13        ITEM14        ITEM15        ITEM16        ITEM17
              ________      ________      ________      ________      ________
 ITEM13         0.994
 ITEM14         0.994         0.998
 ITEM15         0.993         0.996         0.998
 ITEM16         0.991         0.994         0.994         0.995
 ITEM17         0.992         0.995         0.995         0.994         0.997
```
对角线上的元素是单个变量的非缺失数据占比， 而非对角线上的元素指的是两个变量都不缺失的比率。

从这个数据中， 我们可以解读出来， 变量 ITEM13 有缺失数据， 缺失数据占比是 1-0.994， 
如果同时考虑 ITEM13 和 ITEM15， 这两个变量如果有一个缺失就算该样本缺失的话， 样本的缺失率是 1-0.993 。


# UNIVARIATE SAMPLE STATISTICS

```
         Variable/         Mean/     Skewness/   Minimum/ % with                Percentiles
        Sample Size      Variance    Kurtosis    Maximum  Min/Max      20%/60%    40%/80%    Median

     AL1                   4.069      -0.171       1.000    8.66%       2.000      4.000      4.000
             404.000       2.896      -0.897       7.000    6.68%       5.000      6.000
     AL2                   4.252      -0.278       1.000    9.16%       3.000      4.000      4.000
             404.000       3.189      -1.001       7.000    8.17%       5.000      6.000
     AL3                   4.329      -0.431       1.000    4.95%       3.000      4.000      5.000
             404.000       2.305      -0.455       7.000    5.69%       5.000      6.000
     BL1                   4.436      -0.475       1.000    9.16%       3.000      4.000      5.000
```

## 注释

### Sample Size 样本量

很容易理解， 就是样本的个数， 但是要排除缺失值， 如果变量都没有缺失数据， 那么所有变量的样本量都应该一样

### Mean /  Variance 均值和方差

mplus的数据摆放格式很奇怪， 比如这里， 它把均值和标准差放到一列， 比如AL1的均值是 4.069 ， AL1 的方差是2.896。

### Skewness / Kurtosis 偏度/峰度

变量的偏度和峰度用于衡量变量符合正态分布的成都， 关于这两个概念， 可以查看我之前的视频：

[正态性检验01-偏度](https://www.bilibili.com/video/BV1TV411m7tP/)

[正态性检验02-峰度](https://www.bilibili.com/video/BV1xZ4y1N7qy/)

### Minimum/ Maximum 变量的最小最大值

如题

### % with Min/Max

最小值和最大值的占比

### Percentiles 

- 20%/60% 位于这两个百分位的数值
- 40%/80% 位于这两个百分位的数值
- Median 中位数

# MODEL FIT INFORMATION

```
MODEL FIT INFORMATION

Number of Free Parameters                      147

Loglikelihood

          H0 Value                      -26030.375
          H1 Value                      -25118.961

Information Criteria

          Akaike (AIC)                   52354.750
          Bayesian (BIC)                 52942.958
          Sample-Size Adjusted BIC       52476.510
            (n* = (n + 2) / 24)

Chi-Square Test of Model Fit

          Value                           1822.829
          Degrees of Freedom                   842
          P-Value                           0.0000

RMSEA (Root Mean Square Error Of Approximation)

          Estimate                           0.054
          90 Percent C.I.                    0.050  0.057
          Probability RMSEA <= .05           0.036

CFI/TLI

          CFI                                0.923
          TLI                                0.917

Chi-Square Test of Model Fit for the Baseline Model

          Value                          13620.375
          Degrees of Freedom                   903
          P-Value                           0.0000

SRMR (Standardized Root Mean Square Residual)

          Value                              0.094
```

## 注释

### Number of Free Parameters  

自由参数的数量， 比如因子载荷就是参数， 还有比如潜变量的均值和标准差， 
我们可以通过模型计算得到参数的数量， 但是这个不是本教程的重点。

### Loglikelihood

对数似然值， 想要理解这个值就必须了解极大似然估计方法， 但是这个超出本教程范围， 
我们直观上的理解就是这个值越小代表模型越好， 但是我们看到mplus输出有两个对数似然值：
H0就是代表我们的模型的对数似然值， H1代表无限制模型， 也就是观测变量的均值、方差和协方差是无限制的。
我们要知道 Loglikelihood 值越大越好。

输出这两个值的目的是让你看到， 我们模型增加了限制，但是我们不希望这种限制会显著降低模型的拟合度，  所以这两个值越接近越好。

### Information Criteria

#### Akaike (AIC)  

在Mplus中AIC的计算方法来自 Akaike (1987)：

```
AIC = -2logL + 2*r
```

r 代表自由参数的个数， logL 代表对数似然值 。  
在我们的例子中， AIC 是 52354.750， 它是如何得到的？

```
-26030.375 * (-2) + 147 * 2
```

里面用到的数据都是可以在mplus输出中找到。

Akaike 信息准则 (AIC) 是一种数学方法，用于评估模型与其生成数据的拟合程度。 
在统计学中，AIC 用于比较不同的可能模型并确定哪一个最适合数据。 总的来说， AIC越小模型拟合越好。

### Bayesian (BIC) 与 Sample-Size Adjusted BIC

BIC 与 AIC 类似， 当用于模型选择时，BIC 对模型中参数数量的惩罚程度比 AIC 更大。 因此，平均而言，根据BIC选择模型将得到一个参数较少的模型。

### Chi-Square Test of Model Fit 与 Chi-Square Test of Model Fit for the Baseline Model

首先这是卡方值， 卡方值都是越小越好， 在结构方程中， 我们的虚无假设是卡方为0 ， 意思是我们的模型与数据暗含的模型之间没有差异。
P-Value 就是对这个虚无假设进行检验后的概率， 显然这个虚无假设不成立， 因为P-Value 是显著的（低于0.05）。 意思是我们的模型与数据暗示的模型之间有显著差异。
但是因为模型越复杂， 卡方越大， 所以当模型比较复杂的时候， 卡方检验是无效的。

其次， 我们需要理解什么是baseline model， 下面是一个对比， 第一个图是我们设置的模型， 第二个图是 baseline model：

图1 ：
<img src="model.png">

该模型的代码：

```
Model:
	acad by math science socst;
	acad on read;
	read on female;
```

图2 baseline model：
<img src="baseline-model.png">

该模型的代码：

```
Model:
	acad by math@1 science@1 socst@1;
	acad@0;
	acad on read@0;
	read on female@0;
```

怎么理解自由度和基线模型， 可以看下这篇文章[SEM如何理解自由度以及空模型和基线模型](/2023/09/19/SEM如何理解自由度以及空模型和基线模型/)

### RMSEA (Root Mean Square Error Of Approximation)

```
RMSEA (Root Mean Square Error Of Approximation)

          Estimate                           0.054
          90 Percent C.I.                    0.050  0.057
          Probability RMSEA <= .05           0.036
```

RMSEA 是  root mean square error of approximation 的简称， 意思是近似均方根误差。
Earlier research (e.g., Browne & Cudeck, 1993; Jöreskog & Sörbom, 1993) 建议当RMSEA小于0.05的时候认为拟合良好，
当RMSEA小于0.08的时候认为合理。可以看到RMSEA越小说明模型拟合越好， 所以mplus输出了一个概率（Probability RMSEA <= .05），
从上面的结果可以得出结论， RMSEA小于0.05的概率是0.036 。

Bentler and Bonett (1980) recommended that TLI > .90 indicates an acceptable fit.

### CFI/TLI 

Bentler and Bonett (1980) 建议CFI、TLI大于0.9比较好， 不过这个标准其实是主观的， 没有统计依据的。
这些指标叫做相对指标， 因为这个指标的大小是相对于基线模型的。 前面我们介绍过基线模型了， 而相对拟合指标的意思是， 当你的模型比基线模型拟合更好的话， 这个相对指标就比较好。

### SRMR (Standardized Root Mean Square Residual)

Hu and Bentler (1999) 认为SRMR低于0.08是可接受的。

# MODEL RESULTS

这部分就是模型中参数的估计， 比如By（因子载荷）， with（协方差）和on（路径系数）。

```

MODEL RESULTS

                                                    Two-Tailed
                    Estimate       S.E.  Est./S.E.    P-Value

 AL       BY
    AL1                1.000      0.000    999.000    999.000
    AL2                1.062      0.034     31.551      0.000
    AL3                0.728      0.037     19.908      0.000

 BL       BY
    BL1                1.000      0.000    999.000    999.000
    BL2                0.840      0.028     29.500      0.000
    BL3                0.739      0.038     19.232      0.000

 SQA      BY
    SQ1                1.000      0.000    999.000    999.000
    SQ2                1.142      0.054     21.198      0.000
    SQ3                1.133      0.043     26.631      0.000
    SQ4                1.025      0.052     19.662      0.000
```

在验证性因子分析中， 最重要的就是因子载荷了， 在mplus中用By来设定因子及其测量指标。 
MODEL RESULTS 中列出了因子载荷及其显著性检验， 我们注意到， 一个因子下往往第一个指标的因子载荷是999， 
显著性也是999， 注意999代表缺失， 因为在算法中， 我们固定了第一个测量指标的因子载荷， 它就是1， 所以没不必进行显著性检验。
这部分重要的结果就是显著性， 我们要求所有的因子载荷都应该是显著的， 否则这个测量指标就是可以被删除的。

# STANDARDIZED MODEL RESULTS

```
STANDARDIZED MODEL RESULTS


STDYX Standardization

                                                    Two-Tailed
                    Estimate       S.E.  Est./S.E.    P-Value

 AL       BY
    AL1                0.927      0.011     85.243      0.000
    AL2                0.938      0.010     90.511      0.000
    AL3                0.757      0.023     32.663      0.000

 BL       BY
    BL1                0.953      0.011     86.826      0.000
    BL2                0.909      0.013     71.032      0.000
    BL3                0.737      0.025     29.950      0.000
```

对于验证性因子分析， 这部分最重要的就是标准化因子载荷， 就是BY语句下面的参数。
一般符合 Hair, et al (2009)及 Fornell and Larcker (1981)的标准就行：标准化因素负荷量大于 0.5, 理想情况应该是大于0.7。


# 参考文献

关于拟合指标的标准， 参考这篇论文：

Hu, L., & Bentler, P. M. (1999). Cutoff criteria for fit indexes in covariance structure analysis: Conventional criteria versus new alternatives. Structural Equation Modeling, 6, 1-55.

https://www.statmodel.com/download/SRMR2.pdf

https://link.springer.com/article/10.3758/s13428-018-1055-2
