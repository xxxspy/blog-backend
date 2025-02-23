---
title: 多层线性模型SPSS教程附视频教程
date: 2025-02-24 06:04:43
tags: [hlm, spss]
---



本教程将引导您逐步了解如何使用多层线性模型（Hierarchical Linear Modeling, HLM），也称为混合效应模型或多水平模型，来分析嵌套数据。我们将基于Heck et al. (2014) 第3章的示例进行讲解，该示例探讨了学生数学成绩与学生和学校层面的因素之间的关系。本教程假设您具备基本的统计学知识，并且熟悉SPSS软件的操作。

视频教程在最下方

## 1. 引言：为什么需要多层线性模型？

在教育研究、心理学、社会科学等领域，我们经常遇到嵌套数据。例如，学生嵌套在班级中，班级嵌套在学校中，学校嵌套在学区中。在这种情况下，简单地将所有数据视为独立个体进行分析可能会导致以下问题：

*   **违反独立性假设**：同一学校的学生之间可能存在相关性，而简单线性回归假设个体之间相互独立。
*   **标准误估计不准确**：忽略数据的层次结构会导致标准误估计偏小，从而增加I类错误的概率（错误地拒绝零假设）。
*   **无法解释组间差异**：简单线性回归无法解释不同学校之间的差异，而这些差异可能受到学校层面的因素的影响。

多层线性模型能够有效地解决上述问题。它通过明确地对数据的层次结构进行建模，考虑了组内和组间的变异，从而得到更准确和更全面的分析结果。

## 2. 示例数据描述

本教程使用的示例数据集包含6871名学生，他们嵌套在419所学校中。数据集中的变量包括：

*   **Level 1 (学生层面)**：
    *   `Schcode`: 学校代码。
    *   `Rid`: 学生在给定学校内的ID。
    *   `ID`: 学生在所有学校中的唯一ID。
    *   `Female`: 性别 (0=男性, 1=女性)。
    *   `SES`: 学生社会经济地位。
    *   `Math`: 数学成绩（连续变量）。
*   **Level 2 (学校层面)**：
    *   `SES_mean`: 学校平均社会经济地位。
    *   `Prop47yrc`: 学校中计划上四年制大学的学生比例。
    *   `Public`: 学校类型 (1=公立, 0=其他，如私立)。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_0.png)

我们的目标是回答以下问题：

1.  学生数学成绩是否在不同学校之间存在差异？
2.  学生社会经济地位 (SES) 与数学成绩之间是否存在关系？
3.  SES对数学成绩的影响在学校层面是否会“增强”？其他学校层面的组成因素是否也能预测学生成绩？
4.  学生SES与数学成绩的关系斜率在不同学校之间是否不同？如果存在差异，学校层面的环境因素能否解释这些斜率的变异？

## 3. 单层回归分析：一个不恰当的开始

在开始多层建模之前，让我们先尝试使用单层回归来分析数据，以了解其局限性。我们将建立一个简单的线性回归模型，预测学生数学成绩，仅使用学生SES作为预测变量。

**模型:**

`Math_i = b0 + b1 * SES_i + e_i`

其中:

*   `Math_i`是学生i的数学成绩。
*   `SES_i`是学生i的社会经济地位。
*   `b0`是截距。
*   `b1`是SES的回归系数。
*   `e_i`是残差。

在SPSS中，使用“分析” -> “回归” -> “线性”进行分析。将`Math`作为因变量，`SES`作为自变量。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_2.png)

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%2014%29-3a%20%281%29_3.png)

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_4.png)

**结果解释:**

根据PPT中的结果：

*   R平方=0.143，表明SES解释了数学成绩14.3%的变异，模型整体显著 (F(1, 6869) = 1146.382, p < .001)。
*   SES是一个显著的正向预测因子 (b = 4.255, s.e. = 0.126, p < .001)。这意味着，学生的社会经济地位越高，数学成绩也越高。

**预测方程：**

`Math_i = b0 + 4.255 * SES_i` (其中b0为截距值)

**单层回归的局限性：**

虽然这个模型表明SES与数学成绩之间存在显著关系，但它存在一些关键问题：

1.  **忽略了学校的影响**:  模型假设所有学校的学生都是一样的，忽略了学校可能对学生成绩产生的影响。
2.  **固定效应假设**:  模型将截距和斜率视为固定参数，即对所有学校都是一样的，这可能并不现实。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_5.png)

下图说明了不同学校的学生SES和数学成绩之间的关系可能不同，截距和斜率可能存在变异。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_6.png)

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_7.png)

## 4. 多层线性模型建模步骤

Heck et al. (2014) 推荐的多层模型建模步骤如下：

1.  **步骤1：建立和检验零模型 (Null Model)**:  评估学校层面是否存在显著的变异。
2.  **步骤2：建立和检验Level 1模型**:  加入学生层面的预测变量 (例如，SES)。
3.  **步骤3：建立和检验Level 2模型**:  加入学校层面的预测变量 (例如，学校平均SES)。
4.  **步骤4：建立和检验随机斜率模型（可选）**: 允许学生层面的预测变量的斜率在学校层面变异。

### 4.1 步骤1：建立和检验零模型 (Null Model)

零模型，也称为方差分解模型或随机截距模型，不包含任何预测变量。其目的是确定因变量（本例中为数学成绩）在不同学校之间是否存在显著的变异。

**模型公式：**

*   **Level 1 (学生层面)**： `Math_ij = b0j + e_ij`
*   **Level 2 (学校层面)**： `b0j = g00 + u0j`

其中：

*   `Math_ij`是学校`j`中学生`i`的数学成绩。
*   `b0j`是学校`j`的平均数学成绩 (截距)。
*   `e_ij`是学生层面的随机误差项，假设服从均值为0，方差为σ²的分布。
*   `g00`是所有学校的平均数学成绩 (总体平均数)。
*   `u0j`是学校层面的随机效应，表示学校`j`的平均数学成绩与总体平均数之间的差异，假设服从均值为0，方差为τ²的分布。

**混合模型公式：**

`Math_ij = g00 + u0j + e_ij`

**在SPSS中进行分析：**

1.  选择 "分析" -> "混合模型" -> "线性...".

2.  在弹出的窗口中，选择 `ID` 作为“主体”变量，`Schcode` 作为“重复测量”变量。主体变量指的是最低层级的个体ID，而重复测量是更高层级的ID。
    **注意:** `Schcode`实际上不是重复测量，但是SPSS需要一个重复测量变量才能运行混合模型，在这里将level 2的学校code放入这个位置。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_8.png)

3.  点击 "继续"。

4.  在下一个窗口中，将 `Math` 移到“因变量”框中。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_10.png)

5.  点击 "固定..." 按钮，确保“截距”在模型中，且没有其他变量。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_11.png)

6.  点击 "随机..." 按钮，将 `Schcode` 移到 “组合” 框中。这指定了随机效应的水平。确保“包含截距”已选中。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_12.png)

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_13.png)

7.  点击 "估计" 按钮，将估计方法从 "REML" 改为 "ML"，因为我们要进行模型比较。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_14.png)

8.  点击 "统计..." 按钮，选择 “参数估计”，“协方差参数的检验” 和 “随机效应的协方差”。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_15.png)

9.  点击 “确定” 运行模型。

**结果解释：**

SPSS输出的结果将包含以下关键信息：

*   **固定效应的估计值**：`g00`，即所有学校的平均数学成绩。
*   **随机效应的方差估计**：`σ²` (Level 1残差方差) 和 `τ²` (Level 2截距方差，即学校间变异)。
*   **协方差参数的检验**：检验τ²是否显著大于0。
*   **-2对数似然值 (-2LL)**: 用于模型比较。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_16.png)

如果`τ²`的检验结果显著 (p < 0.05)，则表明学校之间的数学成绩存在显著差异。这意味着，解释学生数学成绩不仅仅需要考虑学生层面的因素，还需要考虑学校层面的因素。

**计算组内相关系数 (ICC)：**

组内相关系数（Intraclass Correlation Coefficient, ICC）用于衡量观测值在组内的聚集程度。它表示总方差中，组间方差所占的比例。

`ICC = τ² / (τ² + σ²)`

在本例中，ICC表示学生数学成绩的总变异中，有多少比例是由学校差异造成的。

![](img%5CTwo-level%20multilevel%20model%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_21.png)

根据PPT，`ICC = 6.515 / (6.515 + 40.679) = 0.138`， 意味着大约13.8%的数学成绩差异存在于学校之间。  通常，ICC值大于0.05被认为是重要的集群效应的指标。

**结论：**

如果 ICC 显著大于 0，说明学生数学成绩在学校层面存在显著的集群效应，这表明使用多层模型是合适的。

### 4.2 步骤2：建立和检验Level 1模型

在步骤2中，我们将在Level 1模型中加入学生层面的预测变量，以解释学生数学成绩的个体差异。在本例中，我们将加入学生社会经济地位 (SES) 作为预测变量。

**模型公式：**

*   **Level 1 (学生层面)**： `Math_ij = b0j + b1 * SES_ij + e_ij`
*   **Level 2 (学校层面)**： `b0j = g00 + u0j`

其中：

*   `Math_ij`是学校`j`中学生`i`的数学成绩。
*   `SES_ij`是学校`j`中学生`i`的社会经济地位。
*   `b0j`是学校`j`的平均数学成绩 (截距)。
*   `b1`是SES的回归系数，假设在所有学校中都是相同的（固定斜率）。
*   `e_ij`是学生层面的随机误差项。
*   `g00`是所有学校的平均数学成绩 (总体平均数)。
*   `u0j`是学校层面的随机效应。

**在SPSS中进行分析：**

1.  打开步骤1中的模型分析界面（如果关闭了SPSS，需要重新按照步骤1操作至第四步）。
2.  将 `SES` 移到 “协变量” 框中。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_23.png)

3.  点击 "固定..." 按钮，确保“截距”和`SES`都在模型中。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_24.png)

4.  点击 “确定” 运行模型。

**结果解释：**

SPSS输出的结果将包含以下关键信息：

*   **固定效应的估计值**：`g00` (总体平均数)，`b1` (SES的回归系数)。
*   **随机效应的方差估计**：`σ²` (Level 1残差方差) 和 `τ²` (Level 2截距方差)。
*   **-2对数似然值 (-2LL)**: 用于模型比较。

![](img%5CTwo-level%20multilevel%20model%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_26.png)

**模型比较：**

为了确定加入SES是否显著提高了模型的拟合度，我们需要将步骤2的模型与步骤1的零模型进行比较。这可以通过似然比检验（Likelihood Ratio Test）来完成。似然比检验的统计量为：

`χ² = -2LL(Model 1) - (-2LL(Model 2))`

其中，Model 1是零模型，Model 2是加入了SES的Level 1模型。该统计量服从自由度为模型参数差异数的卡方分布。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_29.png)

如果似然比检验结果显著 (p < 0.05)，则表明加入SES显著提高了模型的拟合度。

**伪R平方（Pseudo-R-squared）：**

伪R平方用于衡量加入SES后，模型解释的Level 1变异的增加比例。其计算公式为：

`Pseudo-R-squared = (σ²(Model 1) - σ²(Model 2)) / σ²(Model 1)`

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_34.png)

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_35.png)

根据PPT内容，伪R平方为 `(40.679-38.343)/40.679 = 0.057`  表明加入 SES 解释了 5.7% 的学校内部的变异。

**结论：**

如果似然比检验结果显著，且SES的回归系数显著，则表明学生社会经济地位是学生数学成绩的重要预测因素。

### 4.3 步骤3：建立和检验Level 2模型

在步骤3中，我们将在模型中加入学校层面的预测变量，以解释学校之间的平均数学成绩的差异。在本例中，我们将加入学校平均SES (`SES_mean`)、学校中计划上四年制大学的学生比例 (`Prop47yrc`) 和学校类型 (`Public`) 作为预测变量。

**模型公式：**

*   **Level 1 (学生层面)**： `Math_ij = b0j + b1 * SES_ij + e_ij`
*   **Level 2 (学校层面)**： `b0j = g00 + g01 * SES_mean_j + g02 * Prop47yrc_j + g03 * Public_j + u0j`

其中：

*   `Math_ij`是学校`j`中学生`i`的数学成绩。
*   `SES_ij`是学校`j`中学生`i`的社会经济地位。
*   `b0j`是学校`j`的平均数学成绩 (截距)。
*   `b1`是SES的回归系数，假设在所有学校中都是相同的（固定斜率）。
*   `e_ij`是学生层面的随机误差项。
*   `g00`是所有学校的平均数学成绩 (总体平均数)。
*   `SES_mean_j`是学校`j`的平均社会经济地位。
*   `Prop47yrc_j`是学校`j`中计划上四年制大学的学生比例。
*   `Public_j`是学校`j`的类型 (1=公立, 0=其他)。
*   `g01`, `g02`, `g03` 是对应的回归系数。
*   `u0j`是学校层面的随机效应。

**在SPSS中进行分析：**

1.  打开步骤2中的模型分析界面。
2.  将 `SES_mean`、`Prop47yrc` 和 `Public` 移到 “协变量” 框中。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_38.png)

3.  点击 "固定..." 按钮，确保“截距”, `SES`,  `SES_mean`, `Prop47yrc` 和 `Public` 都在模型中。

    ![](img%5CTwo-level%20multilevel%20model%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_39.png)

4.  点击 “确定” 运行模型。

**结果解释：**

SPSS输出的结果将包含以下关键信息：

*   **固定效应的估计值**：`g00`, `b1`,  `g01`, `g02`, `g03`.
*   **随机效应的方差估计**：`σ²` (Level 1残差方差) 和 `τ²` (Level 2截距方差)。
*   **-2对数似然值 (-2LL)**: 用于模型比较。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_43.png)

**模型比较：**

将步骤3的模型与步骤2的模型进行比较，使用似然比检验判断加入Level 2预测变量是否显著提高了模型的拟合度。

**结果分析：**

根据PPT内容，在Level 1，SES是一个显著正向预测因子 (b = 3.19, s.e. = 0.16, p < .001)。在Level 2，学校平均SES (b = 2.47, s.e. = 0.31, p < .001) 和计划上四年制大学的学生比例 (b = 1.42, s.e. = 0.47, p < .001) 也是显著正向预测因子。学校类型 (b = -0.16, s.e. = 0.27, p = .549) 不是显著预测因子。

**结论：**

如果似然比检验结果显著，且Level 2预测变量的回归系数显著，则表明学校层面的因素对学生数学成绩存在显著影响。

### 4.4 步骤4：建立和检验随机斜率模型

在之前的模型中，我们假设学生SES对数学成绩的影响在所有学校中都是相同的（固定斜率）。然而，实际情况可能并非如此。例如，在某些学校，SES对学生成绩的影响可能更大。为了检验这种可能性，我们需要建立一个随机斜率模型，允许学生SES的斜率在不同学校之间变异。

**模型公式：**

*   **Level 1 (学生层面)**： `Math_ij = b0j + b1j * SES_ij + e_ij`
*   **Level 2 (学校层面)**：
    *   `b0j = g00 + g01 * SES_mean_j + g02 * Prop47yrc_j + g03 * Public_j + u0j`
    *   `b1j = g10 + u1j`

其中：

*   `b1j`是学校`j`中SES的回归系数。
*   `g10`是所有学校中SES回归系数的平均值。
*   `u1j`是学校层面的随机效应，表示学校`j`的SES回归系数与总体平均值之间的差异，假设服从均值为0，方差为τ1²的分布。
*   其他变量的含义与之前相同。

**在SPSS中进行分析：**

1.  打开步骤3中的模型分析界面。
2.  点击 "随机..." 按钮。
3.  将 `SES` 移到 “模型” 框中，这指定了SES的斜率可以随机变异。

    ![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_56.png)

4.  点击 “继续” 并运行模型。

**结果解释：**

SPSS输出的结果将包含以下关键信息：

*   **固定效应的估计值**：`g00`, `g01`, `g02`, `g03`, `g10`.
*   **随机效应的方差估计**：`σ²`, `τ²` (截距方差) 和 `τ1²` (SES斜率方差)。
*   **-2对数似然值 (-2LL)**: 用于模型比较。

关键在于检查`τ1²`是否显著大于0。如果检验结果显著 (p < 0.05)，则表明SES的斜率在不同学校之间存在显著差异。

**进一步分析：跨层次交互作用**

如果发现SES的斜率在学校层面存在显著差异，我们可以进一步分析学校层面的哪些因素能够解释这种差异。例如，我们可以检验学校平均SES是否会影响SES对学生成绩的影响。这可以通过添加跨层次交互作用项来实现。

**添加跨层次交互项：**

1. 在步骤4的基础上，在"固定..."对话框中，添加交互项`SES*SES_mean`, `SES*Prop47yrc`, `SES*Public`。 这些项代表学生SES与学校层面变量的交互作用。
2. 再次运行模型。

根据PPT中内容，只有`SES*Public`是显著的交互项，说明学生层面的SES对数学成绩的影响受到学校类型的影响。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_64.png)

我们可以绘制简单斜率图来可视化这种交互作用。

**绘制简单斜率图**

1. 使用PPT提供的Excel计算器计算不同学校类型（公立/私立）下，不同SES水平（低、中、高）的预测数学成绩。这需要SES的均值和标准差，以及模型估计的系数。
2. 使用计算结果在Excel中绘制图表。

结果显示，SES与数学成绩的关系在不同类型的学校中略有不同。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_67.png)

**其他交互作用的探索**

虽然`SES*Prop47yrc`, `SES*SES_mean`的交互项不显著，但也可以绘制相应的图表进行探索。

**加入性别变量**

最后，PPT还演示了加入性别变量（Female）作为 Level 1 预测变量，并允许其斜率在学校间随机变化，并检验 Female 与 School Type (Public) 的跨层次交互作用。结果发现，Female 与 School Type 存在显著的交互作用。

![](img%5CTwo-level%20multilevel%20model%20%28illustration%20from%20chapter%203%20Heck%20et%20al%2C%202014%29-3a%20%281%29_99.png)

使用类似的步骤，可以绘制简单斜率图来可视化这种交互作用。

## 5. 总结

本教程通过一个具体的例子，详细介绍了如何使用多层线性模型分析嵌套数据。我们从简单的零模型开始，逐步加入了学生层面和学校层面的预测变量，并最终建立了随机斜率模型。通过模型比较和结果解释，我们能够更深入地了解学生数学成绩的影响因素，并探索不同学校之间的差异。

希望本教程能够帮助您掌握多层线性模型的基本原理和应用方法。请记住，多层模型是一种非常强大的工具，可以应用于各种领域的研究。

## 视频教程

<iframe src="//player.bilibili.com/player.html?bvid=BV1sjPPepEad&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>
<iframe src="//player.bilibili.com/player.html?bvid=BV1jaPPeGEhW&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>
<iframe src="//player.bilibili.com/player.html?bvid=BV1jaPPeGE4C&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>
<iframe src="//player.bilibili.com/player.html?bvid=BV15iPPezEXQ&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>
<iframe src="//player.bilibili.com/player.html?bvid=BV15iPPezETc&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>
<iframe src="//player.bilibili.com/player.html?bvid=BV15iPPezEtj&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>

<iframe src="//player.bilibili.com/player.html?bvid=BV15iPPezEtj&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>
<iframe src="//player.bilibili.com/player.html?bvid=BV15iPPezE4M&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>
<iframe src="//player.bilibili.com/player.html?bvid=BV1LvPPegEip&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width:800px;height:600px;"> </iframe>

