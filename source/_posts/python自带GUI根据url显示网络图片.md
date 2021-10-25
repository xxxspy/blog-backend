
---

title: python自带GUI根据url显示网络图片
date: 2019-07-13 12:44:03
tags: [python, pil, tkinter]

---

我们知道一个图片的url, 如何显示到GUI中, 下面就是来演示一下, 我们使用的是python3.6, 利用官方自带的tkinter作为GUI。 使用urlopen下载图片, 然后使用io模块存放图片数据, 最后使用PIL转换为图片, 最后将图片显示到GUI中。

<!-- more -->

下面我安装一下PIL模块:


```python
!pip install pillow
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Collecting pillow
  Downloading https://files.pythonhosted.org/packages/4e/d9/468422371e6fcf02d6a162ee30db4552221de8b2b3ff837363bf54cbb347/Pillow-6.1.0-cp36-cp36m-win_amd64.whl (2.0MB)
Installing collected packages: pillow
Successfully installed pillow-6.1.0

</div>
{% endraw %}

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
You are using pip version 19.0.3, however version 19.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

</div>
{% endraw %}

下面是代码, 里面有注释:


```python
import io
from PIL import Image, ImageTk
import tkinter as tk
from urllib.request import urlopen
root = tk.Tk()
# 随便挑了一个网页图片
url = "https://checkimage.etest.net.cn/460032A72DDE122655301C16E6225789.jpg"
# 下载图片数据
image_bytes = urlopen(url).read()
# 将数据存放到data_stream中
data_stream = io.BytesIO(image_bytes)
# 转换为图片格式
pil_image = Image.open(data_stream)
# 获取图片的宽度和高度
w, h = pil_image.size
# 获取图片的文件名
fname = url.split('/')[-1]
sf = "{} ({}x{})".format(fname, w, h)
# 设置窗口title
root.title(sf)
# 将pil格式的图片转换为tk格式的image
tk_image = ImageTk.PhotoImage(pil_image)
# 创建个label组件, root作为父节点
label = tk.Label(root, image=tk_image, bg='black')
# 设置一些padding
label.pack(padx=5, pady=5)
root.mainloop()
```


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python自带GUI根据url显示网络图片.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
