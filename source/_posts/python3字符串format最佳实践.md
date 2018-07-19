
---
title: python3字符串format最佳实践
date: 2018-07-19
20:17:55
tags: [python, 格式化字符串]
toc: true
xiongzhang: true


---
<span></span>
<!-- more -->

> 声明: 本文由[DataScience](http://mlln.cn)原创发表, 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.

本文代码运行环境:

- windows10
- python3.6
- jupyter notebook


### 简介

之前写了一篇文章广受欢迎:[f-string格式化字符串的高级用法](http://www.mlln.cn/2018/05/19/python3%20f-string%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95/), 但是, 这篇文章针对的是有经验的python程序员, 下面这篇文章更多的是针对刚入门python的新人。

Python的字符串类的`str.format()`方法允许您进行变量替换和值格式化。本教程将指导您完成Python中格式化程序的一些常见用法，这有助于使您的代码和程序更具可读性和用户友好性。

### 基本用法

格式化通过将一个或多个占位符（由一对花括号`{}`定义）放入字符串, 并调用str.format方法填充这些占位符。说一万句话不如一个例子, 看例子:


```python
print("我有{}个气球".format(5))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有5个气球
    <br />
</div>
{% endraw %}


```python
print("我有{n}个气球".format(n=5))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有5个气球
    <br />
</div>
{% endraw %}

上面的代码有相同的效果, 只是第一种方法需要严格控制传入的参数的位置, 而第二种方法没有这种限制, 而且第二种方法还有一个好处就是增加代码的可读性, 并且你可以在字符串中插入多个相同的值, 而在format方法中只传入一个值, 类似这样:


```python
print("我有{n}个气球和{n}个棒棒糖".format(n=5))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有5个气球和5个棒棒糖
    <br />
</div>
{% endraw %}

我们还可以先把格式化的字符串保存到一个变量, 然后再调用format方法:


```python
open_string = "我有{}个气球"
print(open_string.format("5"))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有5个气球
    <br />
</div>
{% endraw %}

### 多个占位符

使用格式化字符串时，可以使用多对花括号。如果我们想在上面的句子中添加另一个占位符，我们可以通过添加第二对花括号并将第二个值传递给方法来实现：


```python
print("我有{}个气球和{}个棒棒糖".format(5, 6))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有5个气球和6个棒棒糖
    <br />
</div>
{% endraw %}

为了添加另一个占位符，我们在原始字符串中添加了第二对花括号。然后，我们将两个字符串传递给str.format方法，用逗号分隔它们。

遵循相同的语法，我们可以添加更多占位符：


```python
print("我有{}个气球, {}个奶瓶和{}个棒棒糖".format(5, 6, 7))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有5个气球, 6个奶瓶和7个棒棒糖
    <br />
</div>
{% endraw %}

但是, 当你使用的占位符过多时, 我建议你使用关键字参数, 这样程序的可读性会更好。


```python
print("我有{q}个气球, {n}个奶瓶和{b}个棒棒糖".format(b=5,q= 6, n=7))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有6个气球, 7个奶瓶和5个棒棒糖
    <br />
</div>
{% endraw %}

还有一种做法, 虽然你可以这样做, 但是我不推荐你这样做, 这样做使得阅读代码变得困难。


```python
print("我有{1}个气球, {2}个奶瓶和{0}个棒棒糖".format(5, 6, 7))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有6个气球, 7个奶瓶和5个棒棒糖
    <br />
</div>
{% endraw %}

上面的写法让我们很难直观看出每个参数到底传给了哪个占位符。

下面的例子显示使用与位置参数一起使用的关键字参数。我们可以在位置参数后面填写关键字参数，并可以移动这些参数来更改结果字符串：


```python
print("Sammy the {pr} {1} a {0}.".format("shark", "made", pr = "pull request"))
```

{% raw %}
<div class="output">
输出(stream):<br>
    Sammy the pull request made a shark.
    <br />
</div>
{% endraw %}

### 设定格式

我们可以在语法的花括号中包含更多参数。我们将使用格式代码语法{field_name：conversion}，其中field_name指str.format方法的参数的索引号或关键字，conversion是指数据要转换成的类型。

转换类型是指Python使用的单字符类型代码。`s`代表字符串，`d`代表十进制整数（10-base），以及`f`代表带小数位的浮点数。您可以通过Python3的官方文档阅读有关[Format-Specification Mini-Language](https://docs.python.org/3.6/library/string.html#format-specification-mini-language)的更多信息。

我们看一个例子:


```python
print("我吃了{0:f}个{1}!".format(75, "pizza"))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我吃了75.000000个pizza!
    <br />
</div>
{% endraw %}

当然, 我们可以指定需要保留几位小数:


```python
print("我吃了{0:.3f}个{1}!".format(75, "pizza"))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我吃了75.000个pizza!
    <br />
</div>
{% endraw %}

看下面的例子, 你就知道, 数字保留位数时是四舍五入的:


```python
print("我吃了{0:.3f}个{1}!".format(75.666666666, "pizza"))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我吃了75.667个pizza!
    <br />
</div>
{% endraw %}

我们再试试其他数据格式(你会看到, 浮点数不能转换为整数):


```python
print("我吃了{0:d}个{1}!".format(75.666666666, "pizza"))
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-25-015fb03281f2> in <module>()
    ----> 1 print("我吃了{0:d}个{1}!".format(75.666666666, "pizza"))
    

    ValueError: Unknown format code 'd' for object of type 'float'


所以你只能这么做:


```python
print("我吃了{0:.0f}个{1}!".format(75.666666666, "pizza"))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我吃了76个pizza!
    <br />
</div>
{% endraw %}

### 字符串补齐

您可以通过其他参数填充或创建元素周围的空间。当我们需要呈现大量数据时，这非常有用。只需要在冒号后面指定一个数字:


```python
print("我有{0:4}红色的{1:16}!".format(5, "苹果"))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我有   5红色的苹果              !
    <br />
</div>
{% endraw %}

上面的例子你很难理解为什么要这么干, 但是下面的例子你就懂了, 补齐以后数据显得更有条理:


```python
data = [[14, "aa", "5元"],
        [0, "bdsd", "115元"],
        [24, "desde", "15元"],
       [2, "aaa", "5元"]]

for d in data:
    print("{0:2},{1:5},{2:4}".format(*d))
```

{% raw %}
<div class="output">
输出(stream):<br>
    14,aa   ,5元  
    <br /> 0,bdsd ,115元
    <br />24,desde,15元 
    <br /> 2,aaa  ,5元  
    <br />
</div>
{% endraw %}

正如我们所看到的，默认情况下, 字符串在字段内是左对齐的，数字是右对齐的。您可以通过在冒号后面放置对齐代码来修改它。 `<`将左对齐字段中的文本，`^`将文本居中于字段中，`>`将右对齐它。


```python
for d in data:
    print("{0:<2},{1:>5},{2:^4}".format(*d))
```

{% raw %}
<div class="output">
输出(stream):<br>
    14,   aa, 5元 
    <br />0 , bdsd,115元
    <br />24,desde,15元 
    <br />2 ,  aaa, 5元 
    <br />
</div>
{% endraw %}

默认情况下，当我们使用格式化补全字段时，Python将使用空白字符填充该字段。我们可以通过指定这个符号, 用直接跟在冒号后面的字符来代替空白字符：


```python
for d in data:
    print("{0:+<2},{1:+>5},{2:+^4}".format(*d))
```

{% raw %}
<div class="output">
输出(stream):<br>
    14,+++aa,+5元+
    <br />0+,+bdsd,115元
    <br />24,desde,15元+
    <br />2+,++aaa,+5元+
    <br />
</div>
{% endraw %}

我们可以将这些参数与我们之前使用过的其他参数结合起来：


```python
for d in data:
    print("{0:+<5.2f},{1:+>5s},{2:+^4s}".format(*d))
```

{% raw %}
<div class="output">
输出(stream):<br>
    14.00,+++aa,+5元+
    <br />0.00+,+bdsd,115元
    <br />24.00,desde,15元+
    <br />2.00+,++aaa,+5元+
    <br />
</div>
{% endraw %}

### 使用变量


```python
n_app = 5
print('我吃了{}个苹果'.format(n_app))
print('我吃了{n_app}个苹果'.format(n_app=n_app))
```

{% raw %}
<div class="output">
输出(stream):<br>
    我吃了5个苹果
    <br />我吃了5个苹果
    <br />
</div>
{% endraw %}

当你要传入的变量非常多, 或者并不确定你需要多少变量时, 你可以直接把`locals()`的返回结果直接传进去:


```python
def summary(fmt):
    a=1
    b=2
    c=3
    return fmt.format(**locals())

print(summary('{a}+{b}={c}'))
```

{% raw %}
<div class="output">
输出(stream):<br>
    1+2=3
    <br />
</div>
{% endraw %}

### 总结

使用format进行变量替换是连接字符串和组织值和数据的有效方法。 format方法对于确保输出可读且用户友好非常有用。另外, 在python3.6以后, f-string开始流行, 也就是在字符串前面加f, 表明时一个可以被格式化的字符串, 关于如何使用f字符串, 请移步我之前的一篇文章:[f-string格式化字符串的高级用法](http://www.mlln.cn/2018/05/19/python3%20f-string%E6%A0%BC%E5%BC%8F%E5%8C%96%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E9%AB%98%E7%BA%A7%E7%94%A8%E6%B3%95/)


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python3字符串format最佳实践.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
