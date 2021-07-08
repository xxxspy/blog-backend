
---
title: keras教程-n-图片风格转换理论和实践
date: 2018-10-31 20:17:55
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

这必须是最酷的机器学习实现之一。如果你不知道什么是`neural style transfer`，它的大概意思就是将一个图片的内容和两个图片的风格融合构成一个新的图片。

例如, 左边的图片提供内容, 中间的图片提供风格, 最后融合成右边的图片:

<img src="images/style-trans.png" />


在本教程中，我们将学习如何使用深度学习将图片的风格进行转换。这被称为`neural style transfer`！这是Leon A. Gatys的论文“A Neural Algorithm of Artistic Style,”中概述的一种技术，这个论很好，你一定要看看它:https://arxiv.org/abs/1508.06576

Neural style transfer 是一种优化方法, 它需要三张图片, 一张是内容图片, 一张是风格图片, 第三张是生成图片(初始值使用内容图片), 通过迭代优化, 最终使得第三张图片结合了第一张图片的内容和第二张图片的风格。 

Neural style transfer的原理是定义两个距离函数，一个描述两个图像的内容有多么不同，`$L_{content}$`，一个描述两个图像之间的风格`$L_{style}$`

### 总体步骤

- 数据的准备
- 定义损失函数
- 构建模型(使用预训练权重)
- 训练模型

本篇文章主要面向使用过keras的人, 大约阅读实践50分钟。

#### 关于VGG19

如果你自己训练过类似的模型, 你就会发现, 想要得到一个良好的风格转换模型是需要很长的训练时间的, 所以我们可以使用一些预训练模型。最流行的图片分类预训练模型就是VGG, 它是由Oxford的一些人在ImageNet数据集上训练得到的。原始版的VGG使用了Caffe进行训练, 所以没法直接在Tensorflow中直接使用。不过, Keras提供了一个VGG19的类, 它可以下载官方支持的Keras权重。

### 代码实现

引入用到的库并设置图片的高和宽:


```python
import numpy as np
import tensorflow.contrib.keras.api.keras.backend as K
from scipy.misc import imsave, imresize
from scipy.optimize import fmin_l_bfgs_b
from tensorflow.contrib.keras.api.keras.applications import vgg19
from tensorflow.contrib.keras.api.keras.preprocessing.image import load_img, img_to_array
from IPython.display import Image

# 图片的高和宽
img_h = 80
img_w = 100

# 两张图片
CONTENT_IMG_PATH = './images/content.jpg'
STYLE_IMG_PATH = './images/style.jpg'

Image(filename=CONTENT_IMG_PATH, width='200', height='180')

```




![jpeg](output_9_0.jpeg)




```python
Image(filename=STYLE_IMG_PATH, width='200', height='180')
```




![jpeg](output_10_0.jpeg)



#### 准备数据


图片预处理


```python
def preprocess(img_path):
    img = load_img(img_path)
    img = img_to_array(img)
    # 图片缩放到设置的大小
    img = imresize(img, (img_h, img_w, 3))
    img = img.astype('float64')
    # 增加一个维度, 为了将三张图片在这个维度上合并
    img = np.expand_dims(img, axis=0)
    # 图片处理成vgg模型需要的
    img = vgg19.preprocess_input(img)
    return img


# 只是为了测试
print(preprocess(CONTENT_IMG_PATH).shape)
```

{% raw %}
<div class="output">
输出(stream):<br>
    (1, 80, 100, 3)
    <br />
</div>
{% endraw %}

{% raw %}
<div class="output">
输出(stream):<br>
    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\ipykernel_launcher.py:5: DeprecationWarning: `imresize` is deprecated!
    <br />`imresize` is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
    <br />Use ``skimage.transform.resize`` instead.
    <br />  """
    <br />
</div>
{% endraw %}

#### 构建输入张量并下载模型


```python

content_img = K.variable(preprocess(CONTENT_IMG_PATH))
style_img = K.variable(preprocess(STYLE_IMG_PATH))
gen_img = K.placeholder(shape=(1, img_h, img_w, 3))
# 注意: 三个图片构成一个输入张量, 而每个图像所在位置要记住
input_tensor = K.concatenate([content_img, style_img, gen_img], axis=0)

model = vgg19.VGG19(include_top=False, weights='imagenet', input_tensor=input_tensor)
print('Model loaded')

outputs_dict = dict([(layer.name, layer.output) for layer in model.layers])

```

{% raw %}
<div class="output">
输出(stream):<br>
    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\ipykernel_launcher.py:5: DeprecationWarning: `imresize` is deprecated!
    <br />`imresize` is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
    <br />Use ``skimage.transform.resize`` instead.
    <br />  """
    <br />
</div>
{% endraw %}

{% raw %}
<div class="output">
输出(stream):<br>
    Downloading data from https://github.com/fchollet/deep-learning-models/releases/download/v0.1/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5
    <br />80142336/80134624 [==============================] - 70s 1us/step
    <br />Model loaded
    <br />
</div>
{% endraw %}

我们可以大概看一下预训练的模型的基本结构:


```python
outputs_dict
```




{% raw %}
<div class="output">
输出(plain):<br/>

    {'input_1': <tf.Tensor 'concat:0' shape=(3, 80, 100, 3) dtype=float32>,
    <br /> 'block1_conv1': <tf.Tensor 'block1_conv1/Relu:0' shape=(3, 80, 100, 64) dtype=float32>,
    <br /> 'block1_conv2': <tf.Tensor 'block1_conv2/Relu:0' shape=(3, 80, 100, 64) dtype=float32>,
    <br /> 'block1_pool': <tf.Tensor 'block1_pool/MaxPool:0' shape=(3, 40, 50, 64) dtype=float32>,
    <br /> 'block2_conv1': <tf.Tensor 'block2_conv1/Relu:0' shape=(3, 40, 50, 128) dtype=float32>,
    <br /> 'block2_conv2': <tf.Tensor 'block2_conv2/Relu:0' shape=(3, 40, 50, 128) dtype=float32>,
    <br /> 'block2_pool': <tf.Tensor 'block2_pool/MaxPool:0' shape=(3, 20, 25, 128) dtype=float32>,
    <br /> 'block3_conv1': <tf.Tensor 'block3_conv1/Relu:0' shape=(3, 20, 25, 256) dtype=float32>,
    <br /> 'block3_conv2': <tf.Tensor 'block3_conv2/Relu:0' shape=(3, 20, 25, 256) dtype=float32>,
    <br /> 'block3_conv3': <tf.Tensor 'block3_conv3/Relu:0' shape=(3, 20, 25, 256) dtype=float32>,
    <br /> 'block3_conv4': <tf.Tensor 'block3_conv4/Relu:0' shape=(3, 20, 25, 256) dtype=float32>,
    <br /> 'block3_pool': <tf.Tensor 'block3_pool/MaxPool:0' shape=(3, 10, 12, 256) dtype=float32>,
    <br /> 'block4_conv1': <tf.Tensor 'block4_conv1/Relu:0' shape=(3, 10, 12, 512) dtype=float32>,
    <br /> 'block4_conv2': <tf.Tensor 'block4_conv2/Relu:0' shape=(3, 10, 12, 512) dtype=float32>,
    <br /> 'block4_conv3': <tf.Tensor 'block4_conv3/Relu:0' shape=(3, 10, 12, 512) dtype=float32>,
    <br /> 'block4_conv4': <tf.Tensor 'block4_conv4/Relu:0' shape=(3, 10, 12, 512) dtype=float32>,
    <br /> 'block4_pool': <tf.Tensor 'block4_pool/MaxPool:0' shape=(3, 5, 6, 512) dtype=float32>,
    <br /> 'block5_conv1': <tf.Tensor 'block5_conv1/Relu:0' shape=(3, 5, 6, 512) dtype=float32>,
    <br /> 'block5_conv2': <tf.Tensor 'block5_conv2/Relu:0' shape=(3, 5, 6, 512) dtype=float32>,
    <br /> 'block5_conv3': <tf.Tensor 'block5_conv3/Relu:0' shape=(3, 5, 6, 512) dtype=float32>,
    <br /> 'block5_conv4': <tf.Tensor 'block5_conv4/Relu:0' shape=(3, 5, 6, 512) dtype=float32>,
    <br /> 'block5_pool': <tf.Tensor 'block5_pool/MaxPool:0' shape=(3, 2, 3, 512) dtype=float32>}

</div>
{% endraw %}



#### 定义损失函数

损失函数是这个教程最重要的部分,它决定了你是否能理解这个风格转换模型。所以, 让我们亲手把损失函数写出来:

##### 内容损失函数

内容损失函数只是对应像素值的差值的平方和(具体内容看注释):


```python
# 内容图片和生成图片的像素点数值的差的平方和
def content_loss(content, gen):
    return K.sum(K.square(gen-content))
```


```python
# 内容损失权重
CONTENT_WEIGHT  = 0.025
# 初始损失值为0
loss = 0.
# 我们并不是选择最后一层作为输出层
# 因为我们希望提取的是一些基本特征, 比如直线/斜线等
# 而越靠后的层的特征越倾向于识别更宏观的特征, 比如眼睛
layer_features = outputs_dict['block5_conv2']
# 内容图片位于第一
content_img_features = layer_features[0, :, :, :]
# 生成的图片位于最后
gen_img_features = layer_features[2, :, :, :]
# 损失值是需要加权的
loss += CONTENT_WEIGHT * content_loss(content_img_features, gen_img_features)
```

##### 风格损失函数

风格损失函数有点复杂, 它需要用到gram矩阵, 它是衡量特征之间的相关关系, 所以风格损失函数就是为了最小化风格图片和生成图片之间的特征相关矩阵的欧式距离。

- K.batch_flatten: 将一个n阶张量转变为2阶张量，其第一维度保留不变
- K.permute_dimensions: 转置
- gram matrix: 编码了不同特征之间的相关关系


```python

def gram_matrix(x):
    assert K.ndim(x) == 3
    # 将一个3阶张量转变为2阶张量，其第一维度保留不变
    features = K.batch_flatten(K.permute_dimensions(x, (2, 0, 1)))
    gram = K.dot(features, K.transpose(features))
    return gram


def style_loss(style, gen):
    assert K.ndim(style) == 3
    assert K.ndim(gen) == 3
    S = gram_matrix(style)
    G = gram_matrix(gen)
    channels = 3
    size = img_h * img_w
    return K.sum(K.square(S - G)) / (4. * (channels ** 2) * (size ** 2))
```


```python
# 注意加权
STYLE_WEIGHT = 1
feature_layer_names = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
for name in feature_layer_names:
    layer_features = outputs_dict[name]
    style_features = layer_features[1, :, :, :]
    gen_img_features = layer_features[2, :, :, :]
    s1 = style_loss(style_features, gen_img_features)
    loss += (STYLE_WEIGHT / len(feature_layer_names)) * s1
```

##### 方差损失

还是有第三个损失函数, 是为了使生成的图片平滑, 减少噪音的产生, 具体看注释:


```python
def total_variation_loss(x):
    assert K.ndim(x) == 4
    # 纵向 相邻像素点差值的平方
    a = K.square(x[:, :img_h - 1, :img_w - 1, :] - x[:, 1:, :img_w - 1, :])
    # 横向 相邻像素点差值的平方
    b = K.square(x[:, :img_h - 1, :img_w - 1, :] - x[:, :img_h - 1, 1:, :])
    return K.sum(K.pow(a + b, 1.25))
```

所有的损失加和:


```python
TV_WEIGHT = 1
loss += TV_WEIGHT * total_variation_loss(gen_img)
```

#### 梯度和损失

梯度很容易计算。我们只是将生成的图像和损失函数传递给K.gradients（）函数即可。

我们还需要定义一个Keras函数，用于计算优化过程中的损失和梯度。



```python
grads = K.gradients(loss, gen_img)

outputs = [loss]
if isinstance(grads, (list, tuple)):
    outputs += grads
else:
    outputs.append(grads)

f_output = K.function([gen_img], outputs)


def eval_loss_and_grads(x):
    x = x.reshape((1, img_h, img_w, 3))
    outs = f_output([x])
    loss_value = outs[0]
    if len(outs[1:]) == 1:
        grad_values = outs[1].flatten().astype('float64')
    else:
        grad_values = np.array(outs[1:]).flatten().astype('float64')
    return loss_value, grad_values


class Evaluator(object):
    def __init__(self):
        self.loss_value = None
        self.grads_value = None

    def loss(self, x):
        assert self.loss_value is None
        loss_value, grad_value = eval_loss_and_grads(x)
        self.loss_value = loss_value
        self.grads_value = grad_value
        return self.loss_value

    def grads(self, x):
        assert self.loss_value is not None
        grads_values = np.copy(self.grads_value)
        self.loss_value = None
        self.grads_value = None
        return grads_values

```


```python
evaluator = Evaluator()

# Run L-BFGS optimizer
x = preprocess(CONTENT_IMG_PATH)

x, min_val, info = fmin_l_bfgs_b(evaluator.loss, x.flatten(), fprime=evaluator.grads, maxiter=100)
print('    loss: {}'.format(min_val))
# Save img
# print(x.reshape(img_h, img_w, 3))
img = x.reshape(img_h, img_w, 3)
imsave('./output/img0.jpg', img)
```

{% raw %}
<div class="output">
输出(stream):<br>
    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\ipykernel_launcher.py:5: DeprecationWarning: `imresize` is deprecated!
    <br />`imresize` is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
    <br />Use ``skimage.transform.resize`` instead.
    <br />  """
    <br />
</div>
{% endraw %}

{% raw %}
<div class="output">
输出(stream):<br>
        loss: 1516893568.0
    <br />
</div>
{% endraw %}

{% raw %}
<div class="output">
输出(stream):<br>
    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\ipykernel_launcher.py:11: DeprecationWarning: `imsave` is deprecated!
    <br />`imsave` is deprecated in SciPy 1.0.0, and will be removed in 1.2.0.
    <br />Use ``imageio.imwrite`` instead.
    <br />  # This is added back by InteractiveShellApp.init_path()
    <br />
</div>
{% endraw %}


```python

Image(filename = './output/img0.jpg')
```




![jpeg](output_34_0.jpeg)




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](keras教程-n-图片风格转换理论和实践.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
