
---
title: keras教程-n-CUDA无法找到cudnn的错误解决
date: 2018-10-17 20:17:55
tags: [keras教程]
toc: true
xiongzhang: false

---
<span></span>
<!-- more -->


本文适用于如下环境:

- ubuntu16
- python3.6
- jupyter notebook
- tensorflow 1.x
- keras 2.x

作者信息:

- 邮箱: xxxspy[at]126.com
- QQ: 675495787
- 转载请注明来自 mlln.cn

今天在使用keras的时候发现一个错误, 主要的错误是`Unknown: Fail to find the dnn implementation`, 具体看traceback如下:

```cmd
 Unknown: Fail to find the dnn implementation.
Traceback (most recent call last):
  File "train.py", line 33, in <module>
    num_epochs=20)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/textgenrnn/textgenrnn.py", line 320, in train_from_file
    texts, context_labels=context_labels, **kwargs)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/textgenrnn/textgenrnn.py", line 291, in train_new_model
    **kwargs)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/textgenrnn/textgenrnn.py", line 221, in train_on_texts
    validation_steps=val_steps
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/keras/legacy/interfaces.py", line 91, in wrapper
    return func(*args, **kwargs)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/keras/engine/training.py", line 1415, in fit_generator
    initial_epoch=initial_epoch)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/keras/engine/training_generator.py", line 213, in fit_generator
    class_weight=class_weight)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/keras/engine/training.py", line 1215, in train_on_batch
    outputs = self.train_function(ins)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py", line 2666, in __call__
    return self._call(inputs)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py", line 2636, in _call
    fetched = self._callable_fn(*array_vals)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/tensorflow/python/client/session.py", line 1454, in __call__
    self._session._session, self._handle, args, status, None)
  File "/home/bnu/venvs/deeplearning3.6/lib/python3.6/site-packages/tensorflow/python/framework/errors_impl.py", line 519, in __exit__
    c_api.TF_GetCode(self.status.status))
tensorflow.python.framework.errors_impl.UnknownError: Fail to find the dnn implementation.
         [[Node: rnn_1_2/CudnnRNN = CudnnRNN[T=DT_FLOAT, _class=["loc:@training/RMSprop/gradients/rnn_1_2/CudnnRNN_grad/CudnnRNNBackprop"], direction="unidirectional", dropout=0, input_mode="linear_input", is_training=true, rnn_mode="lstm", seed=87654321, seed2=0, _device="/job:localhost/replica:0/task:0/device:GPU:0"](rnn_1_2/transpose, rnn_1_2/ExpandDims_1, rnn_1_2/ExpandDims_1, rnn_1_2/concat)]]
         [[Node: loss_2/mul/_241 = _Recv[client_terminated=false, recv_device="/job:localhost/replica:0/task:0/device:CPU:0", send_device="/job:localhost/replica:0/task:0/device:GPU:0", send_device_incarnation=1, tensor_name="edge_2251_loss_2/mul", tensor_type=DT_FLOAT, _device="/job:localhost/replica:0/task:0/device:CPU:0"]()]]
```

### 问题和解决方法

经过各种搜索以后, 我知道这是因为cuDNN安装错误或者根本没有安装导致的, 所以我们就重新安装一遍cuDNN即可, 下面就是我的解决步骤:

- 下载cudnn压缩包

为了避免你从官网下载(速度慢/还需要注册/填写问卷) ,我把要下载的cudnn放在了百度网盘:

下载链接：https://pan.baidu.com/s/1Wz9G9KtzmrBuXv0fLDo2GQ 

提取码：zvp4

- 重命名文件

主要是加上文件后缀`.tgz`, 那么现在这个文件为`cudnn-9.0-linux-x64-v7.3.1.20.solitairetheme8.tgz`

- 文件放到某个文件夹

后文用`cudnn_dir`来表示这个文件夹路径, cd到这个文件夹

- 解压:

``$tar -xzvf cudnn-9.0-linux-x64-v7.3.1.20.solitairetheme8.tgz`

你会看到在当前文件夹下多了一个文件夹`cuda`

- 复制文件到/usr/local/cuda中, 命令我都给你写好了:


```
$` sudo cp cuda/include/cudnn.h /usr/local/cuda/include
`$ sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
$`


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](keras教程-n-CUDA无法找到cudnn的错误解决.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
