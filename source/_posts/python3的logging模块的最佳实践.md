
---

title: python3的logging模块的最佳实践
date: 2019-07-21 12:44:03
tags: [python, logging]

---

日志记录的内容非常丰富, 日志的形式也千变万化。
在本文中，我们将探讨如何使用Python的logging模块进行日志记录，
以便更好地了解应用程序中发生了什么。此外，我将探索一些最佳实践，
这些实践将帮助您使用内置的Python模块从日志中获得最大价值。

<!-- more -->

### 简介


如果操作正确，日志是你开发的软件的重要组成部分。日志讲述了应用程序中数据如何变化的。他们让您回答以下问题：为什么John Doe在结账时收到错误？他提供什么输入数据？

日志记录的内容非常丰富, 日志的形式也千变万化。在本文中，我们将探讨如何使用Python的logging模块进行日志记录，以便更好地了解应用程序中发生了什么。此外，我将探索一些最佳实践，这些实践将帮助您使用内置的Python模块从日志中获得最大价值。

### 为什么不直接使用print语句

很多python入门教程都使用print语句来输出数据, 让学习者看到程序在做什么, 但是这种实践让很多学习者误入歧途, 在工业界很少有合格的程序员使用print作为日志工具。

虽然`print`在较小的脚本程序中很有用，但随着应用程序需求的增长，`print`成为一种不太可行的解决方案。它不能为您提供关闭整个输出的灵活性，它只允许您输出到标准输出(stdout)。它还会遗漏print的行号和时间等信息，这些信息可以帮助调试代码。虽然print是最简单的方法，因为它不需要设置，它可以很快反馈给你。使用包含print语句的第三方库也是不提倡的，因为它会让你无法控制自己的程序的输出, 除非你修改他的代码, 否则你无法控制什么东西会被打印出来, 对于你调试程序, 额外的无用输出是很恼人的。



### Logging.info("Hello world")


logging模块是Python标准库的一部分，从版本2.3开始。它会自动将日志（例如行号和时间戳）添加到日志中。该模块可以轻松添加命名空间日志记录和日志级别，以便您更好地控制输出的位置和内容。

我相信最好的学习方法就是"去做"，所以我鼓励你跟进Python REPL。开始使用日志记录模块很简单，这就是您需要做的所有事情：




```python
import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.critical("logging is easier than I was expecting!")
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
CRITICAL:__main__:logging is easier than I was expecting!

</div>
{% endraw %}

上面的代码做了什么, 其实很简单, 首先我们使用`getLogger`获取了logger实例, 然后用实例的`critical`方法记录了一条日志: logging is easier than I was expecting!, 日志的重要性级别就是`critical`。



### Levels

Python模块允许您根据日志的严重性级别区分日志。级别表示为0到50之间的整数。logging模块在整个范围中定义了五个常量，便于区分日志等级。

运行下面的五个语句, 查看输出:



```python
logger.critical("this better be bad")
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
CRITICAL:__main__:this better be bad

</div>
{% endraw %}


```python
logger.error("more serious problem")
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
ERROR:__main__:more serious problem

</div>
{% endraw %}


```python
logger.warning("an unexpected event")
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
WARNING:__main__:an unexpected event

</div>
{% endraw %}


```python
logger.info("show user flow through program")
```


```python
logger.debug("used to track variables when coding")
```

你会发现, info和debug这两个方法并没有像标准输出中产生任何影响。默认情况下, 日志模块仅仅会将`warning/error/critical`级别的日志信息打印到标准输出中。你可以自定义这个行为, 并且在程序运行时修改这些设置。


```python
logger.setLevel(logging.DEBUG)
```


```python
logger.info('Hello')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
INFO:__main__:Hello

</div>
{% endraw %}

### 格式化日志消息

默认格式化程序对格式化日志没有用，因为它不包含关键信息。日志记录模块使您可以通过更改格式轻松添加它。

我们将设置格式以显示时间，级别和消息：


```python
%%script python

import logging
logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=logFormatter, level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info("test")
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
2019-07-21 14:46:21,141 - INFO - test

</div>
{% endraw %}

注意: 我在程序的开头写了`%%script python`, 因为我的程序运行在jupyter notebook中, 因此为了正确显示log信息, 我需要让程序运行在一个独立的环境中, 所以我使用了notebook的魔法`script`来调用python命令, 独立执行这段代码。

### 添加额外信息

虽然日志格式化了, 更好看了, 但是缺少一些必要信息。 想象一下，如果你必须通过你的日志了解购物车的动态。这使得很难回答以下问题：物品什么时候删除？谁删除了它？他们删除了什么？

所以, 我们能不能在日志中添加以下额外信息呢, 答案是可以!


```python
%%script python

import logging
# 下面的格式中, 有一个额外的信息: user
logFormatter = '%(asctime)s - %(user)s - %(levelname)s - %(message)s'
logging.basicConfig(format=logFormatter, level=logging.DEBUG)
logger = logging.getLogger(__name__)
# 在输出日志的时候, 我们需要提供参数extra来提供上下文信息
logger.info('purchase completed', extra={'user': 'Sid Panjwani'})
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
2019-07-21 14:53:45,539 - Sid Panjwani - INFO - purchase completed

</div>
{% endraw %}

### 性能问题

记录日志有时候对性能的影响较大, 比如要记录一些计算值。 虽然开销通常可以忽略不计，但不良做法和错误可能导致不幸的情况。

比如有一个函数的计算结果需要1秒, 你只希望在软件开发的阶段记录这个日志, 但是下面的写法就是错误的:

```py
logger.debug('%s', func_needs_time())
```

这种写法, 需要先计算函数返回值, 然后再去判断是否记录这个输出值。

严格的写法应该是这样:

```py
# 先判断当前是否能输出debug日志:
if logger.isEnabledFor(logging.INFO):
    logger.debug('%s', expensive_func())
```

### 保存和获取日志

现在您已经学会了编写这些（漂亮的）日志，您必须确定如何保存它们。默认情况下，日志会写入标准输出设备（可能是您的终端窗口），但Python的logging模块提供了一组丰富的选项来自定义存储方式。我们提倡将日志记录到标准输出，Heroku，Amazon Elastic Beanstalk和Docker等平台通过捕获标准输出并重定向到平台级别的其他日志记录工具来存储日志。

但是, 有时候我们还需要使用其他一些存储方式, 这里做简单介绍:

- 存储到文件





```python
%%script python

import logging
logger = logging.getLogger(__name__)

handler = logging.FileHandler('myLogs.log')
handler.setLevel(logging.INFO)

logger.addHandler(handler)
logger.warn('You can find this written in myLogs.log')
```


```python
open('myLogs.log', 'r').read()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'You can find this written in myLogs.log\nYou2 can find this written in myLogs.log\nYou can find this written in myLogs.log\n'

</div>
{% endraw %}



### Logging in Library

当你开发一个python库, 你的库最好是共享一个日志配置, 而不是每个模块都重新配置日志。

在库中实例化logger时的最佳做法是仅使用`__name__`全局变量创建它们：logging模块使用点表示法创建记录器层次结构，因此使用`__name__`可确保没有名称冲突。

下面是python著名的requests库所采用的方法, 在`__init__.py`文件中, 有如下代码:

```py
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
```

位于logging包中的NullHandler类不执行任何格式化或输出。它本质上是一个供库开发人员使用的“无操作”处理程序。类似于占位符。 当然, 你可以使用文件处理器来替换它:


```python
import logging

logging.getLogger(__name__).addHandler(logging.FileHandler('myLogs.log'))
```

### Logging in an Application

twelve factor应用程序是应用程序开发中良好实践的权威参考，其中包含日志的最佳实践。它着重提倡将日志事件视为事件流，并将该事件流发送到标准输出以由应用程序环境处理。

在应用程序开发中, 至少有三种方式来配置日志系统:

- 使用ini文件
- 使用json文件
- 使用python代码

#### 使用init文件的例子

```
[loggers]
keys=root

[handlers]
keys=stream_handler

[formatters]
keys=formatter

[logger_root]
level=DEBUG
handlers=stream_handler

[handler_stream_handler]
class=StreamHandler
level=DEBUG
formatter=formatter
args=(sys.stderr,)

[formatter_formatter]
format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s
```

在代码中, 使用`logging.config.fileConfig() `来加载ini配置文件:


```python
import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')
```

#### 字典或者json配置


```python
import logging
from logging.config import dictConfig

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['h'],
        'level': logging.DEBUG,
        },
)

dictConfig(logging_config)

logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')
```

#### 在python代码中配置


```python
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists')
```


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python3的logging模块的最佳实践.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
