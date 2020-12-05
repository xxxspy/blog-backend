---
title: T检验和方差分析是等价的-证明过程来了
date: 2020-12-04 19:53:37
tags: [t检验, 方差分析]
mathjax: true
---

我经常纠正童鞋们的错误观念--两样本情况下必须用T检验不能用方差分析, 
这是错误的, 因为两样本情况下T检验和F检验实际上等价的, 也就是结果一样!
我已经用实际的数据做过比较, 请看这个[视频](https://www.bilibili.com/video/BV1gk4y1o7Zw/)。

我一直说我们可以用公式推导的方式证明T检验和F检验是等价的(两分类情况下), 
但是我百度了一下发现找不到这个推导的帖子, 于是我就自己写一下。

<!-- more -->

### F和T的计算公式

F的计算公式:

`$
F_{a-1, N-a} = \frac{MST}{MSE} = \frac{\frac{SST}{a-1}}{\frac{SSE}{N-a}} \tag{1}
$`


 `$t^2$`的计算公式:(注意是t的平方,不是t)

 `$
 t_{k}^2 = \frac{(\bar{y}_{1.} - \bar{y}_{2.})^2}{S_{p}^2(\frac{1}{n_{1}} + \frac{1}{n_{2}})} \tag{2}
 $`

 公式中用到的符号的意义是:

- SSE: Sum of Squares due to Error
- SST: Sum of Squares of Treatment
- a: 处理水平数或者分类数
- `$n_1$`: 第一组的样本量
- `$n_2$`: 第二组的样本量
- N: 总样本量
- `$\bar{y}_i$`: 第i组的平均值
- `$\bar{y}$`: 两组总的的平均值
- `k = N - a`: 自由度

我们的证明思路很清晰, 就是证明`$F=t^2$`, 证明了这个等式, 就意味着我们不管用哪个方法, 最终得到的统计量具有等价性, 
但是有童鞋肯定要怀疑, F和t的平方相等, 但是他们显著性相同吗? 可以负责人的告诉你, 显著性也相同。

### 化简分母MSE

当a=2的时候:

`$
MSE = \frac{SSE}{N-2} = \frac{\sum_{j=1}^{n_1}{(y_{1j} - \bar{y}_{1.})^2} + \sum_{j=1}^{n_2}{(y_{2j} - \bar{y}_{2.})^2}}{N-2} \tag{3}
$`

我们回想一下计算标准差的公式:

`$
S_{i}^2 = \frac{\sum_{j=1}^{n_i}(y_{ij} - \bar{y}_{i.})^2}{n_{i} - 1}
$`

我们可以想到有这样的等式:

`$
(n_{1} - 1) S_{1}^2 = \sum_{j=1}^{n_1}{(y_{1j} - \bar{y}_{1.})^2}
$`

将(3)式用S代替, 就可以得到下面的结果:

`$
\frac{SSE}{N-2} = \frac{(n_{1} - 1) S_{1}^2 + (n_{2} - 1) S_{2}^2}{n_{1} + n_{2} - 2} = S_{p}^2 \tag{4}
$`

熟悉T检验的都知道`$S_{p}^2$`就是联合方差。

### 化简分子MST

当a=2的时候, 分子是这样的:

`$
\frac{SST}{2-1} = SST = \sum_{1}^2 n_{i} (\bar{y}_{i.} - \bar{y}_{..})^2
$`

我们写成这样:

`$
\begin{eqnarray}
SST & = & \sum_{1}^2 n_{i} (\bar{y}_{i.} - \bar{y}_{..})^2 \\
& = & n_{1} (\bar{y}_{1.} - \bar{y}_{..})^2 + n_{2} (\bar{y}_{2.} - \bar{y}_{..})^2 \\
\end{eqnarray} \tag{5}
$`

`$\bar{y}_{..}$`是全体样本的平均值, 那么, 我们换一种形式:

`$
\bar{y}_{..} = \frac{n_{1} \bar{y}_{1.} + n_{2} \bar{y}_{2.}}{N} \tag{6}
$`

我们把(6)式代入(5)式:

`$
SST = \underbrace{n_1 \big[ \bar{y}_{1.} - (\frac{n_1 \bar{y}_{1.} + n_2 \bar{y}_{2.}}{N}) \big]^2}_{\text{Part a}} + \underbrace{n_2 \big[ \bar{y}_{2.} - (\frac{n_1 \bar{y}_{1.} + n_2 \bar{y}_{2.}}{N}) \big]^2}_{\text{Part b}} \tag{7}
$`

#### 化简Part a

Part a 是这样的:

`$
\text{Part a} = n_1 \big[ \bar{y}_{1.} - (\frac{n_1 \bar{y}_{1.} + n_2 \bar{y}_{2.}}{N}) \big]^2
$`

将中括号中的式子化简:

`$
n_1 \big[\frac{N \bar{y}_{1.} - n_1 \bar{y}_{1.} - n_2 \bar{y}_{2.}}{N} \big]^2
$`

提取公因子y1:

`$
n_1 \big[\frac{(N - n_1) \bar{y}_{1.} - n_2 \bar{y}_{2.}}{N} \big]^2
$`

我们知道样本量的计算: `$(N - n_{1}) = n_{2}$`

所以可以接着化简:

`$
n_1 \big[\frac{n_2 \bar{y}_{1.} - n_2 \bar{y}_{2.}}{N} \big]^2
$`

接下来就一目了然了:

`$
\text{Part a} = \frac{n_{1} n_{2}^2}{N^2}  (\bar{y}_{1.} - \bar{y}_{2.})^2
$`

#### 化简Part b

同样的方式可以可到part b的化简:

`$
\text{Part b} = \frac{n_{2} n_{1}^2}{N^2}  (\bar{y}_{2.} - \bar{y}_{1.})^2
$`

#### 代入part a 和part b

我们将(7)式中的part a 和 part b 用化简后的式子代替:

`$
SST = \frac{n_{1} n_{2}^2}{N^2} (\bar{y}_{1.} - \bar{y}_{2.})^2 + \frac{n_{2} n_{1}^2}{N^2} (\bar{y}_{2.} - \bar{y}_{1.})^2 \tag{8}
$`

接着提取公因子:

`$
SST = \underbrace{\big[ \frac{n_{1} n_{2}^2}{N^2} + \frac{n_{2} n_{1}^2}{N^2} \big]}_{\text{Part c}} (\bar{y}_{1.} - \bar{y}_{2.})^2 \tag{9}
$`

#### 化简 part c


`$
\begin{eqnarray}
\text{Part c} & = & \frac{n_{1} n_{2}^2}{N^2} + \frac{n_{2} n_{1}^2}{N^2} \tag{a}\\
& = & {\frac{n_{1} n_{2} (n_{1} + n_{2})}{N^2}}  \tag{b}\\
& = & {\frac{n_{1} n_{2} N}{N^2}}  \tag{c}\\
& = & \frac{n_{1} n_{2}}{N}  \tag{d}\\
& = & \frac{1}{\frac{N}{n_{1} n_{2}}}  \tag{e}\\
& = & \frac{1}{\frac{n_{1} + n_{2}}{n_{1} n_{2}}}  \tag{f}\\
& = & \frac{1}{\frac{1}{n_{1}} + \frac{1}{n_{2}}}  \tag{g}
\end{eqnarray}
$`

最后代入(9)式:

`$
SST = \frac{1}{\frac{1}{n_{1}} + \frac{1}{n_{2}}} (\bar{y}_{1.} - \bar{y}_{2.})^2
$`

### 化简F的计算公式

前面已经计算得到了SSE和SST的化简公式, 分别是(4)式和(10)式, 代入F的计算公式(1):

`$
F_{1, k} = \frac{\frac{SST}{2-1}}{\frac{SSE}{N-2}} = \frac{(\bar{y}_{1.} - \bar{y}_{2.})^2}{S_{p}^2 \big( \frac{1}{n_{1}} + \frac{1}{n_{2}} \big)} = t_{k}^2
$`

然而由于`$F_{1, k}$`的概率密度函数和`$t_{k}^2$`的概率密度函数是一样的, 因此所得到的P值也是相同的。具体证明可以看下图:

<img src="pdf.png">