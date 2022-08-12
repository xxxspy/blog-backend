---
title: R中如何自动整理结果为论文可用格式
date: 2022-08-12 13:11:34
tags: R语言
---


任何曾经为了学术目的或在行业中写作的人都必须处理 APA 格式。
汇报结果的规则和期望似乎是无穷无尽的，而且总是在变化。即便能够掌握几种规则，你仍然必须确定你的格式是否符合期刊的要求。

R 中有一个包，它至少可以消除如何报告方差分析、相关性和回归表的麻烦。这个包被称为“apaTables”。在这篇文章中，我们将看看如何使用这个包来制作根据 APA 格式化的表格。

<!-- more -->

## 加载库

我们将使用“gapminder”数据集创建方差分析、相关性和回归表的示例。下面是我们安装和加载库的代码。

```r
## install.packages("apaTables")
library(apaTables)
library(gapminder)
```

## ANOVA

我们现在先来做另一个ANOVA分析, 你需要使用`lm`函数创建模型, 这是R中做线性模型的通用方法, 

```r
attach(gapminder)
anova = lm(lifeExp ~ continent)
```

使用`apa.aov.table`函数可以创建apa表格, 并输出到word文件, 函数的第一个参数就是anova结果, 我们保存在anova变量中, 
然后使用filename参数指定输出的word文件名.

```r
apa.aov.table(anova, filename = "anova.doc")
```

输出的表格如图:

<img src="anova.png">

## 描述性统计表格

通过上面的例子你已经看到`apaTables`的厉害之处了, 我们实际上有时候还需要在论文里汇报均值和标准差, 
让我们试试下面的代码, 使用函数`apa.1way.table`, 
指定自变量iv, 因变量dv, 数据data, 以及输出的文件名:

```r
apa.1way.table(iv = continent, dv = lifeExp, data = gapminder, 
               filename = "description.doc")
```

输出的表格如图:

<img src="description.png">

我们甚至可以输出更复杂的表格, 比如用`apa.d.table`生成不仅仅有均值标准差, 
还输出任意两个均值的差值d, 及其置信区间:

```r
apa.d.table(iv = continent, dv = lifeExp, data = gapminder, 
            filename = "dvalue.doc")
```

输出的表格如图:

<img src="dvalue.png">

## 相关
我们现在将看一个相关的示例。这个函数是“apa.cor.table”。此函数仅适用于少数变量。否则，表格会变得比单张纸还大。此外，您可能希望抑制置信区间以节省空间。您可以自行探索其他参数。下面是代码

```r
apa.cor.table(gapminder, table.number = 5, show.conf.interval = FALSE, filename = 'corr1.doc')
```

输出的表格如图:

<img src="corr1.png">

显然我们的输出有些不合理, 不需要用到的变量也被计算了相关, 那么我们先做一个变量筛选:



```r
library(dplyr)
apa.cor.table(select(gapminder, lifeExp, pop, gdpPercap), table.number = 5, show.conf.interval = FALSE, filename = 'corr2.doc')
```

输出的表格如图:

<img src="corr2.png">

## 回归

有了上面的例子, 你应该能自己写出回归的代码了, 
但是我们介绍一个新功能, apatables帮你自动整合多个回归的结果:

```r
reg1 = lm(lifeExp ~ pop)
reg2 = lm(lifeExp ~ pop + log(gdpPercap))


apa.reg.table(reg1, reg2, filename='reg.doc', table.number = 6)
```

输出的表格如图:

<img src="reg.png">