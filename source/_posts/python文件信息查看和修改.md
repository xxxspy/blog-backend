
---

title: python文件信息查看和修改
date: 2019-06-25 12:44:03
tags: [python, os]

---

这篇文章主要介绍文件信息的获取和修改(主要是文件的访问和修改时间)

<!--more-->

### 文件信息的读取

文件系统本身可以显示有关文档的一些有趣信息。例如，它可以告诉你文档文件的大小，以及创建/修改或上次读取的时间。在某些平台上，你还可以找出拥有相关文件的人员。要在Python中获取此信息，您可以在跨平台的os模块中使用stat函数：


```python
import os

st = os.stat("d:/test.html")
print('Type of st:', type(st))
print('st:', st)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Type of st: <class 'os.stat_result'>
st: os.stat_result(st_mode=33206, st_ino=10133099161596645, st_dev=3649960629, st_nlink=1, st_uid=0, st_gid=0, st_size=9649, st_atime=1561387614, st_mtime=1561387614, st_ctime=1552207589)

</div>
{% endraw %}

如果你懂点英文可能已经看出来我们可以获取的信息: 

- mod: 此文件的访问权限
- ino/dev: ino（I节点）和dev（设备）成员可用于确定文件的物理位置。在UNIX系统上，（dev，ino）可以唯一标识物理文件。在Windows系统上，设备编号对应于驱动器号
- nlink: 在UNIX系统上，这是此文件的硬链接数。在Windows下，此成员始终为1。
- uid,gid: 在UNIX系统上，这些可用于确定给定文件的所有者。在Windows下，这些都为0。
- size: 文件的大小，以字节为单位。
- atime, mtime, ctime: 上次访问文件，上次修改文件以及上次更改文件信息的时间。时间以秒为单位，因为参考时间（“epoch”，通常是1970年）与time.time（）一起返回当前时间。在Windows下，上次访问的时间通常无效。

下面是一个例子, 用来打印文件的大小和修改时间:


```python
st = os.stat('d:/test.html')
print('size:', st.st_size)
print('修改时间:', st.st_mtime)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
size: 9649
修改时间: 1561387614.9498422

</div>
{% endraw %}
如果你想要看到人类能读懂的时间, 可以使用time模块进行转换:

```python
import time

time.asctime(time.localtime(st.st_mtime))
```




{% raw %}
<div class="output">
输出(plain):<br/>

    'Mon Jun 24 22:46:54 2019'

</div>
{% endraw %}



os模块还提供了一个fstat函数，可以在打开的文件中使用。它需要一个整数文件句柄，而不是文件对象，因此您必须在文件对象上使用fileno方法以便获取文件句柄：


```python
f = open('d:/test.html', 'r')
st = os.fstat(f.fileno())
print(st)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
os.stat_result(st_mode=33206, st_ino=10133099161596645, st_dev=3649960629, st_nlink=1, st_uid=0, st_gid=0, st_size=9613, st_atime=1561427779, st_mtime=1561427779, st_ctime=1552207589)

</div>
{% endraw %}

### 修改"文件的修改时间"

语法是: `os.utime(path, time)`

- path -- 文件路径

- times -- 如果时间是 None, 则文件的访问和修改设为当前时间 。 否则, 时间是一个 2-tuple数字, (atime, mtime) 用来分别作为访问和修改的时间。 注意atime和mtime都是参考1970年的时间戳。

我们用下面的小例子来说明:


```python
now = time.time()
print('当前的时间:', now)
# 文件真实的访问和修改时间
st = os.stat('d:/test.html')
print('文件的真实修改时间:', st.st_mtime)
# 修改文件修改时间
os.utime('d:/test.html', (now, now-100))
st = os.stat('d:/test.html')
print('文件的修改时间变成:', st.st_mtime)

```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
当前的时间: 1561428715.2898495
文件的真实修改时间: 1561428043.960675
文件的修改时间变成: 1561428615.2898495

</div>
{% endraw %}


```python

```


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python文件信息查看和修改.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
