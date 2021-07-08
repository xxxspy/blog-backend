
---
title: keras教程-06-优化器详细解释
date: 2018-09-01 20:17:55
tags: [keras教程]
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

### 综述

优化器的选择在深度学习中是非常重要的, 所以我们在这里汇总了keras里内建的优化器(optimizer), 以便于我们在接下来的学习中能更清楚的知道如何选择优化器。下面我们依然按照本系列教程的思路, 先通过实验来得到一个感官认识,然后再从理论上分析一下。 下面是我们列出来的需要讨论的优化器:

- SGD 随机梯度下降优化器。
- RMSprop Geoff Hinton提出的一种自适应学习率方法
- Adagrad 自适应子梯度方法 在线学习和随机优化
- Adadelta 一种自适应学习率方法
- Adam 一种基于一阶梯度的随机目标函数优化算法，基于低阶矩的自适应估计
- Adamax
- Nadam
- TFOptimizer

下面代码来自上一篇文章: {% post_link keras教程-05-实验验证神经网络的深度-样本量-dropout %}

我们采用上一篇文章的代码是为了快速测试不同的优化器。


```python
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (7,7) # Make the figures a bit bigger

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

def prepare_data(n=6000, test_n=3000):
    '''准备用到的数据'''
    nb_classes = 10
    # 这个方法可以加载数据
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    X_train = X_train.reshape(60000, 784)
    X_train = X_train[:n, :]
    y_train = y_train[:n]
    X_test = X_test.reshape(10000, 784)
    X_test = X_test[:test_n, :]
    y_test = y_test[:test_n]
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255
    Y_train = np_utils.to_categorical(y_train, nb_classes)
    Y_test = np_utils.to_categorical(y_test, nb_classes)
    return (X_train, Y_train), (X_test, Y_test)

def net_work(n_layer, has_dropout=False):
    model = Sequential()
    assert n_layer >= 1
    for i in range(n_layer):
        if i == 0:
            model.add(Dense(512, input_shape=(784,)))
        else:
            model.add(Dense(512))
        model.add(Activation('relu'))
        if has_dropout:
            model.add(Dropout(0.2))
    # 输出层
    model.add(Dense(10))
    # 分类任务的输出通常是softmax, 这保证的所有的输出值都在0-1之间, 并且他们之和为1
    model.add(Activation('softmax')) 
    return model


### 请注意, 这里我们可以传入一个参数: optimizer
def train(model, train_data, test_data, optimizer):
    X_train, y_train = train_data
    X_test, y_test = test_data
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model.fit(X_train, y_train,
          batch_size=128, epochs=20,
          validation_data=(X_test, y_test))
```


```python
# prepare_data的第一个参数就是训练样本的样本量
train_data, test_data = prepare_data(8192)
results = {}

# 循环模型的层数
for opt in ('sgd', 'RMSprop', 'Adagrad', 'Adadelta', 'Adam', 'Adamax', 'Nadam'):
    print(f'Using optimizer: {opt} ###################')
    model = net_work(2, True)
    results[opt] = train(model, train_data, test_data, opt)
```

{% raw %}
<div class="output">
输出(stream):<br>
    Using optimizer: sgd ###################
    <br />Train on 8192 samples, validate on 3000 samples
    <br />Epoch 1/20
    <br />8192/8192 [==============================] - 2s 250us/step - loss: 2.1350 - acc: 0.3016 - val_loss: 1.9318 - val_acc: 0.5853
    <br />Epoch 2/20
    <br />8192/8192 [==============================] - 1s 87us/step - loss: 1.7166 - acc: 0.6145 - val_loss: 1.5469 - val_acc: 0.6953
    <br />Epoch 3/20
    <br />8192/8192 [==============================] - 1s 84us/step - loss: 1.3232 - acc: 0.7262 - val_loss: 1.2065 - val_acc: 0.7550
    <br />Epoch 4/20
    <br />8192/8192 [==============================] - 1s 84us/step - loss: 1.0413 - acc: 0.7731 - val_loss: 0.9750 - val_acc: 0.7820
    <br />Epoch 5/20
    <br />8192/8192 [==============================] - 1s 85us/step - loss: 0.8575 - acc: 0.7970 - val_loss: 0.8295 - val_acc: 0.8100
    <br />Epoch 6/20
    <br />8192/8192 [==============================] - 1s 80us/step - loss: 0.7362 - acc: 0.8186 - val_loss: 0.7329 - val_acc: 0.8237
    <br />Epoch 7/20
    <br />8192/8192 [==============================] - 1s 78us/step - loss: 0.6552 - acc: 0.8319 - val_loss: 0.6673 - val_acc: 0.8367
    <br />Epoch 8/20
    <br />8192/8192 [==============================] - 1s 82us/step - loss: 0.5992 - acc: 0.8429 - val_loss: 0.6215 - val_acc: 0.8430
    <br />Epoch 9/20
    <br />8192/8192 [==============================] - 1s 78us/step - loss: 0.5504 - acc: 0.8551 - val_loss: 0.5887 - val_acc: 0.8473
    <br />Epoch 10/20
    <br />8192/8192 [==============================] - 1s 76us/step - loss: 0.5239 - acc: 0.8593 - val_loss: 0.5586 - val_acc: 0.8507
    <br />Epoch 11/20
    <br />8192/8192 [==============================] - 1s 84us/step - loss: 0.4954 - acc: 0.8612 - val_loss: 0.5362 - val_acc: 0.8560
    <br />Epoch 12/20
    <br />8192/8192 [==============================] - 1s 87us/step - loss: 0.4763 - acc: 0.8683 - val_loss: 0.5163 - val_acc: 0.8613
    <br />Epoch 13/20
    <br />8192/8192 [==============================] - 1s 94us/step - loss: 0.4546 - acc: 0.8716 - val_loss: 0.5021 - val_acc: 0.8657
    <br />Epoch 14/20
    <br />8192/8192 [==============================] - 1s 86us/step - loss: 0.4390 - acc: 0.8744 - val_loss: 0.4924 - val_acc: 0.8627
    <br />Epoch 15/20
    <br />8192/8192 [==============================] - 1s 81us/step - loss: 0.4267 - acc: 0.8807 - val_loss: 0.4778 - val_acc: 0.8687
    <br />Epoch 16/20
    <br />8192/8192 [==============================] - 1s 78us/step - loss: 0.4101 - acc: 0.8864 - val_loss: 0.4676 - val_acc: 0.8707
    <br />Epoch 17/20
    <br />8192/8192 [==============================] - 1s 77us/step - loss: 0.3957 - acc: 0.8872 - val_loss: 0.4580 - val_acc: 0.8733
    <br />Epoch 18/20
    <br />8192/8192 [==============================] - 1s 78us/step - loss: 0.3893 - acc: 0.8907 - val_loss: 0.4505 - val_acc: 0.8750
    <br />Epoch 19/20
    <br />8192/8192 [==============================] - 1s 80us/step - loss: 0.3780 - acc: 0.8955 - val_loss: 0.4436 - val_acc: 0.8743
    <br />Epoch 20/20
    <br />8192/8192 [==============================] - 1s 77us/step - loss: 0.3711 - acc: 0.8951 - val_loss: 0.4363 - val_acc: 0.8733
    <br />Using optimizer: RMSprop ###################
    <br />Train on 8192 samples, validate on 3000 samples
    <br />Epoch 1/20
    <br />8192/8192 [==============================] - 2s 220us/step - loss: 0.5748 - acc: 0.8170 - val_loss: 0.3857 - val_acc: 0.8853
    <br />Epoch 2/20
    <br />8192/8192 [==============================] - 1s 103us/step - loss: 0.2433 - acc: 0.9253 - val_loss: 0.2770 - val_acc: 0.9147
    <br />Epoch 3/20
    <br />8192/8192 [==============================] - 1s 101us/step - loss: 0.1605 - acc: 0.9495 - val_loss: 0.2239 - val_acc: 0.9287
    <br />Epoch 4/20
    <br />8192/8192 [==============================] - 1s 98us/step - loss: 0.1105 - acc: 0.9662 - val_loss: 0.2401 - val_acc: 0.9270
    <br />Epoch 5/20
    <br />8192/8192 [==============================] - 1s 98us/step - loss: 0.0835 - acc: 0.9724 - val_loss: 0.2014 - val_acc: 0.9420
    <br />Epoch 6/20
    <br />8192/8192 [==============================] - 1s 117us/step - loss: 0.0662 - acc: 0.9778 - val_loss: 0.2599 - val_acc: 0.9270
    <br />Epoch 7/20
    <br />8192/8192 [==============================] - 1s 114us/step - loss: 0.0446 - acc: 0.9861 - val_loss: 0.2026 - val_acc: 0.9427
    <br />Epoch 8/20
    <br />8192/8192 [==============================] - 1s 104us/step - loss: 0.0436 - acc: 0.9857 - val_loss: 0.2130 - val_acc: 0.9387
    <br />Epoch 9/20
    <br />8192/8192 [==============================] - 1s 99us/step - loss: 0.0271 - acc: 0.9924 - val_loss: 0.2399 - val_acc: 0.9460
    <br />Epoch 10/20
    <br />8192/8192 [==============================] - 1s 97us/step - loss: 0.0234 - acc: 0.9910 - val_loss: 0.2250 - val_acc: 0.9513
    <br />Epoch 11/20
    <br />8192/8192 [==============================] - 1s 97us/step - loss: 0.0202 - acc: 0.9929 - val_loss: 0.2413 - val_acc: 0.9437
    <br />Epoch 12/20
    <br />8192/8192 [==============================] - 1s 99us/step - loss: 0.0223 - acc: 0.9935 - val_loss: 0.2705 - val_acc: 0.9413
    <br />Epoch 13/20
    <br />8192/8192 [==============================] - 1s 99us/step - loss: 0.0128 - acc: 0.9968 - val_loss: 0.2596 - val_acc: 0.9460
    <br />Epoch 14/20
    <br />8192/8192 [==============================] - 1s 98us/step - loss: 0.0111 - acc: 0.9972 - val_loss: 0.2772 - val_acc: 0.9497
    <br />Epoch 15/20
    <br />8192/8192 [==============================] - 1s 97us/step - loss: 0.0125 - acc: 0.9957 - val_loss: 0.3191 - val_acc: 0.9433
    <br />Epoch 16/20
    <br />8192/8192 [==============================] - 1s 105us/step - loss: 0.0111 - acc: 0.9962 - val_loss: 0.2761 - val_acc: 0.9483
    <br />Epoch 17/20
    <br />8192/8192 [==============================] - 1s 98us/step - loss: 0.0096 - acc: 0.9965 - val_loss: 0.2942 - val_acc: 0.9497
    <br />Epoch 18/20
    <br />8192/8192 [==============================] - 1s 102us/step - loss: 0.0081 - acc: 0.9969 - val_loss: 0.4533 - val_acc: 0.9243
    <br />Epoch 19/20
    <br />8192/8192 [==============================] - 1s 128us/step - loss: 0.0074 - acc: 0.9977 - val_loss: 0.3173 - val_acc: 0.9457
    <br />Epoch 20/20
    <br />8192/8192 [==============================] - 1s 117us/step - loss: 0.0099 - acc: 0.9968 - val_loss: 0.3319 - val_acc: 0.9487
    <br />Using optimizer: Adagrad ###################
    <br />Train on 8192 samples, validate on 3000 samples
    <br />Epoch 1/20
    <br />8192/8192 [==============================] - 2s 221us/step - loss: 0.7796 - acc: 0.8015 - val_loss: 0.3912 - val_acc: 0.8817
    <br />Epoch 2/20
    <br />8192/8192 [==============================] - 1s 93us/step - loss: 0.2133 - acc: 0.9359 - val_loss: 0.2538 - val_acc: 0.9207
    <br />Epoch 3/20
    <br />8192/8192 [==============================] - 1s 95us/step - loss: 0.1438 - acc: 0.9561 - val_loss: 0.2272 - val_acc: 0.9323
    <br />Epoch 4/20
    <br />8192/8192 [==============================] - 1s 93us/step - loss: 0.1087 - acc: 0.9708 - val_loss: 0.2148 - val_acc: 0.9343
    <br />Epoch 5/20
    <br />8192/8192 [==============================] - 1s 93us/step - loss: 0.0855 - acc: 0.9747 - val_loss: 0.2020 - val_acc: 0.9380
    <br />Epoch 6/20
    <br />8192/8192 [==============================] - 1s 92us/step - loss: 0.0644 - acc: 0.9823 - val_loss: 0.1935 - val_acc: 0.9403
    <br />Epoch 7/20
    <br />8192/8192 [==============================] - 1s 92us/step - loss: 0.0527 - acc: 0.9851 - val_loss: 0.1961 - val_acc: 0.9417
    <br />Epoch 8/20
    <br />8192/8192 [==============================] - 1s 100us/step - loss: 0.0477 - acc: 0.9873 - val_loss: 0.1881 - val_acc: 0.9387
    <br />Epoch 9/20
    <br />8192/8192 [==============================] - 1s 105us/step - loss: 0.0366 - acc: 0.9902 - val_loss: 0.1911 - val_acc: 0.9433
    <br />Epoch 10/20
    <br />8192/8192 [==============================] - 1s 106us/step - loss: 0.0292 - acc: 0.9924 - val_loss: 0.1843 - val_acc: 0.9447
    <br />Epoch 11/20
    <br />8192/8192 [==============================] - 1s 106us/step - loss: 0.0279 - acc: 0.9935 - val_loss: 0.1832 - val_acc: 0.9447
    <br />Epoch 12/20
    <br />8192/8192 [==============================] - 1s 95us/step - loss: 0.0255 - acc: 0.9943 - val_loss: 0.1800 - val_acc: 0.9483
    <br />Epoch 13/20
    <br />8192/8192 [==============================] - 1s 95us/step - loss: 0.0195 - acc: 0.9955 - val_loss: 0.1860 - val_acc: 0.9447
    <br />Epoch 14/20
    <br />8192/8192 [==============================] - 1s 92us/step - loss: 0.0189 - acc: 0.9960 - val_loss: 0.1905 - val_acc: 0.9477
    <br />Epoch 15/20
    <br />8192/8192 [==============================] - 1s 93us/step - loss: 0.0148 - acc: 0.9968 - val_loss: 0.1934 - val_acc: 0.9457
    <br />Epoch 16/20
    <br />8192/8192 [==============================] - 1s 94us/step - loss: 0.0117 - acc: 0.9984 - val_loss: 0.1954 - val_acc: 0.9470
    <br />Epoch 17/20
    <br />8192/8192 [==============================] - 1s 91us/step - loss: 0.0108 - acc: 0.9987 - val_loss: 0.1952 - val_acc: 0.9460
    <br />Epoch 18/20
    <br />8192/8192 [==============================] - 1s 92us/step - loss: 0.0109 - acc: 0.9977 - val_loss: 0.1902 - val_acc: 0.9493
    <br />Epoch 19/20
    <br />8192/8192 [==============================] - 1s 91us/step - loss: 0.0105 - acc: 0.9978 - val_loss: 0.1944 - val_acc: 0.9470
    <br />Epoch 20/20
    <br />8192/8192 [==============================] - 1s 101us/step - loss: 0.0100 - acc: 0.9987 - val_loss: 0.1940 - val_acc: 0.9490
    <br />Using optimizer: Adadelta ###################
    <br />Train on 8192 samples, validate on 3000 samples
    <br />Epoch 1/20
    <br />8192/8192 [==============================] - 2s 267us/step - loss: 0.7134 - acc: 0.7839 - val_loss: 0.4253 - val_acc: 0.8730
    <br />Epoch 2/20
    <br />8192/8192 [==============================] - 1s 118us/step - loss: 0.2871 - acc: 0.9155 - val_loss: 0.3048 - val_acc: 0.9073
    <br />Epoch 3/20
    <br />8192/8192 [==============================] - 1s 117us/step - loss: 0.2041 - acc: 0.9398 - val_loss: 0.2832 - val_acc: 0.9107
    <br />Epoch 4/20
    <br />8192/8192 [==============================] - 1s 118us/step - loss: 0.1563 - acc: 0.9541 - val_loss: 0.2416 - val_acc: 0.9197
    <br />Epoch 5/20
    <br />8192/8192 [==============================] - 1s 117us/step - loss: 0.1196 - acc: 0.9634 - val_loss: 0.2177 - val_acc: 0.9327
    <br />Epoch 6/20
    <br />8192/8192 [==============================] - 1s 117us/step - loss: 0.0946 - acc: 0.9730 - val_loss: 0.2279 - val_acc: 0.9267
    <br />Epoch 7/20
    <br />8192/8192 [==============================] - 1s 128us/step - loss: 0.0770 - acc: 0.9772 - val_loss: 0.2009 - val_acc: 0.9360
    <br />Epoch 8/20
    <br />8192/8192 [==============================] - 1s 134us/step - loss: 0.0608 - acc: 0.9836 - val_loss: 0.2020 - val_acc: 0.9390
    <br />Epoch 9/20
    <br />8192/8192 [==============================] - 1s 136us/step - loss: 0.0485 - acc: 0.9860 - val_loss: 0.2073 - val_acc: 0.9377
    <br />Epoch 10/20
    <br />8192/8192 [==============================] - 1s 128us/step - loss: 0.0382 - acc: 0.9901 - val_loss: 0.2089 - val_acc: 0.9397
    <br />Epoch 11/20
    <br />8192/8192 [==============================] - 1s 124us/step - loss: 0.0323 - acc: 0.9907 - val_loss: 0.2021 - val_acc: 0.9413
    <br />Epoch 12/20
    <br />8192/8192 [==============================] - 1s 121us/step - loss: 0.0310 - acc: 0.9907 - val_loss: 0.2065 - val_acc: 0.9400
    <br />Epoch 13/20
    <br />8192/8192 [==============================] - 1s 122us/step - loss: 0.0209 - acc: 0.9957 - val_loss: 0.2226 - val_acc: 0.9403
    <br />Epoch 14/20
    <br />8192/8192 [==============================] - 1s 122us/step - loss: 0.0180 - acc: 0.9957 - val_loss: 0.2035 - val_acc: 0.9433
    <br />Epoch 15/20
    <br />8192/8192 [==============================] - 1s 125us/step - loss: 0.0139 - acc: 0.9973 - val_loss: 0.2287 - val_acc: 0.9397
    <br />Epoch 16/20
    <br />8192/8192 [==============================] - 1s 145us/step - loss: 0.0121 - acc: 0.9973 - val_loss: 0.2183 - val_acc: 0.9437
    <br />Epoch 17/20
    <br />8192/8192 [==============================] - 1s 144us/step - loss: 0.0115 - acc: 0.9972 - val_loss: 0.2069 - val_acc: 0.9507
    <br />Epoch 18/20
    <br />8192/8192 [==============================] - 1s 127us/step - loss: 0.0088 - acc: 0.9982 - val_loss: 0.2085 - val_acc: 0.9500
    <br />Epoch 19/20
    <br />8192/8192 [==============================] - 1s 123us/step - loss: 0.0075 - acc: 0.9987 - val_loss: 0.2298 - val_acc: 0.9393
    <br />Epoch 20/20
    <br />8192/8192 [==============================] - 1s 119us/step - loss: 0.0063 - acc: 0.9994 - val_loss: 0.2150 - val_acc: 0.9473
    <br />Using optimizer: Adam ###################
    <br />Train on 8192 samples, validate on 3000 samples
    <br />Epoch 1/20
    <br />8192/8192 [==============================] - 2s 248us/step - loss: 0.6292 - acc: 0.8148 - val_loss: 0.3604 - val_acc: 0.8940
    <br />Epoch 2/20
    <br />8192/8192 [==============================] - 1s 113us/step - loss: 0.2254 - acc: 0.9346 - val_loss: 0.2854 - val_acc: 0.9150
    <br />Epoch 3/20
    <br />8192/8192 [==============================] - 1s 122us/step - loss: 0.1522 - acc: 0.9558 - val_loss: 0.2545 - val_acc: 0.9217
    <br />Epoch 4/20
    <br />8192/8192 [==============================] - 1s 128us/step - loss: 0.1113 - acc: 0.9678 - val_loss: 0.2486 - val_acc: 0.9237
    <br />Epoch 5/20
    <br />8192/8192 [==============================] - 1s 131us/step - loss: 0.0802 - acc: 0.9750 - val_loss: 0.2071 - val_acc: 0.9347
    <br />Epoch 6/20
    <br />8192/8192 [==============================] - 1s 116us/step - loss: 0.0610 - acc: 0.9825 - val_loss: 0.2356 - val_acc: 0.9353
    <br />Epoch 7/20
    <br />8192/8192 [==============================] - 1s 113us/step - loss: 0.0453 - acc: 0.9856 - val_loss: 0.1896 - val_acc: 0.9470
    <br />Epoch 8/20
    <br />8192/8192 [==============================] - 1s 113us/step - loss: 0.0322 - acc: 0.9910 - val_loss: 0.2194 - val_acc: 0.9347
    <br />Epoch 9/20
    <br />8192/8192 [==============================] - 1s 111us/step - loss: 0.0252 - acc: 0.9927 - val_loss: 0.1920 - val_acc: 0.9473
    <br />Epoch 10/20
    <br />8192/8192 [==============================] - 1s 113us/step - loss: 0.0172 - acc: 0.9960 - val_loss: 0.2107 - val_acc: 0.9467
    <br />Epoch 11/20
    <br />8192/8192 [==============================] - 1s 115us/step - loss: 0.0147 - acc: 0.9974 - val_loss: 0.2266 - val_acc: 0.9423
    <br />Epoch 12/20
    <br />8192/8192 [==============================] - 1s 120us/step - loss: 0.0178 - acc: 0.9944 - val_loss: 0.2208 - val_acc: 0.9403
    <br />Epoch 13/20
    <br />8192/8192 [==============================] - 1s 129us/step - loss: 0.0173 - acc: 0.9943 - val_loss: 0.2088 - val_acc: 0.9467
    <br />Epoch 14/20
    <br />8192/8192 [==============================] - 1s 132us/step - loss: 0.0146 - acc: 0.9962 - val_loss: 0.2348 - val_acc: 0.9430
    <br />Epoch 15/20
    <br />8192/8192 [==============================] - 1s 118us/step - loss: 0.0106 - acc: 0.9976 - val_loss: 0.2158 - val_acc: 0.9483
    <br />Epoch 16/20
    <br />8192/8192 [==============================] - 1s 115us/step - loss: 0.0082 - acc: 0.9974 - val_loss: 0.2274 - val_acc: 0.9490
    <br />Epoch 17/20
    <br />8192/8192 [==============================] - 1s 112us/step - loss: 0.0087 - acc: 0.9976 - val_loss: 0.2463 - val_acc: 0.9450
    <br />Epoch 18/20
    <br />8192/8192 [==============================] - 1s 113us/step - loss: 0.0085 - acc: 0.9973 - val_loss: 0.2588 - val_acc: 0.9443
    <br />Epoch 19/20
    <br />8192/8192 [==============================] - 1s 123us/step - loss: 0.0109 - acc: 0.9963 - val_loss: 0.2517 - val_acc: 0.9440
    <br />Epoch 20/20
    <br />8192/8192 [==============================] - 1s 113us/step - loss: 0.0116 - acc: 0.9952 - val_loss: 0.3055 - val_acc: 0.9343
    <br />Using optimizer: Adamax ###################
    <br />Train on 8192 samples, validate on 3000 samples
    <br />Epoch 1/20
    <br />8192/8192 [==============================] - 2s 286us/step - loss: 0.5693 - acc: 0.8280 - val_loss: 0.3915 - val_acc: 0.8837
    <br />Epoch 2/20
    <br />8192/8192 [==============================] - 1s 126us/step - loss: 0.2448 - acc: 0.9305 - val_loss: 0.3368 - val_acc: 0.8947
    <br />Epoch 3/20
    <br />8192/8192 [==============================] - 1s 119us/step - loss: 0.1795 - acc: 0.9462 - val_loss: 0.2626 - val_acc: 0.9177
    <br />Epoch 4/20
    <br />8192/8192 [==============================] - 1s 113us/step - loss: 0.1344 - acc: 0.9637 - val_loss: 0.2368 - val_acc: 0.9253
    <br />Epoch 5/20
    <br />8192/8192 [==============================] - 1s 109us/step - loss: 0.1119 - acc: 0.9681 - val_loss: 0.2327 - val_acc: 0.9273
    <br />Epoch 6/20
    <br />8192/8192 [==============================] - 1s 116us/step - loss: 0.0861 - acc: 0.9760 - val_loss: 0.2047 - val_acc: 0.9357
    <br />Epoch 7/20
    <br />8192/8192 [==============================] - 1s 107us/step - loss: 0.0683 - acc: 0.9819 - val_loss: 0.2027 - val_acc: 0.9343
    <br />Epoch 8/20
    <br />8192/8192 [==============================] - 1s 105us/step - loss: 0.0621 - acc: 0.9829 - val_loss: 0.1958 - val_acc: 0.9407
    <br />Epoch 9/20
    <br />8192/8192 [==============================] - 1s 110us/step - loss: 0.0491 - acc: 0.9868 - val_loss: 0.2046 - val_acc: 0.9367
    <br />Epoch 10/20
    <br />8192/8192 [==============================] - 1s 129us/step - loss: 0.0391 - acc: 0.9902 - val_loss: 0.1949 - val_acc: 0.9423
    <br />Epoch 11/20
    <br />8192/8192 [==============================] - 1s 126us/step - loss: 0.0309 - acc: 0.9928 - val_loss: 0.1956 - val_acc: 0.9410
    <br />Epoch 12/20
    <br />8192/8192 [==============================] - 1s 110us/step - loss: 0.0274 - acc: 0.9945 - val_loss: 0.1978 - val_acc: 0.9450
    <br />Epoch 13/20
    <br />8192/8192 [==============================] - 1s 106us/step - loss: 0.0254 - acc: 0.9930 - val_loss: 0.1957 - val_acc: 0.9430
    <br />Epoch 14/20
    <br />8192/8192 [==============================] - 1s 109us/step - loss: 0.0204 - acc: 0.9956 - val_loss: 0.1951 - val_acc: 0.9440
    <br />Epoch 15/20
    <br />8192/8192 [==============================] - 1s 105us/step - loss: 0.0180 - acc: 0.9951 - val_loss: 0.1989 - val_acc: 0.9457
    <br />Epoch 16/20
    <br />8192/8192 [==============================] - 1s 103us/step - loss: 0.0142 - acc: 0.9977 - val_loss: 0.1996 - val_acc: 0.9473
    <br />Epoch 17/20
    <br />8192/8192 [==============================] - 1s 104us/step - loss: 0.0127 - acc: 0.9973 - val_loss: 0.1998 - val_acc: 0.9503
    <br />Epoch 18/20
    <br />8192/8192 [==============================] - 1s 105us/step - loss: 0.0096 - acc: 0.9982 - val_loss: 0.2095 - val_acc: 0.9473
    <br />Epoch 19/20
    <br />8192/8192 [==============================] - 1s 106us/step - loss: 0.0100 - acc: 0.9972 - val_loss: 0.2099 - val_acc: 0.9460
    <br />Epoch 20/20
    <br />8192/8192 [==============================] - 1s 121us/step - loss: 0.0073 - acc: 0.9988 - val_loss: 0.2129 - val_acc: 0.9470
    <br />Using optimizer: Nadam ###################
    <br />Train on 8192 samples, validate on 3000 samples
    <br />Epoch 1/20
    <br />8192/8192 [==============================] - 2s 269us/step - loss: 0.5246 - acc: 0.8372 - val_loss: 0.3264 - val_acc: 0.8970
    <br />Epoch 2/20
    <br />8192/8192 [==============================] - 1s 117us/step - loss: 0.1910 - acc: 0.9441 - val_loss: 0.2329 - val_acc: 0.9310
    <br />Epoch 3/20
    <br />8192/8192 [==============================] - 1s 117us/step - loss: 0.1147 - acc: 0.9646 - val_loss: 0.2304 - val_acc: 0.9300
    <br />Epoch 4/20
    <br />8192/8192 [==============================] - 1s 118us/step - loss: 0.0795 - acc: 0.9762 - val_loss: 0.2485 - val_acc: 0.9273
    <br />Epoch 5/20
    <br />8192/8192 [==============================] - 1s 119us/step - loss: 0.0624 - acc: 0.9801 - val_loss: 0.2540 - val_acc: 0.9263
    <br />Epoch 6/20
    <br />8192/8192 [==============================] - 1s 120us/step - loss: 0.0437 - acc: 0.9869 - val_loss: 0.2317 - val_acc: 0.9387
    <br />Epoch 7/20
    <br />8192/8192 [==============================] - 1s 122us/step - loss: 0.0270 - acc: 0.9926 - val_loss: 0.2116 - val_acc: 0.9433
    <br />Epoch 8/20
    <br />8192/8192 [==============================] - 1s 152us/step - loss: 0.0257 - acc: 0.9918 - val_loss: 0.2554 - val_acc: 0.9413
    <br />Epoch 9/20
    <br />8192/8192 [==============================] - 1s 135us/step - loss: 0.0285 - acc: 0.9908 - val_loss: 0.2315 - val_acc: 0.9447
    <br />Epoch 10/20
    <br />8192/8192 [==============================] - 1s 119us/step - loss: 0.0218 - acc: 0.9932 - val_loss: 0.2988 - val_acc: 0.9233
    <br />Epoch 11/20
    <br />8192/8192 [==============================] - 1s 118us/step - loss: 0.0283 - acc: 0.9901 - val_loss: 0.2554 - val_acc: 0.9420
    <br />Epoch 12/20
    <br />8192/8192 [==============================] - 1s 119us/step - loss: 0.0254 - acc: 0.9919 - val_loss: 0.2562 - val_acc: 0.9440
    <br />Epoch 13/20
    <br />8192/8192 [==============================] - 1s 122us/step - loss: 0.0173 - acc: 0.9941 - val_loss: 0.2665 - val_acc: 0.9410
    <br />Epoch 14/20
    <br />8192/8192 [==============================] - 1s 118us/step - loss: 0.0159 - acc: 0.9954 - val_loss: 0.2869 - val_acc: 0.9417
    <br />Epoch 15/20
    <br />8192/8192 [==============================] - 1s 120us/step - loss: 0.0321 - acc: 0.9899 - val_loss: 0.3693 - val_acc: 0.9290
    <br />Epoch 16/20
    <br />8192/8192 [==============================] - 1s 124us/step - loss: 0.0285 - acc: 0.9911 - val_loss: 0.2545 - val_acc: 0.9463
    <br />Epoch 17/20
    <br />8192/8192 [==============================] - 1s 139us/step - loss: 0.0189 - acc: 0.9932 - val_loss: 0.2909 - val_acc: 0.9420
    <br />Epoch 18/20
    <br />8192/8192 [==============================] - 1s 136us/step - loss: 0.0250 - acc: 0.9933 - val_loss: 0.3189 - val_acc: 0.9357
    <br />Epoch 19/20
    <br />8192/8192 [==============================] - 1s 123us/step - loss: 0.0193 - acc: 0.9928 - val_loss: 0.2861 - val_acc: 0.9443
    <br />Epoch 20/20
    <br />8192/8192 [==============================] - 1s 125us/step - loss: 0.0197 - acc: 0.9945 - val_loss: 0.3062 - val_acc: 0.9423
    <br />
</div>
{% endraw %}


```python
%matplotlib inline

plt.figure(figsize=(8,12))

i = 0
for metric in ('loss', 'val_loss'):
    i += 1
    plt.subplot(2, 1, i )
    for opt in results:
        r = results[opt]
        data = r.history[metric]
        plt.plot(range(1, len(data)+1), data,  label=opt)
        plt.title(metric)
        plt.legend()
```


![png](output_4_0.png)



> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](keras教程-06-优化器详细解释.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
