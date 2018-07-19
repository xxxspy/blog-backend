
---
title: python3 f-string格式化字符串的高级用法
date: 2018-07-19 18:17:55
tags: [python, 格式化字符串]
toc: true

---
<span></span>
<!-- more -->


> 如果你刚入门python, 可以先看这篇字符串格式化的最佳实践, 它更适合入门:[python3字符串format最佳实践](/2018/07/01/python3字符串format最佳实践/)

主要内容
------

从Python 3.6开始，f-string是格式化字符串的一种很好的新方法。与其他格式化方式相比，它们不仅更易读，更简洁，不易出错，而且速度更快！

在本文的最后，您将了解如何以及为什么今天开始使用f-string(后文称为`F字符串`)。

但首先, 我们要聊以下在F字符串出现之前我们怎么实现格式化字符的。



### 旧时代的格式化字符串

在Python 3.6之前，有两种将Python表达式嵌入到字符串文本中进行格式化的主要方法：`％-formatting`和`str.format（）`。您即将看到如何使用它们以及它们的局限性。

#### Option #1: %-formatting

这是Python格式化的OG(original generation)，伴随着python语言的诞生。您可以在Python文档中阅读更多内容。请记住，文档不建议使用％格式，其中包含以下注释：

> “The formatting operations described here exhibit a variety of quirks that lead to a number of common errors (such as failing to display tuples and dictionaries correctly).

> Using the newer formatted string literals or the str.format() interface helps avoid these errors. These alternatives also provide more powerful, flexible and extensible approaches to formatting text.” 

#### 怎样使用 %-formatting

字符串对象具有使用％运算符的内置操作，您可以使用它来格式化字符串。以下是实践中的情况：


```python
name = "Eric"
"Hello, %s." % name
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric.'

</div>
{% endraw %}



为了插入多个变量，您必须使用这些变量的元组。以下是你如何做到这一点：


```python
name = "Eric"
age = 74
"Hello, %s. You are %s." % (name, age)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric. You are 74.'

</div>
{% endraw %}



#### 为什么 %-formatting不好用

上面刚刚看到的代码示例足够易读。但是，一旦你开始使用几个参数和更长的字符串，你的代码将很快变得不太容易阅读。事情已经开始显得有点凌乱：


```python
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
"Hello, %s %s. You are %s. You are a %s. You were a member of %s." %\
(first_name, last_name, age, profession, affiliation)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric Idle. You are 74. You are a comedian. You were a member of Monty Python.'

</div>
{% endraw %}



不幸的是，这种格式不是很好，因为它是冗长的，会导致错误，比如不能正确显示元组或字典。幸运的是，未来有更光明的日子。

### Option #2: str.format()

这种更新的工作方式是在Python 2.6中引入的。您可以查看Python文档以获取更多信息。

#### 怎样使用Use str.format()


`str.format（）`是对`%-formatting`的改进。它使用正常的函数调用语法，并且可以通过对要转换为字符串的对象的`__format __（）`方法进行扩展。

使用`str.format（）`，替换字段用大括号标记：


```python
"Hello, {}. You are {}.".format(name, age)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric. You are 74.'

</div>
{% endraw %}



您可以通过引用其索引来以任何顺序引用变量：


```python
"Hello, {1}. You are {0}-{0}.".format(age, name)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric. You are 74-74.'

</div>
{% endraw %}



但是，如果插入变量名称，则会获得额外的能够传递对象的权限，然后在大括号之间引用参数和方法：


```python
person = {'name': 'Eric', 'age': 74}
"Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric. You are 74.'

</div>
{% endraw %}



你也可以使用`**`来用字典来完成这个巧妙的技巧：


```python
"Hello, {name}. You are {age}.".format(**person)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric. You are 74.'

</div>
{% endraw %}



与`f-string`相比，`str.format()`绝对是一个升级版本，但它并非总是好的。


#### 为什么 str.format() 并不好

使用`str.format()`的代码比使用`%-formatting`的代码更易读，但当处理多个参数和更长的字符串时，`str.format()`仍然可能非常冗长。看看这个：


```python
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print(("Hello, {first_name} {last_name}. You are {age}. " + 
       "You are a {profession}. You were a member of {affiliation}.") \
       .format(first_name=first_name, last_name=last_name, age=age, \
               profession=profession, affiliation=affiliation))
```

{% raw %}
<div class="output">
输出(stream):<br>
    Hello, Eric Idle. You are 74. You are a comedian. You were a member of Monty Python.
    <br />
</div>
{% endraw %}


如果你有想要传递给字典中的`.format()`的变量，那么你可以用`.format（** some_dict）`解压缩它，并通过字符串中的键引用这些值，但是必须有更好的的方法

### f-Strings：一种改进Python格式字符串的新方法

好消息是，F字符串在这里可以节省很多的时间。他们确实使格式化更容易。他们自Python 3.6开始加入标准库。您可以在PEP 498中阅读所有内容。

也称为“格式化字符串文字”，F字符串是开头有一个f的字符串文字，以及包含表达式的大括号将被其值替换。表达式在运行时进行渲染，然后使用`__format__`协议进行格式化。与往常一样，Python文档是您想要了解更多信息的最佳读物。

以下是f-strings可以让你的生活更轻松的一些方法。

#### 简单例子

语法与`str.format（）`使用的语法类似，但较少细节啰嗦。看看这是多么容易可读：


```python
name = "Eric"
age = 74
f"Hello, {name}. You are {age}."
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric. You are 74.'

</div>
{% endraw %}



使用大写字母F也是有效的：


```python
F"Hello, {name}. You are {age}."
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hello, Eric. You are 74.'

</div>
{% endraw %}



你喜欢F格式化字符串吗？我希望在本文的最后，你会回答`>>> F"{Yes！}"`。

#### 任意表达式

由于f字符串是在运行时进行渲染的，因此可以将任何有效的Python表达式放入其中。这可以让你做一些漂亮的事情。

你可以做一些非常简单的事情，就像这样：


```python
f"{2 * 37}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    '74'

</div>
{% endraw %}



你可以调用函数


```python
f"{name.lower()} is funny."
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'eric is funny.'

</div>
{% endraw %}



你甚至可以使用带有f字符串的类创建对象。想象一下你有以下类：


```python
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"
```


```python
new_comedian = Comedian("Eric", "Idle", "74")
f"{new_comedian}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Eric Idle is 74.'

</div>
{% endraw %}



`__str __（）`和`__repr __（）`方法处理对象如何呈现为字符串，因此您需要确保在类定义中包含至少一个这些方法。如果必须选择一个，请使用`__repr __（）`，因为它可以代替`__str __（）`。

`__str __（）`返回的字符串是对象的非正式字符串表示，应该可读。` __repr __（）`返回的字符串是官方表示，应该是明确的。调用`str（）`和`repr（）`比直接使用`__str __（）`和`__repr __（）`更好。

默认情况下，f字符串将使用`__str __（）`，但如果包含转换标志`!r`，则可以确保它们使用`__repr __（）`：


```python
f"{new_comedian}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Eric Idle is 74.'

</div>
{% endraw %}




```python
f"{new_comedian!r}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Eric Idle is 74. Surprise!'

</div>
{% endraw %}



#### 多行f-string

你可以有多行字符串：


```python
message = (f"Hi {name}. "
        f"You are a {profession}. "
        f"You were in {affiliation}.")
message
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hi Eric. You are a comedian. You were in Monty Python.'

</div>
{% endraw %}



但请记住，您没必要将f放在多行字符串的每一行的前面。以下代码也能work：


```python
message = (f"Hi {name}. "
        "You are a {profession}. "
        "You were in {affiliation}.")
message
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Hi Eric. You are a {profession}. You were in {affiliation}.'

</div>
{% endraw %}



但是如果你使用`"""`这将会发生什么：


```python
message = f"""
    Hi {name}. 
    You are a {profession}. 
    You were in {affiliation}.
 """

message
```




{% raw %}
<div class="output">
输出(plain):<br/>

    '\n    Hi Eric. \n    You are a comedian. \n    You were in Monty Python.\n '

</div>
{% endraw %}



#### 性能

f字符串中的f也可以代表“速度快”。

f-字符串比`％-formatting`和`str.format（）`都快。正如你已经看到的，f-字符串是运行时渲染的表达式，而不是常量值。以下是文档摘录：

> “F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python source code, an f-string is a literal string, prefixed with f, which contains expressions inside braces. The expressions are replaced with their values.” (Source)

在运行时，大括号内的表达式将在其自己的作用域中进行求值，然后将其与其余字符串组合在一起。

以下是速度比较:


```python
%%timeit
name = "Eric" 
age = 74 
'%s is %s.' % (name, age)
```

{% raw %}
<div class="output">
输出(stream):<br>
    202 ns ± 2.05 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    <br />
</div>
{% endraw %}


```python
%%timeit
name = "Eric" 
age = 74 
'{} is {}.'.format(name, age)
```

{% raw %}
<div class="output">
输出(stream):<br>
    244 ns ± 5.52 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    <br />
</div>
{% endraw %}


```python
%%timeit
name = "Eric" 
age = 74 
'{name} is {age}.'
```

{% raw %}
<div class="output">
输出(stream):<br>
    14.4 ns ± 0.0121 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)
    <br />
</div>
{% endraw %}

你可以看到, 速度最快的就是f字符串.

### Python f-Strings：Pesky细节

现在你已经知道了为什么F字符串很好，我确定你想要出去并开始使用它们。当你冒险进入这个勇敢的新世界时，请记住一些细节。

#### 引号

您可以在表达式中使用各种类型的引号。只要确保在表达式中使用的f-字符串外部没有使用相同类型的引号即可。

以下写法都是正确的:


```python
f"{'Eric Idle'}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Eric Idle'

</div>
{% endraw %}




```python
f'{"Eric Idle"}'
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Eric Idle'

</div>
{% endraw %}




```python
f"""Eric Idle"""
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Eric Idle'

</div>
{% endraw %}




```python
f'''Eric Idle'''
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Eric Idle'

</div>
{% endraw %}




```python
f"The \"comedian\" is {name}, aged {age}."
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'The "comedian" is Eric, aged 74.'

</div>
{% endraw %}



#### 字典

说到引号，注意你在使用字典的时候。如果要为字典的键使用单引号，请记住确保对包含键的f字符串使用双引号。

以下代码是有效的:


```python
comedian = {'name': 'Eric Idle', 'age': 74}
f"The comedian is {comedian['name']}, aged {comedian['age']}."
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'The comedian is Eric Idle, aged 74.'

</div>
{% endraw %}



但是，以下代码就是一个语法错误：


```python
f'The comedian is {comedian['name']}, aged {comedian['age']}.'
```


      File "<ipython-input-40-cd7d8a3db23b>", line 1
        f'The comedian is {comedian['name']}, aged {comedian['age']}.'
                                        ^
    SyntaxError: invalid syntax
    


如果您在字典键周围使用与在f字符串外部使用相同类型的引号，则第一个字典键开头的引号将被解释为字符串的结尾。

### 大括号

为了使字符串出现大括号，您必须使用双大括号：


```python
f"{{74}}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    '{74}'

</div>
{% endraw %}



但是，如果使用三个以上的大括号，则可以获得更多大括号：


```python
f"{{{{74}}}}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    '{{74}}'

</div>
{% endraw %}



#### 反斜杠

正如您之前所看到的，您可以在f字符串的字符串部分使用反斜杠转义符。但是，您不能使用反斜杠在f字符串的表达式部分中进行转义：


```python
f"{\"Eric Idle\"}"
```


      File "<ipython-input-43-35cb9fe0ccc1>", line 1
        f"{\"Eric Idle\"}"
                          ^
    SyntaxError: f-string expression part cannot include a backslash
    


#### lambda表达式

如果您需要使用lambda表达式，请记住，解析f-字符串的方式会稍微复杂一些。

如果`!, :`或`}`不在括号，大括号，括号或字符串中，则它将被解释为表达式的结尾。由于lambda使用`：`，这可能会导致一些问题：



```python
f"{lambda x: x * 37 (2)}"
```


      File "<fstring>", line 1
        (lambda x)
                 ^
    SyntaxError: unexpected EOF while parsing
    


您可以通过将您的lambda嵌套在圆括号中来解决此问题：


```python
f"{(lambda x: x * 37) (2)}"
```




{% raw %}
<div class="output">
输出(plain):<br/>

    '74'

</div>
{% endraw %}



### 结束语

您仍然可以使用格式化字符串的较旧方式，但使用F字符串时，您现在可以使用更简洁，更易读且更方便的方式，既快速又不易出错。如果您尚未进行切换，则使用Python 3.6简化您的生活是开始使用Python 3.6的重要原因。 （如果您仍在使用Python 2，请不要忘记2020年即将到来！）

根据Python的哲学，当你需要决定如何做某事时，那么“这里应该是一个 - 并且最好只有一个 - 明显的方法来做到这一点”。尽管F字符串不是唯一可能的方式为了格式化字符串，他们很有可能成为完成工作的一种明显方式。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python3 f-string格式化字符串的高级用法.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
