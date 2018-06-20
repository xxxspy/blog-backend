
---
title: tensorflow教程01-神经网络模型通俗理解和简单案例
date: 2018-06-20 20:17:55
tags: [tensorflow教程, python, 深度学习]
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
- tensorflow 1.x

### 什么是人工神经网络

首先必须澄清, 人工神经网络和生物神经网络没有必然关系, 只是人类为了通俗理解而作的一个比喻. 这不是我的观点, 是吴恩达在他的深度学习课程中多次重申的.

人工神经网络(后文简称神经网络)由很多神经元相互链接构成一个网络, 而所谓的链接其实就是计算路径, 所以, 神经网络可以看成是一个计算图, 神经元就是一个计算, 链接神经元的边就是数据流通的路径. 下图是一个经典的神经网络. 圆圈代表神经元, 边代表计算路径.

<img src="images/nn.png" />

通常我们把一个神经网络分为三层: 输入层, 隐藏层和输出层. 输入层其实就是你的输入的数据, 比如, 我们现在有个向量`X=[1,2,3]`, X的每个元素可以当作输入层神经元的激活值, 比如第一个神经元的激活值是1, 第二个神经元的激活值是2. 

得到了输入层的激活值, 我们接着计算隐藏层的激活值, 如果你懂得点线性代数, 你可以用矩阵的运算得到隐层的激活向量`$A_1$`:

`$$
A_1 = sigmoid(W_1  X)
$$`

`$W_1$`代表的是输入层和隐藏层之间每个神经元两两连接的线的权重, `$A_1$`表示图中的`$[a_4, a_5, a_6, a_7]$`, `$sigmoid$`表示激活函数, 它就是一个函数, 如果不知道可以先不理会. 从上图中, 你可以看出, `$W_1$`的形状是 4x3, 因为隐层是4个神经元, 输入层是3个神经元. 如果你没有学过线性代数, 那么你学习机器学习还是很有难度的, 但是没关系, 我这里列出计算隐层第一个神经元激活量`$a_4$`的公式:

`$$
a_4 = sigmoid(x_1 * a_{41} + x_2 * a_{42} + a_{43})
$$`

这个公式里都是实数运算, 不涉及任何的矩阵运算. 到此, 我们就得到了隐藏层的激活量. 然后才能计算输出层的激活量, 算法和之前是一样的.

`$$
\hat Y = sigmoid(W_2 A_1)
$$`

### 神经网络如何进行学习

神经网络中可变的量就是上面提到的权重`$W_1$`和`$W_2$`, 后面我们统称为`$W$`, 当然不同的神经网络架构还会有不同的参数, 但是为了简便起见, 我们暂时只使用权重. 有过小学经验的你应该可以知道, 通过改变`$W$`的值就能改变输出层的激活量Y. 神经网络科学家的任务就是通过让机器学习已经准备好的训练数据, 找到最佳的W值, 让神经网络的计算结果`$\hat Y$`尽量接近训练数据`$Y$`. 

所以所谓的学习, 就指的是调整W的数值, 以便降低`$\hat Y$`

### 世界上最简单的一个神经网络

下面我们就用代码来实现一个简单的神经网络, 它只有两层(输入和输出), 一个神经元.

<img src="images/single-nn.png" />

引入用到的库


```python
import tensorflow as tf
sess = tf.InteractiveSession()
```


```python
# 输入值, 只是一个实数
input_value = tf.constant(0.5, name="input_value")

# 权重, 它时一个可变量, 用Variable
weight = tf.Variable(1.0,name="weight") 

# 期望的输出值, 也就是正确答案
expected_output = tf.constant(0.0,name="expected_output")

# 计算输出值, 其实就是简单的相乘, 
output = input_value * weight

```

计算损失值, 也就是衡量模型好坏的指标, 其实就是`$Y$`和`$\hat Y$`


```python
loss = (expected_output - output) ** 2
```

设置优化方法, 我们就用最普通的梯度下降法即可, 目标是让loss最小化, loss越小表示神经网络的计算所得与期望所得越接近.


```python
optimizer = tf.train.GradientDescentOptimizer(0.025).minimize(loss)

```

训练模型, 让权重weight调整大小, 以便于让输出值output接近0, 总共学习100次:


```python
sess.run(tf.global_variables_initializer())
for i in range(200):
    if i % 10 ==0:
        print('step: ', i)
        print('output: ', output.eval())
        print('loss:', loss.eval())
    sess.run(optimizer)

print('最后的预测值:', output.eval())
print('最后的loss:', loss.eval())
```

{% raw %}
<div class="output">
输出:
    step:  0
    output:  0.5
    loss: 0.25
    step:  10
    output:  0.44090095
    loss: 0.19439365
    step:  20
    output:  0.3887873
    loss: 0.15115556
    step:  30
    output:  0.3428334
    loss: 0.11753474
    step:  40
    output:  0.30231112
    loss: 0.09139202
    step:  50
    output:  0.26657856
    loss: 0.07106413
    step:  60
    output:  0.23506948
    loss: 0.055257663
    step:  70
    output:  0.20728472
    loss: 0.042966954
    step:  80
    output:  0.18278405
    loss: 0.03341001
    step:  90
    output:  0.16117933
    loss: 0.025978778
    step:  100
    output:  0.14212826
    loss: 0.020200443
    step:  110
    output:  0.12532897
    loss: 0.015707351
    step:  120
    output:  0.11051533
    loss: 0.012213639
    step:  130
    output:  0.09745263
    loss: 0.009497016
    step:  140
    output:  0.08593392
    loss: 0.0073846392
    step:  150
    output:  0.0757767
    loss: 0.005742109
    step:  160
    output:  0.06682004
    loss: 0.004464918
    step:  170
    output:  0.058922045
    loss: 0.0034718073
    step:  180
    output:  0.05195757
    loss: 0.0026995891
    step:  190
    output:  0.045816287
    loss: 0.0020991322
    最后的预测值: 0.04040089
    最后的loss: 0.0016322319
    
</div>
{% endraw %}

### 总结

通过上面的例子你应该可以知道机器学习的本质--调整权重(参数)以便于让输出结果靠近我们的期望结果. 而且你也看到了, 机器是能够调整参数的.


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](tensorflow教程01-神经网络模型通俗理解和简单案例.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
