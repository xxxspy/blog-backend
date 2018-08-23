---
title: DataScience博客重大更新-在线运行示例代码
date: 2018-08-23 12:54:31
tags: [python]
toc: true
repl: "https://repl.it/@xxxspy/basic-python?lite=true"


---

在征询广大网友的意见以后, 我决定在博客网页上增加实时运行代码的功能。我选择repl.it作为本站的程序运行后台服务, 它的好处是免费的, 并且可以任意安装依赖库, 并且可以随意嵌入到网页中。

<!-- more -->

### repl使用方法

在本网站的博客上, 如果某个页面支持repl, 那么你会在示例代码的下方发现这几个按钮:

<img src="buttons.png" class="img-thumbnail"/>

点击"调试"按钮就能打开repl编辑器:

<img src="editor.png" class="img-thumbnail"/>

在这里你可以复制我页面上的代码, 然后粘贴到编辑器中, 点击"运行", 你就能看到代码运行结果:

<img src="run.png" class="img-thumbnail"/>

需要注意的是, 初次运行需要安装一些依赖, 除非代码没有依赖第三方库, 否则可能需要一两分钟的安装时间。

不过只是第一次运行的时候需要安装依赖, 以后再次运行就不必了。

### 试玩repl

下面是一行代码, 你需要做的是:

- 双击代码, 复制代码
- 点击"调试"打开编辑器
- 粘贴代码, 然后点击运行

```python
print('mlln.cn','\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
```