
---

title: python中logging模块的error和exception的区别和最佳实践
date: 2019-08-04 12:44:03
tags: [logging, python]

---

在python中, logging模块是用于处理日志信息的, 几乎在所有项目中都会用到这个模块。
而logging.error和logging.exception这两个方法很相似, 用起来也容易混淆。

<!-- more -->



其实这两个方法只有一个区别, loging.error只是记录一个日志消息, 日志等级是error, 而exception在记录消息的同时, 默认会记录错误发生的traceback信息, 所以说, 如果你想记录更详细的错误信息, 你最好是使用exception, 但是error方法也可以输出traceback信息, 只需要你设置一个参数`exc_info`, 下面我们使用例子来看看具体的区别:

先引入logging模块:


```python
import logging

log = logging.getLogger(__name__)
```

### 使用error记录错误日志

你只能看到一个简单的信息:


```python
try:
    raise ValueError('A error happend !')
except ValueError as e:
    log.error("值错误")
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
值错误

</div>
{% endraw %}

我们使用`exc_info`参数: 这样就能看到traceback信息:


```python
try:
    raise ValueError('A error happend !')
except ValueError as e:
    log.error("值错误", exc_info=True)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
值错误
Traceback (most recent call last):
  File "<ipython-input-9-7b3dde823828>", line 2, in <module>
    raise ValueError('A error happend !')
ValueError: A error happend !

</div>
{% endraw %}

### 使用exception

exception默认就会输出traceback信息:


```python
try:
    raise ValueError('A error happend !')
except ValueError as e:
    log.exception('值错误')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
值错误
Traceback (most recent call last):
  File "<ipython-input-10-aaffeaaf1df4>", line 2, in <module>
    raise ValueError('A error happend !')
ValueError: A error happend !

</div>
{% endraw %}


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python中logging模块的error和exception的区别和最佳实践.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
