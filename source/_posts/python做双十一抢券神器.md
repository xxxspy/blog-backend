
---
title: python做双十一抢券神器
date: 2018-11-11 20:17:55
tags: [pywinauto, python, 游戏]
toc: true
xiongzhang: true
xiongzhang_images: [images/huodong.png ]

---
<span></span>
<!-- more -->


本文代码运行环境:

- windows10
- python3.6
- jupyter notebook

### 背景介绍

<img src="images/huodong.png" />

小米的双十一活动是这样的, 在小米商城微信小程序上有一个小游戏, 点击按钮开始计时, 然后点击停止, 如果中间时间刚好是11.11秒, 那么恭喜你就会得到一个优惠券。

作为一个做机器学习的小程序员, 我有几种方案: 

- 尝试找到活动的web页面, 用网页技术查看后台代码, 通过检测html代码来决定何时点击
- 使用机器学习刻识别时间数字, 等到合适的时候点击页面


不过这两种思路都失败了, 一是我没有找到web页面, 二是没有数据供我训练模型。

但是最后我还是做出来了, 具体步骤是这样的:

### 步骤一: 手机模拟器

使用手机模拟器可以在电脑上实现所有的手机功能, 我一开始尝试了几种手机模拟器, 失败了很多次, 主要问题就是打开微信的时候或者打开小程序的时候模拟器就会崩溃, 可见这些模拟器真的是很low, 不过最后找到了网易出品的MuMu模拟器, 凑合能用。

安装模拟器很简单, 安装微信也很简单。

### 步骤二: 开发点击按钮的程序

使用`pywinauto`模块, 可以很容易的实现鼠标点击的功能,但是我们需要知道点击屏幕的什么位置, 所以, 我先通过以下的代码追踪鼠标坐标, 然后查看鼠标放到按钮上的时候的坐标(我是在jupyter notebook中开发的程序):


```python
from IPython.display import display, clear_output
import win32api


def mouse_pos():
    # 无限循环程序
    while True:
        # 获取坐标
        x,y = win32api.GetCursorPos()
        # 清理输出区域的内容
        clear_output(wait=True)
        # 输出坐标
        display('x={},y={}'.format(x, y))
        # 休息0.5秒, 主要是为了降低程序执行的频率
        time.sleep(.5)
        
mouse_pos()
```

然后, 点击鼠标我们使用下面的代码:


```python
def click_button(btn_pos):
    s = time.time()
    x1, y1, x2, y2 = btn_pos
    x = int((x1 + x2)/2)
    y = int((y1+y2)/2)
    # sourcepos = win32api.GetCursorPos()
    win32api.SetCursorPos((x, y))
    # print('befor click:', time.time() - s)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    # 程序暂停0.1秒
    # time.sleep(.01)
    # print('mid click:', time.time() - s)
    # 鼠标左键释放
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)
```

### 步骤三: 计时

这个游戏很简单, 只需要点击两次鼠标, 并且确保点击鼠标之间的时间间隔是11.11秒, 所以我的思路就是下面这样:


```python
def go():
    # 第一次点击, 开始计时
    click_button(btn_box)
    start = time.time()
    pred = 0
    
    while True:
        d = time.time() - start
        # 时间快到11.11秒时, 我们触发点击动作
        if d >= 11.105:
            click_button(btn_box)
            break
        # elif d-pred >= 1:
        #     print(d)
        #     pred = d
        else:
            pass
```

### 结果

一开始的结果让我很失望, 因为实际上小米应该是做了一些随机动作的, 比如可以让开始时间在一定范围内随机, 那么我虽然确保两次点击的时间间隔是11.11秒, 但是因为你点击后, 它是随机开始计时的, 并且计算机程序也有时间误差, 所以我的程序总是失败, 一般误差在0.1秒以内, 没办法, 我尝试了很多次最终也只是运气好才成功的, 命中率不到1/20, 当然这个成绩比人强很多了, 所以我建议, 以后类似的活动, 小米官方应该考虑增加随机性, 不然以后所有节日都是程序员节了。


### Bonus Time

<embed src='//player.youku.com/player.php/sid/XMzkxNDMwMTcxMg==/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>



> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python做双十一抢券神器.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
