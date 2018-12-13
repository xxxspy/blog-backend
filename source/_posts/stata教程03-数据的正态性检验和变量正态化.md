
---
title: stata教程03-数据的正态性检验和变量正态化
date: 2018-12-11 18:17:55
tags: [stata]
toc: true
mathjax: true

---

变量是否符合正态分布? 怎么检验变量的正态分布假设? 如果变量不满足正太分布假设怎么办? 下面我们使用stata来回答以上问题。
<span></span>
<!-- more -->

### 数据介绍

使用stata系统自带的数据auto.dta来演示今天的例子。


```stata
sysuse auto
```

{% raw %}
<div class="output">
输出(stream):<br>
    (1978 Automobile Data)
    <br />
</div>
{% endraw %}

查看数据的基本信息:


```stata
describe
```

{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />Contains data from C:\Program Files (x86)\Stata15\ado\base/a/auto.dta
    <br />  obs:            74                          1978 Automobile Data
    <br /> vars:            12                          13 Apr 2016 17:45
    <br /> size:         3,182                          (_dta has notes)
    <br />---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    <br />              storage   display    value
    <br />variable name   type    format     label      variable label
    <br />---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    <br />make            str18   %-18s                 Make and Model
    <br />price           int     %8.0gc                Price
    <br />mpg             int     %8.0g                 Mileage (mpg)
    <br />rep78           int     %8.0g                 Repair Record 1978
    <br />headroom        float   %6.1f                 Headroom (in.)
    <br />trunk           int     %8.0g                 Trunk space (cu. ft.)
    <br />weight          int     %8.0gc                Weight (lbs.)
    <br />length          int     %8.0g                 Length (in.)
    <br />turn            int     %8.0g                 Turn Circle (ft.)
    <br />displacement    int     %8.0g                 Displacement (cu. in.)
    <br />gear_ratio      float   %6.2f                 Gear Ratio
    <br />foreign         byte    %8.0g      origin     Car type
    <br />---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    <br />Sorted by: foreign
    <br />
</div>
{% endraw %}

### 绘制概率图

绘制变量mpg, 查看变量是否和正太分布相似:


```stata
hist mpg, normal
```

{% raw %}
<div class="output">
输出(stream):<br>
    (bin=8, start=12, width=3.625)
    <br />
</div>
{% endraw %}


![svg](output_8_1.svg)


{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />
    <br />
    <br />
</div>
{% endraw %}

上面的命令中, hist指的是直方图, mpg就是变量名, normal指的是正态密度函数。从图中我们可以看到, 这个数据直方图和正态密度函数的曲线有一些差距, 也可以绘制和密度图:


```stata
kdensity mpg, normal
```


![svg](output_10_0.svg)


绘制变量的QQ图:


```stata
qnorm mpg
```

{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />(note: file C:/Users/syd/.stata_kernel_cache/graph2.svg not found)
    <br />
</div>
{% endraw %}


![svg](output_12_1.svg)


{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />
    <br />
</div>
{% endraw %}

### 进行正态性检验

但是不管绘制哪种图形, 都有一个问题, 我们无法精确的检验数据是否满足正态分布的假设。所以, 我们可以进行JB检验:


```stata
su mpg, detail
```

{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />                        Mileage (mpg)
    <br />-------------------------------------------------------------
    <br />      Percentiles      Smallest
    <br /> 1%           12             12
    <br /> 5%           14             12
    <br />10%           14             14       Obs                  74
    <br />25%           18             14       Sum of Wgt.          74
    <br />
    <br />50%           20                      Mean            21.2973
    <br />                        Largest       Std. Dev.      5.785503
    <br />75%           25             34
    <br />90%           29             35       Variance       33.47205
    <br />95%           34             35       Skewness       .9487176
    <br />99%           41             41       Kurtosis       3.975005
    <br />
</div>
{% endraw %}

su命令有一个detail选项, 使用该选项可以输出偏度和峰度, 从上面的结果可以看到偏度Skewness=.9487176, 峰度Kurtosis=3.975005, 根据这两个值, 我们可以计算JB统计量为:


```stata
di (r(N)/6) * ((r(skewness)^2) + [(1/4)*(r(kurtosis)-3)^2])
```

{% raw %}
<div class="output">
输出(stream):<br>
    14.031924
    <br />
</div>
{% endraw %}

由于JB统计量满足自由度为2的卡方分布, 所以我们可以计算JB统计量所对应的p值:


```stata
di chi2tail(2, 14.031924)
```

{% raw %}
<div class="output">
输出(stream):<br>
    .00089744
    <br />
</div>
{% endraw %}

p值小于1%, 因此拒绝虚无假设, 即数据不满足正太分布的假设。

实际上, JB检验有对应的第三方程序, 我们可以使用下面的命令来安装这个程序:


```stata
ssc install jb6
```

{% raw %}
<div class="output">
输出(stream):<br>
    checking jb6 consistency and verifying not already installed...
    <br />installing into c:\ado\plus\...
    <br />installation complete.
    <br />
</div>
{% endraw %}

然后一个命令即可进行JB检验:


```stata
jb6 mpg
```

{% raw %}
<div class="output">
输出(stream):<br>
    Jarque-Bera normality test:  14.03 Chi(2)  9.0e-04
    <br />Jarque-Bera test for Ho: normality: (mpg)
    <br />
</div>
{% endraw %}

进行D'Agostino检验:


```stata
sktest mpg
```

{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />                    Skewness/Kurtosis tests for Normality
    <br />                                                          ------ joint ------
    <br />    Variable |        Obs  Pr(Skewness)  Pr(Kurtosis) adj chi2(2)   Prob>chi2
    <br />-------------+---------------------------------------------------------------
    <br />         mpg |         74     0.0015        0.0804       10.95         0.0042
    <br />
</div>
{% endraw %}

该检验也显示, 变量不属于正态分布。

进行Shapiro-Wilk检验, 结果也类似:


```stata
swilk mpg
```

{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />                   Shapiro-Wilk W test for normal data
    <br />
    <br />    Variable |        Obs       W           V         z       Prob>z
    <br />-------------+------------------------------------------------------
    <br />         mpg |         74    0.94821      3.335     2.627    0.00430
    <br />
</div>
{% endraw %}

进行Shapiro-Francia检验:


```stata
sfrancia mpg
```

{% raw %}
<div class="output">
输出(stream):<br>
    
    <br />                  Shapiro-Francia W' test for normal data
    <br />
    <br />    Variable |       Obs       W'          V'        z       Prob>z
    <br />-------------+-----------------------------------------------------
    <br />         mpg |        74    0.94872      3.650     2.510    0.00604
    <br />
</div>
{% endraw %}

### 变量正态化

我们可以对变量取log自然对数, 然后再检验它的正态性:

生成新变量: lnmpg


```stata
gen lnmpg = log(mpg)
```

绘制核密度图:


```stata
kdensity lnmpg, normal 
```


![svg](output_37_0.svg)


这个图看起来更像正态分布了。

进行JB检验:


```stata
jb6 lnmpg
```

{% raw %}
<div class="output">
输出(stream):<br>
    Jarque-Bera normality test:  .8632 Chi(2)  .6495
    <br />Jarque-Bera test for Ho: normality: (lnmpg)
    <br />
</div>
{% endraw %}

结果显示, p值并不显著, 我们无法拒绝正态分布的假设。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](stata教程03-数据的正态性检验和变量正态化.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
