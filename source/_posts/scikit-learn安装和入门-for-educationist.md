---
title: scikit-learn安装和入门(for_educationist)
date: 2017-10-12 17:37:45
tags: [python, 机器学习]
---

本篇文章介绍了如何安装scikit-learn, 并且如何用支持向量机(SVM)识别手写字. 作为一篇scikit-learn入门文章, 并没有深入讲解什么是支持向量机(SVM), 我们的目的仅仅是感受一下什么是机器学习.

<!-- more -->

### 下载所需文件

windows环境

- python下载链接：http://pan.baidu.com/s/1i51R98h 密码：xzvi
- wheels下载链接：https://pan.baidu.com/s/1dETxbwd 密码：5jwl

> 说明：wheel是编译后的python库，为了避免你自己编译（编译时间太长还容易出错）

### 安装过程

#### - 安装python

和安装qq一样简单.

#### - 测试是否安装成功

按下快捷键`win`+`R`，打开运行窗口，输入`cmd`，按下回车，打开命令窗口。

输入python，查看输出结果：


这是正确的输出：

```cmd
E:\programs\myblog\source\_posts>python
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

这是python没有安装成功的输出：

```cmd
E:\programs\myblog\source\_posts>python
'python' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
```

#### - 可能出现的问题

1，可能是环境变量没有配置

> - 找到python安装在哪里：搜索python，然后右键点击，选择"打开文件所在的位置"

{% asset_img findpython.jpg %}

> - 复制路径

{% asset_img path.jpg %}

> - 编辑路径

{% asset_img system_path.jpg %}

> - 添加两个路径，两个路径分别是：

```
C:\Users\wangluobu\AppData\Local\Programs\Python\Python35
C:\Users\wangluobu\AppData\Local\Programs\Python\Python35\scripts
```
> 两个路径一个是python.exe的目录, 一个是scripts文件夹，这个文件夹里包含很多有用的命令
> 注意: 你的电脑肯定不是这个路径，每个人的安装路径都可能不同
{% asset_img add_path.jpg %}


### 安装依赖库

#### - 下载适合的版本

scikit-learn需要两个依赖库：numpy 和 scipy. 建议安装matplotlib用于数据可视化. 从上面的下载链接里下载. 注意自己的电脑是64bit还是32bit, 还需要知道自己的python版本号. 根据这些信息,下载不同的文件.

文件名中包含了python版本和系统位数:

{% asset_img bit_version.jpg %}

#### - pip安装

确保你已经联网, 因为安装过程需要下载一些依赖库. 打开cmd, cd到你下载的wheel文件所在文件夹, 然后分步执行以下4条命令:

```cmd
pip install numpy-1.11.3+mkl-cp35-cp35m-win_amd64.whl
pip install scipy-0.19.0-cp35-cp35m-win_amd64.whl
pip install matplotlib
pip install scikit-learn
```

#### - 测试是否安装成功

执行如下命令:

```python
import matplotlib
import scipy
from sklearn import svm
```

如果没有报错, 就是安装成功了.

### scikit-learn实现手写字识别

#### - 什么是手写数字

我们不妨看一下scikit-learn内置的手写数字数据集:

```python
from sklearn import datasets
digits = datasets.load_digits()
# 打印所有数据
digits.data
#打印第一条数据
digits.data[0]
# 它是哪个数字?
digits.target[0]
# 以图片矩阵方式显示
digits.images[0]
```

现在问题是, 怎么以图片方式显示数据?

```python
from matplotlib import pyplot as plt
plt.imshow(digits.images[0], cmap='gray')
plt.show()
```

#### - 如何预测手写数字

使用支持向量机模型进行建模, 关于什么是支持向量机, [这里](https://www.zhihu.com/question/21094489)有一个通俗的解释.

```python
from sklearn import svm
clf = svm.SVC()
```

clf就是我们建立的一个svm模型, 我们想要模型具有预测性, 必须进行训练, 训练调用的是clf的fit方法:

```python
clf.fit(digits.data[:-10], digits.target[:-10])
```

预测剩下的10个手写数字:

```python
clf.predict(digits.data[-10:])
array([5, 4, 8, 8, 4, 9, 0, 8, 9, 8])
```

再看一眼target中存放的正确答案:

```python
digits.target[-10:]
array([5, 4, 8, 8, 4, 9, 0, 8, 9, 8])
```

#### - 能不能用回归模型?

用最简单的线性回归试试:

```python
from sklearn import linear_model
reg=lr = linear_model.LinearRegression()
reg.fit(digits.data[:-10], digits.target[:-10])
# 输出LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
reg.predict(digits.data[-10:])
# 输出
#shuarray([ 7.01785182,  2.75570626,  4.04426873,  3.91523444,  4.44370151,
#        8.08125875,  0.70934708,  7.18568382,  5.84047984,  8.83303969])
digits.target[-10:]
#array([5, 4, 8, 8, 4,
# 9, 0, 8, 9, 8])
```
为什么输出结果是浮点数? 因为线性回归要求预测值Y必须是连续数据? 我们可以尝试用逻辑回归解决分类问题.

```python
lg=linear_model.LogisticRegression()
lg.fit(digits.data[:-10], digits.target[:-10])
#LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
#          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
#          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
#          verbose=0, warm_start=False)
lg.predict(digits.data[-10:])
#array([5, 4, 8, 8, 4, 9, 0, 8, 9, 8])
digits.target[-10:]
#array([5, 4, 8, 8, 4, 9, 0, 8, 9, 8])
```

### scikit-learn其他案例

{% iframe http://scikit-learn.org/stable/auto_examples/index.html %}

### 神经网络入门

{% post_link 人工神经网络入门-代码实现ORC %}

### 讨论

尝试用keras构建一个神经网络识别手写数字. 参考 {% post_link 神经网络python库keras在windows下部署过程，带下载链接 %}