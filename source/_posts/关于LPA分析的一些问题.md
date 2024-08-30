---
title: 关于LPA分析的一些问题
date: 2024-08-30 10:55:53
tags: [lpa, mplus]
mathjax: true
---

这里汇总了关于潜在类别分析的一些问题。

<!-- more -->

### 警告信息

今天有人咨询，关于使用mplus做lpa潜在剖面分析时，mplus提示警告信息：

```
*** WARNING in MODEL command
  All variables are uncorrelated with all other variables within class.
  Check that this is what is intended.
   1 WARNING(S) FOUND IN THE INPUT INSTRUCTIONS
```

关于这个问题，mplus官网已经回复过：

    This message can be ignored with LCA because you want the variables to be uncorrelated.
    ---- Linda K. Muthen

也就说，这个情况没问题，LCA模型本身就假定了变量之间是相互独立，所以这个警告可以忽略。

### LPA 模型假定

为什么LPA假定了变量（观测指标）之间是独立的？关于这个问题我继续阅读了几篇文献，我们要回答这个问题，需要进一步了解LPA模型。

这是模型公式：

<math><msubsup is="true"><mi is="true">σ</mi><mi is="true">i</mi><mn is="true">2</mn></msubsup><mo linebreak="goodbreak" is="true">=</mo><munderover is="true"><mo is="true">∑</mo><mrow is="true"><mi is="true">k</mi><mo is="true">=</mo><mn is="true">1</mn></mrow><mi is="true">K</mi></munderover><msub is="true"><mi is="true">π</mi><mi is="true">k</mi></msub><msup is="true"><mfenced close=")" open="(" is="true"><mrow is="true"><msub is="true"><mi is="true">μ</mi><mi mathvariant="italic" is="true">ik</mi></msub><mo linebreak="badbreak" is="true">−</mo><msub is="true"><mi is="true">μ</mi><mi is="true">i</mi></msub></mrow></mfenced><mn is="true">2</mn></msup><mo linebreak="badbreak" is="true">+</mo><munderover is="true"><mo is="true">∑</mo><mrow is="true"><mi is="true">k</mi><mo is="true">=</mo><mn is="true">1</mn></mrow><mi is="true">K</mi></munderover><msub is="true"><mi is="true">π</mi><mi is="true">k</mi></msub><msubsup is="true"><mi is="true">σ</mi><mi mathvariant="italic" is="true">ik</mi><mn is="true">2</mn></msubsup><mo is="true">,</mo></math>

我们介绍一下潜在剖面分析（Latent Profile Analysis, LPA）的基本假设和模型约束，特别是在处理多维数据时的统计方法。

在LPA中，数据被视为多个分布的混合，这个总体由多个不同的潜在群组（或称为“profile”）组成。对于每个变量i，μik和σik分别表示第k个群组（profile）的特定均值和方差，而πk则表示这个群组的密度，即N个参与者中属于第k个群组的比例。

LPA基于几个关键假设：

1. **混合分布假设**：样本数据是从一个由K个不同群组特定分布混合而成的总体中抽取的。这意味着，观察到的数据是不同群组数据的混合。

2. **正态分布假设**：观察到的指标变量y是正态分布的。这是为了简化统计分析和模型估计。

3. **群组特定均值**：每个群组的特定均值向量μk是该群组在所有观察到的变量上的均值。这反映了不同群组在变量取值上的差异。

然而，如果为每个群组分别估计其均值向量（μk）和协方差矩阵（Σk），那么随着观察变量数量的增加，需要估计的参数数量将迅速增加，从而导致模型过于复杂且难以估计。为了解决这个问题，LPA通常施加两个模型约束：

1. **局部独立性假设**：在给定正确的潜在群组划分的情况下，每个群组内的所有变量y都是不相关的。这意味着每个群组内的协方差矩阵的非对角线元素都是零，即协方差矩阵是对角矩阵。这个假设简化了群组内部变量间的关系，减少了需要估计的参数数量。

2. **同质性假设**：所有群组的协方差矩阵的对角线元素（即各变量的方差）都是相等的。这进一步简化了模型，使得所有群组在变量间的变异性上具有相同的模式，只是均值向量μk不同。因此，可以用一个共同的协方差矩阵Σ来表示所有群组的变异性。

综合这两个假设，LPA模型假设不同群组的协方差矩阵既是对角的又是同质的，即群组之间的差异仅体现在均值向量μk上，而不在变量间的关系形式Σ上。这种模型结构使得LPA能够用较少的参数来捕捉数据中的群组差异和变异性。

因为局部独立性假设的存在， 所以我们需要设定观测指标之间的相关。

### 其他尝试

我们尝试了增加指标之间的相关性， 使用了mplus的WITH命令，但是mplus提示错误：

```
*** ERROR in MODEL command
  No OVERALL or class label for the following MODEL statement(s):
  TS WITH IP CM EA;
```

因为在每个潜在类别下， 相同的观测指标也是不同的变量， 所以无法简单的使用with语句， 必须指定哪个类别或者族群。

### 什么是 熵（entropy）

$$
E=1+\frac{1}{N\log(k)}\biggl(\sum_{i=1}^{N}\sum_{k=1}^{K}P(C=k|U_{i})\log(P(C=k|U_{i}))\biggr)
$$

其中 C 是潜在变量，K 是类别数，N 是样本大小，Ui 是所有潜在类别指示变量的向量，概率 P(C = k|Ui) 是根据估计模型计算得出的。熵越大，潜在类别识别越清晰。熵值介于 0 和 1 之间。熵值接近 1 表示类别分离清晰。

从熵的计算公式可以看出， 概率P越大， 熵值越大， 但是概率P大是什么意思？ P(C = k|Ui) 是根据估计模型计算得出的， 估计了每个潜在类别的条件概率， 当指标取某些值的时候，该样本属于一个类别的概率越大， 那么熵值越大。 

在LPA分析中， 熵值超过0.8 时， 认为该模型拟合度较高， 可以认为该模型拟合了数据， 可以进行后续分析。