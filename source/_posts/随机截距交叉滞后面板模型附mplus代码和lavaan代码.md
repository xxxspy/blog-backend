---
title: 随机截距交叉滞后面板模型附mplus代码和lavaan代码
date: 2025-02-26 10:30:02
tags: [交叉滞后模型,clpm, lavaan, mplus]
mathjax: true
---



本教程旨在帮助研究者了解和使用随机截距交叉滞后面板模型（RI-CLPM）的三个常见扩展，并提供使用 R 包 `lavaan` 和 Mplus 进行建模的实用指导和代码示例。这些扩展包括：纳入时不变预测变量和/或结果变量，进行多组分析，以及纳入多重指标。

<!-- more -->

# RI-CLPM 模型

## 1. RI-CLPM 简介

RI-CLPM 是一种结构方程模型（SEM）方法，用于分析纵向数据。它将观测得分分解为个体内部的动态变化和个体之间稳定的差异两部分。传统的交叉滞后面板模型 (CLPM) 没有区分个体内部和个体之间的差异，RI-CLPM 通过引入随机截距来解决这个问题。

### 1.1 基本 RI-CLPM 的构建

构建 RI-CLPM 的关键是将观测得分分解为三个部分：总均值、个体间稳定成分（随机截距）和个体内部波动成分。以原文中的睡眠问题 (S) 和焦虑 (A) 为例，对于个体 *i* 在时间点 *t* 的观测得分可以表示为：

`$S_{it} = \mu_t + BS_i + WS_{it}$`

`$A_{it} = \pi_t + BA_i + WA_{it}$`

其中：

*   `$\mu_t$` 和 `$\pi_t$ `分别是时间点 *t* 的睡眠问题和焦虑的总均值。
*   `$BS_i$` 和 `$BA_i$` 分别是个体 *i* 的睡眠问题和焦虑的随机截距，代表个体间稳定的差异。在 SEM 软件中，通过创建一个潜变量，并将重复测量作为其指标，且所有因子载荷固定为 1 来实现。
*   `$WS_{it}$` 和 `$WA_{it}$` 分别是个体 *i* 在时间点 *t* 的睡眠问题和焦虑的个体内部波动成分，代表个体相对于其自身均值的偏差。在 SEM 软件中，通过为每个测量创建一个潜变量并约束其测量来创建这些成分。

结构关系：自回归效应（`$\alpha_t$` 和 `$\delta_t$`）代表个体内部的持续效应，交叉滞后效应（`$\beta_t$` 和 `$\gamma_t$`）代表一个领域的状态对另一个领域状态的影响。

### 1.2 模型约束

为了检验特定的假设，可以对模型施加约束，并使用卡方差检验或 AIC/BIC 等指标来比较模型的拟合优度。常见的约束包括：

*   **滞后回归系数的时间不变性：** 检验滞后回归系数是否随时间变化。需要注意的是，只有当重复测量的时间间隔大致相等时，这种约束才有意义。
*   **总均值的时间不变性：** 检验总均值是否随时间变化。

### 1.3 RI-CLPM 与传统 CLPM 的关系

如果将 RI-CLPM 中所有随机截距的方差（及其协方差）约束为零，则得到的模型在统计上等同于传统的 CLPM。

## 2. RI-CLPM 的扩展

### 2.1 扩展 1：纳入时不变的预测变量和结果变量

#### 2.1.1 纳入时不变预测变量

例如，想将神经质 (`$N_i$`) 作为睡眠问题和焦虑的预测变量。如图 2 顶部所示，可以将 `$N_i$` 作为观测变量 `$S_{it}$` 和 `$A_{it}$` 的预测变量。

```R
# lavaan 示例代码
model <- '
  # 随机截距
  BS =~ 1*S1 + 1*S2 + 1*S3 + 1*S4 + 1*S5
  BA =~ 1*A1 + 1*A2 + 1*A3 + 1*A4 + 1*A5

  # 回归
  S1 ~ b1 * N
  S2 ~ b2 * N
  S3 ~ b3 * N
  S4 ~ b4 * N
  S5 ~ b5 * N
  A1 ~ a1 * N
  A2 ~ a2 * N
  A3 ~ a3 * N
  A4 ~ a4 * N
  A5 ~ a5 * N
'
fit <- sem(model, data = data)
summary(fit)
```

也可以将 `$N_i$` 作为随机截距 `$BS_i$` 和 `$BA_i$` 的预测变量。  当随机截距的因子载荷都固定为1时，将观测变量作为时不变预测变量与将随机截距作为预测变量是等价的。

```R
# lavaan 示例代码
model <- '
  # 随机截距
  BS =~ 1*S1 + 1*S2 + 1*S3 + 1*S4 + 1*S5
  BA =~ 1*A1 + 1*A2 + 1*A3 + 1*A4 + 1*A5

  # 回归
  BS ~ b * N
  BA ~ a * N
'
fit <- sem(model, data = data)
summary(fit)
```

#### 2.1.2 纳入时不变结果变量

例如，想用睡眠问题和焦虑预测之后的生活满意度 (`$L_i$`)。 可以将 `$L_i$` 回归到随机截距` $BS_i$` 和 `$BA_i$`，个体内部的波动 `$WS_{it}$` 和 `$WA_{it}$` 或观测变量 `$S_{it}$` 和 `$A_{it}$`。

```R
# lavaan 示例代码：将 L 回归到随机截距
model <- '
  # 随机截距
  BS =~ 1*S1 + 1*S2 + 1*S3 + 1*S4 + 1*S5
  BA =~ 1*A1 + 1*A2 + 1*A3 + 1*A4 + 1*A5

  # 回归
  L ~ b * BS + a * BA
'
fit <- sem(model, data = data)
summary(fit)
```

```R
# lavaan 示例代码：将 L 回归到随机截距和个体内部波动
model <- '
  # 随机截距
  BS =~ 1*S1 + 1*S2 + 1*S3 + 1*S4 + 1*S5
  BA =~ 1*A1 + 1*A2 + 1*A3 + 1*A4 + 1*A5

  # 个体内部波动
  WS1 =~ 1*S1
  WS2 =~ 1*S2
  WS3 =~ 1*S3
  WS4 =~ 1*S4
  WS5 =~ 1*S5
  WA1 =~ 1*A1
  WA2 =~ 1*A2
  WA3 =~ 1*A3
  WA4 =~ 1*A4
  WA5 =~ 1*A5

  # 回归
  L ~ b * BS + a * BA + ws1 * WS1 + ws2 * WS2 + ws3 * WS3 + ws4 * WS4 + ws5 * WS5 + wa1 * WA1 + wa2 * WA2 + wa3 * WA3 + wa4 * WA4 + wa5 * WA5
'
fit <- sem(model, data = data)
summary(fit)
```

#### 结果解读：
**显著正相关**：如果神经质对睡眠问题和焦虑有显著的正向影响，这意味着高神经质的个体倾向于报告更多的睡眠问题和焦虑症状。回归系数的大小表示这种影响的强度。
**非显著相关**：如果睡眠问题或焦虑对生活满意度没有显著影响，可能表明这些因素与生活满意度之间的关系较为复杂，或者存在其他的调节或中介变量。

### 2.2 扩展 2：多组 RI-CLPM

多组分析允许检验不同组别之间滞后关系是否存在差异。例如，想检验神经质水平高低的两组个体，睡眠问题和焦虑之间的相互影响是否存在差异。

```R
# lavaan 示例代码
model <- '
  # 随机截距
  BS =~ 1*S1 + 1*S2 + 1*S3 + 1*S4 + 1*S5
  BA =~ 1*A1 + 1*A2 + 1*A3 + 1*A4 + 1*A5

  # 交叉滞后效应
  S2 ~ a1*S1 + b1*A1
  S3 ~ a2*S2 + b2*A2
  S4 ~ a3*S3 + b3*A3
  S5 ~ a4*S4 + b4*A4
  A2 ~ c1*A1 + d1*S1
  A3 ~ c2*A2 + d2*S2
  A4 ~ c3*A3 + d3*S3
  A5 ~ c4*A4 + d4*S4
'
fit <- sem(model, data = data, group = "neuroticism_group")
summary(fit, standardized = TRUE)
```

首先，拟合一个没有跨组约束的多组 RI-CLPM。然后，拟合一个滞后参数在组间恒定的模型。如果卡方差检验表明这个约束不能被施加，这意味着 (一些) 滞后系数在组间是不同的: 变量之间的滞后效应取决于分组变量的水平。

### 2.3 扩展 3：多指标 RI-CLPM

当每个结构都有多个指标时，可以采用两种方法扩展 RI-CLPM。如图 3 所示，可以在每个指标中包含一个随机截距，也可以在潜在变量水平上包含随机截距。

#### 2.3.1 包含指标特异性随机截距

```R
# lavaan 示例代码
model <- '
  # 随机截距
  BS1 =~ 1*S1_1 + 1*S2_1 + 1*S3_1 + 1*S4_1 + 1*S5_1
  BS2 =~ 1*S1_2 + 1*S2_2 + 1*S3_2 + 1*S4_2 + 1*S5_2
  BS3 =~ 1*S1_3 + 1*S2_3 + 1*S3_3 + 1*S4_3 + 1*S5_3
  BA1 =~ 1*A1_1 + 1*A2_1 + 1*A3_1 + 1*A4_1 + 1*A5_1
  BA2 =~ 1*A1_2 + 1*A2_2 + 1*A3_2 + 1*A4_2 + 1*A5_2
  BA3 =~ 1*A1_3 + 1*A2_3 + 1*A3_3 + 1*A4_3 + 1*A5_3

  # 状态部分 因子模型
  S1 =~ S1_1 + S1_2 + S1_3
  S2 =~ S2_1 + S2_2 + S2_3
  S3 =~ S3_1 + S3_2 + S3_3
  S4 =~ S4_1 + S4_2 + S4_3
  S5 =~ S5_1 + S5_2 + S5_3
  A1 =~ A1_1 + A1_2 + A1_3
  A2 =~ A2_1 + A2_2 + A2_3
  A3 =~ A3_1 + A3_2 + A3_3
  A4 =~ A4_1 + A4_2 + A4_3
  A5 =~ A5_1 + A5_2 + A5_3

  # 交叉滞后效应
  S2 ~ a1*S1 + b1*A1
  S3 ~ a2*S2 + b2*A2
  S4 ~ a3*S3 + b3*A3
  S5 ~ a4*S4 + b4*A4
  A2 ~ c1*A1 + d1*S1
  A3 ~ c2*A2 + d2*S2
  A4 ~ c3*A3 + d3*S3
  A5 ~ c4*A4 + d4*S4
'
fit <- sem(model, data = data)
summary(fit, standardized = TRUE)
```

#### 2.3.2 在潜在层面包含随机截距

```R
# lavaan 示例代码
model <- '
  # 状态部分 因子模型
  S1 =~ S1_1 + S1_2 + S1_3
  S2 =~ S2_1 + S2_2 + S2_3
  S3 =~ S3_1 + S3_2 + S3_3
  S4 =~ S4_1 + S4_2 + S4_3
  S5 =~ S5_1 + S5_2 + S5_3
  A1 =~ A1_1 + A1_2 + A1_3
  A2 =~ A2_1 + A2_2 + A2_3
  A3 =~ A3_1 + A3_2 + A3_3
  A4 =~ A4_1 + A4_2 + A4_3
  A5 =~ A5_1 + A5_2 + A5_3

  # 随机截距
  BS =~ 1*S1 + 1*S2 + 1*S3 + 1*S4 + 1*S5
  BA =~ 1*A1 + 1*A2 + 1*A3 + 1*A4 + 1*A5

  # 交叉滞后效应
  S2 ~ a1*S1 + b1*A1
  S3 ~ a2*S2 + b2*A2
  S4 ~ a3*S3 + b3*A3
  S5 ~ a4*S4 + b4*A4
  A2 ~ c1*A1 + d1*S1
  A3 ~ c2*A2 + d2*S2
  A4 ~ c3*A3 + d3*S3
  A5 ~ c4*A4 + d4*S4
'
fit <- sem(model, data = data)
summary(fit, standardized = TRUE)
```

为了有意义地比较因素随时间的变化，因素载荷应该是时间不变的，这样就存在了 (至少) 弱因子不变性。

#### 结果解读：

**卡方检验结果：**

*   **显著性结果**：如果卡方差异检验显著，则意味着模型之间的拟合存在显著差异。具体而言，如果具有约束的模型（例如，因子载荷跨时间相等）与未约束的模型相比，拟合显著变差，则意味着跨时间相等约束不成立。这可能表示测量结构随时间变化，使得跨时间点直接比较潜在结构变得复杂。
*   **非显著性结果**：如果卡方差异检验不显著，则意味着具有约束的模型与未约束的模型相比，拟合没有显著差异。这支持了在模型中施加约束（例如，跨时间等同的因子载荷），这增加了模型的简约性，而不显著降低模型的拟合优度。

## 结论

本教程介绍了 RI-CLPM 的三个常见扩展，并提供了使用 `lavaan` 和 Mplus 进行建模的实用指南和代码示例。通过理解这些扩展以及如何使用适当的软件实现它们，研究人员可以更好地利用 RI-CLPM 分析纵向数据，并获得对复杂动态关系的更深入的理解。

# Mplus 示例代码



为了使 Mplus [@Mplus8] 正常工作，请确保将包含模型规范的输入文件 (*example.inp*) 与数据文件 (*example.dat*) 保存在同一文件夹中。 您可以在[此处](https://github.com/jeroendmulder/RI-CLPM/tree/master/data)下载模拟的示例数据集。 Mplus 包含一些默认设置，例如：

* 观察到的和潜在的外生变量是相关的，并且
* 路径模型中观察到的和潜在的结果变量（不预测任何内容）的残差是相关的。

包含这些默认设置是为了简化许多标准 SEM 模型的规范，但它们并非总是在当前的建模上下文中有效。 因此，我们使用命令 `ANALYSIS: MODEL = NOCOV;` 来覆盖这些协方差的默认设置，并将它们全部设置为零。

::: {.callout-tip title="Mplus 残差语言" appearance="simple"}
从 Mplus 8.7 版本开始，残差结构方程建模 (RSEM) 功能得到了扩展 [@asparouhov_residual_2021]。 这使得使用 `^` 命令可以大大简化 RI-CLPM 的模型语法。 您可以在 [残差语法](https://jeroendmulder.github.io/RI-CLPM/mplus.html#Residual_syntax) 部分找到使用此替代 hats 符号的基本 RI-CLPM（包括有时限和无时限的情况）的 Mplus 语法。
:::



## RI-CLPM

要指定 RI-CLPM，我们需要四个部分。

* 一个*组间*部分，由随机截距组成。 它使用 `BY` 命令指定，`RIx BY x1@1 x2@1 ...;`，其中 `@1` 将因子载荷固定为 1。
* 一个*组内*部分，由组内波动组成。 它也使用 `BY` 命令指定，`wx1 BY x1; wx2 BY x2; ...`。 我们不必将因子载荷约束为 1，因为这已经是 Mplus 中潜在变量的第一个指标的因子载荷的默认设置。 但是，我们需要将测量误差方差约束为零，因为当我们使用 `BY` 语句时，Mplus 默认情况下会包含它们。 我们通过包含 `x1@0 x2@0 x3@0 x4@0 x5@0;` 来做到这一点，其中 `@0` 将测量误差方差固定为零，这与说没有测量误差相同。
* 使用 `wx2 ON wx1 wy1; wx3 ON wx2 wy2; ...` 在组内成分之间进行的*滞后回归*。
* 组间和组内部分的相关*协方差*。 在组内部分中，第 1 波的成分及其在第 2 波及以后的残差在每波内是相关的，使用 `wx1 WITH wy1; wx2 WITH wy2;...`。 对于组间部分，我们必须指定随机截距使用 `RIx WITH RIy;` 相关。

::: {.panel-tabset}
## 基本模型
下面给出了指定基本 RI-CLPM 的语法。

```default
TITLE:	    The basic RI-CLPM, 5 waves. 
       
DATA:       FILE = RICLPM.dat;
                    
VARIABLE:   NAMES = x1-x5 y1-y5;
    
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
        
MODEL:      ! Create between components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;
        
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1; 
            wx5 BY x5@1;
            
            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1; 
            wy5 BY y5@1;
    
            ! Constrain measurement error variances to 0
            x1-y5@0;
    
            ! Estimate lagged effects between within-person centered variables
            wx2 wy2 ON wx1 wy1;
            wx3 wy3 ON wx2 wy2;
            wx4 wy4 ON wx3 wy3;
            wx5 wy5 ON wx4 wy4;
    
            ! Estimate covariance between random intercepts
            RIx WITH RIy;
    
            ! Estimate covariance between within-person components at first wave
            wx1 WITH wy1;
                
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations)
            wx2 WITH wy2;
            wx3 WITH wy3; 
            wx4 WITH wy4;
            wx5 WITH wy5; 
                
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```

## 随时间推移的约束
通过给参数添加标签，并对您想要约束为相等的参数使用相同的标签，可以实现对模型的约束。 通过在参数后添加 `(label)` 来指定标签。 下面我们指定一个具有以下约束的 RI-CLPM：

* 随时间推移的固定自回归和交叉滞后关系，`(a b c d)`，
* 组内部分中随时间不变的（残差）（共）方差 `(cov)`、`(vx)` 和 `(vy)`，以及
* 随时间推移的约束总均值，`(mx)` 和 `(my)`。

```default
TITLE:	    The basic RI-CLPM, 5 waves. 
            Constrain the grand means, (residual) variances, and 
            lagged effects over time.   
    
DATA:       FILE = RICLPM.dat;  
                
VARIABLE:   NAMES = x1-x5 y1-y5;
    
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
        
MODEL:	    ! Create between components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;
      
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1; 
            wx5 BY x5@1;
                
            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1; 
            wy5 BY y5@1;
    
            ! Constrain measurement error variances to 0
            x1-y5@0;
    
            ! Estimate lagged effects between within-person centered variables
            wx2 wy2 ON wx1 wy1 (a b c d);
            wx3 wy3 ON wx2 wy2 (a b c d);
            wx4 wy4 ON wx3 wy3 (a b c d);
            wx5 wy5 ON wx4 wy4 (a b c d);
  
            ! Estimate covariance between random intercepts
            RIx WITH RIy;
    
            ! Estimate covariance between within-person components at the first wave
            wx1 WITH wy1;
                
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations) and constrain these and residual variances to be 
            ! invariant over time
            wx2 WITH wy2 (cov); wx2 (vx); wy2 (vy);
            wx3 WITH wy3 (cov); wx3 (vx); wy3 (vy);
            wx4 WITH wy4 (cov); wx4 (vx); wy4 (vy); 
            wx5 WITH wy5 (cov); wx5 (vx); wy5 (vy);

            ! Constrain grand means to be invariant over time
            [x1 x2 x3 x4 x5] (mx);
            [y1 y2 y3 y4 y5] (my);
                
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```

## 约束 *标准化* 滞后效应
与对随时间推移的非标准化自回归和交叉滞后关系施加约束不同，我们可以对标准化滞后效应施加约束，如[FAQ](https://jeroendmulder.github.io/RI-CLPM/faq.html#Standardization)中所述。 与基本模型相比，语法有多个变化。 首先，我们自由估计将观测变量链接到组内成分的因子载荷，而不是将它们固定为 1：

```default
! Create within-components with freely estimated factor loadings
wx1 BY x1*; 
wx2 BY x2*;
wx3 BY x3*; 
wx4 BY x4*; 
wx5 BY x5*;
                
wy1 BY y1*; 
wy2 BY y2*;
wy3 BY y3*; 
wy4 BY y4*; 
wy5 BY y5*;
```

其次，我们将第一波的组内成分的方差设置为 1，并标记它们之间的协方差（现在也是相关性）：

```default
! Set variances of within-components at first wave to 1
wx1@1 wy1@1;

! Estimate correlation between within-components at first wave
wx1 WITH wy1 (cor1);
```

第三，我们为每个组内成分之间的残差方差和协方差提供唯一的标签：

```default
wx2 WITH wy2 (rcov2); wx2 (rvx2); wy2 (rvy2);
wx3 WITH wy3 (rcov3); wx3 (rvx3); wy3 (rvy3);
wx4 WITH wy4 (rcov4); wx4 (rvx4); wy4 (rvy4); 
wx5 WITH wy5 (rcov5); wx5 (rvx5); wy5 (rvy5);
```

最后，我们计算每个波中 *组内成分本身* 之间的相关性，然后约束残差方差以确保每个组内成分的总方差等于 1。 这在 `MODEL CONSTRAINT` 命令中完成：

```default
MODEL CONSTRAINT:
  ! Compute correlations of within-components at each wave
  NEW(cor2);
  NEW(cor3);
  NEW(cor4);
  
  cor2 = a*c + b*d + a*d*cor1 + b*c*cor1 + rcov2;
  cor3 = a*c + b*d + a*d*cor2 + b*c*cor2 + rcov3;
  cor4 = a*c + b*d + a*d*cor3 + b*c*cor3 + rcov4;
 
  ! Contrain residual variances of within-components such that variance of each 
  ! within-component equals 1
  rvx2 = 1 - (a*a + b*b + 2*a*b*cor1);
  rvy2 = 1 - (c*c + d*d + 2*c*d*cor1);
  rvx3 = 1 - (a*a + b*b + 2*a*b*cor2);
  rvy3 = 1 - (c*c + d*d + 2*c*d*cor2);
  rvx4 = 1 - (a*a + b*b + 2*a*b*cor3);
  rvy4 = 1 - (c*c + d*d + 2*c*d*cor3);
  rvx5 = 1 - (a*a + b*b + 2*a*b*cor4);
  rvy5 = 1 - (c*c + d*d + 2*c*d*cor4);

```
:::


## 扩展 1：包括随时间不变的预测变量和结果变量
使用下面的选项卡导航到 RI-CLPM 的模型规范，其中包含

* 观察变量随时间不变的预测变量 $z_{1}$（$z_{1}$ $\rightarrow$ 观察到的），
* 随机截距随时间不变的预测变量 $z_{1}$（$z_{1}$ $\rightarrow$ RIs），
* 随机截距预测随时间不变的结果 $z_{2}$（RIs $\rightarrow$ $z_{2}$），或者
* 组内成分预测随时间不变的结果 $z_{2}$（组内 $\rightarrow$ $z_{2}$）。

::: {.panel-tabset}
## $z_{1}$ $\rightarrow$ 观察到的
下面您可以找到 RI-CLPM 的语法，其中包含 5 个波，以及观察到的变量随时间不变的预测变量 $z_{1}$。 $z_{1}$ 对观察到的变量的影响被约束为在各个波中相同。

```default
TITLE:	    RI-CLPM, 5 waves, including a time-invariant predictor for
            the observed variables. 
       
DATA:       FILE = RICLPM-Z.dat;
                
VARIABLE:   NAMES = x1-x5 y1-y5 z2 z1;
            USEVARIABLES = x1-y5 z1;
        
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
        
MODEL:      ! Create between components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;
    
            ! Estimate covariance between random intercepts
            RIx WITH RIy;
    
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1;
            wx5 BY x5@1;
    
            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1;
            wy5 BY y5@1;

            ! Constrain measurement error variances to 0
            x1-y5@0;

            ! Regression of observed variables on z1 (unconstrained)
            x1-x5 ON z1 (s1);
            y1-y5 ON z1 (s2);

            ! Estimate lagged effects between within-person centered variables
            wx2 wy2 ON wx1 wy1;
            wx3 wy3 ON wx2 wy2;
            wx4 wy4 ON wx3 wy3;
            wx5 wy5 ON wx4 wy4;

            ! Estimate covariance between within-person components at first wave 
            wx1 WITH wy1;
           
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations)
            wx2 WITH wy2;
            wx3 WITH wy3; 
            wx4 WITH wy4; 
            wx5 WITH wy5;
  
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```

## $z_{1}$ $\rightarrow$ RIs
下面您可以找到 RI-CLPM 的语法，其中包含 5 个波，以及随机截距随时间不变的预测变量 $z_{1}$。

```default
TITLE:	    RI-CLPM, 5 waves, including a time-invariant predictor for
            the random intercepts. 
       
DATA:       FILE = RICLPM-Z.dat;
                  
VARIABLE:   NAMES = x1-x5 y1-y5 z2 z1;
            USEVARIABLES = x1-y5 z1;
        
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
        
MODEL:      ! Create between components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;
    
            ! Estimate covariance between random intercepts
            RIx WITH RIy;
    
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1;
            wx5 BY x5@1;

            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1;
            wy5 BY y5@1;
    
            ! Constrain measurement error variances to 0
            x1-y5@0;
    
            ! Regression of random intercepts on z1
            RIx RIy ON z1;
    
            ! Estimate lagged effects between within-person centered variables
            wx2 wy2 ON wx1 wy1;
            wx3 wy3 ON wx2 wy2;
            wx4 wy4 ON wx3 wy3;
            wx5 wy5 ON wx4 wy4;
  
            ! Estimate covariance between within-person components at first wave 
            wx1 WITH wy1;
               
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations)
            wx2 WITH wy2;
            wx3 WITH wy3; 
            wx4 WITH wy4; 
            wx5 WITH wy5;
  
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```

## RIs $\rightarrow$ $z_{2}$
下面您可以找到 RI-CLPM 的语法，其中包含 5 个波，以及预测随时间不变的结果 $z_{2}$ 的随机截距。 

```default
TITLE:	    RI-CLPM, 5 waves.
	          Time-invariant predictor z1 for observed variables (constrained).
	          Between components predicting time-invariant outcome z2.
       
DATA:       FILE = RICLPM-Z.dat;
                  
VARIABLE:   NAMES = x1-x5 y1-y5 z2 z1;
        
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
    
MODEL:      ! Create between components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;
    
            ! Estimate covariance between random intercepts
            RIx WITH RIy;
    
            ! Regres distal outcome on random intercepts
            z2 ON RIx RIy;
                
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1;
            wx5 BY x5@1;
  
            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1;
            wy5 BY y5@1;
    
            ! Constrain measurement error variances to 0
            x1-y5@0;
  
            ! Regression of observed variables on z1 (constrained)
            x1-x5 ON z1 (s1);
            y1-y5 ON z1 (s2);
    
            ! Estimate lagged effects between within-person centered variables
            wx2 wy2 ON wx1 wy1;
            wx3 wy3 ON wx2 wy2;
            wx4 wy4 ON wx3 wy3;
            wx5 wy5 ON wx4 wy4;
    
            ! Estimate covariance between within-person components at first wave 
            wx1 WITH wy1;
           
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations)
            wx2 WITH wy2;
            wx3 WITH wy3; 
            wx4 WITH wy4; 
            wx5 WITH wy5;
    
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```

## 组内 $\rightarrow$ $z_{2}$
下面您可以找到 RI-CLPM 的语法，其中包含 5 个波，以及预测随时间不变的结果 $z_{2}$ 的组内成分。

```default
TITLE:	    RI-CLPM, 5 waves
	          Time-invariant predictor z1 for observed variables (constrained).
	          Within components predicting time-invariant outcome z2.
       
DATA:       FILE = RICLPM-Z.dat;
                  
VARIABLE:   NAMES = x1-x5 y1-y5 z2 z1;
    
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
    
MODEL:      ! Create between-components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;

            ! Estimate covariance between random intercepts
            RIx WITH RIy;
    
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1;
            wx5 BY x5@1;
    
            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1;
            wy5 BY y5@1;
    
            ! Constrain measurement error variances to 0
            x1-y5@0;

	          ! Regres distal outcome on within components
            z2 ON wx1-wx5 wy1-wy5;
            
            ! Regression of observed variables on z1 (constrained)
            x1-x5 ON z1 (s1);
            y1-y5 ON z1 (s2);

            ! Estimate lagged effects between within-person centered variables
            wx2 wy2 ON wx1 wy1;
            wx3 wy3 ON wx2 wy2;
            wx4 wy4 ON wx3 wy3;
            wx5 wy5 ON wx4 wy4;
    
            ! Estimate covariance between within-person components at first wave 
            wx1 WITH wy1;
               
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations)
            wx2 WITH wy2;
            wx3 WITH wy3; 
            wx4 WITH wy4; 
            wx5 WITH wy5;
  
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```
:::

## 扩展 2：多组
使用下面的选项卡导航到基本多组模型的模型规范，或者具有约束滞后参数（以及跨组截距）的模型。

要指定多组 RI-CLPM，我们需要覆盖 Mplus 将施加的一些默认设置，这些默认设置与多组因子分析相关联。 这样做的原因是，当我们结合多组使用 `BY` 语句时，Mplus 会自动施加与强因子不变性相关联的默认设置 [@meredith_measurement_1993]。 这些默认设置是：

* 各组之间的因子载荷相等，
* 各组之间观察到的变量的截距相等，以及
* 第二组（和后续组）中的自由潜在均值。

在多组 RI-CLPM 的上下文中，第一个约束不是问题，因为所有因子载荷都应该在两组中都约束为 1。 但是，对截距的第二个约束以及第二组中潜在均值的释放在这里并不明智。 定义了 `BY` 语句的观测变量将少于潜在变量（即，每个观测变量的组内部分，加上每个变量的随机截距）； 结果，我们将尝试估计比观测到的均值更多的均值。 这样的模型是未识别的。 因此，我们应该覆盖与均值结构相关联的默认设置。 我们通过为第二组添加 `[x1 x2 ...];` 来做到这一点，这释放了第二组中观测到的变量的截距。 此外，我们为第二组添加 `[wx1@0 wx2@0 ... ]; [RIx@0];`，这确保所有潜在均值都固定为零。

::: {.panel-tabset}
## 基本模型
下面您可以找到包含 5 个波的多组 RI-CLPM 的代码。

```default
TITLE:	    Multiple group RI-CLPM, 5 waves. 
            Overruling the Mplus multiple group factor analysis defaults.
                
DATA:       FILE = RICLPM-MG.dat;
                  
VARIABLE:   NAMES = x1-x5 y1-y5 GROUP;
            GROUPING = GROUP (1=G1 2=G2);
        
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
        
MODEL:      ! Create between components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;
        
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1; 
            wx5 BY x5@1;
                
            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1; 
            wy5 BY y5@1;
        
            ! Constrain measurement error variances to 0
            x1-y5@0;
        
            ! Estimate lagged effects between within-person centered variables
            wx2 wy2 ON wx1 wy1;
            wx3 wy3 ON wx2 wy2;
            wx4 wy4 ON wx3 wy3;
            wx5 wy5 ON wx4 wy4;
        
            ! Estimate covariance between random intercepts
            RIx WITH RIy;
        
            ! Estimate covariance between within-person components at first wave
            wx1 WITH wy1;
                    
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations)
            wx2 WITH wy2;
            wx3 WITH wy3; 
            wx4 WITH wy4;
            wx5 WITH wy5; 
        
MODEL G2:   ! Overrule multiple group factor analysis default of equal intercepts 
            ! across groups
            [x1-y5];
              
            ! Overrule multiple group factor analysis default of free latent means 
            ! in second group
            [wx1-wy5@0];
            [RIx@0 RIy@0];
                       
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```

## 约束滞后参数
下面您可以找到多组 RI-CLPM 的代码，包含 5 个波。 滞后参数被约束为在一段时间内相等。

```default
TITLE:	    Multiple group RI-CLPM, 5 waves, with equal lagged parameters 
            across groups. 
            Overruling the Mplus multiple group factor analysis defaults.
                
DATA:       FILE = RICLPM-MG.dat;
                
VARIABLE:   NAMES = x1-x5 y1-y5 GROUP;
            GROUPING = GROUP (1=G1 2=G2);
        
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
    
MODEL:      ! Create between components (random intercepts)
            RIx BY x1@1 x2@1 x3@1 x4@1 x5@1;
            RIy BY y1@1 y2@1 y3@1 y4@1 y5@1;
    
            ! Create within-person centered variables
            wx1 BY x1@1; 
            wx2 BY x2@1;
            wx3 BY x3@1; 
            wx4 BY x4@1; 
            wx5 BY x5@1;
                
            wy1 BY y1@1; 
            wy2 BY y2@1;
            wy3 BY y3@1; 
            wy4 BY y4@1; 
            wy5 BY y5@1;
        
            ! Constrain measurement error variances to 0
            x1-y5@0;
        
            ! Estimate lagged effects between within-person centered variables 
            ! (constrained across groups)
            wx2 wy2 ON wx1 wy1 (a1 b1 c1 d1);
            wx3 wy3 ON wx2 wy2 (a2 b2 c2 d2);
            wx4 wy4 ON wx3 wy3 (a3 b3 c3 d3);
            wx5 wy5 ON wx4 wy4 (a4 b4 c4 d4);
        
            ! Estimate covariance between random intercepts
            RIx WITH RIy;
    
            ! Estimate covariance between within-person components at first wave
            wx1 WITH wy1;
                    
            ! Estimate covariances between residuals of within-person components 
            ! (i.e., innovations)
            wx2 WITH wy2;
            wx3 WITH wy3; 
            wx4 WITH wy4;
            wx5 WITH wy5; 
    
MODEL G2:   ! Overrule multiple group factor analysis default of equal intercepts 
            ! across groups
            [x1-y5];
              
            ! Overrule multiple group factor analysis default of free latent means 
            ! in second group
            [wx1-wy5@0];
            [RIx@0 RIy@0];

            ! Estimate lagged effects between within-person centered variables 
            ! (constrained across groups)
            wx2 wy2 ON wx1 wy1 (a1 b1 c1 d1);
            wx3 wy3 ON wx2 wy2 (a2 b2 c2 d2);
            wx4 wy4 ON wx3 wy3 (a3 b3 c3 d3);
            wx5 wy5 ON wx4 wy4 (a4 b4 c4 d4);
                   
OUTPUT:	    TECH1 STDYX SAMPSTAT CINTERVAL;
```
:::

## 扩展 3：多个指标
使用下面的选项卡导航到多指标 RI-CLPM 的模型规范，包含 5 个波，以及每个变量在每个波中包含 3 个指标。 这五个步骤对应于：

* 配置模型（步骤 1），
* 弱因子不变性（步骤 2），
* 强因子不变性（步骤 3），
* 因子载荷等于组内因子载荷的强因子不变性（额外），以及
* 潜在 RI-CLPM（步骤 4）。

::: {.panel-tabset}
## 步骤 1
当我们有三个指标 $X$，在五个波中测量时，我们指定三个随机截距来捕获每个指标的特质部分，即 `RIX1 BY x11@1 x21@1 ...;`、`RIX2 BY x12@1 x22@1 ...;` 和 `RIX3 BY x13@1 x23@1 ...;`。 此外，我们指定五个组内成分来捕获每个波的状态部分，使用 `WFX1 BY x11 x12 x13; WFX2 BY x21 x22 x23; ...`。

在潜在的组内级别，我们使用 `WFX2 ON WFY1 WFX1; WFX3 ON WFY2 WFX2; ...` 在 Mplus 中指定动态模型。 此外，我们允许第一波的组内因子及其在后续波中的残差在每个波中是相关的，`WFX1 WITH WFY1; WFX2 WITH WFY2; ...`。 允许通过 `RIX1-RIY3 WITH RIX1-RIY3;` 自由地将六个随机截距彼此相关联。

```default
TITLE:      Multiple indicator RI-CLPM, 5 waves, with 3 indicators for 
            each variable at each wave (30 observed variables) and with 
            random intercepts for each indicator separately.
    
DATA:       FILE = RICLPM-MI.dat;
                
VARIABLE:   NAMES = x11 x12 x13 x21 x22 x23 x31 x32 x33 
                    x41 x42 x43 x51 x52 x53 y11 y12 y13 
                    y21 y22 y23 y31 y32 y33 y41 y42 y43 
                    y51 y52 y53;
    
ANALYSIS:   MODEL = NOCOV; ! Sets all default covariances to zero
    
MODEL:      
            !!!!!!!!!!!!!!!!    
            ! BETWEEN PART !
            !!!!!!!!!!!!!!!!
    
            ! Create between factors (random intercepts) for each indicator separately
            RIX1 BY x11@1 x21@1 x31@1 x41@1 x51@1;
            RIX2 BY x12@1 x22@1 x32@1 x42@1 x52@1;
            RIX3 BY x13@1 x23@1 x33@1 x43@1 x53@1;
            
            RIY1 BY y11@1 y21@1 y31@1 y41@1 y51@1;
            RIY2 BY y12@1 y22@1 y32@1 y42@1 y52@1;
            RIY3 BY y13@1 y23@1 y33@1 y43@1 y53@1;

            ! Add covariances between all RIs
            RIX1-RIY3 WITH RIX1-RIY3;
 
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ! WITHIN PART: MEASUREMENT MODEL !
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
            ! Due to having a random intercept per indicator, the measurement model 
            ! is only on the within part of the measurements

            ! Factor models for X at 5 waves
            WFX1 BY x11-x13;
            WFX2 BY x21-x23;
            WFX3 BY x31-x33;
            WFX4 BY x41-x43; 
            WFX5 BY x51-x53;   
            
            ! Factor models for Y at 5 waves
            WFY1 BY y11-y13;
            WFY2 BY y21-y23;
            WFY3 BY y31-y33;
            WFY4 BY y41-y43;
            WFY5 BY y51-y53;

            !!!!!!!!!!!!!!!!!!!!!!!!!
            ! WITHIN PART: DYNAMICS !
            !!!!!!!!!!!!!!!!!!!!!!!!!

            ! Specify lagged effects between within-person centered latent variables
            WFX2 WFY2 ON WFX1 WFY1;
            WFX3 WFY3 ON WFX2 WFY2;
            WFX4 WFY