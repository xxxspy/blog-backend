
---
title: keras教程-03-深度学习基础和keras入门
date: 2018-07-17 20:17:55
tags: [keras教程]
toc: true
xiongzhang: true
mathjax: true

---
<span></span>
<!-- more -->

> 声明: 本文由[DataScience](http://mlln.cn)编辑发表, 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.

本文代码运行环境:

- windows10
- python3.6
- jupyter notebook
- tensorflow 1.x
- keras 2.x

#### 感知器

<img src="images/perception-map.png" />

<center>图1 感知器模型</center>



感知器是一种简单的算法，输入是一个向量`$x$`, 向量`$x$`由`$m$`个数构成`$(x_1，x_2，...，x_n)$`，通常称为输入特征或简单特征，输出是1或0。在数学上，我们定义感知器为：

第一部计算输入值, `$z和b$`都是一个实数, `$wx$`代表点积`$\sum_{j=1}w_j x_j $`

#### 激活函数平滑化

<img src="images/sigmoid-tanh.png" />
<center>图3 sigmoid和tanh激活函数</center>

##### sigmoid函数

它能够把输入的连续实值“压缩”到0和1之间。 
特别的，如果是非常大的负数，那么输出就是0；如果是非常大的正数，输出就是1. 
sigmoid 函数曾经被使用的很多，不过近年来，用它的人越来越少了。主要是因为它的一些 缺点：

- Sigmoids saturate and kill gradients. sigmoid 有一个非常致命的缺点，当输入非常大或者非常小的时候（saturation），这些神经元的梯度是接近于0的，从图中可以看出梯度的趋势。所以，你需要尤其注意参数的初始值来尽量避免saturation的情况。如果你的初始值很大的话，大部分神经元可能都会处在saturation的状态而把gradient kill掉，这会导致网络变的很难学习。

- Sigmoid 的 output 不是0均值. 这是不可取的，因为这会导致后一层的神经元将得到上一层输出的非0均值的信号作为输入。 产生的一个结果就是：如果数据进入神经元的时候是正的(e.g. x>0 elementwise in f=wTx+b)，那么 w 计算出的梯度也会始终都是正的。 当然了，如果你是按batch去训练，那么那个batch可能得到不同的信号，所以这个问题还是可以缓解一下的。因此，非0均值这个问题虽然会产生一些不好的影响，不过跟上面提到的 kill gradients 问题相比还是要好很多的。


##### tanh函数

tanh 是上图中的右图，可以看出，tanh 跟sigmoid还是很像的，实际上，tanh 是sigmoid的变形。tanh优于sigmoid的地方在于它的输出是均值为0的。

##### relu函数

<img src="images/relu.png" />

relu函数近年来越来越火, 它的函数形式如下:

`$$
f(x) = max(0, x)
$$`

#### 使用keras实现简单感知机

假设一个神经元有三个输入值`$(x_1, x_2, x_3)$`


```python
from keras.models import Sequential
from keras.layers import Dense, Activation
model = Sequential()
# 只有一个神经元, 三个输入数值
model.add(Dense(1, input_dim=3, kernel_initializer='random_normal', name="Dense"))
# 激活函数使用sigmoid
model.add( Activation('sigmoid', name="Activation"))
```

可视化model:


```python
from keras.utils import plot_model
plot_model(model, to_file='images/simple-perception.png')
```

<img src="images/simple-perception.png" />

### Keras实战

使用keras实现如下网络结构, 并训练模型:

<img src="images/nn.png" />

使用场景:

输入值`$(x_1, x_2, x_3)$`代表人的身高体重和年龄, 输出值`$(y_1, y_2)$`


```python
import numpy as np
# 总人数是1000, 一半是男生
n = 1000
# 所有的身体指标数据都是标准化数据, 平均值0, 标准差1
tizhong = np.random.normal(size = n) 
shengao = np.random.normal(size=n)
nianling = np.random.normal(size=n)
# 性别数据, 前500名学生是男生, 用数字1表示
gender = np.zeros(n)
gender[:500] = 1
# 男生的体重比较重,所以让男生的体重+1
tizhong[:500] += 1

# 男生的身高比较高, 所以让男生的升高 + 1
shengao[:500] += 1

# 男生的年龄偏小, 所以让男生年龄降低 1
nianling[:500] -= 1
```

#### 创建模型


```python
model = Sequential()
# 只有一个神经元, 三个输入数值
model.add(Dense(4, input_dim=3, kernel_initializer='random_normal', name="Dense1"))
# 激活函数使用softmax
model.add( Activation('relu', name="hidden"))
# 添加输出层
model.add(Dense(2, input_dim=4, kernel_initializer='random_normal', name="Dense2"))
# 激活函数使用softmax
model.add( Activation('softmax', name="output"))
```

#### 编译模型

需要指定优化器和损失函数:


```python
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

#### 训练模型


```python
# 转换成one-hot格式
from keras import utils
gender_one_hot = utils.to_categorical(gender, num_classes=2)
# 身体指标都放入一个矩阵data 
data = np.array([tizhong, shengao, nianling]).T
# 训练模型
model.fit(data, gender_one_hot, epochs=10, batch_size=8)
```

{% raw %}
<div class="output">
输出(stream):<br>
    Epoch 1/10<br />1000/1000 [==============================] - 0s 235us/step - loss: 0.6743 - acc: 0.7180<br />Epoch 2/10<br />1000/1000 [==============================] - 0s 86us/step - loss: 0.6162 - acc: 0.7310<br />Epoch 3/10<br />1000/1000 [==============================] - 0s 88us/step - loss: 0.5592 - acc: 0.7570<br />Epoch 4/10<br />1000/1000 [==============================] - 0s 87us/step - loss: 0.5162 - acc: 0.7680<br />Epoch 5/10<br />1000/1000 [==============================] - 0s 89us/step - loss: 0.4867 - acc: 0.7770<br />Epoch 6/10<br />1000/1000 [==============================] - 0s 88us/step - loss: 0.4663 - acc: 0.7830<br />Epoch 7/10<br />1000/1000 [==============================] - 0s 87us/step - loss: 0.4539 - acc: 0.7890<br />Epoch 8/10<br />1000/1000 [==============================] - 0s 86us/step - loss: 0.4469 - acc: 0.7920<br />Epoch 9/10<br />1000/1000 [==============================] - 0s 88us/step - loss: 0.4431 - acc: 0.7940<br />Epoch 10/10<br />1000/1000 [==============================] - 0s 88us/step - loss: 0.4407 - acc: 0.7900<br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    <keras.callbacks.History at 0x2022ef0e2b0>

</div>
{% endraw %}



#### 进行预测


```python
test_data = np.array([[0, 0, 0]])
probability = model.predict(test_data)
if probability[0, 0]>0.5:
    print('女生')
else:
    print('男生')
```

{% raw %}
<div class="output">
输出(stream):<br>
    女生<br />
</div>
{% endraw %}

#### 关键词解释

- input_dim: 输入的维度数
- kernel_initializer: 数值初始化方法, 通常是正太分布
- batch_size: 一次训练中, 样本数据被分割成多个小份, 每一小份包含的样本数叫做batch_size
- epochs: 如果说将所有数据训练一次叫做一轮的话。epochs决定了总共进行几轮训练。
- optimizer: 优化器, 可以理解为求梯度的方法
- loss: 损失函数, 可以理解为用于衡量估计值和观察值之间的差距, 差距越小, loss越小
- metrics: 类似loss, 只是metrics不参与梯度计算, 只是一个衡量算法准确性的指标, 分类模型就用accuracy


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](keras教程-03-深度学习基础和keras入门.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
