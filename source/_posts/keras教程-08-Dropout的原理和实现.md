
---
title: keras教程-08-Dropout的原理和实现
date: 2018-10-16 20:17:55
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

神经网络和深度学习模型的简单而强大的正则化技术是`Dropout`。在这篇文章中，您将发现dropout正则化技术以及如何将其应用于Keras的模型中。

阅读这篇文章后你会知道：

- dropout正则化技术原理
- 如何在输入层上使用dropout。
- 如何在隐藏图层上使用dropout。
- 如何根据不同的问题情景调整dropout水平

### Dropout正则化原理

Dropout 是Srivastava等人提出的神经网络模型的正则化技术。在2014年的论文 Dropout: A Simple Way to Prevent Neural Networks from Overfitting ([下载 PDF](http://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf) )

Dropout是一种在训练过程中随机忽略神经元的技术。他们随机“Dropout”, 意味着它们对下游神经元激活的贡献在正向通过时暂时消除，并且任何权重更新都不会发生于这些神经元。

当神经网络训练时，不同神经元会根据不同特征来调整自己的参数。神经元变得依赖于这种特殊的特征, 有些特省甚至是有害的，如果学习太多这些特征可能导致模型泛化能力下降, 无法适应训练数据以外的数据。

您可以想象，如果在训练期间神经元随机掉出网络，其他神经元将不得不承担这些缺失神经元的工作, 分担缺失神经元的一部分特征表示。我们相信, 这会导致网络学习多个独立的内部表示。

其结果是网络对神经元的特定权重变得不那么敏感。这反过来导致网络能够更好地概括并且不太可能过度拟合训练数据。



### Keras中的Dropout层

每次训练时, 以一定的概率(比如20%)丢弃一些神经元很容易实现。这就是在Keras中实施Dropout的方式。 Dropout仅在模型训练期间使用，在评估模型的效果时不使用。

接下来，我们将探讨在Keras中使用Dropout的几种不同方法。

这些示例将使用Sonar数据集。这是一个二元分类问题，其目标是从声纳信息中正确识别岩石和模拟地雷。它是神经网络的一个很好的测试数据集，因为所有输入值都是数字的并且具有相同的单位。

可以从UCI机器学习库下载数据集。您可以将声纳数据集放在notebook所在目录下的data文件夹中，文件名为`sonar.csv`。

我们将使用scikit-learn中的10折交叉验证法来评估的模型，以便更好地梳理结果中的差异。

输入是60维的向量，输出是1维的。输入值在用于训练之前已标准化。基线神经网络模型具有两个隐藏层，第一层具有60个单元，第二层具有30个。使用随机梯度下降法进行模型训练, 并且设置相对较低的学习率。

下面列出了完整的基线模型。


```python
# Baseline Model on the Sonar Dataset
import numpy
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.constraints import maxnorm
from keras.optimizers import SGD
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load dataset
dataframe = read_csv("./data/sonar.csv", header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:60].astype(float)
Y = dataset[:,60]
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# baseline
def create_baseline():
    # create model
    model = Sequential()
    model.add(Dense(60, input_dim=60, kernel_initializer='normal', activation='relu'))
    model.add(Dense(30, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
    # Compile model
    sgd = SGD(lr=0.01, momentum=0.8, decay=0.0, nesterov=False)
    model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
    return model

numpy.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=create_baseline, epochs=300, batch_size=16, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, X, encoded_Y, cv=kfold)
print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
```

{% raw %}
<div class="output">
输出(stream):<br>
    Baseline: 81.66% (6.89%)
    <br />
</div>
{% endraw %}

### 在输入层使用Dropout

在下面的示例中，我们在输入层和第一个隐藏层之间添加一个新的Dropout层。dropout值设置为20％，这意味着每个更新周期中将随机排除五分之一输入。

此外，正如Dropout原始论文中所建议的那样，对每个隐藏层的权重施加约束，确保权重的最大范数不超过值3.这可以通过在Dropout层上设置kernel_constraint参数来完成。

学习率提高了一个数量级，momentum增加到0.9。原始Dropout论文中也推荐了这些学习率。

从上面的基线示例继续，下面的代码使用相同的网络, 只是在输入层添加了dropout。


```python
# dropout in the input layer with weight constraint
def create_model():
	# create model
	model = Sequential()
	model.add(Dropout(0.2, input_shape=(60,)))
	model.add(Dense(60, kernel_initializer='normal', activation='relu', kernel_constraint=maxnorm(3)))
	model.add(Dense(30, kernel_initializer='normal', activation='relu', kernel_constraint=maxnorm(3)))
	model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
	# Compile model
	sgd = SGD(lr=0.1, momentum=0.9, decay=0.0, nesterov=False)
	model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
	return model

numpy.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=create_model, epochs=300, batch_size=16, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, X, encoded_Y, cv=kfold)
print("Visible: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
```

{% raw %}
<div class="output">
输出(stream):<br>
    Visible: 85.09% (5.87%)
    <br />
</div>
{% endraw %}

### 在隐藏层使用Dropout


Dropout可以应用于网络中的隐藏层神经元。

在下面的示例中，Dropout应用于两个隐藏层之间以及最后一个隐藏层和输出层之间。再次使用20％的dropout值，以及对这些层的权重约束。


```python
# dropout in hidden layers with weight constraint
def create_model():
	# create model
	model = Sequential()
	model.add(Dense(60, input_dim=60, kernel_initializer='normal', activation='relu', kernel_constraint=maxnorm(3)))
	model.add(Dropout(0.2))
	model.add(Dense(30, kernel_initializer='normal', activation='relu', kernel_constraint=maxnorm(3)))
	model.add(Dropout(0.2))
	model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
	# Compile model
	sgd = SGD(lr=0.1, momentum=0.9, decay=0.0, nesterov=False)
	model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
	return model

numpy.random.seed(seed)
estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=create_model, epochs=300, batch_size=16, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, X, encoded_Y, cv=kfold)
print("Hidden: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
```

{% raw %}
<div class="output">
输出(stream):<br>
    Hidden: 81.68% (4.85%)
    <br />
</div>
{% endraw %}

我们可以看到，针对此问题以及所选网络配置，在隐藏层中使用Dropout不会提升性能。可能需要额外的训练或者需要进一步调整学习速率。

### 使用Dropout的一些技巧

关于Dropout的原始论文提供了一套标准机器学习问题的实验结果。因此，在实践中使用Dropout时，他们提供了许多有用的启发式。

- 通常，使用20％-50％神经元的小dropout值，20％提供良好的起点。概率太低具有最小的影响，而太高的值导致网络的学习不足。
- 使用更大的网络。当在较大的网络上使用dropout时，您可能会获得更好的性能，从而为模型提供更多学习独立表示的机会。
- 在输入层和隐藏层上使用dropout。在网络的每一层应用Dropout已经显示出良好的结果。
- 使用具有衰减和大momentum的学习率。将学习率提高10到100倍，并使用0.9或0.99的momentum值。
- 限制网络权重的大小。较大的学习速率可能导致非常大的网络权重。对网络权重的大小施加约束，例如大小为4或5的最大范数正则化已被证明可以改善结果。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](keras教程-08-Dropout的原理和实现.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
