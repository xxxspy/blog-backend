---
title: mplus做混合增长模型GMM时没有输出CFI等拟合指标
date: 2025-02-21 22:09:17
tags: [GMM, 混合增长模型, 纵向数据分析, Mplus, 潜在类别分析]
---



在使用 Mplus 进行混合增长模型 (GMM) 分析时，经常会遇到输出结果中缺少 CFI (Comparative Fit Index) 的情况。这并非总是模型错误或不合理的信号，而是与 GMM 的复杂性、所选的估计方法以及 CFI 本身的适用性有关。

<!-- more -->

**1. MLR 估计器与 CFI：**

*   当在 Mplus 中使用 `ESTIMATOR = MLR;` (Maximum Likelihood with Robust standard errors) 时，CFI 通常不会被输出。
*   MLR 是一种稳健的估计方法，用于处理数据不满足完全正态性假设的情况。 然而，传统的拟合指数 (如 CFI、TLI、RMSEA 和 SRMR) 最初是为基于正态性假设的最大似然估计 (ML) 设计的。
*   虽然 Mplus 提供了 MLR 的缩放校正，但这些缩放校正并非对所有拟合指数都适用，也就是说，即使进行了缩放校正，CFI 的结果也可能不准确或者没有意义。因此，Mplus 选择不输出 CFI。

**2. GMM 的复杂性：**

*   GMM 模型 inherently 复杂，需要仔细识别 (carefully identified)。模型识别问题仍然是一个重要的考虑因素。
*   传统的卡方检验和基于卡方检验的拟合指数 (包括 CFI) 可能不太适合 GMM，因为模型的复杂性和潜在的局部最优解。

**3. 如何处理 CFI 缺失的情况：**

*   **关注信息标准：** 在 MLR 估计和 GMM 的情况下，AIC (Akaike Information Criterion)、BIC (Bayesian Information Criterion) 和 SABIC (Sample-Size Adjusted BIC) 等信息标准通常是更可靠的模型选择指标。BIC 和 SABIC 在惩罚模型复杂性方面更为严格，在选择 GMM 中的类别数量时可能是有利的。
*   **Entropy：** 检查 Entropy 值，它衡量类别的区分程度。较高的 Entropy 值（接近 1）表明类别区分良好。
*   **BLRT：** 考虑使用 Bootstrap 似然比检验 (BLRT) 来比较具有不同类别数量的模型。BLRT 是一种更适合混合模型的类别数量选择方法。在 Mplus 中，需要包含 `LRTSTARTS` 命令。
*   **检查模型识别：** 仔细检查模型规范，确保增长因子被正确识别。考虑对参数施加理论约束，以帮助模型识别。
*   **增加随机起始值:** 增加随机起始值的数量 (`STARTS` 语句) 可以帮助模型找到更好的解并提高稳定性。
*   **贝叶斯估计 (可选):** 考虑贝叶斯估计，它提供后验预测检查 (PPCs) 来评估模型拟合度。

**4. 如何确定 Mplus 使用了哪个估计器：**

*   **显式指定：** 为了消除歧义，始终在 `ANALYSIS:` 部分显式指定估计器，例如 `ESTIMATOR = ML;` 或 `ESTIMATOR = MLR;`。
*   **Mplus 输出：** 仔细阅读 Mplus 输出的 “SUMMARY OF ANALYSIS” 部分，其中会明确列出实际使用的估计器。
*   **Mplus 用户手册：** 查阅 Mplus 用户手册，了解 `TYPE = MIXTURE` 命令的默认估计器是什么。

**总结：**

在 Mplus 的 GMM 分析中，如果使用 MLR 估计器，CFI 缺失是很常见的现象。这并不一定意味着模型存在问题。应该将重点放在 AIC、BIC、Entropy、BLRT 以及仔细的模型评估上，以获得关于最佳类别数量和模型拟合度的可靠信息。始终查阅 Mplus 用户手册，并仔细检查输出结果，以确保模型规范正确且结果具有可解释性。
