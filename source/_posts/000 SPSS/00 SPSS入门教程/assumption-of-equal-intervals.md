---
title: SPSS教程：等距假设及有序变量计算
date: 2025-06-21 18:04:13
permalink: /2025/06/21/assumption-of-equal-intervals/
---

[ ![SPSS tutorials website header logo](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/wp-content-themes-spss-tutorials-11-img-spss-tutorials-logo-44.png.png) SPSS 教程 ](#) [](#) [](#) [](#) 视频课程 基础 方差分析 (ANOVA) 回归分析 (REGRESSION) 因子分析 (FACTOR)

### 入门[](#)

  * 基础
  * 数据准备 (Data Preparation)

### 统计检验 - 入门[](#)

  * 方差分析 (ANOVA)
  * 回归分析 (Regression)
  * 相关分析 (Correlation)
  * T 检验 (T-Tests)
  * 卡方检验 (Chi-Square Tests)

### 统计检验 - 中级[](#)

  * 因子分析 (Factor Analysis)
  * 非参数检验 (Nonparametric Tests)

### 数据分析 (Data Analysis)[](#)

  * SPSS 数据分析
  * SPSS 中的图表 (Charts in SPSS)
  * SPSS 中的表格 (Tables in SPSS)

### 编辑数据 (Editing Data)[](#)

  * SPSS 字符串变量 (SPSS String Variables)
  * SPSS 日期 & 时间变量 (SPSS Date & Time Variables)
  * SPSS 字典教程 (SPSS Dictionary Tutorial)

### Python[](#)

  * SPSS Python 基础 (SPSS Python Basics)

### 其他[](#)

  * SPSS A-Z
  * 统计 A-Z
  * SPSS 工具 (SPSS Tools)
  * SPSS 博客 (SPSS Blog)

## 等距假设 – 对有序变量的计算

作者：Ruben Geert van den Berg

等距假设 (Assumption of Equal Intervals) 指的是，在受访者的感知中，相邻答案类别之间的所有距离都是相等的。这个假设试图证明将有序变量 (Ordinal Variables) 视为如同连续变量 (Metric Variables) 一样是合理的。这样做可以计算有序变量的均值 (Means)、标准差 (Standard Deviations) 和 Pearson 相关系数 (Pearson Correlations)。这比使用更合适的技术要简单。

## 等距假设 - 例子

假设我们有一个变量，旨在衡量客户满意度，并具有以下答案类别：

  * 非常差 (1)
  * 差 (2)
  * 中性 (3)
  * 好 (4)
  * 非常好 (5)

现在我们有两位男性受访者的得分分别为 2 和 4，两位女性受访者的得分都为 3。现在，一位市场人员想知道男性是否比女性更满意或更不满意。但答案是**我们不知道**。这是因为我们不知道“2：差”和“3：中性”之间的差异（或任何其他答案）*在受访者的感知中*是多少。“感知”没有任何固定的测量单位。（由于答案类别的顺序是无可争议的，我们将其视为有序变量。）

## 假设等距

如果假设答案之间的间隔相等，则有序变量将被视为连续变量。现在我们可以简单地计算出，男性的平均得分为 (2 + 4) / 2 = 3，女性的平均得分也为 (3 + 3) / 2 = 3。这回答了我们市场人员提出的“无法回答”的问题。皆大欢喜。或者不是吗？

## 如果假设不成立怎么办？

![等距假设](2025/06/21/000%20SPSS/00%20SPSS入门教程/assumption-of-equal-intervals/medias/da7a29326ad492832ce5.png)等距假设

但是，如果受访者感知到的间隔*不相等*怎么办？假设后者真实地反映在以下值中（见图示）：

  * 非常差 (1)
  * 差 (1.5)
  * 中性 (2.25)
  * 好 (3.5)
  * 非常好 (5)

如果真是这样，那么实际上男性更满意 (1.5 + 3.5) / 2 = 2.5，而女性 (2.25 + 2.25) / 2 = 2.25。因此，先前得出的结论具有误导性。

## 结论

根据某些学术标准，做出等距假设是不合理的做法，并被严格禁止。但是，在现实生活中的研究中（取决于您的领域），这可能非常普遍。至少要意识到这种争议，并记住自己在做什么。

## 告诉我们你的想法！

*必填字段。 您的评论将在版主批准后显示。

## 本教程有 7 条评论：

  * ![](#)

### Biswarup Chatterjee 于 2020 年 9 月 16 日

请在假设等距部分将 2+4/3= 3 的出版错误更正为 2+4/2=3

  * ![](#)

### Ruben Geert van den Berg 于 2020 年 9 月 17 日

嗨 Biswarup，感谢您告知我们本文中的错误！ 您的眼光确实很敏锐，大多数人都没有注意到。

谢谢！

SPSS 教程

展开 [评论](#) | [所有评论](#)

[](#) [1](#) 2

