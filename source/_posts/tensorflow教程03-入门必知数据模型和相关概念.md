
---
title: tensorflow教程03-入门必知数据模型和相关概念
date: 2018-07-02 20:17:55
tags: [tensorflow教程, 深度学习]
toc: true
xiongzhang: true
mathjax: true

---
<span></span>
<!-- more -->

> 声明: 本文由[DataScience](http://mlln.cn)原创发表, 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.

本文代码运行环境:

- windows10
- python3.6
- jupyter notebook
- tensorflow 1.x

在入门任何一门语言的时候我们都会首先介绍这个语言使用的数据模型, 数据模型相当于一门语言的基石, 所有的功能都是在对数据模型进行操作。TensorFlow中的数据模型由张量表示, 也就是tensor, 而名字"tensorflow"意义就是张量在图中的流动。为了避免复杂的数学定义，我们可以说一个张量（在TensorFlow中）标识了一个多维数值数组。该数据结构由三个参数 - 秩，形状和类型表征。下面我们一一介绍这三个概念, 并使用代码让你对这三个概念有一个感性认识。

### 什么是张量的秩(Rank)

每个张量由称为秩的维度单位描述。它标识张量的维数，因此，秩是已知的 - 作为张量的阶或维度。秩为零的张量是标量，秩为一的张量是向量，而秩为二的张量是矩阵。下面的代码定义了一个TensorFlow标量，一个向量，一个矩阵和一个三维张量(下面我们使用tf.constant创建一个张量, 但这并不表示张量只能由constant创建)：


```python
import tensorflow as tf
# 你可以用constant创建一个张量
scalar = tf.constant(100)
# 向量
vector = tf.constant([1,2,3,4,5])
# 矩阵
matrix = tf.constant([[1,2,3], [4,5,6]])
# 立方
cube_matrix = tf.constant([[[1],[2],[3]],[[4],[5],[6]],[[7],[8],[9]]])
print('标量:', scalar.get_shape())

```

{% raw %}
<div class="output">
输出:
    标量: ()
    
</div>
{% endraw %}


```python
print('向量:', vector.get_shape())

```

{% raw %}
<div class="output">
输出:
    向量: (5,)
    
</div>
{% endraw %}


```python
print('矩阵:', matrix.get_shape())

```

{% raw %}
<div class="output">
输出:
    矩阵: (2, 3)
    
</div>
{% endraw %}


```python
print('立方体:', cube_matrix.get_shape())
```

{% raw %}
<div class="output">
输出:
    立方体: (3, 3, 1)
    
</div>
{% endraw %}

### 什么是张量的形状(Shape)

张量的形状是它所具有的行数和列数。现在我们看一下张量形状与张量秩的关系：

- 张量的形状用`TensorShape`类来定义, 它可以被看做一个list或者tuple, 形状内的每个元素表示每个维度上的长度。比如向量的形状:


```python
vector.get_shape()
```




{% raw %}
<div class="output">
输出:
    TensorShape([Dimension(5)])
</div>
{% endraw %}



矩阵的形状:


```python
matrix.get_shape()
```




{% raw %}
<div class="output">
输出:
    TensorShape([Dimension(2), Dimension(3)])
</div>
{% endraw %}



### tensorfloa常见哪些数据类型(Data types)



```python
print('32位浮点数:',tf.float32)
print('64位浮点数:',tf.float64)
print('8位整数:',tf.int8)
print('16位整数:',tf.int16)
print('32位整数:',tf.int32)
print('64位整数:',tf.int64)
print('8位无符号整数:',tf.uint8)
print('字符串:',tf.string)
print('布尔值:',tf.bool)
print('64位复数:',tf.complex64)
print('128位复数:',tf.complex128)
```

{% raw %}
<div class="output">
输出:
    32位浮点数: <dtype: 'float32'>
    64位浮点数: <dtype: 'float64'>
    8位整数: <dtype: 'int8'>
    16位整数: <dtype: 'int16'>
    32位整数: <dtype: 'int32'>
    64位整数: <dtype: 'int64'>
    8位无符号整数: <dtype: 'uint8'>
    字符串: <dtype: 'string'>
    布尔值: <dtype: 'bool'>
    64位复数: <dtype: 'complex64'>
    128位复数: <dtype: 'complex128'>
    
</div>
{% endraw %}

请注意，TensorFlow的这些API用于管理张量与NumPy数组之间的转换。要建立一个具有常数值的张量，将一个NumPy数组传递给tf.constant（）运算符，结果将是一个具有该值的TensorFlow张量, 并且数据类型保持一致：


```python
import numpy as np
arr = np.array([1,2,3,4,5,6])
vec = tf.constant(arr)
print('arr数据类型:', arr.dtype, '       vec数据类型:', vec.dtype)
```

{% raw %}
<div class="output">
输出:
    arr数据类型: int32        vec数据类型: <dtype: 'int32'>
    
</div>
{% endraw %}

### 什么是变量(Variable)

变量通常代表可更新的参数, 是TensorFlow中的对象。变量必须被初始化;你也可以保存并恢复它来分析你的代码。变量由tf.Variable（）语句创建。在下面的例子中，我们学习率逐渐降低的过程：


```python
learning_rate = tf.Variable(0.5, name='Learning-Rate', dtype=tf.float32)
step = tf.constant(-0.1, name='Step', dtype=tf.float32)
update = tf.add(learning_rate, step)
update = tf.assign(learning_rate, update,  'Update-LR')
# 因为图中有变量, 所以需要初始化
initialize_var = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(initialize_var)
    for _ in range(5):
        sess.run(update)
        print(sess.run(learning_rate))
```

{% raw %}
<div class="output">
输出:
    0.4
    0.3
    0.20000002
    0.10000002
    1.4901161e-08
    
</div>
{% endraw %}

### 怎样获取计算图中张量的值

获取节点张量的输出，通过调用会话对象的run（）函数来执行计算图，并传入要检索的张量。除了取单个张量节点外，还可以取多个张量。

在交互式环境中, 我们通常使用`InteractiveSession`, 关于这个类的说明引用官方说法:

> 使用InteractiveSession一个主要的变化是：运行在没有指定会话对象的情况下运行变量。这是与Session（）最大的不同。


```python
sess = tf.InteractiveSession()
```

{% raw %}
<div class="output">
输出:
    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\tensorflow\python\client\session.py:1711: UserWarning: An interactive session is already active. This can cause out-of-memory errors in some cases. You must explicitly call `InteractiveSession.close()` to release resources held by the other session(s).
      warnings.warn('An interactive session is already active. This can '
    
</div>
{% endraw %}


```python
learning_rate = tf.Variable(0.5, name='Learning-Rate', dtype=tf.float32)
step = tf.constant(-0.1, name='Step', dtype=tf.float32)
update = tf.add(learning_rate, step)
update = tf.assign(learning_rate, update, name= 'Update-LR')
# 因为图中有变量, 所以需要初始化
initialize_var = tf.global_variables_initializer()
sess.run(initialize_var)
for _ in range(5):
    update.eval()
    print(learning_rate.eval())
```

{% raw %}
<div class="output">
输出:
    0.4
    0.3
    0.20000002
    0.10000002
    1.4901161e-08
    
</div>
{% endraw %}

### Feeds

Feed机制(我不知道怎么翻译)功能就是用于向计算图中提供数据。它用张量值暂时替换计算图中的`tf.placeholder`所代表的张量。 


```python
data = [1,2,3,4,5]
x = tf.placeholder(tf.float32, shape=())
y = tf.square(x)
for d in data:
    print(y.eval(feed_dict={x: d}))
```

{% raw %}
<div class="output">
输出:
    1.0
    4.0
    9.0
    16.0
    25.0
    
</div>
{% endraw %}


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](tensorflow教程03-入门必知数据模型和相关概念.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
