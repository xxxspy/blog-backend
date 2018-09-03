
---
title: keras基础-Dense的输入的秩大于2时的注意事项
date: 2018-08-30 20:17:55
tags: [keras教程, keras基础]
toc: true
xiongzhang: false

---
<span></span>
<!-- more -->


本文代码运行环境:

- windows10
- python3.6
- jupyter notebook
- tensorflow 1.x
- keras 2.x

### 问题描述

keras的Dense层的输入通常是一个二维的矩阵(batch_size, n_input), 但其实, 你的输入的秩可以是大于2的, 比如下面的代码是正确的:


```python
from keras import layers

# 注意keras中, batch size是省略的
input1 = layers.Input((2,3))
dense = layers.Dense(4)
output = dense(input1)
output
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <tf.Tensor 'dense_5/add:0' shape=(?, 2, 4) dtype=float32>

</div>
{% endraw %}



而权重的形状是这样的:


```python
dense.kernel
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <tf.Variable 'dense_5/kernel:0' shape=(3, 4) dtype=float32_ref>

</div>
{% endraw %}



我们可以看到, 输出`output`的形状是`(batch_size, 2, 4)`, 为什么会是这样的? 我查阅了keras中的文档, 文档中说:`if the input to the layer has a rank greater than 2, then it is flattened prior to the initial dot product with  kernel`, 但是, 实际情况不是这样的, 如果被flatten以后, 输出应该是这样的: 


```python
input1 = layers.Input((2,3))
flat = layers.Flatten()(input1)
dense = layers.Dense(4)
output = dense(flat)
output
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <tf.Tensor 'dense_4/BiasAdd:0' shape=(?, 4) dtype=float32>

</div>
{% endraw %}



而权重的形状是这样的:


```python
dense.kernel
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <tf.Variable 'dense_4/kernel:0' shape=(6, 4) dtype=float32_ref>

</div>
{% endraw %}



### Dense的算法就是`dot`

很显然, 文档说的有问题, 代码并不是这样的运行的。所以我查阅了Keras的源码, 我发现Dense前向传播的计算方法是在这里:

```python
def call(self, inputs):
    # 理解内部发生了什么, 关键要看这一行
    output = K.dot(inputs, self.kernel)
    if self.use_bias:
        output = K.bias_add(output, self.bias, data_format='channels_last')
    if self.activation is not None:
        output = self.activation(output)
    return output
```

所以, 我们要看一下keras中`dot`的行为:


```python
from keras import backend as K

x = K.placeholder(shape=(2, 2, 3))
y = K.placeholder(shape=(3, 4))
xy = K.dot(x, y)
xy
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <tf.Tensor 'Reshape_8:0' shape=(2, 2, 4) dtype=float32>

</div>
{% endraw %}




```python
import tensorflow as tf

sess = tf.InteractiveSession()
```


```python
import numpy as np
np.random.seed(123)
x_data = np.random.randint(1,10, (2,2,3))
y_data = np.random.randint(1,5, (3,4))
xy_data = xy.eval(feed_dict={x:x_data, y:y_data})
print('x:', x_data)
print('y:', y_data)
print('xy:', xy_data)
```

{% raw %}
<div class="output">
输出(stream):<br>
    x: [[[3 3 7]
    <br />  [2 4 7]]
    <br />
    <br /> [[2 1 2]
    <br />  [1 1 4]]]
    <br />y: [[3 2 1 1]
    <br /> [1 1 2 4]
    <br /> [4 3 1 4]]
    <br />xy: [[[40. 30. 16. 43.]
    <br />  [38. 29. 17. 46.]]
    <br />
    <br /> [[15. 11.  6. 14.]
    <br />  [20. 15.  7. 21.]]]
    <br />
</div>
{% endraw %}

这个结果和我们直接用`np.dot`的方法结果是一样的。


```python
np.dot(x_data, y_data)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([[[40, 30, 16, 43],
    <br />        [38, 29, 17, 46]],
    <br />
    <br />       [[15, 11,  6, 14],
    <br />        [20, 15,  7, 21]]])

</div>
{% endraw %}




```python
np.dot(x_data, y_data[:, 1])
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([[30, 29],
    <br />       [11, 15]])

</div>
{% endraw %}



### 总结

其实两个tensor之间的点乘大家应该懂了, keras官方文档有问题导致对它的理解又产生了疑惑。如果三维的tensor不容易理解的话, 可以去掉batch_size这个维度来看:


```python

x=np.random.randint(1,5,(2, 3))
y=np.random.randint(1,5,(3, 3))
print('正常情况下, x只是个向量:')
np.dot(x[0,:],y)
```

{% raw %}
<div class="output">
输出(stream):<br>
    正常情况下, x只是个向量:
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    array([28, 26, 16])

</div>
{% endraw %}




```python
print('特殊情况下, x只是个矩阵:')
np.dot(x,y)
```

{% raw %}
<div class="output">
输出(stream):<br>
    特殊情况下, x只是个矩阵:
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    array([[28, 26, 16],
    <br />       [40, 36, 23]])

</div>
{% endraw %}



一句话总结的话, Dense的输入为一个矩阵的时候, 相当于它的每一个行向量分别进入Dense层进行计算, 然后把计算得到的向量拼接成矩阵。有问题来我网站提问:mlln.cn , 转载请注明出处。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](keras基础-Dense的输入的秩大于2时的注意事项.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
