---
title: MathJax入门
date: 2017-06-02 18:02:32
tags: MathJax, Latex
categoris: 数学
mathjax: true
---

## MathJax简介

MathJax是一款展示数学符号、数学公式的JavaScript库，可以解析Latex、MathML和ASCIIMathML等标记语言，将其渲染成人类可读的公式。今天我在这里总结一点入门的知识点，主要是给自己学习用。

## 公式标记

用符号`$`作为公的开头和结尾，比如`$a \neq b$`可以渲染成`\(a \neq b\)`

## 首先是希腊字母的写法

不同的数学符号都有大小写，都列在下表中。

| 名称	|大写	|Tex	|小写	|Tex
| ----	|----	|---	|----	|-----|-----
|alpha	|`$A$`	| `\(A\)`	|`$\alpha$`	| `\(\alpha\)`
|beta	|`$B$`	|`\(B\)`	|`$\beta$`	|`\(\beta\)`
|gamma	|$\Gamma$	|`\(\Gamma\)`	|$\gamma$	|`\(\gamma\)`
|delta	|$\Delta$	|`\(\Delta\)`	|$\delta$	|`\(\delta\)`
|epsilon	|$E$	|`\(E\)`	|$\epsilon$	|`\(\epsilon\)`
|zeta	|$Z$	|`\(Z\)`	|$\zeta$	|`\(\zeta\)`
|eta	|$H$	|`\(H\)`	|$\eta$	|`\(\eta\)`
|theta	|$\Theta$	|`\(\Theta\)`	|$\theta$	|`\(\theta\)`
|iota	|$I$	|`\(I\)`	|$\iota$	|`\(\iota\)`
|kappa	|$K$	|`\(K\)`	|$\kappa$	|`\(\kappa\)`
|lambda	|$\Lambda$	|`\(\Lambda\)`	|$\lambda$	|`\(\lambda\)`
|mu	|$M$	|`\(M\)`	|$\mu$	|`\(\mu\)`
|nu	|$N$	|`\(N\)`	|$\nu$	|`\(\nu\)`
|xi	|$\Xi$	|`\(\Xi\)`	|$\xi$	|`\(\xi\)`
|omicron	|$O$	|`\(O\)`	|$\omicron$	|`\(\omicron\)`
|pi	|$\Pi$	|`\(\Pi\)`	|$\pi$	|`\(\pi\)`
|rho	|$P$	|`\(P\)`	|$\rho$	|`\(\rho\)`
|sigma	|$\Sigma$	|`\(\Sigma\)`	|$\sigma$	|`\(\sigma\)`
|tau	|$T$	|`\(T\)`	|$\tau$	|`\(\tau\)`
|upsilon	|$\Upsilon$	|`\(\Upsilon\)`	|$\upsilon$	|`\(\upsilon\)`
|phi	|$\Phi$	|`\(\Phi\)`	|$\phi$	|`\(\phi\)`
|chi	|$X$	|`\(X\)`	|$\chi$	|`\(\chi\)`
|psi	|$\Psi$	|`\(\Psi\)`	|$\psi$	|`\(\psi\)`
|omega	|$\Omega $	|`\(\Omega\)`	|$\omega$	|`\(\omega\)`


## 上标与下标

上标和下标分别使用^与_，例如`\(x_i^2\)`显示为`\(x_i^2\)`。默认情况下，上下标符号仅仅对下一个组起作用。一个组即单个字符或者使用`{..}`包裹起来的内容。也就是说，如果使用`10^10`，会得到`\(10^10\)`，而`10^{10}`才是`\(10^{10}\)`。同时，大括号还能消除二义性，如`x^5^6`将得到一个错误`\(x^5^6\)`，必须使用大括号来界定`^`的结合性，如`{x^5}^6`：`\({x^5}^6\)` 或者 `x^{5^6}`：`\(x^{5^6}\)`。

## 括号

- 小括号与方括号：使用原始的( )，[ ]即可，如(2+3)[4+4]：`\((2+3)[4+4]\)`
- 大括号：时由于大括号`{}`被用来分组，因此需要使用`{`和`}`表示大括号，也可以使用`\lbrace` 和`\rbrace`来表示。
如`\{ a*b \}`:  `\(\{a*b\}\)`，`\lbrace a\*b \rbrace`：`\(\lbrace a*b \rbrace\)`。
- 尖括号：使用`\langle` 和 `\rangle`表示左尖括号和右尖括号。如`\langle x \rangle`：`\(\langle x \rangle\)`。
- 上取整：使用`\lceil` 和 `\rceil` 表示。 如，`\lceil x \rceil`：`\(\lceil x \rceil\)`。
- 下取整：使用\lfloor 和 \rfloor 表示。如，\lfloor x \rfloor：`\(\lfloor x \rfloor\)`。

## 常见函数

- 三角函数：\sin x --> `\(\sin x\)` ; \cos a --> `\(\cos a\)` ; \arctan x --> `\(\arctan x\)`
- 极限符号: `\lim_{1\to\infty}` --> `\(\lim_{1\to\infty}\)`

## 常见符号

- 比较运算符：`\lt \gt \le \ge \neq` --> `\(\lt \gt \le \ge \neq\)`
- 箭头符号：`\to \rightarrow \leftarrow \Rightarrow \Leftarrow \mapsto` --> `\(\to \rightarrow \leftarrow \Rightarrow \Leftarrow \mapsto\)`


## 顶部符号

我们有时候需要在字母上方书写符号，用`{}`来表示组合，例如:

- 单字母`\hat xy`--> `\(\hat x\)`
- 多字母`\widehat {xy}` --> `\(\widehat {xy} \)`
- 横线`\overline x` --> `\(\overline x\)`
- 向量`\vec {xy}` --> `\(\vec {xy}\)`
- 点 `\dot x` --> `\(\dot x\)`
- 箭头`\overrightarrow {xy}` --> `\(\overrightarrow {xy}\)`
- 两点 `\ddot x` --> `\(\ddot x\)`

## 求和

`\sum` 用来表示求和符号`\(\sum\)`, 有很多不同的写法：
- 下标表示下限：`\sum_1` --> `\(\sum_1\)`
- 上标表示上限：`\sum^n` --> `\(\sum^n\)`
- 上下结合，可以写为：`\sum_1^n` --> `\(\sum_1^n\)`

## 积分

`\int` 表示积分符号 `\(\int\)`, 和求和符号类似：
- 积分上下限：\int_1^n --> `\(\int_1^n\)`

#### 和积分类似的符号还有以下这些

- 累积 \prod --> `\(\prod\)`
- 并集 \bigcup --> `\(\bigcup\)`
- 交集 \bigcap --> `\(\bigcap\)`
- 二重积分 \iint --> `\(\iint\)`

## 分数和根号

分数用\frac 表示，例如`\frac ab` --> `\(\frac ab\)`, `{}`可以帮助你分组，例如`\frac a{b*c}` --> `\(\frac a{b*c}\)`，带括号的分数`(\frac ab)^2` --> `\((\frac ab)^2\)` 。 还有一种写法是使用\over，例如`1+2 \over 3+4` --> `\(1+2 \over 3+4\)`。

使用\sqrt表示根号，例如 \sqrt[4] x --> `\(\sqrt[4] x\)`。

## 矩阵和表格

使用`\begin{array}{列样式}…\end{array}`这样的形式来创建表格，列样式可以是`clr`表示居中，左，右对齐，还可以使用`|`表示一条竖线。表格中 各行使用`\\`分隔，各列使用`&`分隔。使用`\hline`在本行前加入一条直线。 例如，

```
\begin{array}{c|lcr}
n & \text{Left} & \text{Center} & \text{Right} \\
\hline
1 & 0.24 & 1 & 125 \\
\hline
2 & -1 & 189 & -8 \\
3 & -20 & 2000 & 1+10i \\
\end{array}
```
`\[
\begin{array}{c|lcr}
n & \text{左} & \text{中} & \text{右} \\
\hline
1 & 0.24 & 1 & 125 \\
\hline
2 & -1 & 189 & -8 \\
3 & -20 & 2000 & 1+10i \\
\end{array}
\]`

`
\[J_\alpha(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma (m + \alpha + 1)} {\left({ \frac{x}{2} }\right)}^{2m + \alpha}\]
`























