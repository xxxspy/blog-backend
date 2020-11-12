
---

title: 嵌入式python的zip安装和并安装pip
date: 2020-11-04 12:44:03
tags: [python, ]

---

- 本篇教程的演示系统是:windows10

在python支持的安装方式中, 有一种就是"embedded"安装, 或者叫嵌入式安装, 
这种安装方法是方便将python集成到其他软件中, 比如桌面软件, 但是这种安装方式不支持pip,
这是官方声称的不支持, 但是也指明了如果你非得安装pip也不是不可能。

<img src="images/embedded-installer.png">

<!--more-->

### 下载和解压zip

我们从上面的截图中可以看到zip的<a href="https://www.python.org/downloads/windows/">下载链接</a>, 
下载完成就只需要解压到你想要的位置就可以了。

### 修改路径

假如我下载的是python38, 那么找到解压得到的文件夹, 修改这个文件"python38._pth", 注意文件名中的数字就是python的版本号。

打开这个文件, 将最后一样取消注释, 下面就是取消注释以后的内容:
```py
python38.zip
.

# Uncomment to run site.main() automatically
import site

```

### 安装pip

你需要先下载脚本文件https://bootstrap.pypa.io/get-pip.py, 将这个文件保存至任何方便的位置, 然后使用你解压得到的python.exe文件执行这个脚本:

```
python.exe get-pip.py
```

执行以后, 稍等一会就会得到pip。

### 测试pip

pip安装完成以后, 你要注意pip被安装在这个位置:

```
python解压文件夹/Scripts/pip.exe
```

你需要在命令行执行下面的命令来安装文件:

```
python解压文件夹路径/Scripts/pip.exe install 库名称
```



### 修改系统环境变量

如果你不想要每次执行pip的时候都输入绝对路径, 你可以将`python解压文件夹路径/Scripts`这个路径添加到电脑的path变量中。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](嵌入式python的zip安装和并安装pip.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
