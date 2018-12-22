
---
title: stata教程08-中介效应分析
date: 2018-12-22 15:17:55
tags: [stata]
toc: true
mathjax: true

---


<span></span>
<!-- more -->

### 中介分析原理

下面是我之前写过的关于中介效应的文章, 大家看后就知道原理了:

<a href="/2015/05/23/SPSS实例：[16]中介效应的检验过程/">
    <span class="archive-date">
        May 2015
    </span>
    SPSS实例：[16]中介效应的检验过程
</a>
<a href="/2016/02/01/SPSS实例：[18]中介效应占总效应百分比/">
    <span class="archive-date">
        Feb 2016
    </span>
    SPSS实例：[18]中介效应占总效应百分比
</a>

<a href="/2016/01/11/SPSS实例：[20]检验中介效应的操作方法/">
    <span class="archive-date">
        Jan 2016
    </span>
    SPSS实例：[20]检验中介效应的操作方法
</a>

<a href="/2016/10/15/SPSS实例：[17]进行sobel检验(小白教程)/">
    <span class="archive-date">
        Oct 2016
    </span>
    SPSS实例：[17]进行sobel检验(小白教程)
</a>

<a href="https://mlln.cn/2018/09/26/%E5%9C%A8%E7%BA%BF%E7%BB%98%E5%88%B6%E4%B8%AD%E4%BB%8B%E6%95%88%E5%BA%94%E5%9B%BE/">
    <span class="archive-date">
        Oct 2016
    </span>
    在线绘制中介效应图
</a>





在这里我重新声明一下具体的过程:

下面的回归模型中都带有控制变量，只不过为了简洁，没有在下面描述。首先使用自变量ind预测因变量dep, 得到模型1(`dep=c1 * ind +e1`), 然后使用自变量ind预测中介变量med, 得到模型2(`med=a * ind +e2`), 最后使用自变量ind和中介变量med预测因变量dep, 得到模型3(`dep=b* med + c2 * ind + e3`)。

### 本案例的数据介绍

本案例使用的是自己编制的数据，自变量就是ind, 因变量就是dep, 中介变量就是med, 其他控制变量都以`control+数字`的格式命名。

下面加载这个数据:


```stata
use "data/mediator-data.dta", clear
```

### 过滤缺失值

我们需要做三个回归分析, 但是因为回归分析涉及的变量不同, 如果变量存在缺失值, 那么很有可能造成三个回归方程使用的观测数据有差异(因为有不同的缺失值), 所以我们再做回归之前, 先要生成一个miss_num变量, 如果自变量/中介变量/因变量/控制变量都没有缺失, 那么miss_num=0, 否则miss_num>0。


```stata
egen miss_num = rowmiss(dep med ind control1 control2 control3 control4 control5)
```

看一下缺失情况: 从下表可以看出, 没有缺失的有861个样本。


```stata
tab miss_num
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

   miss_num |      Freq.     Percent        Cum.
------------+-----------------------------------
          0 |        861       73.72       73.72
          1 |        298       25.51       99.23
          2 |          1        0.09       99.32
          3 |          1        0.09       99.40
          4 |          7        0.60      100.00
------------+-----------------------------------
      Total |      1,168      100.00

</div>
{% endraw %}

### 回归1: 自变量预测因变量

`dep=c1 * ind +e1`


```stata
reg dep ind control1 control2 control3 control4 control5 if miss_num==0
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

      Source |       SS           df       MS      Number of obs   =       861
-------------+----------------------------------   F(6, 854)       =      2.76
       Model |  .459843972         6  .076640662   Prob > F        =    0.0115
    Residual |  23.6942548       854  .027745029   R-squared       =    0.0190
-------------+----------------------------------   Adj R-squared   =    0.0121
       Total |  24.1540988       860  .028086161   Root MSE        =    .16657

------------------------------------------------------------------------------
         dep |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         ind |  -.0745096   .0352931    -2.11   0.035    -.1437809   -.0052382
    control1 |  -.0003018   .0043662    -0.07   0.945    -.0088715     .008268
    control2 |  -.0133247     .00578    -2.31   0.021    -.0246693     -.00198
    control3 |  -.0044711   .0044726    -1.00   0.318    -.0132497    .0043075
    control4 |   .1799002   .0983623     1.83   0.068      -.01316    .3729603
    control5 |   .0340114   .0191444     1.78   0.076    -.0035642    .0715871
       _cons |   .7167078   .2593365     2.76   0.006     .2076962     1.22572
------------------------------------------------------------------------------

</div>
{% endraw %}

从上面的结果中可以看到, c1这个系数是显著的, c1 = -.0745096, sc1 = .0352931

### 回归2: 自变量预测中介变量

`med=a * ind +e2`


```stata
reg med ind control1 control2 control3 control4 control5 if miss_num == 0
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

      Source |       SS           df       MS      Number of obs   =       861
-------------+----------------------------------   F(6, 854)       =      2.90
       Model |  3.83093084         6  .638488473   Prob > F        =    0.0083
    Residual |  187.834574       854  .219946808   R-squared       =    0.0200
-------------+----------------------------------   Adj R-squared   =    0.0131
       Total |  191.665505       860  .222866867   Root MSE        =    .46898

------------------------------------------------------------------------------
         med |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         ind |  -.1950457   .0993702    -1.96   0.050    -.3900841   -7.35e-06
    control1 |   .0279925   .0122933     2.28   0.023     .0038638    .0521211
    control2 |   .0083398    .016274     0.51   0.608    -.0236019    .0402814
    control3 |   .0271718   .0125929     2.16   0.031     .0024551    .0518885
    control4 |   .8851904   .2769459     3.20   0.001     .3416161    1.428765
    control5 |   .0229235   .0539025     0.43   0.671    -.0828733    .1287204
       _cons |   2.094221     .73018     2.87   0.004     .6610633    3.527379
------------------------------------------------------------------------------

</div>
{% endraw %}

从上面的结果中可以看到, 这个系数是显著的, a =-.1950457, sa = .0993702

### 回归3: 自变量和中介变量预测因变量

`dep=b* med + c2 * ind + e3`


```stata
reg dep med ind control1 control2 control3 control4 control5 if miss_num == 0
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>

      Source |       SS           df       MS      Number of obs   =       861
-------------+----------------------------------   F(7, 853)       =      2.99
       Model |  .578216371         7  .082602339   Prob > F        =    0.0042
    Residual |  23.5758824       853  .027638784   R-squared       =    0.0239
-------------+----------------------------------   Adj R-squared   =    0.0159
       Total |  24.1540988       860  .028086161   Root MSE        =    .16625

------------------------------------------------------------------------------
         dep |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         med |  -.0251037   .0121303    -2.07   0.039    -.0489124   -.0012949
         ind |  -.0794059   .0353048    -2.25   0.025    -.1487004   -.0101114
    control1 |    .000401    .004371     0.09   0.927    -.0081783    .0089802
    control2 |  -.0131153   .0057698    -2.27   0.023      -.02444   -.0017906
    control3 |   -.003789   .0044762    -0.85   0.398    -.0125746    .0049966
    control4 |   .2021217   .0987592     2.05   0.041     .0082821    .3959613
    control5 |   .0345869   .0191098     1.81   0.071    -.0029208    .0720946
       _cons |   .7692805   .2600831     2.96   0.003     .2588026    1.279758
------------------------------------------------------------------------------

</div>
{% endraw %}

从上面的结果中可以看到, 这个b系数是显著的, b =--.0251037, sb =  .0121303

c2系数也是显著的: c2 = -.0794059, sc2 = .0353048

### 结论

因为所有系数都是显著的, 所以我们可以认为中介效应是存在的, 并且属于部分中介效应。中介的效应量可以这样计算:

`m = a*b`


```stata
display -.1950457 * -.0251037
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
.00489637

</div>
{% endraw %}

中介效应占总效应的百分比就是:


```stata
display (-.1950457 * -.0251037) /  -.0745096 * 100
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
-6.5714602

</div>
{% endraw %}

### 使用插件

实际上我们可以把以上的代码都封装成一个命令, 恰好我在网上找到了一段代码, 可以做中介效应。你需要把以下代码保存到stata安装目录的这个路径下:

`Stata15\ado\base\s`, 在这个文件夹下创建一个文件名为`sgmediation.ado`, 把以下代码贴进去, 然后重启stata。

```stata
*! version 1.1.1 -- 5/17/06 -- pbe
*! verion 1.0 -- 2/28/05 -- pbe
program define sgmediation
/* sobel-goodman mediation tests */
version 8.0
syntax varlist(max=1) [if/] [in], iv(varlist numeric max=1) ///
   mv(varlist numeric max=1) [ cv(varlist numeric) BOOTstrap reps(integer 200) level(integer 95)]
marksample touse
markout `touse' `varlist' `mv' `iv' `cv'
tempname coef emat

display
tabulate  `mv' if `touse'

display
display as text "Model with dv regressed on iv"
regress `varlist' `iv' `cv' if `touse'
local ccoef=_b[`iv']

display
display "Model with mediator regressed on iv"
regress `mv' `iv' `cv' if `touse'

local acoef=_b[`iv']
local avar=_se[`iv']^2

display
display "Model with dv regressed on mediator and iv"
regress `varlist' `mv' `iv' `cv' if `touse'

local bcoef=_b[`mv']
local bvar=_se[`mv']^2

local sobel =(`acoef'*`bcoef')
local serr=sqrt(`bcoef'^2*`avar' + `acoef'^2*`bvar')
local stest=`sobel'/`serr'
local g1err=sqrt(`bcoef'^2*`avar' + `acoef'^2*`bvar' + `avar'*`bvar')
local good1=`sobel'/`g1err'
local g2err=sqrt(`bcoef'^2*`avar' + `acoef'^2*`bvar' - `avar'*`bvar')
local good2=`sobel'/`g2err'
local toteff = `sobel'/((`acoef'*`bcoef')+(`ccoef'-(`acoef'*`bcoef')))
local ratio = `sobel'/((`ccoef'-(`acoef'*`bcoef')))

display
display "Sobel-Goodman Mediation Tests"
display
display "             Coef         Std Err     Z           P>|Z|"
display as txt "Sobel       " as res `sobel' _skip(4) `serr'  %8.4g ///
`stest', _skip(5) 2*(1-norm(abs(`stest')))
display as txt "Goodman-1   " as res `sobel' _skip(4) `g1err' %8.4g ///
`good1', _skip(5) 2*(1-norm(abs(`good1')))
display as txt "Goodman-2   " as res `sobel' _skip(4) `g2err' %8.4g ///
`good2', _skip(5) 2*(1-norm(abs(`good2')))
display
display as txt "Pecent of total effect that is mediated: ", as res ///
%5.2f 100*`toteff',"%"
display as txt "Ratio of indirect to direct effect:     ", as res %8.4f `ratio'

if "`bootstrap'"~="" {
  display 
  display as txt "Percentile and Bias-corrected bootstrap results for Sobel: `reps' replications"
  display

  quietly bootstrap coef=r(sobel), reps(`reps') level(`level'): sgboot `varlist' , mv(`mv') iv(`iv') cv(`cv' )
  estat bootstrap, bc percentile noheader
  }

end
```

最后你在使用的时候, 就可以直接调用这个命令即可:


```stata
sgmediation dep, mv(med) iv(ind) cv(control1 control2 control3 control4 control5  )
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>


        med |      Freq.     Percent        Cum.
------------+-----------------------------------
          0 |        573       66.55       66.55
          1 |        288       33.45      100.00
------------+-----------------------------------
      Total |        861      100.00

        med |      Freq.     Percent        Cum.
------------+-----------------------------------
          0 |        730       62.50       62.50
          1 |        438       37.50      100.00
------------+-----------------------------------
      Total |      1,168      100.00

Model with dv regressed on iv

      Source |       SS           df       MS      Number of obs   =       861
-------------+----------------------------------   F(6, 854)       =      2.76
       Model |  .459843972         6  .076640662   Prob > F        =    0.0115
    Residual |  23.6942548       854  .027745029   R-squared       =    0.0190
-------------+----------------------------------   Adj R-squared   =    0.0121
       Total |  24.1540988       860  .028086161   Root MSE        =    .16657

------------------------------------------------------------------------------
         dep |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         ind |  -.0745096   .0352931    -2.11   0.035    -.1437809   -.0052382
    control1 |  -.0003018   .0043662    -0.07   0.945    -.0088715     .008268
    control2 |  -.0133247     .00578    -2.31   0.021    -.0246693     -.00198
    control3 |  -.0044711   .0044726    -1.00   0.318    -.0132497    .0043075
    control4 |   .1799002   .0983623     1.83   0.068      -.01316    .3729603
    control5 |   .0340114   .0191444     1.78   0.076    -.0035642    .0715871
       _cons |   .7167078   .2593365     2.76   0.006     .2076962     1.22572
------------------------------------------------------------------------------

Model with mediator regressed on iv

      Source |       SS           df       MS      Number of obs   =       861
-------------+----------------------------------   F(6, 854)       =      2.90
       Model |  3.83093084         6  .638488473   Prob > F        =    0.0083
    Residual |  187.834574       854  .219946808   R-squared       =    0.0200
-------------+----------------------------------   Adj R-squared   =    0.0131
       Total |  191.665505       860  .222866867   Root MSE        =    .46898

------------------------------------------------------------------------------
         med |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         ind |  -.1950457   .0993702    -1.96   0.050    -.3900841   -7.35e-06
    control1 |   .0279925   .0122933     2.28   0.023     .0038638    .0521211
    control2 |   .0083398    .016274     0.51   0.608    -.0236019    .0402814
    control3 |   .0271718   .0125929     2.16   0.031     .0024551    .0518885
    control4 |   .8851904   .2769459     3.20   0.001     .3416161    1.428765
    control5 |   .0229235   .0539025     0.43   0.671    -.0828733    .1287204
       _cons |   2.094221     .73018     2.87   0.004     .6610633    3.527379
------------------------------------------------------------------------------

Model with dv regressed on mediator and iv

      Source |       SS           df       MS      Number of obs   =       861
-------------+----------------------------------   F(7, 853)       =      2.99
       Model |  .578216371         7  .082602339   Prob > F        =    0.0042
    Residual |  23.5758824       853  .027638784   R-squared       =    0.0239
-------------+----------------------------------   Adj R-squared   =    0.0159
       Total |  24.1540988       860  .028086161   Root MSE        =    .16625

------------------------------------------------------------------------------
         dep |      Coef.   Std. Err.      t    P>|t|     [95% Conf. Interval]
-------------+----------------------------------------------------------------
         med |  -.0251037   .0121303    -2.07   0.039    -.0489124   -.0012949
         ind |  -.0794059   .0353048    -2.25   0.025    -.1487004   -.0101114
    control1 |    .000401    .004371     0.09   0.927    -.0081783    .0089802
    control2 |  -.0131153   .0057698    -2.27   0.023      -.02444   -.0017906
    control3 |   -.003789   .0044762    -0.85   0.398    -.0125746    .0049966
    control4 |   .2021217   .0987592     2.05   0.041     .0082821    .3959613
    control5 |   .0345869   .0191098     1.81   0.071    -.0029208    .0720946
       _cons |   .7692805   .2600831     2.96   0.003     .2588026    1.279758
------------------------------------------------------------------------------

Sobel-Goodman Mediation Tests

             Coef         Std Err     Z           P>|Z|
Sobel       .00489637    .       .      .
Goodman-1   .00489637    .       .      .
Goodman-2   .00489637    .       .      .

Pecent of total effect that is mediated:  -6.57 %
Ratio of indirect to direct effect:       -0.0617

</div>
{% endraw %}


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](stata教程08-中介效应分析.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
