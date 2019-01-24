
---
title: 数学小白用python做极大似然估计MLE
date: 2019-01-24 21:17:55
tags: [numpy, scipy]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]
mathjax: true

---

<span></span>
<!-- more -->

我们需要从模型中估计一个参数。通常，我们选择一个模型 - 比如说线性回归 - 并使用观测数据X来估计模型的参数θ。

那么模型参数到底是如何估计出来的呢?例如, 我们从均值为`mu`标准差为`sd`的总体中随机抽取样本`x`, 我们的目标就是估计mu和sd的值。

设想你正在做一个线性回归, 并且你要估计出模型自变量x的系数:

### 估计参数

我们从正态分布的概率密度函数(PDF)出发, 讲一些数学知识。

`$$
f(x) =
\frac{1}{\sigma \sqrt{2\pi}} \exp\left(−\frac{(x−\mu)^2}{2\sigma^2}\right).
$$`


```python
from scipy.stats import norm

norm.pdf(3, 3, 1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0.3989422804014327

</div>
{% endraw %}



如果总体参数是`$\mu=7$`和`$\sigma=2$`


```python
norm.pdf(3, 7, 2)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0.02699548325659403

</div>
{% endraw %}



综上所述, pdf告诉我们, 一个样本来自于某个总体的概率的大小。 那么我们的样本量不是1, 而是大于1呢? 其实也很简单, 根据概率公式, 多个独立事件出现的概率就是每个事件概率之积。

比如现在有两个样本x=[2, 7], 那么他们来自总体N($(2, 1)的概率是:


```python
norm.pdf(2, 2, 1) * norm.pdf(7, 2, 1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    5.931152735254122e-07

</div>
{% endraw %}



### 根据样本选择分布

假如现在给你两个可能分布N(2, 1)和N(3, 2), 让你猜测, 样本x=[2, 7]来自哪个分布?

我们很容易想到, 分别求出样本x来自两个总体的概率即可:


```python
p1 = norm.pdf(2, 2, 1) * norm.pdf(7, 2, 1)
p2 = norm.pdf(2, 3, 2) * norm.pdf(7, 3, 2)
print('p1:', p1)
print('p2:', p2)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
p1: 5.931152735254122e-07
p2: 0.0047520868169464775

</div>
{% endraw %}

所以我们说, 样本更有可能来自于N(3, 2)。

到这里我们就大概知道MLE在做什么了, MLE就是知道一个样本, 让你求参θ(比如pdf的`$\mu$`和`$\sigma$`

用数学来表达这件事就是, 我们知道x出现的概率可以这样计算:

`$$
f(x) =
\frac{1}{\sigma \sqrt{2\pi}} \exp\left(−\frac{(x−\mu)^2}{2\sigma^2}\right).
$$`

### 实战

根据高中知识, 求函数的最大值, 可以使用求导的方式, 让导数为0 ,就可以得到极值点。

因为我比较懒, 不喜欢求导数, 所以我用了一个求导数的python模块sympy, 下面我们先写出上面的公式`$\log p$`


```python
from sympy import symbols, pi, exp, log
from sympy.stats import Probability, Normal

# 样本
X = [1,2,3,4,5, 3,4,2,5,6,]
x = symbols('x')
# 总体 mu 和 sigma
m, s = symbols('m s')
# pdf
pdf = 1/ (s * (2*pi)**0.5)*exp( -(x-m)**2 / (2*s**2) )
logpdf = log(pdf)
logpdf
```




{% raw %}
<div class="output">
输出(plain):<br/>

    log(0.707106781186547*pi**(-0.5)*exp(-(-m + x)**2/(2*s**2))/s)

</div>
{% endraw %}



上面输出的内容就是logpdf公式。

下面我们求已知样本后的累加log联合概率, 也叫似然函数:


```python
logP = 0
for xi in X:
    logP += logpdf.subs({x: xi})
    
logP
```




{% raw %}
<div class="output">
输出(plain):<br/>

    log(0.707106781186547*pi**(-0.5)*exp(-(-m + 1)**2/(2*s**2))/s) + 2*log(0.707106781186547*pi**(-0.5)*exp(-(-m + 2)**2/(2*s**2))/s) + 2*log(0.707106781186547*pi**(-0.5)*exp(-(-m + 3)**2/(2*s**2))/s) + 2*log(0.707106781186547*pi**(-0.5)*exp(-(-m + 4)**2/(2*s**2))/s) + 2*log(0.707106781186547*pi**(-0.5)*exp(-(-m + 5)**2/(2*s**2))/s) + log(0.707106781186547*pi**(-0.5)*exp(-(-m + 6)**2/(2*s**2))/s)

</div>
{% endraw %}



然后我们知道, 要求logP的最大值, 只需要分别求得m和s的偏导数, 然后让偏导数为0可以得到联立方程组:



```python
from sympy import diff

logp_diff_m = diff(logP, m)
logp_diff_s = diff(logP, s)

print('m偏导数:', str(logp_diff_m))
print('s偏导数:', str(logp_diff_s))
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
m偏导数: -0.5*(2*m - 12)/s**2 - 1.0*(2*m - 10)/s**2 - 1.0*(2*m - 8)/s**2 - 1.0*(2*m - 6)/s**2 - 1.0*(2*m - 4)/s**2 - 0.5*(2*m - 2)/s**2
s偏导数: 1.4142135623731*pi**0.5*s*(-0.707106781186547*pi**(-0.5)*exp(-(-m + 1)**2/(2*s**2))/s**2 + 0.707106781186547*pi**(-0.5)*(-m + 1)**2*exp(-(-m + 1)**2/(2*s**2))/s**4)*exp((-m + 1)**2/(2*s**2)) + 2.82842712474619*pi**0.5*s*(-0.707106781186547*pi**(-0.5)*exp(-(-m + 2)**2/(2*s**2))/s**2 + 0.707106781186547*pi**(-0.5)*(-m + 2)**2*exp(-(-m + 2)**2/(2*s**2))/s**4)*exp((-m + 2)**2/(2*s**2)) + 2.82842712474619*pi**0.5*s*(-0.707106781186547*pi**(-0.5)*exp(-(-m + 3)**2/(2*s**2))/s**2 + 0.707106781186547*pi**(-0.5)*(-m + 3)**2*exp(-(-m + 3)**2/(2*s**2))/s**4)*exp((-m + 3)**2/(2*s**2)) + 2.82842712474619*pi**0.5*s*(-0.707106781186547*pi**(-0.5)*exp(-(-m + 4)**2/(2*s**2))/s**2 + 0.707106781186547*pi**(-0.5)*(-m + 4)**2*exp(-(-m + 4)**2/(2*s**2))/s**4)*exp((-m + 4)**2/(2*s**2)) + 2.82842712474619*pi**0.5*s*(-0.707106781186547*pi**(-0.5)*exp(-(-m + 5)**2/(2*s**2))/s**2 + 0.707106781186547*pi**(-0.5)*(-m + 5)**2*exp(-(-m + 5)**2/(2*s**2))/s**4)*exp((-m + 5)**2/(2*s**2)) + 1.4142135623731*pi**0.5*s*(-0.707106781186547*pi**(-0.5)*exp(-(-m + 6)**2/(2*s**2))/s**2 + 0.707106781186547*pi**(-0.5)*(-m + 6)**2*exp(-(-m + 6)**2/(2*s**2))/s**4)*exp((-m + 6)**2/(2*s**2))

</div>
{% endraw %}

我们知道让logp_diff_m=0和logp_diff_s=0可以得到联立方程组,然后解方程就可以得到参数的值, 但是我好像不会解这样的方程!!!

先化简一下:


```python
from sympy import simplify

logp_diff_m = simplify(logp_diff_m)
logp_diff_m
```




{% raw %}
<div class="output">
输出(plain):<br/>

    (-10.0*m + 35.0)/s**2

</div>
{% endraw %}




```python
logp_diff_s= simplify(logp_diff_s)
logp_diff_s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    (10.0*m**2 - 70.0*m - 10.0*s**2 + 145.0)/s**3

</div>
{% endraw %}



其实你看到上面化简的式子就能够手动解这个方程了, 不过我还是太懒了, 我想sympy一定能解!


```python
from sympy import solve

funcs = [logp_diff_s, logp_diff_m]
solve(funcs, [m, s])
```




{% raw %}
<div class="output">
输出(plain):<br/>

    [(3.50000000000000, -1.50000000000000), (3.50000000000000, 1.50000000000000)]

</div>
{% endraw %}



好了上面得到了m和s的值, 有两组解, 但是我们知道s>0, 所以第二组解是对的。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](数学小白用python做极大似然估计MLE.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
