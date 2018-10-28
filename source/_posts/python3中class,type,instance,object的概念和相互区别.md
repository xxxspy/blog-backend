
---
title: python3中class,type,instance,object的概念和相互区别
date: 2018-10-27 20:17:55
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

python中这四个概念经常让新手产生疑惑:class/type/instance/object, 如果非要把他们翻译成中文就是: 类/类型/实例/对象。但是如果交流的时候使用中文, 很容易造成概念的混乱, 因为说起"类"和"类型"的区别, 通俗的理解真的觉得没区别。所以, 我们还是说 英文吧。我的观点主要从这篇英文文章( https://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary )中提取的, 如果你英文好, 建议直接读英文文章, 忽略我这篇文章。

### class和type

这两个概念来自python2的早期版本, 内建的类通常叫做type, 而用户自定义的类, 通常叫做class(假设继承子object), 但是在python3中, 这种概念差别已经不存在, 所以在python3中type和class就是一种东西: 


```python
# 创建一个变量
astr = 'a string'
```

在python2中, 命令`print(type(astr))`输出 `<type 'str'>`, 而在python3中, 命令`print(type(astr))`输出 `<class 'str'>`。

在python2中, 只有用户自定义的类才会输出 `<class 'str'>`, 你自己可以试试。

### instance和object

类的实例就是对象, 不管在python2还是在python3中这句话都没有错, 所以实例其实就是对象的一个别称。


### class和instance/object

从类到对象的过程叫做实例化, 所以对象是实例化的产物, 


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python3中class,type,instance,object的概念和相互区别.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
