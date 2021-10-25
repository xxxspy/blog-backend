
---

title: python深入理解print函数
date: 2019-08-18 12:44:03
tags: [print, python]

---

如果你像大多数Python用户一样，包括我在内，那么你可以通过学习print（）来开始你的Python之旅。它帮助你写了你自己的hello world。您可以使用它在屏幕上显示格式化的消息，也许会发现一些错误。但是，如果你认为你掌握了有关Python的print函数的全部知识，那么你肯定错了！

<!-- more -->

继续阅读这个看似无聊和不受重视的小功能。本教程将帮助您快速有效地使用Python print（）。但是，当您继续浏览各个部分时，请准备好, 你可能会对print函数感到惊讶！

#### 在本教程结束后, 你将会学会:

- 避免print函数的常用函数
- 处理换行符，字符编码和缓存
- print到文件
- 在终端中构建高级用户界面

如果您是一个完全的初学者，那么您将从阅读本教程的第一部分中获益最多，该教程阐述了使用Python进行打印的基本要素。否则，请随意跳过该部分并按照您认为合适的方式跳转。

> 注意: print是Python3的一个重要升级，它取代了Python2中提供的旧print语句。正如你很快就会看到的那样，有很多很好的理由支持我们这样做。虽然本教程侧重于Python3，但它确实展示了Python中旧的打印方式以供参考。

## 基础入门

熟悉python的人可以跳过该部分。

让我们通过查看Python中几个真实的打印示例来介绍。在本节结束时，您将了解调用print的每种可能方式。或者，在程序员术语中，您会说您将熟悉函数签名(function signature)。

### 调用print

使用Python print的最简单的例子只需几个按键：


```python
print()
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>


</div>
{% endraw %}

你没有传递任何参数，但你仍然需要在末尾放置空括号，这告诉Python实际执行该函数而不是仅仅按名称引用它。

这将输出一个不可见的换行符，这反过来会导致屏幕上出现一个空行。您可以多次调用print来添加垂直空间。就像你在文字处理器上按键盘上的Enter键一样。


```python
for i in range(10):
    print()
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>











</div>
{% endraw %}

正如你刚才看到的那样，调用不带参数的print会产生一个空白行，这是一行仅由换行符组成的行。不要将它与空行混淆，空行根本不包含任何字符，甚至不包括换行符！

使用print可以打印几乎任何东西: 比如:


```python
print('HelloWorld')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
HelloWorld

</div>
{% endraw %}

不仅仅是字符串，但其他数据类型如何呢？让我们尝试不同内置的数据类型，看看会出现什么：


```python
print(42)                            # <class 'int'>

print(3.14)                          # <class 'float'>

print(1 + 2j)                        # <class 'complex'>

print(True)                          # <class 'bool'>

print([1, 2, 3])                     # <class 'list'>

print((1, 2, 3))                     # <class 'tuple'>

print({'red', 'green', 'blue'})      # <class 'set'>

print({'name': 'Alice', 'age': 42})  # <class 'dict'>

print('hello')                       # <class 'str'>

print(None)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
42
3.14
(1+2j)
True
[1, 2, 3]
(1, 2, 3)
{'green', 'red', 'blue'}
{'name': 'Alice', 'age': 42}
hello
None

</div>
{% endraw %}

但要注意None常数。尽管用于表示缺少值，但它将显示为“None”而不是空字符串。

print函数如何知道如何使用所有这些不同的类型？嗯，简短的回答是它并不知道。它隐含地在幕后调用str方法来将任何对象类型转换为字符串。之后，它以统一的方式处理字符串。

在本教程的后面，您将学习如何使用此机制打印自定义数据类型（如类）。

好的，您现在可以使用单个参数或不带任何参数调用print。您知道如何在屏幕上打印固定或格式化的消息。下一小节将对消息格式进行一些扩展。

### 分离多个参数

您看到print在没有任何参数的情况下调用以生成空行，然后使用单个参数调用以显示固定或格式化的消息。

但是，事实证明这个函数可以接受任意数量的位置参数，包括零个，一个或多个参数。这在消息格式化的常见情况下非常方便，您可能希望将几个元素连接在一起。

下面我们看一个例子:


```python
import os

print('My name is', os.getlogin(), 'and I am', 42)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
My name is syd and I am 42

</div>
{% endraw %}

print连接传递给它的所有四个参数，并在它们之间插入一个空格，这样你就不会得到像“MynameissydandIam42”这样被压扁的信息。

请注意，它还通过在将每个参数连接在一起之前隐式调用str来处理类型转换。如果从上一小节中回忆一下，由于类型不兼容，简单的连接可能很容易导致错误：


```python
print('My age is: ' + 42)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-d56594833ec4> in <module>
    ----> 1 print('My age is: ' + 42)
    

    TypeError: must be str, not int


除了接受可变数量的位置参数之外，print（）还定义了四个命名或关键字参数，这些参数是可选的，因为它们都具有默认值。您可以通过从交互式解释器调用help（print）来查看其简要文档。


```python
help(print)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.


</div>
{% endraw %}

我们先来看`sep`这个关键字参数, 它指的是位置参数之间的间隔字符, 比如:


```python
print(1, 2, sep='+')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
1+2

</div>
{% endraw %}

如果使用换行符呢?


```python
print(1, 2, 3, 4, 5, sep='\n')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
1
2
3
4
5

</div>
{% endraw %}

一个更有用的sep参数示例是打印文件路径之类的东西：


```python
print('home', 'user', 'documents', sep='/')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
home/user/documents

</div>
{% endraw %}

请记住，分隔符位于元素之间，而不是它们周围，因此您需要以某种方式实现它：


```python
print('/home', 'user', 'documents', sep='/')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
/home/user/documents

</div>
{% endraw %}


```python
print('', 'home', 'user', 'documents', sep='/')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
/home/user/documents

</div>
{% endraw %}

### 换行符

Python的print函数总是在没有询问的情况下添加\n，因为在大多数情况下这就是你想要的。要禁用它，您可以利用另一个关键字参数end，它决定了该行的结尾。


```python
print('q')
print('q')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
q
q

</div>
{% endraw %}


```python
print('q', end='')
print('q')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
qq

</div>
{% endraw %}

### 打印输出到文件

信不信由你，print（）不知道如何将消息转换成屏幕上的文本，坦率地说它不需要。这是低级代码层的工作，它可以理解字节并知道如何显示它们。

print（）是对底层的抽象，提供了一个方便的接口，只是将实际打印委托给流或类文件对象。流可以是磁盘上的任何文件，网络套接字或内存缓冲区。

除此之外，操作系统还提供三种标准流：

- stdin：标准输入
- stdout：标准输出
- stderr：标准错误

在Python中，您可以通过内置的sys模块访问所有标准流：


```python
import sys

print(sys.stdin, sys.stdin.fileno())
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='cp936'> 0

</div>
{% endraw %}


```python
print(sys.stdout)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
<ipykernel.iostream.OutStream object at 0x00000235BE87EB38>

</div>
{% endraw %}


```python
print(sys.stderr)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
<ipykernel.iostream.OutStream object at 0x00000235BE87E7B8>

</div>
{% endraw %}

如您所见，这些预定义值类似于具有模式和编码属性的文件类对象以及.read（）和.write（）方法等。

默认情况下，print（）通过其file参数绑定到sys.stdout，但您可以更改它。使用该关键字参数指示在写入或追加模式下打开的文件，以便消息直接进入：


```python
with open('file.txt', mode='w') as file_object:
    print('hello world', file=file_object)
```

这将使您的代码免受操作系统级别的流重定向，这可能是也可能不是你想要的。

> 注意, 不要使用pring来打印binary数据, 如果你想在屏幕上打印bytes数据, 你可能得不到你想要的:


```python
print(b'\x41')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
b'A'

</div>
{% endraw %}

请注意，print（）无法控制字符编码。流是负责将接收的Unicode字符串正确编码为字节。在大多数情况下，您不会自己设置编码，因为默认的UTF-8就是您想要的。在windows系统下, 我们可能会遇到这样的错误:

```py
print('über 🙂')
```

输出:
```
Traceback (most recent call last):
    print('über \U0001f642')
UnicodeEncodeError: 'gbk' codec can't encode character '\U0001f642' in position 5: illegal multibyte sequence
```

正如我上面所说, 我们无法控制print的编码问题。我们唯一能做的就是, 不要print系统无法处理的字符串。

### 缓存print

在上一小节中，您了解到print（）将打印委托给类似文件的对象，例如sys.stdout。但是，某些流会缓冲某些I/O操作以提高性能，这可能会引起你的困惑。我们来看一个例子吧。


```python
# 这段代码在notebook中没有效果

import time

num_seconds = 3
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end='...')
        time.sleep(1)
    else:
        print('Go!')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
3...2...1...Go!

</div>
{% endraw %}

在你的终端中运行这个代码的效果是这样的:

<img src="https://files.realpython.com/media/print_countdown.ba38eb242915.gif">

这是因为在这种情况下，操作系统会缓冲对标准输出的后续写入。您需要知道缓冲有三种流：

- Unbuffered 不缓存
- Line-buffered 缓存直到换行
- Block-buffered 缓存达到某个量以后才输出

标准输出中, 使用了后面两种缓存方式, 具体到底是哪种缓存, 这取决于哪个先达到标准。

缓冲有助于减少昂贵的I/O调用次数。例如，考虑通过高延迟网络发送消息。当您连接到远程服务器以通过SSH协议执行命令时，您的每次击键实际上可能会产生一个单独的数据包，这个数据包比其有效负载大几个数量级。等到输入至少几个字符然后将它们一起发送是有意义的。

另一方面，缓冲有时会产生不良影响，正如您在倒计时示例中看到的那样。要修复它，您可以简单地告诉print（）强制刷新流：


```python
num_seconds = 3
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end='...', flush=True)
        time.sleep(1)
    else:
        print('Go!')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
3...2...1...Go!

</div>
{% endraw %}

就这样。你的倒计时现在应该按预期工作，但不要相信我的话。继续测试它以查看差异。

恭喜！此时，您已经看到了调用print（）的示例，其中包含了所有参数。你知道他们的目的以及何时使用它们。然而，理解函数签名只是一个开始。在接下来的部分中，您将了解原因。

## 自定义打印方式

到目前为止，您只处理了内置数据类型，如字符串和数字，但您经常需要打印自己构建的类。我们来看看定义它们的打印方式。

对于没有任何逻辑的简单对象，其目的是携带数据，您通常会利用标准库中提供的namedtuple。命名元组具有开箱即用的简洁文本表示：


```python
from collections import namedtuple
Person = namedtuple('Person', 'name age')
jdoe = Person('John Doe', 42)
print(jdoe)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Person(name='John Doe', age=42)

</div>
{% endraw %}

只要保存数据namedtuple就足够了，但是为了向Person类型添加方法，你最终需要定义一个类。看看这个例子：


```python
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
        
jdoe = Person('John Doe', 42)
print(jdoe)    

```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
<__main__.Person object at 0x00000235BEA9D6A0>

</div>
{% endraw %}

它是对象的默认表示，打印出了它们在内存中的地址，相应的类名和定义它们的模块。稍后我们要彻底解决这个问题，但只作为快速解决方法，您可以通过继承将namedtuple和自定义类组合在一起：


```python
from collections import namedtuple

class Person(namedtuple('Person', 'name age')):
    pass


jdoe = Person('John Doe', 42)
print(jdoe)   
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Person(name='John Doe', age=42)

</div>
{% endraw %}

### 两个内置函数`str`和`repr`

从前面的小节中，您已经知道print（）隐式调用内置的str（）函数将其位置参数转换为字符串。实际上，对普通Person类的实例手动调用str（）会产生与打印它相同的结果：


```python
str(jdoe)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    "Person(name='John Doe', age=42)"

</div>
{% endraw %}



反过来，str（）在类体中寻找两种魔术方法中的一种，通常是你实现的。如果找不到，那么它会回到丑陋的默认表示。那些神奇的方法是按照这个顺序被搜索的：

- `__str__`
- `__repr__`

建议使用`__str__`返回一个简短的人类可读文本，其中包含最专用要的属性的信息。而且，在打印对象时，您不希望暴露敏感数据，例如用户密码。

但是，另一个`__repr__`应该提供有关对象的完整信息，以允许从字符串恢复其状态。理想情况下，它应返回有效的Python代码，以便您可以将其直接传递给eval（）函数：


```python
repr(jdoe)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    "Person(name='John Doe', age=42)"

</div>
{% endraw %}




```python
eval(repr(jdoe))
```




{% raw %}
<div class="output">
输出(plain):<br/>

    Person(name='John Doe', age=42)

</div>
{% endraw %}



注意使用另一个内置函数repr（），该函数总是尝试在对象中调用`__repr__`，但如果找不到该方法，则回退到默认表示。

### 自定义str和repr

知道上面的方法, 我们就可以自己定义类的打印方式:


```python
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
        
    def __str__(self):
        return f'Person name={self.name}'
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    
jd = Person('John Doe', 42)

print(jd)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Person name=John Doe

</div>
{% endraw %}

但是我们需要注意, 当你的类位于list中时, 打印的时候实际上调用的时`__repr__`函数:


```python
ps = [Person('A', 1), Person('B', 2)]
ps
```




{% raw %}
<div class="output">
输出(plain):<br/>

    [Person(name='A', age=1), Person(name='B', age=2)]

</div>
{% endraw %}



如果没有内置的数据类型满足您的需求，Python在定义您自己的数据类型时会给您很大的自由。其中一些（例如命名元组和数据类）提供的字符串表示看起来很好而不需要您做任何工作。尽管如此，为了获得最大的灵活性，您必须定义一个类并覆盖其上述的魔术方法。

## 风格化打印

如果您认为打印只是在屏幕上点亮像素，那么从技术上讲，您是对的。但是，有一些方法可以让它看起来很酷。在本节中，您将了解如何格式化复杂数据结构，添加颜色和其他装饰，构建界面，使用动画，甚至播放带有文本的声音！

### 优化显示复杂数据

计算机语言允许您以结构化方式表示数据和可执行代码。然而，与Python不同，大多数语言都为您提供了使用空格和格式的大量自由。这可能很有用，例如在压缩中，但有时会导致代码不太可读。

`Pretty-printing`是使一段数据或代码看起来更好看，以便更容易理解。这是通过缩进某些行，插入换行符，重新排序元素等来完成的。

Python在其标准库中附带了`pprint`模块，它可以帮助您完美地打印不适合单行的显示的大型数据结构。因为它以更人性化的方式打印，所以许多流行的REPL工具（包括JupyterLab和IPython）默认使用它来代替常规的print（）函数。

在notebook中, 可以使用`%pprint`魔法来打开和关闭功能:


```python
%pprint
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Pretty printing has been turned OFF

</div>
{% endraw %}


```python
%pprint
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Pretty printing has been turned ON

</div>
{% endraw %}

为了对比, 我们看下下面的结果:


```python
from pprint import pprint as pp
data = {'powers': [x**10 for x in range(10)]}
print(data)
pp(data)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
{'powers': [0, 1, 1024, 59049, 1048576, 9765625, 60466176, 282475249, 1073741824, 3486784401]}
{'powers': [0,
            1,
            1024,
            59049,
            1048576,
            9765625,
            60466176,
            282475249,
            1073741824,
            3486784401]}

</div>
{% endraw %}

该函数应用合理的格式以提高可读性，但您可以使用几个参数进一步自定义它。例如，您可以通过在给定级别下方显示省略号来限制深层嵌套的层次结构：


```python
cities = {'USA': {'Texas': {'Dallas': ['Irving']}}}
pp(cities, depth=3)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
{'USA': {'Texas': {'Dallas': [...]}}}

</div>
{% endraw %}

当对象中存在自我引用的数据时, pp的输出更能让人理解:


```python
items = [1,2,3]
items.append(items)
print(items)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
[1, 2, 3, [...]]

</div>
{% endraw %}


```python
pp(items)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
[1, 2, 3, <Recursion on list with id=2429854515400>]

</div>
{% endraw %}


```python
id(items)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    2429854515400

</div>
{% endraw %}



pprint（）会在打印前自动为您排序字典键，从而实现一致的比较。在比较字符串时，通常不关心序列化属性的特定顺序。无论如何，在序列化之前最好比较实际的词典。

字典通常表示JSON数据，它在Internet上广泛使用。要将字典正确序列化为有效的JSON格式字符串，您可以利用json模块。它也具有漂亮的打印功能：


```python
import json
data = {'username': 'jdoe', 'password': 's3cret'}
ugly = json.dumps(data)
pretty = json.dumps(data, indent=4, sort_keys=True)
print(ugly)
{"username": "jdoe", "password": "s3cret"}
print(pretty)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
{"username": "jdoe", "password": "s3cret"}
{
    "password": "s3cret",
    "username": "jdoe"
}

</div>
{% endraw %}

但请注意，您需要自己处理打印，因为这不是您通常想要做的事情。类似地，pprint模块有一个额外的pformat（）函数，它返回一个字符串，以防你不得不做一些除打印之外的事情。

令人惊讶的是，pprint（）的签名与print（）函数的签名完全不同。您甚至无法传递多个位置参数，这表明它关注打印数据结构的重点。

### 使用ANSI转义序列添加颜色

随着个人电脑越来越复杂，它们拥有更好的图形并可以显示更多颜色。但是，不同的供应商对用于控制它的API设计有自己的想法。几十年前，当美国国家标准协会的人们决定通过定义ANSI转义码来统一它时，情况发生了变化。

今天的大多数终端在某种程度上支持这个标准。直到最近，Windows操作系统才是一个值得注意的例外。因此，如果您想要最佳的可移植性，请使用Python中的colorama库。它将ANSI代码转换为Windows中的相应对应代码，同时在其他操作系统中保持原样。

要检查终端是否理解ANSI转义序列（例如，与颜色相关），您可以尝试使用以下命令：

```
tput colors
```

我在Linux上的默认终端说它可以显示256种不同的颜色，而xterm只给我8. 如果颜色不受支持，命令将返回负数。

ANSI转义序列就像终端的标记语言。在HTML中，您使用标签（例如`<b>`或`<i>`）来更改元素在文档中的显示方式。这些标记与您的内容混合在一起，但它们本身并不可见。同样，只要识别出转义码，转义码就不会显示在终端中。否则，它们将以字面形式出现，就像您正在查看网站的源码一样。

顾名思义，序列必须以不可打印的Esc字符开头，其ASCII值为27，有时表示为十六进制的0x1b或八进制的033。您可以使用Python数字文字来快速验证它确实是相同的数字：


```python
27 == 0x1b == 0o33
```




{% raw %}
<div class="output">
输出(plain):<br/>

    True

</div>
{% endraw %}



此外，您可以在shell中使用`\e`转义序列获取它：

```
echo -e "\e"
```

最常见的ANSI转义序列采用以下形式：

元素 | 描述 | 例子
-- | -- | - |
Esc | 转义符 | `\033`
`[` | 方括号 | `[`
数字代码 | 1个或多个数字以分号间隔 | 0
字符代码 | 大小写字母 | m

数字代码可以是用分号分隔的一个或多个数字，而字符代码只是一个字母。它们的具体含义由ANSI标准定义。例如，要重置所有格式，您可以键入以下命令之一，它使用代码零和字母m：

```
`$ echo -e "\e[0m"
$`

要使用RGB通道设置前景和背景，假设您的终端支持24位深度，您可以提供多个数字：

```
$ echo -e "\e[38;2;0;0;0m\e[48;2;255;255;255mBlack on white\e[0m"
```

您可以使用ANSI转义码设置文本颜色, 还可以清除并滚动终端窗口，更改其背景，移动光标，使文本闪烁或使用下划线进行装饰。

在Python中，您可能会编写一个辅助函数来允许将任意代码包装到序列中：

这会使单词真正显示为红色，粗体和带下划线的字体：


```python
def esc(code):
    return f'\033[{code}m'

print(esc('31;1;4') + 'really' + esc(0) + ' important')
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
[31;1;4mreally[0m important

</div>
{% endraw %}

但是，ANSI转义码有更高级别的抽象，例如上面提到的colorama库，以及在控制台中构建用户界面的工具。

### 构建控制台用户界面

虽然使用ANSI转义码无疑是一大乐趣，但在现实世界中，您宁愿拥有更多抽象构建块来组合用户界面。有一些库可以对终端提供如此高级别的控制，但是curses似乎是最受欢迎的选择。

要在Windows中使用curses库，您需要安装第三方软件包：

这是因为curses在Windows的Python发行版的标准库中不可用。


```python
!pip install windows-curses
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Collecting windows-curses
  Downloading https://files.pythonhosted.org/packages/0d/c7/45bf2a8f517a6c2ee7eacf44cfc4e2520abb73931cadbee94acabfdbedc9/windows_curses-2.0-cp36-cp36m-win_amd64.whl (76kB)
Installing collected packages: windows-curses
Successfully installed windows-curses-2.0

</div>
{% endraw %}

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
You are using pip version 19.0.3, however version 19.2.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

</div>
{% endraw %}

首先，它允许您根据独立的图形小部件而不是一团文本进行思考。此外，你有很大的自由来表达你内心的艺术特质，因为它真的像在画布上画画。工具库隐藏了必须处理不同终端的复杂性。除此之外，它对键盘事件有很大的支持，这可能对编写视频游戏很有用。

制作贪吃蛇游戏怎么样？让我们创建一个Python蛇模拟器：

<img src="https://files.realpython.com/media/snake.a9589582b58a.gif">

首先，您需要导入curses模块。由于它修改了正在运行的终端的状态，因此处理错误并优雅地恢复以前的状态非常重要。您可以手动执行此操作，但该库为您的主要功能提供了一个方便的包装器：


```python
import curses

def main(screen):
    pass

if __name__ == '__main__':
    curses.wrapper(main)
```

注意，该函数必须接受对屏幕对象的引用，也称为stdscr，稍后您将使用该引用进行其他设置。

如果您现在运行此程序，您将看不到任何效果，因为它会立即终止。但是，你可以添加一个小延迟来偷看：


```python
import time, curses

def main(screen):
    time.sleep(1)

if __name__ == '__main__':
    curses.wrapper(main)
```

__注意__以上代码不能在jupyter notebook中运行, 它会提示你"服务似乎挂掉了,但是会立刻重启的."

这次屏幕完全空白一秒钟，但光标仍然闪烁要隐藏它，只需调用模块中定义的配置函数之一：


```python
import time, curses

def main(screen):
    curses.curs_set(0)  # 隐藏光标
    time.sleep(1)

if __name__ == '__main__':
    curses.wrapper(main)
```

让我们将蛇定义为屏幕坐标中的点列表：

```py
snake = [(0, i) for i in reversed(range(20))]
```

蛇的头部始终是列表中的第一个元素，而尾部是最后一个元素。蛇的初始形状是水平的，从屏幕的左上角开始朝向右侧。当其y坐标保持为零时，其x坐标从头到尾减小。

要绘制蛇，你将从头部开始，然后是剩下的部分。列表中每个元素都是（y，x）坐标，因此您可以使用`*`解包它：

```py
# Draw the snake
screen.addstr(*snake[0], '@')
for segment in snake[1:]:
    screen.addstr(*segment, '*')
```


同样，如果您现在运行此代码，它将不会显示任何内容，因为您必须在以后显式刷新屏幕：

```py
import time, curses

def main(screen):
    curses.curs_set(0)  # Hide the cursor

    snake = [(0, i) for i in reversed(range(20))]

    # Draw the snake
    screen.addstr(*snake[0], '@')
    for segment in snake[1:]:
        screen.addstr(*segment, '*')

    screen.refresh()
    time.sleep(1)

if __name__ == '__main__':
    curses.wrapper(main)
```

你想在四个方向中的一个方向移动蛇，可以定义为向量。最终，方向将根据箭头键击而改变，因此您可以将其连接到库的键代码：

```py
directions = {
    curses.KEY_UP: (-1, 0),
    curses.KEY_DOWN: (1, 0),
    curses.KEY_LEFT: (0, -1),
    curses.KEY_RIGHT: (0, 1),
}

direction = directions[curses.KEY_RIGHT]
```

蛇如何移动？事实证明，只有它的头部真正移动到一个新的位置，而所有其他部分向头移动。在每个步骤中，除头部和尾部外，几乎所有部分都保持不变。假设蛇没有生长，你可以删除尾部并在列表的开头插入一个新头：

```py
# Move the snake
snake.pop()
snake.insert(0, tuple(map(sum, zip(snake[0], direction))))
```

要获取头部的新坐标，需要向其添加方向向量。但是，在Python中添加元组会产生更大的元组，而不是相应矢量分量的代数和。解决此问题的一种方法是使用内置的zip（），sum（）和map（）函数。

按键时方向会发生变化，因此您需要调用.getch（）来获取按下的键代码。但是，如果按下的键与之前定义为字典键的箭头键不对应，则方向不会改变：

```py
# Change direction on arrow keystroke
direction = directions.get(screen.getch(), direction)
```

但是，默认情况下，.getch（）是一个阻塞调用，它会阻止蛇移动，除非有击键。因此，您需要通过添加另一个配置来使IO无阻塞：

```py
def main(screen):
    curses.curs_set(0)    # Hide the cursor
    screen.nodelay(True)  #  I/O 不阻塞
```

你差不多完成了，但剩下的还有最后一件事。如果你现在循环这个代码，蛇似乎会增长而不是移动。那是因为你必须在每次迭代之前明确地擦除屏幕。

最后，这就是你在Python中玩蛇游戏所需的一切：

```py
import time, curses

def main(screen):
    curses.curs_set(0)    # Hide the cursor
    screen.nodelay(True)  # Don't block I/O calls

    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1),
    }

    direction = directions[curses.KEY_RIGHT]
    snake = [(0, i) for i in reversed(range(20))]

    while True:
        screen.erase()

        # Draw the snake
        screen.addstr(*snake[0], '@')
        for segment in snake[1:]:
            screen.addstr(*segment, '*')

        # Move the snake
        snake.pop()
        snake.insert(0, tuple(map(sum, zip(snake[0], direction))))

        # Change direction on arrow keystroke
        direction = directions.get(screen.getch(), direction)

        screen.refresh()
        time.sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)
```

这仅仅是curses模块功能的简单展示。您可以将它用于更专业的游戏开发。

### 用酷炫的动画

动画不仅可以使用户界面更吸引眼球，而且还可以改善整体用户体验。例如，当您向用户提供长耗时任务的反馈时，他们会知道您的程序是否仍在工作，或者是否有需要将其杀死。

要在终端中为文本设置动画，您必须能够自由地移动光标。您可以使用前面提到的工具之一，即ANSI转义码或curses库来执行此操作。但是，我想向您展示一种更简单的方法。

如果动画可以约束为单行文本，那么您可能对两个特殊的转义字符序列感兴趣：

- Carriage return: \r
- Backspace: \b

第一个将光标移动到行的开头，而第二个将光标向左侧移动一个字符。它们都以非破坏性的方式工作，而不会覆盖已经编写过的文本。

我们来看几个例子。

您经常需要显示某种旋转轮来指示正在进行的工作，而不确切知道剩下多少时间完成：

<img src="https://files.realpython.com/media/spinning_wheel.c595af6f83ea.gif">

许多命令行工具在通过网络下载数据时使用此技巧。您可以从一系列以循环方式循环的字符制作一个非常简单的定格动画：


```python
from itertools import cycle
from time import sleep

count = 0
for frame in cycle(r'-\|/-\|/'):
    print('\r', frame, sep='', end='', flush=True)
    sleep(0.2)
    count += 1
    if count > 20:
        break
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
-
</div>
{% endraw %}

循环获取要打印的下一个字符，然后将光标移动到行的开头，并覆盖之前的任何内容而不添加换行符。您不希望位置参数之间有额外的空间，因此separator参数必须为空。另外，请注意由于文字中存在反斜杠字符而使用Python的原始字符串。

当您知道剩余时间或任务完成百分比时，您就可以显示动画进度条：

<img src="https://files.realpython.com/media/progress.6bd055d8dcc4.gif">

首先，您需要计算要显示的进度条的长度以及要插入的空白空间数量。接下来，删除该行并从头开始构建：




```python
from time import sleep

def progress(percent=0, width=29):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
[#############################] 100%                           ] 2%#                            ] 6%##                           ] 8%###                          ] 13%#####                        ] 20%######                       ] 22%######                       ] 24%########                     ] 29%########                     ] 31%#########                    ] 33%###########                  ] 40%############                 ] 42%#############                ] 46%###############              ] 53%###############              ] 55%#################            ] 59%##################           ] 64%###################          ] 66%###################          ] 68%#####################        ] 75%######################       ] 79%#######################      ] 81%########################     ] 86%#########################    ] 88%###########################  ] 95%
</div>
{% endraw %}

> 注意, 在notebook中, 你可能看到的是上面输出的混乱的结果。

### 用打印产生声音

如果你的年龄够大你应该知道一些比较古老的电脑，那么你应该还能记得它们独特的嘟嘟声，通常用于指示硬件问题。它们几乎不会发出其他声音，但视频游戏似乎更好。

今天你仍然可以利用小型扬声器，但很有可能你的笔记本电脑没有附带。在这种情况下，您可以在shell中启用终端铃声仿真，以便播放系统警告声音。

继续并输入此命令以查看您的终端是否可以播放声音：

```
$ echo -e "\a"
```

这通常会打印文本，但-e标志可以解释反斜杠转义。如您所见，有一个专用的转义序列`\a`，代表“alert”，它输出一个特殊的铃声字符。有些终端在看到它时发出声音。

同样，您可以在Python中打印此字符。也许在一个循环中形成某种旋律。虽然它只是一个音符，但您仍然可以改变连续实例之间的暂停长度。这似乎是摩尔斯电码回放的完美玩具！


```python
from time import sleep

speed = 0.1

def signal(duration, symbol):
    sleep(duration)
    print(symbol, end='', flush=True)

dot = lambda: signal(speed, '·\a')
dash = lambda: signal(3*speed, '−\a')
symbol_space = lambda: signal(speed, '')
letter_space = lambda: signal(3*speed, '')
word_space = lambda: signal(7*speed, ' ')


while True:
    dot()
    symbol_space()
    dot()
    symbol_space()
    dot()
    letter_space()
    dash()
    symbol_space()
    dash()
    symbol_space()
    dash()
    letter_space()
    dot()
    symbol_space()
    dot()
    symbol_space()
    dot()
    word_space()
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
···−−−··· ···−−−··· ···−−−··· ···−−−··· ···−−−··· ···−−−··· ···−−−··· ···
</div>
{% endraw %}


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-9-651c4daed144> in <module>
         21     dot()
         22     letter_space()
    ---> 23     dash()
         24     symbol_space()
         25     dash()
    

    <ipython-input-9-651c4daed144> in <lambda>()
          8 
          9 dot = lambda: signal(speed, '·\a')
    ---> 10 dash = lambda: signal(3*speed, '−\a')
         11 symbol_space = lambda: signal(speed, '')
         12 letter_space = lambda: signal(3*speed, '')
    

    <ipython-input-9-651c4daed144> in signal(duration, symbol)
          4 
          5 def signal(duration, symbol):
    ----> 6     sleep(duration)
          7     print(symbol, end='', flush=True)
          8 
    

    KeyboardInterrupt: 


> 注意, 在notebook中你不可能听到任何声音


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python深入理解print函数.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
