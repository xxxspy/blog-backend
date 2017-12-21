---
title: python3静态类型编程入门
date: 2017-12-18 08:29:10
tags: notebook
---
本文章转载自于ipython notebook.
<!-- more -->


### 变量声明

在创建变量的时候可以声明变量类型。


```python
# 可以如此声明一个变量， 但是没有赋值
foo1 : str
# 实际上foo1变量没有创建， 直接使用会导致错误
print(type(foo1))

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-37-a1d3092bf8f9> in <module>()
          2 foo1 : str
          3 # 实际上foo1变量没有创建， 直接使用会导致错误
    ----> 4 print(type(foo1))
    

    NameError: name 'foo1' is not defined



```python
# 可以在第一次赋值的时候声明变量类型
foo2 : str = 'abc'
print(type(foo2))
# 但是， python不是强制类型， 可以在运行时改变了变量类型
# 但是当你用代码编辑器的时候， 会提示你应该保持变量类型一致
foo2 = 123 # 不会报错
```

    <class 'str'>
    

### 声明函数输入输出


```python
def infos(a:int, b:str)->dict:
    return {'a':a,'b':b}

infos(123, 'abc')
```




    {'a': 123, 'b': 'abc'}



#### 写错类型， 并不报错


```python
infos('123', 123)
```




    {'a': '123', 'b': 123}



####  类方法


```python
class Foo:
    def foo1(self, a:str, b:int)->dict:
        return {'a':a, 'b':b}
    
foo2 = Foo()
foo2.foo1('abc', 1)
```




    {'a': 'abc', 'b': 1}



### 复杂数据类型

#### 字典


```python
# 错误
user_counts: dict[str, int]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-42-5c3053d8505f> in <module>()
          1 # 错误
    ----> 2 user_counts: dict[str, int]
    

    TypeError: 'type' object is not subscriptable



```python
# 正确
from typing import Dict, List
user_counts: Dict[str, int]={
    'user1':500,
    'user2':600
}
```

#### 列表


```python
from typing import List

user_counts: List[int] = [1,2,3]
```

#### 复合数据类型


```python
users :List[Dict[str, int]]=[{'a':1}, {'b':2}]
```

#### 元组


```python
from typing import Tuple
positions : List[Tuple[int]]=[(12,3),(3,4)]
type(positions)
```




    list



#### 类


```python
class A:
    def amethod(self):
        pass

aa:A=A()
# 嵌套
alist :List[A]
```


本文章转载自于ipython notebook [python3静态类型编程入门](python3静态类型编程入门.ipynb).

### 联系我们

站长QQ: 1497369272(请注明来自mlln)
记住网址: mlln.cn
加入我们的讨论QQ群:680552969(请注明来自mlln) 
