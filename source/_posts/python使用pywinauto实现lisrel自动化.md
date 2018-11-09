
---
title: python使用pywinauto实现lisrel自动化
date: 2018-11-07 20:17:55
tags: [pywinauto, lisrel]
toc: true
xiongzhang: true

---
<span></span>
<!-- more -->


本文代码运行环境:

- windows10
- python3.6
- jupyter notebook

### 简介

这篇教程旨在分享一种桌面软件自动化的方法, 使用的工具就是python第三方库pywinauto。我们今天主要就是使用这个工具, 然后理解这个工具的工作流, 最后实现一个小应用:自动化spss数据转lisrel数据。

我做这篇教程的初衷是我本身经常替人做数据分析, 比如SPSS/AMOS/LISREL/MPLUS/EViews/Stata都是我的常用工具, 而Lisrel是我用过的最难用的工具, 如果不是必要, 我一定不会选择Lisrel做结构方程的! 但是, 实际又有很多现实要求, 所以我下决心做一个Lisrel自动化工具, 使用python封装Lisrel的所有功能。不过本教程不是实现所有的功能, 而仅仅是一个将spss数据转换为lisrel数据的功能。

但是, Lisrel并没有提供自动化的接口, 它只是提供了一个运行syntax的命令, 其他工作仍然无法实现。我最后决定使用pywinauto, 它是一个跨平台的自动化测试工具, 可以根据窗口和控件的名称来选择窗口和控件, 使用起来简单, 而学习成本不高。

#### 教程依赖

你需要自己独立安装好pywinauto和lisrel软件。

### 代码讲解

#### 启动Lisrel

你需要使用下面的代码来启动一个lisrel软件:


```python
from pywinauto.application import Application
# lisrel安装路径
app_exe = r'C:\Program Files\LISREL880_Trial15\LisWin32.exe'
# 启动lisrel
app = Application(backend="uia").start(app_exe)
```

如果你的lisrel已经启动,  你可以使用已经打开的应用, 只需要创建一个连接:


```python
app = Application(backend="uia").connect(title='LISREL for Windows')
```

如果你需要关闭这个应用, 可以使用`kill`方法:


```python
app.kill()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    True

</div>
{% endraw %}



#### 获取主窗口并点击菜单

`LISREL for Windows`是窗口的名称。下面的代码运行以后, 你就可以看到打开了一个对话框, 这个对话框就是用于将外部数据引入到lisrel的。


```python
win = app['LISREL for Windows']
```


```python
win.menu_select('File->Import Data')
```

#### 设置输入的spss数据

我们需要在当前的对话框中设置输入文件的类型为`SPSS Data File(*.sav)`, 输入文件的路径是`D:\jobs\data-analysis\记忆经验问卷修订\记忆经验MEQ_212_212.sav`。


```python
from pywinauto.controls.win32_controls import ComboBoxWrapper, ButtonWrapper
#  点击菜单
win.menu_select('File->Import Data')
# 设置文件类型
ComboBoxWrapper(win.Dialog.ComboBox2).select('SPSS Data File(*.sav)')
# 设置spss文件路径
app.Dialog['文件名(N):Edit'].set_text(r'D:\jobs\data-analysis\记忆经验问卷修订\记忆经验MEQ_212_212.sav')

# 点击[打开]按钮
app.Dialog['打开(O)Button'].click()

```




{% raw %}
<div class="output">
输出(plain):<br/>

    True

</div>
{% endraw %}



#### 设置lisrel数据保存位置


```python
# 等待`保存为`对话框出现
app['保存为Dialog'].wait('visible')
# 设置文件保存的路径
app['保存为Dialog']['文件名(N):Edit'].set_text(r'd:\jobs\data-analysis\data.psf')
# 点击`保存`按钮
app['保存为Dialog']['保存(S)Button'].click()

```

#### 退出lisrel




```python
app.kill()
```


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python使用pywinauto实现lisrel自动化.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
