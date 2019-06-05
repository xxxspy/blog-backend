---
title: 神经网络python库keras在windows下部署过程，带下载链接
date: 2017-06-13 10:00:15
tags: [python, keras, 机器学习, 神经网络]
---

### 环境

- 64位win10
- python 3.5 64 bit

keras的官方文档说，他们只支持python2.7-python3.5。

### 下载wheels

因为numpy和scipy在windows平台上安装会出现编译问题，因为他们依赖一些c库会找不到，所以我们就安装wheel格式的库，他们是预先编译好的。

下载链接：http://pan.baidu.com/s/1dETxbwd 密码：5jwl

在这里你能看到有很多`.whl`格式的文件，如果你跟我的python版本一样，你可以下载，否则你需要下载适合你自己版本的安装文件。

{% asset_img baiduyun.jpg %}

### 安装numpy和scipy

```cmd
cd wheel文件所在的文件夹
pip install "numpy-1.11.3+mkl-cp35-cp35m-win_amd64.whl"
pip install "scipy-0.19.0-cp35-cp35m-win_amd64.whl"
```

### 安装tensorflow

tensorflow是keras的神经网络计算引擎，但是安装keras的时候，不会自动安装它，因为这是一个可选包，所以你的自己安装。

```python
pip install tensorflow
```

### 安装keras

因为在安装麻烦的库已经安装好了，现在可以安装keras了。keras还依赖一些其他的库，比如six/tensorflow/pyyaml等，不过他们可以在安装keras的时候，自动被安装，所以不需要你手动安装。

```cmd
pip install keras
```

### hello keras

打开python shell，可以在cmd中输入python来打开。


首先来构建一个网络结构

```python
from keras.models import Sequential
from keras.layers import Dense, Activation
model.add(Dense(units=25, input_dim=64))
model=Sequential()   #网络基本结构
model.add(Dense(units=25, input_dim=8*8))  #添加一个隐层，有25个节点，64个输入
model.add(Activation("sigmoid"))  #设置激活函数logistic
model.add(Dense(units=10))  #增加一个输出层
model.add(Activation('sigmoid'))  # 设置激活函数
```

准备数据，我们要得到输入和输出矩阵，输入矩阵每一行是一个64维的向量，输出矩阵每一行是一个10维矩阵

```python
data=open('orc-data.csv','r').readlines()
data=[line.strip().split(',') for line in data]
data=[list(map(row, int)) for row in data]
data=[list(map(int, row)) for row in data]
X=[row[1:] for row in data]
temp_Y=[row[0] for row in data]
Y=[]
for y in temp_Y:
	v=[0]*10
	v[y]=1
	Y.append(v)
```

现在我们得到了两个矩阵X和Y。网络结构已经建好，我们可以训练这个模型了

```python
model.compile(loss='categorical_crossentropy',
				optimizer='adam',
				metrics=['accuracy'])
model.fid(X, Y, batch_size=100, nb_epoch=20)			
```