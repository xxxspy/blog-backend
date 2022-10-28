
---

title: R语言做结构方程模型入门
date: 2022-09-20 12:44:03
tags: [结构方程, r]
toc: true

---


这是用R做结构方程的案例, 最下方有视频教程.

<!--more-->

## 目的

这篇教程目的是介绍如何使用R语言的[lavaan](http://lavaan.ugent.be/)包来做结构方程模型， 
如果你不清楚什么是结构方程（SEM）， 建议你先看这个[介绍视频](https://www.bilibili.com/video/BV17v4y1M7Kk/?spm_id_from=333.788.recommend_more_video.1&vd_source=a196c58475bb84633185dbd4a3bdaf20)。
当然， 我们会在教程的前面简要介绍结构方程的概念， 以便于我们教程的完整性。

## 案例介绍

这是一个研究学生的学业成绩影响因素的研究， 
目前数据已经采集技术， 你可以在[这里下载](https://stats.idre.ucla.edu/wp-content/uploads/2021/02/worland5.csv)这个数据,
这个数据有9个观测指标（9个变量）：Motivation（冬季）, Harmony, Stability, Negative Parental Psychology, SES, Verbal IQ, Reading, Arithmetic and Spelling（动机、和谐、稳定、消极的父母心理、SES、语言智力、阅读、算术和拼写）。研究员假设三个潜变量：Adjustment, Risk, Achievement， 他们的测量指标如下， 其中包含了变量名及其解释：

Adjustment
    - motiv Motivation
    - harm Harmony
    - stabi Stability

Risk
    - ppsych (Negative) Parental Psychology
    - ses SES
    - verbal Verbal IQ


Achievement
    - read Reading
    - arith Arithmetic
    - spell Spelling



### 模型表示

对于任何结构方程研究， 你最好事先绘制理论模型图， 下面就是我们的假定模型图：

<img src="imgs/r-sem-model.png">

根据理论模型， 如果用数学符号表示， 我们可以绘制具有数学意义的模型图：


<img src="imgs/r-sem-model2.png">

我们先来解释一下图中的符号的意义：

- observed variable: 显变量或者叫观测指标， 就是在你的数据中有一列数据可以代表该变量， 图中用矩形表示
- latent variable: 潜变量， 数据中不存在， 但是可以在模型中构建出来，图中用椭圆表示
- exogenous variable: 外生变量， 可以认为是自变量， 就是在模型中没有变量预测它， 它用于预测其他变量， 它既可以是显变量`$x$`也可以是潜变量`$\xi$`
- endogenous variable: 内生变量， 可以认为是因变量， 只要有箭头指向它， 它就可以被成为是内生变量， 即可以是显变量`$y$`也可以是潜变量`$\eta$`
- measurement model: 测量模型， 多个显变量和一个潜变量构成的结构， 比如图中`$\xi_1$`与`$x_1 x_2 x_3$`构成的结构
- factor: 因子， 一个潜变量， 由多个显变量所定义， 例如图中的`$\eta_1 \eta_2 \xi_1$`
- loading: 因子载荷， 因子和观测指标之间的连线， 可以用字母`$\lambda$`表示
- structural model: 由自变量和因变量构成的结构， 比如`$\eta_1 \eta_2 \xi_1$`及其连线构成的结构
- regression path: 回归路径， 自变量和因变量之间的连线， 用字母`$\gamma\$`

## R代码

有了数据和模型， 下一步就是如何用R来表示模型和估计模型。


### 模型的表示

R中最常用的SEM包就是lavaan , 它定义了一些模型表示的方法, 列在这里:


- ~ 波浪号, 表示观测变量的回归关系, `(e.g., y ~ x)`
- =~ 等号波浪号, 用于表示测量模型, `(e.g., f =~ q + r + s)`, f表示潜变量, q r s 表示测量指标
- `~~` 协方差 `(e.g., x ~~ x)`
- ~1 截距或者均值, 比如`x ~ 1`估计了变量x的均值
- `*` 固定参数, 比如`f =~ 1*q`意思是f对q的因子载荷固定为1
- NA* 自由参数或者载荷 `(e.g., f =~ NA*q)`
- a* 参数标签, 比如`f =~ a*q`, 意思是f对q的因子载荷是a, 在设定模型constrants时非常有用

<img src="imgs/r-sem-model.png">

参考这个模型图, 我们有三个潜变量, 每个潜变量有三个测量指标, 测量模型的表示为:

``` r
adjust =~ motiv + harm + stabi
risk =~ verbal + ses + ppsych
achieve =~ read + arith + spell
```

结构方程需要你清楚模型中有多少个因变量, 因为有多少因变量, 就可以写几行回归方程, 识别因变量最好的方法就是看有几个变量被箭头指向,
根据模型图, 我们得出两个回归方程, 结构模型的表示:

``` r
adjust ~ risk 
achieve ~ adjust + risk
```

### R 代码

``` r 
# m6b就是模型代码, 它在R中数据类型是字符串
m6b <- '
# measurement model
adjust =~ motiv + harm + stabi
risk =~ verbal + ses + ppsych
achieve =~ read + arith + spell
# regressions
adjust ~ risk 
achieve ~ adjust + risk
'

# 使用SEM函数, 第一个参数是模型代码, 第二个参数是数据(DataFrame)
fit6b <- sem(m6b, data=dat)

# 使用summary输出结果
summary(fit6b, standardized=TRUE, fit.measures=TRUE)
```

## 实战

### 安装和加载库




```R
install.packages("lavaan", dependencies=TRUE)
library(lavaan)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Installing package into 'C:/Users/syd/AppData/Local/R/win-library/4.2'
(as 'lib' is unspecified)


</div>
{% endraw %}

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
package 'lavaan' successfully unpacked and MD5 sums checked

The downloaded binary packages are in
	C:\Users\syd\AppData\Local\Temp\Rtmpa2kU3N\downloaded_packages

</div>
{% endraw %}

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
This is lavaan 0.6-12
lavaan is FREE software! Please report any bugs.


</div>
{% endraw %}

### 下载数据

这是一个网络数据, 你可以下载到本地, 点[这里](https://stats.idre.ucla.edu/wp-content/uploads/2021/02/worland5.csv),
你也可以直接加载到R中.


```R
dat <- read.csv("https://stats.idre.ucla.edu/wp-content/uploads/2021/02/worland5.csv")
```


```R
head(dat) # 查看数据前几行
```


{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<table class="dataframe">
<caption>A data.frame: 6 × 9</caption>
<thead>
	<tr><th></th><th scope=col>motiv</th><th scope=col>harm</th><th scope=col>stabi</th><th scope=col>ppsych</th><th scope=col>ses</th><th scope=col>verbal</th><th scope=col>read</th><th scope=col>arith</th><th scope=col>spell</th></tr>
	<tr><th></th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><th scope=row>1</th><td>-7.907122</td><td> -5.075312</td><td>-3.138836</td><td>-17.800210</td><td>  4.766450</td><td>-3.633360</td><td>-3.488981</td><td>-9.989121</td><td>-6.567873</td></tr>
	<tr><th scope=row>2</th><td> 1.751478</td><td> -4.155847</td><td> 3.520752</td><td>  7.009367</td><td> -6.048681</td><td>-7.693461</td><td>-4.520552</td><td> 8.196238</td><td> 8.778973</td></tr>
	<tr><th scope=row>3</th><td>14.472570</td><td> -4.540677</td><td> 4.070600</td><td> 23.734260</td><td>-16.970670</td><td>-3.909941</td><td>-4.818170</td><td> 7.529984</td><td>-5.688716</td></tr>
	<tr><th scope=row>4</th><td>-1.165421</td><td> -5.668406</td><td> 2.600437</td><td>  1.493158</td><td>  1.396363</td><td>21.409450</td><td>-3.138441</td><td> 5.730547</td><td>-2.915676</td></tr>
	<tr><th scope=row>5</th><td>-4.222899</td><td>-10.072150</td><td>-6.030737</td><td> -5.985864</td><td>-18.376400</td><td>-1.438816</td><td>-2.009742</td><td>-0.623953</td><td>-1.024624</td></tr>
	<tr><th scope=row>6</th><td> 4.868769</td><td>  3.029841</td><td>-7.648277</td><td> 14.668790</td><td> -2.235039</td><td>-6.826892</td><td> 0.822650</td><td> 5.045174</td><td> 0.904154</td></tr>
</tbody>
</table>

</div>
{% endraw %}


根据前面测量模型的代码, 我们知道, 各个变量的意义, 

- adjust的测量指标是: motiv + harm + stabi
- risk 的测量指标是: verbal + ses + ppsych
- achieve 的测量指标是: read + arith + spell

### 估计模型




```R
# m6b就是模型代码, 它在R中数据类型是字符串
m6b <- '
# measurement model
adjust =~ motiv + harm + stabi
risk =~ verbal + ses + ppsych
achieve =~ read + arith + spell
# regressions
adjust ~ risk 
achieve ~ adjust + risk
'

# 使用SEM函数, 第一个参数是模型代码, 第二个参数是数据(DataFrame)
fit6b <- sem(m6b, data=dat)

# 使用summary输出结果
summary(fit6b, standardized=TRUE, fit.measures=TRUE)
```


{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<dl>
	<dt>$header</dt>
		<dd><dl>
	<dt>$lavaan.version</dt>
		<dd>'0.6-12'</dd>
	<dt>$sam.approach</dt>
		<dd>FALSE</dd>
	<dt>$optim.method</dt>
		<dd>'nlminb'</dd>
	<dt>$optim.iterations</dt>
		<dd>112</dd>
	<dt>$optim.converged</dt>
		<dd>TRUE</dd>
</dl>
</dd>
	<dt>$optim</dt>
		<dd><dl>
	<dt>$estimator</dt>
		<dd>'ML'</dd>
	<dt>$estimator.args</dt>
		<dd><ol>
</ol>
</dd>
	<dt>$optim.method</dt>
		<dd>'nlminb'</dd>
	<dt>$npar</dt>
		<dd>21</dd>
	<dt>$eq.constraints</dt>
		<dd>FALSE</dd>
	<dt>$nrow.ceq.jac</dt>
		<dd>0</dd>
	<dt>$nrow.cin.jac</dt>
		<dd>0</dd>
	<dt>$nrow.con.jac</dt>
		<dd>0</dd>
	<dt>$con.jac.rank</dt>
		<dd>0</dd>
</dl>
</dd>
	<dt>$data</dt>
		<dd><dl>
	<dt>$ngroups</dt>
		<dd>1</dd>
	<dt>$nobs</dt>
		<dd>500</dd>
</dl>
</dd>
	<dt>$test</dt>
		<dd><strong>$standard</strong> = <dl>
	<dt>$test</dt>
		<dd>'standard'</dd>
	<dt>$stat</dt>
		<dd>148.981777928469</dd>
	<dt>$stat.group</dt>
		<dd>148.981777928469</dd>
	<dt>$df</dt>
		<dd>24</dd>
	<dt>$refdistr</dt>
		<dd>'chisq'</dd>
	<dt>$pvalue</dt>
		<dd>0</dd>
</dl>
</dd>
	<dt>$fit</dt>
		<dd><style>
.dl-inline {width: auto; margin:0; padding: 0}
.dl-inline>dt, .dl-inline>dd {float: none; width: auto; display: inline-block}
.dl-inline>dt::after {content: ":\0020"; padding-right: .5ex}
.dl-inline>dt:not(:first-of-type) {padding-left: .5ex}
</style><dl class=dl-inline><dt>npar</dt><dd>21</dd><dt>fmin</dt><dd>0.148981777928469</dd><dt>chisq</dt><dd>148.981777928469</dd><dt>df</dt><dd>24</dd><dt>pvalue</dt><dd>0</dd><dt>baseline.chisq</dt><dd>2597.97194315292</dd><dt>baseline.df</dt><dd>36</dd><dt>baseline.pvalue</dt><dd>0</dd><dt>cfi</dt><dd>0.951216570399027</dd><dt>tli</dt><dd>0.92682485559854</dd><dt>logl</dt><dd>-15517.8567323358</dd><dt>unrestricted.logl</dt><dd>-15443.3658433715</dd><dt>aic</dt><dd>31077.7134646715</dd><dt>bic</dt><dd>31166.2202347384</dd><dt>ntotal</dt><dd>500</dd><dt>bic2</dt><dd>31099.5649367478</dd><dt>rmsea</dt><dd>0.102054633215282</dd><dt>rmsea.ci.lower</dt><dd>0.0866822262014351</dd><dt>rmsea.ci.upper</dt><dd>0.118076367501006</dd><dt>rmsea.pvalue</dt><dd>4.04968328870936e-08</dd><dt>srmr</dt><dd>0.0405618347716423</dd></dl>
</dd>
	<dt>$pe</dt>
		<dd><table class="dataframe">
<caption>A data.frame: 24 × 11</caption>
<thead>
	<tr><th scope=col>lhs</th><th scope=col>op</th><th scope=col>rhs</th><th scope=col>exo</th><th scope=col>est</th><th scope=col>se</th><th scope=col>z</th><th scope=col>pvalue</th><th scope=col>std.lv</th><th scope=col>std.all</th><th scope=col>std.nox</th></tr>
	<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><td>adjust </td><td>=~</td><td>motiv  </td><td>0</td><td> 1.0000000</td><td>0.00000000</td><td>        NA</td><td>          NA</td><td> 9.3236112</td><td> 0.9332948</td><td> 0.9332948</td></tr>
	<tr><td>adjust </td><td>=~</td><td>harm   </td><td>0</td><td> 0.8844138</td><td>0.04061818</td><td> 21.773843</td><td>0.000000e+00</td><td> 8.2459306</td><td> 0.8254189</td><td> 0.8254189</td></tr>
	<tr><td>adjust </td><td>=~</td><td>stabi  </td><td>0</td><td> 0.6947893</td><td>0.04345933</td><td> 15.987116</td><td>0.000000e+00</td><td> 6.4779457</td><td> 0.6484433</td><td> 0.6484433</td></tr>
	<tr><td>risk   </td><td>=~</td><td>verbal </td><td>0</td><td> 1.0000000</td><td>0.00000000</td><td>        NA</td><td>          NA</td><td> 7.3185705</td><td> 0.7325900</td><td> 0.7325900</td></tr>
	<tr><td>risk   </td><td>=~</td><td>ses    </td><td>0</td><td> 0.8070235</td><td>0.07608457</td><td> 10.606927</td><td>0.000000e+00</td><td> 5.9062586</td><td> 0.5912174</td><td> 0.5912174</td></tr>
	<tr><td>risk   </td><td>=~</td><td>ppsych </td><td>0</td><td>-0.7701249</td><td>0.07532976</td><td>-10.223381</td><td>0.000000e+00</td><td>-5.6362132</td><td>-0.5641858</td><td>-0.5641858</td></tr>
	<tr><td>achieve</td><td>=~</td><td>read   </td><td>0</td><td> 1.0000000</td><td>0.00000000</td><td>        NA</td><td>          NA</td><td> 9.4035951</td><td> 0.9413013</td><td> 0.9413013</td></tr>
	<tr><td>achieve</td><td>=~</td><td>arith  </td><td>0</td><td> 0.8372176</td><td>0.03426034</td><td> 24.436932</td><td>0.000000e+00</td><td> 7.8728550</td><td> 0.7880740</td><td> 0.7880740</td></tr>
	<tr><td>achieve</td><td>=~</td><td>spell  </td><td>0</td><td> 0.9760348</td><td>0.02842407</td><td> 34.338325</td><td>0.000000e+00</td><td> 9.1782364</td><td> 0.9187428</td><td> 0.9187428</td></tr>
	<tr><td>adjust </td><td>~ </td><td>risk   </td><td>0</td><td> 0.5992803</td><td>0.07647237</td><td>  7.836560</td><td>4.662937e-15</td><td> 0.4704052</td><td> 0.4704052</td><td> 0.4704052</td></tr>
	<tr><td>achieve</td><td>~ </td><td>adjust </td><td>0</td><td> 0.3747906</td><td>0.04635701</td><td>  8.084875</td><td>6.661338e-16</td><td> 0.3716028</td><td> 0.3716028</td><td> 0.3716028</td></tr>
	<tr><td>achieve</td><td>~ </td><td>risk   </td><td>0</td><td> 0.7243599</td><td>0.07828439</td><td>  9.252929</td><td>0.000000e+00</td><td> 0.5637503</td><td> 0.5637503</td><td> 0.5637503</td></tr>
	<tr><td>motiv  </td><td>~~</td><td>motiv  </td><td>0</td><td>12.8702817</td><td>2.85223254</td><td>  4.512354</td><td>6.411220e-06</td><td>12.8702817</td><td> 0.1289607</td><td> 0.1289607</td></tr>
	<tr><td>harm   </td><td>~~</td><td>harm   </td><td>0</td><td>31.8046281</td><td>2.97294639</td><td> 10.698016</td><td>0.000000e+00</td><td>31.8046281</td><td> 0.3186837</td><td> 0.3186837</td></tr>
	<tr><td>stabi  </td><td>~~</td><td>stabi  </td><td>0</td><td>57.8362265</td><td>3.99023894</td><td> 14.494427</td><td>0.000000e+00</td><td>57.8362265</td><td> 0.5795213</td><td> 0.5795213</td></tr>
	<tr><td>verbal </td><td>~~</td><td>verbal </td><td>0</td><td>46.2385229</td><td>4.78776498</td><td>  9.657643</td><td>0.000000e+00</td><td>46.2385229</td><td> 0.4633119</td><td> 0.4633119</td></tr>
	<tr><td>ses    </td><td>~~</td><td>ses    </td><td>0</td><td>64.9161012</td><td>4.97522402</td><td> 13.047875</td><td>0.000000e+00</td><td>64.9161012</td><td> 0.6504620</td><td> 0.6504620</td></tr>
	<tr><td>ppsych </td><td>~~</td><td>ppsych </td><td>0</td><td>68.0331022</td><td>5.06751791</td><td> 13.425330</td><td>0.000000e+00</td><td>68.0331022</td><td> 0.6816944</td><td> 0.6816944</td></tr>
	<tr><td>read   </td><td>~~</td><td>read   </td><td>0</td><td>11.3724048</td><td>1.60764520</td><td>  7.073952</td><td>1.505907e-12</td><td>11.3724048</td><td> 0.1139519</td><td> 0.1139519</td></tr>
	<tr><td>arith  </td><td>~~</td><td>arith  </td><td>0</td><td>37.8181571</td><td>2.68041969</td><td> 14.109043</td><td>0.000000e+00</td><td>37.8181571</td><td> 0.3789394</td><td> 0.3789394</td></tr>
	<tr><td>spell  </td><td>~~</td><td>spell  </td><td>0</td><td>15.5599796</td><td>1.69864710</td><td>  9.160219</td><td>0.000000e+00</td><td>15.5599796</td><td> 0.1559116</td><td> 0.1559116</td></tr>
	<tr><td>adjust </td><td>~~</td><td>adjust </td><td>0</td><td>67.6938212</td><td>6.06585950</td><td> 11.159807</td><td>0.000000e+00</td><td> 0.7787189</td><td> 0.7787189</td><td> 0.7787189</td></tr>
	<tr><td>risk   </td><td>~~</td><td>risk   </td><td>0</td><td>53.5614747</td><td>6.75713280</td><td>  7.926657</td><td>2.220446e-15</td><td> 1.0000000</td><td> 1.0000000</td><td> 1.0000000</td></tr>
	<tr><td>achieve</td><td>~~</td><td>achieve</td><td>0</td><td>30.6848664</td><td>3.44941260</td><td>  8.895679</td><td>0.000000e+00</td><td> 0.3470055</td><td> 0.3470055</td><td> 0.3470055</td></tr>
</tbody>
</table>
</dd>
</dl>

</div>
{% endraw %}


展示模型的概览:


```R
show(fit6b)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
lavaan 0.6-12 ended normally after 112 iterations

  Estimator                                         ML
  Optimization method                           NLMINB
  Number of model parameters                        21

  Number of observations                           500

Model Test User Model:
                                                      
  Test statistic                               148.982
  Degrees of freedom                                24
  P-value (Chi-square)                           0.000

</div>
{% endraw %}

- 获取模型拟合参数


```R
fits = fitMeasures(fit6b)

fits['rmsea']
```


{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<strong>rmsea:</strong> 0.102054633215282
</div>
{% endraw %}



```R
fits[c('chisq', 'df',  'pvalue', 'cfi' ,'rmsea', 'srmr', 'aic')]
```


{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<style>
.dl-inline {width: auto; margin:0; padding: 0}
.dl-inline>dt, .dl-inline>dd {float: none; width: auto; display: inline-block}
.dl-inline>dt::after {content: ":\0020"; padding-right: .5ex}
.dl-inline>dt:not(:first-of-type) {padding-left: .5ex}
</style><dl class=dl-inline><dt>chisq</dt><dd>148.981777928469</dd><dt>df</dt><dd>24</dd><dt>pvalue</dt><dd>0</dd><dt>cfi</dt><dd>0.951216570399027</dd><dt>rmsea</dt><dd>0.102054633215282</dd><dt>srmr</dt><dd>0.0405618347716423</dd><dt>aic</dt><dd>31077.7134646715</dd></dl>

</div>
{% endraw %}


### 计算中介效应和总效应

我们注意到, 这是一个中介模型, 我们想要检验中介效应以及总效应是否显著, 可以使用下面的代码:




```R
# m6b就是模型代码, 它在R中数据类型是字符串
m6b <- '
# measurement model
adjust =~ motiv + harm + stabi
risk =~ verbal + ses + ppsych
achieve =~ read + arith + spell
# regressions
adjust ~ a*risk # 设置参数a
achieve ~ b*adjust + c*risk # 设置参数b和c

# 中介效应
indirect := a * b
total := a*b + c
'

# 使用SEM函数, 第一个参数是模型代码, 第二个参数是数据(DataFrame)
fit6b <- sem(m6b, data=dat)

# 使用summary输出结果
summary(fit6b, standardized=TRUE, fit.measures=TRUE)
```


{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<dl>
	<dt>$header</dt>
		<dd><dl>
	<dt>$lavaan.version</dt>
		<dd>'0.6-12'</dd>
	<dt>$sam.approach</dt>
		<dd>FALSE</dd>
	<dt>$optim.method</dt>
		<dd>'nlminb'</dd>
	<dt>$optim.iterations</dt>
		<dd>112</dd>
	<dt>$optim.converged</dt>
		<dd>TRUE</dd>
</dl>
</dd>
	<dt>$optim</dt>
		<dd><dl>
	<dt>$estimator</dt>
		<dd>'ML'</dd>
	<dt>$estimator.args</dt>
		<dd><ol>
</ol>
</dd>
	<dt>$optim.method</dt>
		<dd>'nlminb'</dd>
	<dt>$npar</dt>
		<dd>21</dd>
	<dt>$eq.constraints</dt>
		<dd>FALSE</dd>
	<dt>$nrow.ceq.jac</dt>
		<dd>0</dd>
	<dt>$nrow.cin.jac</dt>
		<dd>0</dd>
	<dt>$nrow.con.jac</dt>
		<dd>0</dd>
	<dt>$con.jac.rank</dt>
		<dd>0</dd>
</dl>
</dd>
	<dt>$data</dt>
		<dd><dl>
	<dt>$ngroups</dt>
		<dd>1</dd>
	<dt>$nobs</dt>
		<dd>500</dd>
</dl>
</dd>
	<dt>$test</dt>
		<dd><strong>$standard</strong> = <dl>
	<dt>$test</dt>
		<dd>'standard'</dd>
	<dt>$stat</dt>
		<dd>148.981777928469</dd>
	<dt>$stat.group</dt>
		<dd>148.981777928469</dd>
	<dt>$df</dt>
		<dd>24</dd>
	<dt>$refdistr</dt>
		<dd>'chisq'</dd>
	<dt>$pvalue</dt>
		<dd>0</dd>
</dl>
</dd>
	<dt>$fit</dt>
		<dd><style>
.dl-inline {width: auto; margin:0; padding: 0}
.dl-inline>dt, .dl-inline>dd {float: none; width: auto; display: inline-block}
.dl-inline>dt::after {content: ":\0020"; padding-right: .5ex}
.dl-inline>dt:not(:first-of-type) {padding-left: .5ex}
</style><dl class=dl-inline><dt>npar</dt><dd>21</dd><dt>fmin</dt><dd>0.148981777928469</dd><dt>chisq</dt><dd>148.981777928469</dd><dt>df</dt><dd>24</dd><dt>pvalue</dt><dd>0</dd><dt>baseline.chisq</dt><dd>2597.97194315292</dd><dt>baseline.df</dt><dd>36</dd><dt>baseline.pvalue</dt><dd>0</dd><dt>cfi</dt><dd>0.951216570399027</dd><dt>tli</dt><dd>0.92682485559854</dd><dt>logl</dt><dd>-15517.8567323358</dd><dt>unrestricted.logl</dt><dd>-15443.3658433715</dd><dt>aic</dt><dd>31077.7134646715</dd><dt>bic</dt><dd>31166.2202347384</dd><dt>ntotal</dt><dd>500</dd><dt>bic2</dt><dd>31099.5649367478</dd><dt>rmsea</dt><dd>0.102054633215282</dd><dt>rmsea.ci.lower</dt><dd>0.0866822262014351</dd><dt>rmsea.ci.upper</dt><dd>0.118076367501006</dd><dt>rmsea.pvalue</dt><dd>4.04968328870936e-08</dd><dt>srmr</dt><dd>0.0405618347716423</dd></dl>
</dd>
	<dt>$pe</dt>
		<dd><table class="dataframe">
<caption>A data.frame: 26 × 12</caption>
<thead>
	<tr><th scope=col>lhs</th><th scope=col>op</th><th scope=col>rhs</th><th scope=col>label</th><th scope=col>exo</th><th scope=col>est</th><th scope=col>se</th><th scope=col>z</th><th scope=col>pvalue</th><th scope=col>std.lv</th><th scope=col>std.all</th><th scope=col>std.nox</th></tr>
	<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>
</thead>
<tbody>
	<tr><td>adjust  </td><td>=~</td><td>motiv  </td><td>        </td><td>0</td><td> 1.0000000</td><td>0.00000000</td><td>        NA</td><td>          NA</td><td> 9.3236112</td><td> 0.9332948</td><td> 0.9332948</td></tr>
	<tr><td>adjust  </td><td>=~</td><td>harm   </td><td>        </td><td>0</td><td> 0.8844138</td><td>0.04061818</td><td> 21.773843</td><td>0.000000e+00</td><td> 8.2459306</td><td> 0.8254189</td><td> 0.8254189</td></tr>
	<tr><td>adjust  </td><td>=~</td><td>stabi  </td><td>        </td><td>0</td><td> 0.6947893</td><td>0.04345933</td><td> 15.987116</td><td>0.000000e+00</td><td> 6.4779457</td><td> 0.6484433</td><td> 0.6484433</td></tr>
	<tr><td>risk    </td><td>=~</td><td>verbal </td><td>        </td><td>0</td><td> 1.0000000</td><td>0.00000000</td><td>        NA</td><td>          NA</td><td> 7.3185705</td><td> 0.7325900</td><td> 0.7325900</td></tr>
	<tr><td>risk    </td><td>=~</td><td>ses    </td><td>        </td><td>0</td><td> 0.8070235</td><td>0.07608457</td><td> 10.606927</td><td>0.000000e+00</td><td> 5.9062586</td><td> 0.5912174</td><td> 0.5912174</td></tr>
	<tr><td>risk    </td><td>=~</td><td>ppsych </td><td>        </td><td>0</td><td>-0.7701249</td><td>0.07532976</td><td>-10.223381</td><td>0.000000e+00</td><td>-5.6362132</td><td>-0.5641858</td><td>-0.5641858</td></tr>
	<tr><td>achieve </td><td>=~</td><td>read   </td><td>        </td><td>0</td><td> 1.0000000</td><td>0.00000000</td><td>        NA</td><td>          NA</td><td> 9.4035951</td><td> 0.9413013</td><td> 0.9413013</td></tr>
	<tr><td>achieve </td><td>=~</td><td>arith  </td><td>        </td><td>0</td><td> 0.8372176</td><td>0.03426034</td><td> 24.436932</td><td>0.000000e+00</td><td> 7.8728550</td><td> 0.7880740</td><td> 0.7880740</td></tr>
	<tr><td>achieve </td><td>=~</td><td>spell  </td><td>        </td><td>0</td><td> 0.9760348</td><td>0.02842407</td><td> 34.338325</td><td>0.000000e+00</td><td> 9.1782364</td><td> 0.9187428</td><td> 0.9187428</td></tr>
	<tr><td>adjust  </td><td>~ </td><td>risk   </td><td>a       </td><td>0</td><td> 0.5992803</td><td>0.07647237</td><td>  7.836560</td><td>4.662937e-15</td><td> 0.4704052</td><td> 0.4704052</td><td> 0.4704052</td></tr>
	<tr><td>achieve </td><td>~ </td><td>adjust </td><td>b       </td><td>0</td><td> 0.3747906</td><td>0.04635701</td><td>  8.084875</td><td>6.661338e-16</td><td> 0.3716028</td><td> 0.3716028</td><td> 0.3716028</td></tr>
	<tr><td>achieve </td><td>~ </td><td>risk   </td><td>c       </td><td>0</td><td> 0.7243599</td><td>0.07828439</td><td>  9.252929</td><td>0.000000e+00</td><td> 0.5637503</td><td> 0.5637503</td><td> 0.5637503</td></tr>
	<tr><td>motiv   </td><td>~~</td><td>motiv  </td><td>        </td><td>0</td><td>12.8702817</td><td>2.85223254</td><td>  4.512354</td><td>6.411220e-06</td><td>12.8702817</td><td> 0.1289607</td><td> 0.1289607</td></tr>
	<tr><td>harm    </td><td>~~</td><td>harm   </td><td>        </td><td>0</td><td>31.8046281</td><td>2.97294639</td><td> 10.698016</td><td>0.000000e+00</td><td>31.8046281</td><td> 0.3186837</td><td> 0.3186837</td></tr>
	<tr><td>stabi   </td><td>~~</td><td>stabi  </td><td>        </td><td>0</td><td>57.8362265</td><td>3.99023894</td><td> 14.494427</td><td>0.000000e+00</td><td>57.8362265</td><td> 0.5795213</td><td> 0.5795213</td></tr>
	<tr><td>verbal  </td><td>~~</td><td>verbal </td><td>        </td><td>0</td><td>46.2385229</td><td>4.78776498</td><td>  9.657643</td><td>0.000000e+00</td><td>46.2385229</td><td> 0.4633119</td><td> 0.4633119</td></tr>
	<tr><td>ses     </td><td>~~</td><td>ses    </td><td>        </td><td>0</td><td>64.9161012</td><td>4.97522402</td><td> 13.047875</td><td>0.000000e+00</td><td>64.9161012</td><td> 0.6504620</td><td> 0.6504620</td></tr>
	<tr><td>ppsych  </td><td>~~</td><td>ppsych </td><td>        </td><td>0</td><td>68.0331022</td><td>5.06751791</td><td> 13.425330</td><td>0.000000e+00</td><td>68.0331022</td><td> 0.6816944</td><td> 0.6816944</td></tr>
	<tr><td>read    </td><td>~~</td><td>read   </td><td>        </td><td>0</td><td>11.3724048</td><td>1.60764520</td><td>  7.073952</td><td>1.505907e-12</td><td>11.3724048</td><td> 0.1139519</td><td> 0.1139519</td></tr>
	<tr><td>arith   </td><td>~~</td><td>arith  </td><td>        </td><td>0</td><td>37.8181571</td><td>2.68041969</td><td> 14.109043</td><td>0.000000e+00</td><td>37.8181571</td><td> 0.3789394</td><td> 0.3789394</td></tr>
	<tr><td>spell   </td><td>~~</td><td>spell  </td><td>        </td><td>0</td><td>15.5599796</td><td>1.69864710</td><td>  9.160219</td><td>0.000000e+00</td><td>15.5599796</td><td> 0.1559116</td><td> 0.1559116</td></tr>
	<tr><td>adjust  </td><td>~~</td><td>adjust </td><td>        </td><td>0</td><td>67.6938212</td><td>6.06585950</td><td> 11.159807</td><td>0.000000e+00</td><td> 0.7787189</td><td> 0.7787189</td><td> 0.7787189</td></tr>
	<tr><td>risk    </td><td>~~</td><td>risk   </td><td>        </td><td>0</td><td>53.5614747</td><td>6.75713280</td><td>  7.926657</td><td>2.220446e-15</td><td> 1.0000000</td><td> 1.0000000</td><td> 1.0000000</td></tr>
	<tr><td>achieve </td><td>~~</td><td>achieve</td><td>        </td><td>0</td><td>30.6848664</td><td>3.44941260</td><td>  8.895679</td><td>0.000000e+00</td><td> 0.3470055</td><td> 0.3470055</td><td> 0.3470055</td></tr>
	<tr><td>indirect</td><td>:=</td><td>a*b    </td><td>indirect</td><td>0</td><td> 0.2246047</td><td>0.03257583</td><td>  6.894826</td><td>5.393019e-12</td><td> 0.1748039</td><td> 0.1748039</td><td> 0.1748039</td></tr>
	<tr><td>total   </td><td>:=</td><td>a*b+c  </td><td>total   </td><td>0</td><td> 0.9489646</td><td>0.08175637</td><td> 11.607225</td><td>0.000000e+00</td><td> 0.7385542</td><td> 0.7385542</td><td> 0.7385542</td></tr>
</tbody>
</table>
</dd>
</dl>

</div>
{% endraw %}


## 视频教程

<iframe src="//player.bilibili.com/player.html?bvid=BV1RP411H79W&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="width:900px;height:600px"> </iframe>

> **注意**
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的, 不论什么模型都可以, 只限制于1个研究内. 
> 跟我学统计可以代做分析, 每单几百元不等. 
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](R语言做结构方程模型入门.ipynb)
> 可以在微博上@mlln-cn向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
