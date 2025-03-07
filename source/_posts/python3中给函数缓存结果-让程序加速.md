
---

title: python3中给函数缓存结果-让程序加速
date: 2019-09-10 12:44:03
tags: [python, lru_cache]

---

使用称为“memoization”的强大而方便的缓存技术加速Python程序。在本文中，我将向您介绍一种方便的方法来加速您的Python代码，称为memoization（有时拼写为memoisation）：Memoization是一种特定类型的缓存，用作软件优化技术。

<!--more-->

缓存函数的结果以供以后使用。例如你看到的这个网页，关掉这个页面, 将来再次访问它，您的Web浏览器很可能会使用缓存来加快本教程网页的加载速度。

所以，当我谈论memoization和Python时，我正在讨论基于其输入记住或缓存函数的输出。记忆在“备忘录”中找到了答案，这意味着函数速度的加快。

Memoization允许您通过根据您提供的参数缓存其输出来优化Python函数。一旦你记住一个函数，它只会为你调用它的每组参数计算一次输出。第一个之后的每个调用都将从缓存中快速检索。

在本教程中，您将了解如何以及何时使用Python使用这个简单但功能强大的概念，因此您可以使用它来优化您自己的程序，并使它们在某些情况下运行得更快。



### 为什么以及何时在Python程序中使用Memoization？


答案是昂贵的代码：

当我分析代码时，我会根据运行所需的时间和使用的内存来查看代码。如果我正在查看需要很长时间才能运行或使用大量内存的代码，我称代码很昂贵。

这是昂贵的代码，因为它需要花费大量的资源，空间和时间来运行。当您运行昂贵的代码时，它会占用您计算机上其他程序的资源。

如果你想加速Python应用程序中昂贵的部分，那么memoization就是一种很好的技术。在我们亲自动手并自己实施之前，让我们深入了解一下memoization吧！

我在本教程中使用的所有代码示例都是用Python 3编写的，但当然这里演示的一般技术和模式也适用于Python 2。

### Memoization算法介绍


基本的memoization算法如下：

- 为函数结果设置缓存数据结构
- 每次调用该函数时，请执行以下操作之一：
    - 如果有的话，返回缓存的结果;
    - 要么调用函数来计算缺少的结果，然后在将结果返回给调用者之前更新缓存
    - 如果有足够的缓存存储空间，这实际上可以保证一组特定函数参数的函数结果只计算一次。

只要我们有一个缓存结果，我们就不必为同一组输入重新运行函数。相反，我们可以只获取缓存的结果并立即返回。

### 从头开始写一个Memoization装饰器

装饰器是一个函数，它将另一个函数作为输入并将另一个一个函数作为其输出。

这允许我们以通用和可重用的方式实现我们的memoization算法。听起来有点混乱？不用担心，我们将逐步采取这一步骤，当您看到一些真正的代码时，它们将变得更加清晰。

这是实现上述缓存算法的memoize（）装饰器：


```python
def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func
```

此装饰器接受一个函数并返回实现缓存逻辑的相同函数的包装版本。

我在这里使用Python字典作为缓存。在Python中，使用键来查找字典中的值很快。这使得dict成为函数结果缓存的数据结构的一个很好的选择。

每当调用修饰函数时，我们检查参数是否已经在缓存中。如果是，则返回缓存的结果。因此，我们不会重新计算结果，而是快速从缓存中返回。

Bam，memoization！

如果结果不在缓存中，我们必须更新缓存，以便将来节省一些时间。因此，我们首先计算缺失的结果，将其存储在缓存中，然后将其返回给调用者。

[正如我所提到的，装饰器是掌握任何中级或高级Python开发人员的重要概念。如果您想了解更多信息，请查看我的Python装饰器教程，了解逐步介绍。 ]

让我们在递归的Fibonacci序列函数上测试我们的memoization装饰器。首先，我将定义一个计算第n个Fibonacci数的Python函数：


```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

该斐波那契函数将作为“昂贵”计算的一个例子。以这种方式计算第n个斐波那契数具有O（2 ^ n）时间复杂度 - 它需要指数时间才能完成。

这确实使它成为相当昂贵的函数。

接下来，我将进行一些基准测试，以便了解这个函数的计算成本如何。 Python的内置timeit模块让我可以测量任意Python语句的执行时间（以秒为单位）。

以下是我将如何使用Python内置的timeit模块测量我刚刚定义的斐波那契函数的执行时间：


```python
import timeit
timeit.timeit('fibonacci(35)', globals=globals(), number=1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    4.456297800000001

</div>
{% endraw %}



如您所见，在我的机器上，计算Fibonacci序列中的第35个数字大约需要5秒钟。那是一个非常缓慢而昂贵的操作。

让我们看看我们是否可以通过利用memoization装饰器提供的函数结果缓存来加快速度：


```python
memoized_fibonacci = memoize(fibonacci)
timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    4.4849669999999975

</div>
{% endraw %}



记忆功能在第一次运行时仍需大约五秒钟才能返回。到目前为止，没有给人留下深刻的印象......

我们将获得类似的执行时间，因为我第一次运行memoized函数时结果缓存很冷 - 我们开始使用空缓存，这意味着没有预先计算的结果可以帮助加速此函数调用。

让我们第二次运行我们的基准测试：


```python
timeit.timeit('memoized_fibonacci(35)', globals=globals(), number=1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    2.300000005561742e-06

</div>
{% endraw %}



我说过啥！

请注意该浮点数末尾的e-06后缀？第二轮memoized_fibonacci只用了大约2微秒就完成了。那是 - 相当不错的加速！

我们的memoize装饰器不是递归地计算第35个Fibonacci数，而是简单地获取缓存的结果并立即返回它，这就是导致第二次基准测试运行中令人难以置信的加速的原因。

### 查看函数结果缓存

为了真正了解“幕后”的memoization如何工作，我想向你展示上一个例子中使用的函数结果缓存的内容：


```python
memoized_fibonacci.__closure__[0].cell_contents
```




{% raw %}
<div class="output">
输出(plain):<br/>

    {(35,): 9227465}

</div>
{% endraw %}



为了查看缓存，我使用其__closure__属性到达memoized_fibonacci函数的“内部”。缓存dict是第一个局部变量并存储在单元格0中。我不建议您在生产代码中使用此技术 - 但这里它提供了一个很好的小调试技巧  

如您所见，缓存字典将目前发生的每个memoized_fibonacci函数调用的参数元组映射到函数结果（第n个Fibonacci数）。

因此，例如，（35，）是memoized_fibonacci（35）函数调用的参数元组，它与9227465相关联，它是第35个Fibonacci数：


```python
fibonacci(35)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    9227465

</div>
{% endraw %}



我们的memoize装饰器有一个致命缺陷：在此示例中，缓存大小是无限的，这意味着缓存可以随意增长。这通常不是一个好主意，因为它可能导致程序中的内存耗尽错误。

通过在程序中使用的任何类型的缓存，可以限制同时保存在缓存中的数据量。这通常通过对高速缓存大小进行硬限制或通过定义在某个时刻从缓存中删除过期项目来实现。

请记住，我们之前编写的memoize函数是一个用于演示目的的简化实现。在本教程的下一部分中，您将了解如何在Python程序中使用memoization算法的“生产就绪”的方法。

### 使用functools.lru_cache

既然您已经了解了如何自己实现memoization函数，我将向您展示使用Python的functools.lru_cache装饰器可以获得相同的结果，以增加方便性。

我最喜欢Python的一个原因是它的语法的简洁性和美感与其哲学的美感和简洁性密切相关。 Python“包含电池”，这意味着Python捆绑了大量常用的库和模块，你只需要一个导入语句！

我发现functools.lru_cache是这种哲学的一个很好的例子。 lru_cache装饰器是Python在标准库中易于使用的memoization实现。一旦确定何时使用lru_cache，只需几行代码即可快速加速应用程序。

让我们重新审视我们的Fibonacci序列示例。这次我将向您展示如何使用functools.lru_cache装饰器添加memoization：


```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

请注意我传递给lru_cache的maxsize参数，以限制同时存储在缓存中的项目数。

我再一次使用timeit模块运行一个简单的基准测试，这样我就可以了解这种优化对性能的影响：


```python
timeit.timeit('fibonacci(35)', globals=globals(), number=1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    3.4800000094037387e-05

</div>
{% endraw %}




```python
timeit.timeit('fibonacci(35)', globals=globals(), number=1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    1.6999999843392288e-06

</div>
{% endraw %}



您可能想知道为什么我们这次第一次运行的结果要快得多。缓存不应该在第一次运行时没效果吗？

不同之处在于，在本例中，我在函数定义时应用了@lru_cache装饰器。这意味着这次也会在缓存中查找对fibonacci（）的递归调用。

通过使用@lru_cache装饰器装饰fibonacci（）函数，我基本上将其转换为动态编程解决方案，其中每个子问题只需存储子问题解决方案一次即可解决，并在下次从缓存中查找它们。

在这种情况下，这只是一个副作用 - 但我相信你可以开始看到使用memoization装饰器的美感和强大功能，以及它可以用来实现其他动态编程算法的有用工具。

### 为什么我偏爱functools.lru_cache

通常，functools.lru_cache提供的Python的memoization实现比我们的ad hoc memoize函数更全面，正如你在CPython源代码中看到的那样。

例如，它提供了一个方便的功能，允许您使用cache_info方法检索缓存统计信息：


```python
fibonacci.cache_info()
# hits 代表从存储中读取过几次结果
```




{% raw %}
<div class="output">
输出(plain):<br/>

    CacheInfo(hits=33, misses=36, maxsize=128, currsize=36)

</div>
{% endraw %}



再次，正如您在CacheInfo输出中看到的那样，Python的lru_cache（）记忆了对fibonacci（）的递归调用。当我们查看memoized函数的缓存信息时，您会发现为什么它比第一次运行时的版本更快 - 缓存被命中33次。

正如我之前提到的，functools.lru_cache还允许您使用maxsize参数限制缓存结果的数量。通过设置maxsize = None，您可以强制缓存无限制，我通常建议不要这样做。

还有一个类型化的布尔参数，你可以设置为True，以告诉缓存不同类型的函数参数应该单独缓存。例如，斐波那契（35）和斐波纳契（35.0）将被视为具有不同结果的不同调用。

另一个有用的功能是能够使用cache_clear方法随时重置结果缓存：


```python
fibonacci.cache_clear()
fibonacci.cache_info()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)

</div>
{% endraw %}



如果您想了解更多关于使用lru_cache装饰器的复杂性，我建议您查阅Python标准库文档。

总之，您永远不需要写自己的记忆功能。 Python的内置lru_cache（）随时可用，更全面，并经过实战测试。

### 缓存警告 - 什么可以被缓存？

理想情况下，您需要记住返回结果具有确定性的函数。


```python
def deterministic_adder(x, y):
    return x + y
```

这里deterministic_adder（）是一个确定性函数，因为它总是会为同一对参数返回相同的结果。例如，如果将2和3传递给函数，它将始终返回5。

将此行为与以下非确定性函数进行比较：


```python
from datetime import datetime

def nondeterministic_adder(x, y):
    # Check to see if today is Monday (weekday 0)
    if datetime.now().weekday() == 0:
        return x + y + x
    return x + y
```

此函数是不确定的，因为给定输入的输出将根据星期几而变化：如果在星期一运行此函数，缓存将在一周中的任何其他日期返回过时数据。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python3中给函数缓存结果-让程序加速.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
