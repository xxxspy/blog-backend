---
title: mplus绘制调节效应图
date: 2024-10-18 11:53:20
tags: [mplus, 调节效应]
mathjax: true
---


基于mplus用户指南示例 5.13，以下潜在变量示例给出了一个描述 f1 和 f2 在其对 f3 影响中的交互作用的调节图。

<!-- more -->

回归方程为： `$ f3 = b1 \cdot f1 + b2 \cdot f2 + b3 \cdot f1 \cdot f2 + e $` (1)

假设我们这样看待 f1 和 f2 的交互作用，即 f2 调节 f1 对 f3 的影响（也可以表达为 f1 调节 f2 对 f3 的影响）。
这意味着我们将 (1) 中的回归方程重写为： 

`$ f3 = (b1 + b3 \cdot f2) \cdot f1 + b2 \cdot f2 + e $` (2)

f1 对 f3 的影响受 f2 调节，可以通过显示不同 f2 值下 f1 对 f3 的影响来绘制。

Mplus 输入如下。添加了感叹号以标记相对于示例 5.13 添加或修改的行。

```mplus
TITLE: this is an example of a SEM with
 continuous factor indicators and an
 interaction between two latent variables
DATA: FILE IS ex5.13.dat;
VARIABLE: NAMES ARE y1-y12;
ANALYSIS: TYPE = RANDOM;
 ALGORITHM = INTEGRATION;
MODEL: f1 BY y1-y3*; !
 f2 BY y4-y6*; !
 f1-f2@1; !
 f3 BY y7-y9;
 f4 BY y10-y12; 
 f4 ON f3;
 f3 ON f1 (b1) !
 f2 (b2); !
 f1xf2 | f1 XWITH f2;
 f3 ON f1xf2 (b3); !
OUTPUT: TECH1 TECH8;
Model Constraint: !
 PLOT (lowf2 highf2); !
 LOOP(f1, -3, 3, 0.1); !
 lowf2 = (b1+b3*(-1))*f1+b2*(-1); !
 highf2 = (b1+b3*(+1))*f1+b2*(+1); !
Plot: !
 type = plot2; ! 

```


lowf2 和 highf2 表达式对应于 (2) 中 f2 的值分别为 -1 和 +1。
这给出了 f2 在零均值下方 1 个标准差和上方 1 个标准差时，f1 对 f3 的影响图，绘制范围为 f1 的 -3 个标准差到 +3 个标准差。
这类似于 FAQ 潜在变量交互作用中的图 3。注意，通过将 f1 和 f2 的方差固定为 1 来设置它们的度量单位。
这使得 f2 的值 -1 和 +1 分别对应于零均值下方 1 个标准差和上方 1 个标准差。

图可以通过 Plot 菜单中的 LOOP 绘图选项获得。还提供了 95% 的置信区间。

<img src="mplus-interaction.png">