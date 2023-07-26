---
title: 公式推导证明相关系数等于决定系数R方
date: 2023-07-26 12:09:49
tags: [数据分析]
mathjax: true

---

如何用公式证明自变量与因变量的相关系数的平方等于回归中决定系数R方？
前提条件是只有一个自变量的一元线性回归模型，即简单回归。

<!-- more -->

假定有这样一个模型：

`$$
y = \beta_0 + \beta_1 x + \varepsilon, \; \varepsilon_i \sim \mathcal{N}(0, \sigma^2), \; i = 1,\ldots,n
$$`

假定我们使用最小二乘法来求解回归中的回归系数， 这样我们可以得到一个条件， 即决定系数等于自变量与因变量之间的相关系数，

`$$
\label{eq:slr-R2}
R^2 = r_{xy}^2 \; .
$$`

下面是证明过程。

最小二乘法得到参数估计如下：

`$$
\label{eq:slr-ols}
\begin{split}
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1 \bar{x} \\
\hat{\beta}_1 &= \frac{s_{xy}}{s_x^2} \; .
\end{split}
$$`

这样回归模型中的截距(β0)与斜率(β1)都已知了。
并且根据定义， 决定系数定义为自变量解释的方差相对于数据总方差的比例。这可以量化为回归解释的平方和与总平方和的比率：

`$$
\label{eq:slr-R2-s1}
R^2 = \frac{\mathrm{ESS}}{\mathrm{TSS}} \; .
$$`

我们知道因变量的估计值是`$\hat y$`：

`$$
\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_i 
$$`

带入R方的计算公式得到：

`$$
\label{eq:slr-R2-s2}
\begin{split}
R^2 &= \frac{\sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \frac{\sum_{i=1}^{n} (\hat{\beta}_0 + \hat{\beta}_1 x_i - \bar{y})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \; .
\end{split}
$$`

再将β0和β1的计算公式带入， 可以得到：

`$$
\label{eq:slr-R2-s3}
\begin{split}
R^2 &= \frac{\sum_{i=1}^{n} (\bar{y} - \hat{\beta}_1 \bar{x} + \hat{\beta}_1 x_i - \bar{y})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \frac{\sum_{i=1}^{n} \left( \hat{\beta}_1 (x_i - \bar{x}) \right)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \hat{\beta}_1^2 \, \frac{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}{\frac{1}{n-1} \sum_{i=1}^{n} (y_i - \bar{y})^2} \\
&= \hat{\beta}_1^2 \, \frac{s_x^2}{s_y^2} \\ 
&= \left( \frac{s_x}{s_y} \, \hat{\beta}_1 \right)^2 \; .
\end{split}
$$`

根据上面的证明过程， 我们利用相关系数与回归系数的关系（[标准化回归系数等于相关系数](/2023/07/25/回归系数和相关系数的区别和联系/)），可以证明：

`$$
\label{eq:slr-R2-qed}
R^2 = \left( \frac{s_x}{s_y} \, \hat{\beta}_1 \right)^2 = r_{xy}^2 \;
$$`