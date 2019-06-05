---
title: '炫技:用numpy和matplotlib绘制卡通人物'
date: 2018-10-28 13:14:04
tags: [numpy, matplotlib, 数据可视化]
---

这是一个台湾的哥们炫技用的一个作品, 他仅仅使用numpy和matplotlib和一些数学知识就能绘制出一个卡通人脸, 是不是很牛逼。

<!-- more -->

### 视频教程

{% raw %}
<embed src='//player.youku.com/player.php/sid/XMzg5MTYwMTMyOA==/v.swf' allowFullScreen='true' quality='high' width='100%' height='500' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>

{% endraw %}

### 代码

以下代码请在Colab或者jupyter notebook中使用:

```python
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def mirror(a):
  return a|a[:,::-1]

def edge(a, delta=0):
  a = np.float32(a)
  while len(a.shape)>2:
    a = a.sum(axis=-1)
  r = np.zeros(a.shape, dtype=np.bool)
  b = (a[2:,1:-1]+a[:-2,1:-1]+a[1:-1,2:]+a[1:-1,:-2])/4
  r[1:-1,1:-1]= a[1:-1,1:-1]< b-delta
  return r
  
def rwalk(d=1.2):
  a = np.random.normal(0, d, size=(700,1))
  b = np.random.randint(0, 20, size=a.shape)>0
  a[b]=0
  return np.cumsum(a, axis=0)

img_size = (700,600)
y,x = np.indices(img_size)

#@title Default title text { run: "auto", vertical-output: true }
hair_r = 0
hair_r = 0.62 #@param {type:"slider", min:0, max:1, step:0.01}
hair_g = 0.35 #@param {type:"slider", min:0, max:1, step:0.01}
hair_b = 0.31 #@param {type:"slider", min:0, max:1, step:0.01}
show_hair = False #@param {type:"boolean"}
mouth_open = 0 #@param {type:"slider", min:0, max:1, step:0.01}
mouth_smile = 0 #@param {type:"slider", min:-1, max:1, step:0.02}


hair_color = (hair_r, hair_g, hair_b)
img = np.ones(img_size+(3,))*0.8

# head circle
head_circle = (y-250)**2+(x-300)**2 < 200**2  # 圓方程式
img[head_circle]=(1,235/255,223/255)

# jaw
line1 = abs(x-300)+0.35*(y-330)-185 # 直線方程式
line2 = (x-300)+1.7*(y-500)-100  # 直線方程式
line3 = line2[:,::-1] 
jaw = line1*line2*line3 < -180000
img[jaw & (y>330) & (line2<0) & (line3<0)  ]=(1,235/255,223/255)

#eyebrow
eyebrow1 = (x-245)**2 < (y-220)*150 # 拋物線
eyebrow2 = (x-245)**2 > (y-230)*185 # 拋物線
eyebrow_all = eyebrow1 & eyebrow2 & (y-225-(x-250)>0) # 直線方程式
img[mirror(eyebrow_all)] = (163/255, 138/255, 124/255)

# ear
ear1 = (x-110)+1.3*(y-320) # 直線方程式
ear2 = (y-460)-(x-150)  # 直線方程式
ear3 = (y-460)  # 直線方程式
ear = ear1 * ear2*ear3 - 100000
ear_all = (ear>0) & (img[:,:,0]==0.8) & (x>50) & (y<460) & (x<300)
img[mirror(ear_all)] = (1,235/255,223/255)

lip1 = 484-15*mouth_open # 上嘴唇中心高度
lip2 = 486+15*mouth_open # 下嘴唇中心高度
lip3 = 480-20*mouth_smile # 嘴角高度
# 嘴角高度固定在 x=300±30 y=lip3 計算拋物線參數
k1 = (lip1 - lip3)/30**2
k2 = (lip2 - lip3)/30**2

mouth1 = (lip1-k1*(x-300)**2 - y) # 拋物線 
mouth2 = (lip2-k2*(x-300)**2 - y) # 拋物線
img[ (mouth1<=0) & (mouth2>=0)]=(0.6,0.3,0.3)

# make edges
img[edge(img)] = 0
img[edge(jaw)& (line2<0) & (line3<0) & (y>410)]=0

```