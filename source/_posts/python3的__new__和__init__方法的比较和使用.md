
---
title: python3的__new__和__init__方法的比较和使用
date: 2018-11-12 18:17:55
tags: [python]
toc: true

---

这篇文章的目的是在python3环境下, 讨论`__new__`和`__init__`方法的用法。
<span></span>
<!-- more -->

### new和init的差异

`__new__`和`__init__`方法都是类的内置方法, 他们的主要区别是: `__new__`用于对象的创建, 而`__init__`用于对象的实例化, 所以你可以猜到, `__new__`在`__init__`之前被调用。 所以我们如果想要改变类的创建过程, 可以自定义`__new__`方法, 比如动态创建对象(对象的类型是可变的)。




```python
class A:
    def __init__(self, name):
        self.name = name

class B:
    def __init__(self, name):
        self.name = name

class C:
    def __init__(self, name):
        self.name = name

class ABC:
    def __new__(klass, *args, **kwargs):
        if args[0] == 'A':
            return A.__new__(A, *args, **kwargs)
        elif args[0] == 'B':
            return B.__new__(B, *args, **kwargs)
        elif args[0] == 'C':
            return C.__new__(C, *args, **kwargs)
        else:
            print('Befor new')
            ins =  super(ABC, klass).__new__(klass, **kwargs)
            print('After new')
            return ins
        
    def __init__(self, name):
        print('Hi', name)
        self.name = name
        

ABC('A')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <__main__.A at 0x22fb59938d0>

</div>
{% endraw %}




```python
ABC('B')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <__main__.B at 0x22fb59671d0>

</div>
{% endraw %}




```python
ABC('C')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <__main__.C at 0x22fb5bfcbe0>

</div>
{% endraw %}



通过上面的例子, 你可能已经发现,  `__new__`的第一个参数是类本身, 而`__init__`是实例本身。 你需要注意的是, `__new__`返回的实例不是自己的实例时, `__init__`方法不会被调用, 而如果返回的是自己的实例时, 就可以被隐性调用:


```python
ABC('ABC')
```

{% raw %}
<div class="output">
输出(stream):<br>
    Befor new
    <br />After new
    <br />Hi ABC
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    <__main__.ABC at 0x22fb5bfd780>

</div>
{% endraw %}



所以, 当返回其他类的实例时, 你需要自己调用`__init__`方法:


```python
class A:
    def __init__(self, name):
        print('I am in A')

class ABC:
    def __new__(klass, *args, **kwargs):
        if args[0] == 'A':
            ins =  A.__new__(A, *args, **kwargs)
            ins.__init__(*args, **kwargs)
            return ins
        elif args[0] == 'B':
            return B.__new__(B, *args, **kwargs)
        else:
            return C.__new__(C, *args, **kwargs)
        
    def __init__(self, *args, **kwargs):
        print('I am in ABC')
        

        
ABC('A')
```

{% raw %}
<div class="output">
输出(stream):<br>
    I am in A
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    <__main__.A at 0x22fb59677b8>

</div>
{% endraw %}



### 应用

我常常在使用单例模式的时候自定义`__new__`方法, 单例模式的意思就是类只能实例化得到一个实例, 多次实例化返回的还是同一个实例:


```python
class Singleton(object):
    _instance = None  # Keep instance reference 
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
```


```python
s1 = Singleton()
s2 = Singleton()
a1 = ABC('A')
a2 = ABC('A')
print('a1 == a2:', a1 == a2)
print('s1 == s2:', s1 == s2)
```

{% raw %}
<div class="output">
输出(stream):<br>
    I am in A
    <br />I am in A
    <br />a1 == a2: False
    <br />s1 == s2: True
    <br />
</div>
{% endraw %}

### 参考文献

- https://howto.lintel.in/python-__new__-magic-method-explained/
- https://spyhce.com/blog/understanding-new-and-init


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python3的__new__和__init__方法的比较和使用.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
