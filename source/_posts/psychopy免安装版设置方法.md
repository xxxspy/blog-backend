---
title: psychopy免安装版设置方法
date: 2018-03-09 09:36:10
tags: [psychopy]
---

摘要: 无

<!--more-->

从这篇文章中下载psychopy免安装版, 下载以后解压得`psychopy2`文件夹. 注意这个文件夹有一个文件是`pythonw`或者`pythonw.exe`, 记下它的绝对路径, 例如我的绝对路径就是:`e:\PsychoPy2\pythonw.exe`, 下面会用到.

{% asset_img trees.png %}

然后从文件夹中找到一个`启动psychopy`的快捷方式, 右键单击它, 然后选择`属性`.

{% asset_img kuaijiefangshi.png %}

在属性中, 选择`快捷方式`, 复制`目标`路径到一个文本编辑器进行编辑.

{% asset_img shuxing.png %}


如我复制得到的路径是这样的:

`D:\programs\PsychoPy2\pythonw.exe "Lib\site-packages\psychopy\app\psychopyApp.py"`

将其改为`pythonw.exe`所在的真正路径, 它就存放`psychopy2`文件夹中.

`e:\PsychoPy2\pythonw.exe "Lib\site-packages\psychopy\app\psychopyApp.py"`

把修改后的路径填入`目标`中, 然后保存.

{% asset_img baocun.png %}
