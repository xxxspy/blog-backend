---
title: so-vits-svc最强声音克隆拟声软件使用教程
date: 2023-06-04 15:48:48
tags: [人工智能]
---

我们今天介绍一个软件是用来做声音克隆的， 比如你可以将你的声音克隆下来， 然后将一段任何其他人的录音转换成你的声音。
这个工具的全称是“SoftVC VITS Singing Voice Conversion Fork”， 简称为“so-vits-svc”。
我们今天网上看到的很多孙燕姿AI都是这种方法制作的。 我用我自己的声音制作了一段“蜜雪冰城”主题曲， 你可以听下像不像我的声音。

<!-- more -->

<iframe src="//player.bilibili.com/player.html?bvid=BV1xh4y1x759&page=1" 
    scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"
    style="width:800px;height:600px;"
> </iframe>

# 环境介绍

我这里列出我的软件安装环境， 所有安装步骤都是在该环境中适用。

- 系统： win10x64
- 硬件：显卡3090， 24G， 该软件建议现存至少4G，实际上你最少也得6G， 并且内存尽量在12G以上
- conda 22.11.1, conda的安装是你自己的事情， 我这里不

# 安装

安装这种工具都是比较麻烦的， 而使用conda是简化你的安装过程的利器。

## 创建虚拟环境

使用conda创建一个虚拟环境， 名称是so-vits-svc， 名称是你自己任意指定的， 创建虚拟环境的好处是环境之间是相互隔离的，
也就是说你这次会安装很多依赖库， 这些依赖库不会影响到你其他Python项目的环境， 很多时候python版本和依赖库版本不同，
项目之间必须隔离开。

```
conda create --name so-vits-svc
```

激活环境：

```
conda activate so-vits-svc
```
## 安装依赖

首先使用下面的命令安装cuda， 这是使用英伟达显卡必须的：

```
conda install -U torch torchaudio --index-url https://download.pytorch.org/whl/cu118
```

然后安装本软件：

```
conda install -U so-vits-svc-fork
```

以上步骤应该比较费时间， 我很顺利没有报错。

# 训练

安装好了上面的软件以后， 我们接下来就是要训练一个模型， 
本例中， 这个模型就是学习的我的声音，
这个模型可以将任意人的声音转换为我的声音。
我们需要按照下面的步骤整理数据和训练数据。

## 录音

因为我经常录课， 所以我就是把我自己的课程视频转换为音频格式， 
如果你没有现成的多媒体资源， 你可以自己录制声音，
选择你自己喜欢的录音软件， 录制至少十分钟的语音，
音质尽量要好， 录制时间越多越好， 我使用大概1小时的录音作为训练数据。

完成这个步骤， 你将得到一个名字为“recording.mp3”的文件。

## 分割

因为训练数据需要的是10秒以内的音频， 所以我们需要将上面得到的“recording.mp3”文件切割成短音频。
这里需要用到一个音频分割软件“audiosilicer”， 这个软件可以自动的将音频切分为10秒左右。

安装方法是跟上面类似：

```
conda create --name audiosilicer python=3.11 # 创建一个虚拟环境命名为audiosilicer
git clone https://github.com/henrymaas/AudioSlicer.git # 将代码下载到本地的文件夹， 这个文件夹名字是AudioSlicer
cd AudioSlicer # 设置工作目录是 AudioSlicer
pip install -r requirements.txt # 安装依赖
```

这个时候在AudioSlicer文件夹下面你可以看到有一个python文件“AudioSeg.py”， 打开这个文件， 修改你的输入文件, 例如我的输入文件是“recording.mp3”：

```python
# Change the arguments and the input file here
input_file = 'C:\\Teste\\recording.mp3'
output_dir = 'C:\\Teste\\'
```

然后你在命令行运行下面的命令：

```
conda activate audiosilicer
python AudioSeg.py
```
这样在你设置的输出文件夹'C:\\Teste\\'下就可以看到切割好的文件。

## 训练

### 目录结构

有了数据， 下面就开始训练了， 首先你要创建一个目录结构， 例如我的工作目录是`D:\dev\so-vits-svc-fork\`,
然后在这个文件夹下面创建一个原始数据的文件夹， 名字必须为"dataset_raw",
然后在"dataset_raw"中创建文件夹为“me”，这是语音的名字， 你可以任意命名， 最后能代表语音的意义。
把所有切割好的文件复制到me文件夹。

### 采样

工作目录设置为`D:\dev\so-vits-svc-fork\`， 
然后运行命令`svc pre-resample`， 这个命令生成了一个文件夹`dataset`， 里面存放了采样数据， 这是真正用于训练的数据。

### 配置文件

运行命令`svc pre-config`， 这样会生成一个配置文件， 路径是`D:\dev\so-vits-svc-fork\configs\44k\config.json`， 打开这个文件，
你需要重点关注的是`batch_size`， 因为每个人的显卡可能不同， batch size决定的是一次训练多少个样本， 如果设置的过大， 会导致显卡内存溢出，
如果设置过小， 训练时间会太长， 我设置的是32， 你根据自己的显卡大小决定这个参数。

其他配置参数我们会有单独的教程。

### 下载模型

运行命令`svc pre-hubert`， 下载模型。

### 训练

运行命令`svc train -t`，运行这个命令后就开始训练模型， 我花费了2天时间训练完成一个比较满意的效果。

# 使用

模型训练完成以后， 我们开始使用这个模型来生成自己的声音。 因为我不会唱歌， 但是大家都想听我唱歌。
所以我就用这个方法生成唱歌的声音。

## 分离人声

首先我下载了一个挖呀挖呀挖视频， 因为全网都在唱， 我想听听我唱出来是什么样子的。

然后我使用了软件Ultimate Vocal Remover软件， 它可以将音乐和唱声分开，
并且支持视频， 软件是免费的， 地址在： https://github.com/Anjok07/ultimatevocalremovergui

输入视频后， 它生成了两个音频， 一个是背景音乐， 一个是唱声，我们需要用后者， 这个文件名为`1_videoplayback (1)_(Vocals).wav`。

## 转换生成

在命令行运行命令svcg， 就会打开一个界面软件， 这是so-vits-svc-fork提供的界面。

软件会自动搜索你训练好的模型， 所以我没有设置模型的路径， 它自动找到了：

<img src="modelPath.png">

你需要设置的就是输入文件， 就是我们提取得到的人声文件`1_videoplayback (1)_(Vocals).wav`, 

<img src="inputpath.png">

然后点击“infer”按钮， 就开始生成你的声音了， 大概几秒的时间就可以得到转换好的声音。 最后我们来听听效果吧：

<iframe src="//player.bilibili.com/player.html?bvid=BV1xh4y1x759&page=1" 
    scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"
    style="width:800px;height:600px;"
> </iframe>

# 总结

这个软件生成的拟声效果是惊艳的， 很多人听了我"唱"的歌都认为很像。 
所以我们可以深挖这个软件还能做什么， 本篇教程的主要目的就是记录我的安装和使用过程， 
如果大家对这个软件很感兴趣， 我们可以出视频教程， 然后再深入探讨一下各种配置方法和使用方法。
如果你有什么问题， 请在下方留言。
