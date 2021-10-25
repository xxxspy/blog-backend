
---
title: stata教程09-项目反应理论IRT的Rash模型
date: 2018-12-22 17:17:55
tags: [stata]
toc: true
mathjax: true

---

本篇文章主要演示了一下如何使用固定效应的条件逻辑回归模型来估计题目难度。

<span></span>
<!-- more -->

> 本篇文章部分来自于stata的官方文档, 英文好的建议读原文: https://www.stata.com/support/faqs/statistics/rasch-model/

### 背景知识

Rasch模型是心理测量学中二分类题目（例如，选择题只有正确和错误之分）的主要模型之一。设`$y_{ij}$`取值只有(0或者1)，其中`$i=1,...,n$`，n是被试人数，`$j = 1，...，m$`，m是题目的数量。 Rasch模型可以写为logit-linear模型：

`$$
logit P(y_{ij}=1 | \eta_i) = \eta_i − \theta_j
$$`

当将`$\eta$`和`$\theta$`作为参数（固定效应）处理时，人们早就知道最大似然估计在标准的逼近过程中是不一致的（n→无穷大，m是固定的）。我们每多测试一个被试，我们就会多了m个观测数据, 就会有一个额外的`$\eta$`

在20世纪80年代，Andersen展示了`$\theta_j$`的条件极大似然（CML）估计(条件就是每个被试在所有题目上的得分`$y_{i+}$`

心理测量学家也研究了高斯随机效应估计器，这可能只是一个小小的惊喜。从Stata 14开始，使用irt 1pl可以拟合数学上等效的模型。从Stata 13开始，Rasch模型可以使用gsem;见[SEM]例子28g。在Stata 13之前，Rasch模型可以通过随机效果面板估算器拟合，由xtlogit，re命令计算。

### 使用`$\eta$`

考虑最可能的情况;有一个数据集，每一行代表一个被试在所有题上的得分, 每一列代表同一个题目下所有被试的得分。你可以使用clogit中的条件logit固定效应估计器获得Rasch模型的θ参数的CLM估计值（xtlogit，fe相当于键入clogit）。该命令要求所有得分保存为一个变量，而“组”变量用于识别属于同一被试的分数。这可以使用reshape命令完成。最后，可以将Rasch模型描述为具有m个协变量`$x_{ijk}$`，`$k = 1，...，m$`的“clogit模型”，因此对于所有i，如果j = k，则`$x_{ijk}= -1$`(这是因为`$\theta$`的系数为负数), 否则为0。`$x_{ijk}$`的回归系数为`$\theta_k$`

### 案例

想象一下有10题目, 120个学生作答，编码为1（正确）和0（不正确）。我们想知道10个数学问题是否涉及一维尺度，以便无论受试者的能力如何，都可以根据难度对项目进行排序。

加载数据:


```stata
use http://www.stata.com/support/faqs/dta/raschfaq, clear
```


```stata
describe
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

Contains data from http://www.stata.com/support/faqs/dta/raschfaq.dta
  obs:           120                          
 vars:            11                          19 May 2005 07:47
 size:         1,440                          
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
              storage   display    value
variable name   type    format     label      variable label
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
math1           byte    %9.0g      Correct    math item 1
math2           byte    %9.0g      Correct    math item 2
math3           byte    %9.0g      Correct    math item 3
math4           byte    %9.0g      Correct    math item 4
math5           byte    %9.0g      Correct    math item 5
math6           byte    %9.0g      Correct    math item 6
math7           byte    %9.0g      Correct    math item 7
math8           byte    %9.0g      Correct    math item 8
math9           byte    %9.0g      Correct    math item 9
math10          byte    %9.0g      Correct    math item 10
subj_id         int     %9.0g                 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sorted by: 

</div>
{% endraw %}

为了对数据有一个大概的了解, 我们描述一下数据:


```stata
summarize math*
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

    Variable |        Obs        Mean    Std. Dev.       Min        Max
-------------+---------------------------------------------------------
       math1 |        120    .8083333    .3952626          0          1
       math2 |        120        .775    .4193332          0          1
       math3 |        120    .6833333    .4671266          0          1
       math4 |        120         .55    .4995797          0          1
       math5 |        120    .5333333    .5009794          0          1
-------------+---------------------------------------------------------
       math6 |        120         .45    .4995797          0          1
       math7 |        120        .425    .4964157          0          1
       math8 |        120          .3     .460179          0          1
       math9 |        120    .2583333    .4395535          0          1
      math10 |        120    .1666667    .3742406          0          1

</div>
{% endraw %}

为了能够拟合我们的模型, 首先需要reshape我们的数据, 将宽数据转换为长数据, 我们先看下现在的格式(宽格式):


```stata
list in 1/6
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

     +-----------------------------------------------------------------------------------------------------------------------------+
     |   math1     math2       math3       math4       math5       math6       math7       math8       math9      math10   subj_id |
     |-----------------------------------------------------------------------------------------------------------------------------|
  1. | correct   correct     correct   incorrect   incorrect   incorrect   incorrect   incorrect   incorrect   incorrect         1 |
  2. | correct   correct   incorrect   incorrect     correct     correct     correct   incorrect   incorrect   incorrect         2 |
  3. | correct   correct   incorrect   incorrect     correct   incorrect   incorrect   incorrect   incorrect   incorrect         3 |
  4. | correct   correct     correct   incorrect     correct   incorrect     correct   incorrect   incorrect   incorrect         4 |
  5. | correct   correct     correct   incorrect   incorrect     correct     correct     correct   incorrect   incorrect         5 |
     |-----------------------------------------------------------------------------------------------------------------------------|
  6. | correct   correct     correct   incorrect     correct   incorrect   incorrect     correct     correct   incorrect         6 |
     +-----------------------------------------------------------------------------------------------------------------------------+

</div>
{% endraw %}

转换成长格式:


```stata
reshape long math, i(subj_id) j(item)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
(note: j = 1 2 3 4 5 6 7 8 9 10)

Data                               wide   ->   long
-----------------------------------------------------------------------------
Number of obs.                      120   ->    1200
Number of variables                  11   ->       3
j variable (10 values)                    ->   item
xij variables:
                 math1 math2 ... math10   ->   math
-----------------------------------------------------------------------------

</div>
{% endraw %}


```stata
list in 1/30
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

     +----------------------------+
     | subj_id   item        math |
     |----------------------------|
  1. |       1      1     correct |
  2. |       1      2     correct |
  3. |       1      3     correct |
  4. |       1      4   incorrect |
  5. |       1      5   incorrect |
     |----------------------------|
  6. |       1      6   incorrect |
  7. |       1      7   incorrect |
  8. |       1      8   incorrect |
  9. |       1      9   incorrect |
 10. |       1     10   incorrect |
     |----------------------------|
 11. |       2      1     correct |
 12. |       2      2     correct |
 13. |       2      3   incorrect |
 14. |       2      4   incorrect |
 15. |       2      5     correct |
     |----------------------------|
 16. |       2      6     correct |
 17. |       2      7     correct |
 18. |       2      8   incorrect |
 19. |       2      9   incorrect |
 20. |       2     10   incorrect |
     |----------------------------|
 21. |       3      1     correct |
 22. |       3      2     correct |
 23. |       3      3   incorrect |
 24. |       3      4   incorrect |
 25. |       3      5     correct |
     |----------------------------|
 26. |       3      6   incorrect |
 27. |       3      7   incorrect |
 28. |       3      8   incorrect |
 29. |       3      9   incorrect |
 30. |       3     10   incorrect |
     +----------------------------+

</div>
{% endraw %}

按照上面的假设, 我们生成自变量`$x_{ijk}$`, 这k个变量的系数就是(`$\theta_j$`


```stata
forvalues num =1/10{
      gen Th`num' = -(item==`num')
   }
```

看一下现在的数据, 我们得到了Th1-Th10这10个变量, 他们都是自变量, 用于预测math得分。


```stata
list in 1/30
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

     +-----------------------------------------------------------------------------------------+
     | subj_id   item        math   Th1   Th2   Th3   Th4   Th5   Th6   Th7   Th8   Th9   Th10 |
     |-----------------------------------------------------------------------------------------|
  1. |       1      1     correct    -1     0     0     0     0     0     0     0     0      0 |
  2. |       1      2     correct     0    -1     0     0     0     0     0     0     0      0 |
  3. |       1      3     correct     0     0    -1     0     0     0     0     0     0      0 |
  4. |       1      4   incorrect     0     0     0    -1     0     0     0     0     0      0 |
  5. |       1      5   incorrect     0     0     0     0    -1     0     0     0     0      0 |
     |-----------------------------------------------------------------------------------------|
  6. |       1      6   incorrect     0     0     0     0     0    -1     0     0     0      0 |
  7. |       1      7   incorrect     0     0     0     0     0     0    -1     0     0      0 |
  8. |       1      8   incorrect     0     0     0     0     0     0     0    -1     0      0 |
  9. |       1      9   incorrect     0     0     0     0     0     0     0     0    -1      0 |
 10. |       1     10   incorrect     0     0     0     0     0     0     0     0     0     -1 |
     |-----------------------------------------------------------------------------------------|
 11. |       2      1     correct    -1     0     0     0     0     0     0     0     0      0 |
 12. |       2      2     correct     0    -1     0     0     0     0     0     0     0      0 |
 13. |       2      3   incorrect     0     0    -1     0     0     0     0     0     0      0 |
 14. |       2      4   incorrect     0     0     0    -1     0     0     0     0     0      0 |
 15. |       2      5     correct     0     0     0     0    -1     0     0     0     0      0 |
     |-----------------------------------------------------------------------------------------|
 16. |       2      6     correct     0     0     0     0     0    -1     0     0     0      0 |
 17. |       2      7     correct     0     0     0     0     0     0    -1     0     0      0 |
 18. |       2      8   incorrect     0     0     0     0     0     0     0    -1     0      0 |
 19. |       2      9   incorrect     0     0     0     0     0     0     0     0    -1      0 |
 20. |       2     10   incorrect     0     0     0     0     0     0     0     0     0     -1 |
     |-----------------------------------------------------------------------------------------|
 21. |       3      1     correct    -1     0     0     0     0     0     0     0     0      0 |
 22. |       3      2     correct     0    -1     0     0     0     0     0     0     0      0 |
 23. |       3      3   incorrect     0     0    -1     0     0     0     0     0     0      0 |
 24. |       3      4   incorrect     0     0     0    -1     0     0     0     0     0      0 |
 25. |       3      5     correct     0     0     0     0    -1     0     0     0     0      0 |
     |-----------------------------------------------------------------------------------------|
 26. |       3      6   incorrect     0     0     0     0     0    -1     0     0     0      0 |
 27. |       3      7   incorrect     0     0     0     0     0     0    -1     0     0      0 |
 28. |       3      8   incorrect     0     0     0     0     0     0     0    -1     0      0 |
 29. |       3      9   incorrect     0     0     0     0     0     0     0     0    -1      0 |
 30. |       3     10   incorrect     0     0     0     0     0     0     0     0     0     -1 |
     +-----------------------------------------------------------------------------------------+

</div>
{% endraw %}


```stata
summarize math
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

    Variable |        Obs        Mean    Std. Dev.       Min        Max
-------------+---------------------------------------------------------
        math |      1,200        .495    .5001835          0          1

</div>
{% endraw %}

下面就可以进行固定效应条件逻辑回归, `group(subj_id)`用于表示相同的subj_id的数据来自于同一个个体。


```stata
clogit math Th2-Th10, group(subj_id)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
note: multiple positive outcomes within groups encountered.
note: 5 groups (50 obs) dropped because of all positive or
      all negative outcomes.

Iteration 0:   log likelihood = -436.11778  
Iteration 1:   log likelihood =   -435.352  
Iteration 2:   log likelihood = -435.35069  
Iteration 3:   log likelihood = -435.35069  

Conditional (fixed-effects) logistic regression

                                                Number of obs     =      1,150
                                                LR chi2(9)        =     243.80
                                                Prob > chi2       =     0.0000
Log likelihood = -435.35069                     Pseudo R2         =     0.2188

------------------------------------------------------------------------------
        math |      Coef.   Std. Err.      z    P>|z|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         Th2 |    .241266   .3481052     0.69   0.488    -.4410077    .9235397
         Th3 |   .7921615   .3318989     2.39   0.017     .1416515    1.442672
         Th4 |   1.450772   .3241392     4.48   0.000     .8154703    2.086073
         Th5 |   1.528206   .3239802     4.72   0.000     .8932166    2.163195
         Th6 |   1.913438   .3253857     5.88   0.000     1.275694    2.551183
         Th7 |   2.030632   .3265377     6.22   0.000     1.390629    2.670634
         Th8 |   2.662249   .3389274     7.85   0.000     1.997964    3.326535
         Th9 |   2.904665   .3467128     8.38   0.000     2.225121     3.58421
        Th10 |    3.55384   .3771324     9.42   0.000     2.814674    4.293006
------------------------------------------------------------------------------

</div>
{% endraw %}

上面的结果中, 估计得到的系数就是我们需要的`$\theta_j$`


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](stata教程09-项目反应理论IRT的Rash模型.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
