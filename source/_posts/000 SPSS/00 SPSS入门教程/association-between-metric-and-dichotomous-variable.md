---
title: SPSS：度量变量与二分变量关联分析
date: 2025-06-21 18:42:34
permalink: /2025/06/21/association-between-metric-and-dichotomous-variable/
---

## SPSS教程：度量变量与二分变量之间的关联分析

本教程将展示如何创建美观的表格和图表，以研究一个**二分变量 (Dichotomous Variable)** 和一个**度量变量 (Metric Variable)** 之间的关联。如果满足统计假设，可以进行**独立样本t检验 (Independent Samples T-Test)**。例如，我们将研究 freelancers.sav 数据集中 2010 年收入 (income_2010) 与性别 (gender) 之间是否存在关联：女性和男性受访者的 2010 年平均收入是否相等？

![SPSS Data View Dichotomous and Metric Variable](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-metric-and-dichotomous-variable/medias/c592490ab8139e738eeb.png)

### 快速数据检查

在使用这两个变量之前，首先要确保它们不包含任何意外的值。我们将为度量变量运行**直方图 (Histogram)**，为二分变量运行**频率表 (Frequencies Table)**。一种简便方法是使用 **FREQUENCIES** 命令，如下面的 **SPSS 语法 (SPSS Syntax)** 所示。我们还将对 income_2010 运行 **FORMATS** 命令来隐藏小数位。这将抑制稍后在输出表格中出现过多的位数。注意，可以使用 [Set Decimals for Output Tables Tool](../spss-set-decimals-output-tables/) 轻松实现这一点。

### SPSS 数据检查语法

```spss
* 1. 运行 income_2010 的直方图.
FREQUENCIES income_2010
/FORMAT NOTABLE
/HISTOGRAM.

* 2. 检查 gender 的频率.
FREQUENCIES gender.

* 3. 隐藏 income_2010 中的小数位.
FORMATS income_2010(dollar7).
```

**结论：** 在检查 **输出查看器窗口 (Output Viewer Window)** 中的结果后，未发现任何异常。注意，这两个变量都没有**缺失值 (Missing Values)**。我们可以放心地继续我们的调查。

### SPSS MEANS 表格

现在，我们想分别查看女性和男性的平均收入。这里的方法是使用 **MEANS** 命令。我们使用了一个 **SPSS 表格模板 (.stt file)** 来美化输出表格，该模板隐藏了 “Report” 并显示了 **变量标签 (Variable Label)**，就好像它是一个标题。

```spss
* income_2010 按 gender 的基本 MEANS 表格.
MEANS income_2010 BY gender
/CELLS COUNT MEAN STDDEV.
```

![](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-means-output-styled.png.png)

**结论：** 平均而言，男性受访者在 2010 年的收入比女性受访者多约 5,000 美元。

### SPSS 独立均值的条形图

现在，我们将可视化上一个表格中的平均收入。这里的方法是创建**独立均值的条形图 (Bar Chart for Independent Means)**。以下屏幕截图将引导你完成。

![SPSS Create Bar Chart Basic](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-metric-and-dichotomous-variable/medias/19bcd9c3257a92463479.png)
![SPSS Create Bar Chart Independent Means](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-metric-and-dichotomous-variable/medias/078dc2c3dbf844950d2f.png)

### SPSS 独立均值的条形图语法

完成上述屏幕截图中显示的步骤后，会生成以下语法。结果显示在下一个屏幕截图中。

```spss
* 创建独立均值的条形图.
GRAPH
/BAR(SIMPLE)=MEAN(income_2010) BY gender
/TITLE "2010年按性别划分的平均收入".
```

![SPSS Bar Chart Independent Means](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-metric-and-dichotomous-variable/medias/065d77b11c4ee6672151.png)

### SPSS 条形图样式

虽然我们的图表在技术上是正确的，但它很丑陋，而且不够突出。首先，我们将 gender 的频率添加到其值标签中。我们可以通过在它前面加上 TEMPORARY 来使这种修改恢复，如下一个语法示例中的步骤 1 所示。接下来，我们将通过应用 **SPSS 图表模板 (.sgt file)** 来设置图表样式。在本例中，我们将转置它（“把它放在它的侧面”），并使美元轴从 40,000 美元到 50,000 美元。最终结果（经过一些小的额外调整）显示在以下屏幕截图中。

### SPSS 独立均值的条形图语法

```spss
* 1. 指示值标签命令稍后将被反转.
TEMPORARY.

* 2. 将 N 添加到值标签. "\n" 在两行上中断标签 (图表中 gender 下面的 N).
VALUE LABELS gender
0 '女性\nN = 21'
1 '男性\nN = 19'.

* 3. 重新运行图表. 指示 temporary 命令的结束并反转先前的值标签命令.
GRAPH
/BAR(SIMPLE)=MEAN(income_2010) BY gender
/TITLE "2010年按性别划分的平均收入".
```

![SPSS Bar Chart Independent Means Styled](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-metric-and-dichotomous-variable/medias/027f29ab402554743899.png)

### SPSS 人口金字塔

对于这些数据，另一个不错的图表选项是**人口金字塔 (Population Pyramid)**。它可以可视化度量变量和分类变量之间的关联，但如果后者是二分的，效果最好 - 正好是我们这里的情况。以下屏幕截图将引导你完成。

![SPSS Create Population Pyramid](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-metric-and-dichotomous-variable/medias/d7a8f6e78c034702e756.png)

### SPSS 人口金字塔语法

```spss
* income_2010 按 gender 的人口金字塔.
XGRAPH CHART=[HISTOBAR] BY income_2010[s] BY gender[c]
/COORDINATE SPLIT=YES.
```

![SPSS Population Pyramid](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-population-pyramid-unstyled.png.png)

**结论：** 女性受访者更经常拥有 30,000 美元到 40,000 美元之间的收入，而不是男性。反过来，男性受访者更经常拥有 60,000 美元到 80,000 美元之间的收入，而不是女性。这些是最显著的差异，解释了观察到的平均差异。

### SPSS 人口金字塔样式

就像我们的条形图一样，我们将滥用 gender 的变量标签作为标题，我们将再次在它前面加上 TEMPORARY。我们将使用 **SPSS 图表模板** 添加更多样式。

*对我们的假标题和值标签（“男性”和“女性”）进行样式设置非常困难，因为它无法通过图表模板来完成。如果你不想手动进行，你需要深入研究图表的源代码，可能需要使用 Python 脚本。以下屏幕截图显示了我们的最终结果。*

```spss
* 1. 指示以下数据修改稍后将被反转.
TEMPORARY.

* 2. 暂时将图表标题设置为变量标签.
VARIABLE LABELS gender '2010年按性别划分的收入分布'.

* 3. 运行图表，然后结束 temporary 并反转先前的命令.
XGRAPH CHART=[HISTOBAR] BY income_2010[s] BY gender[c]
/COORDINATE SPLIT=YES.
```

![SPSS Population Pyramid](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-population-pyramid-styled.png.png)

