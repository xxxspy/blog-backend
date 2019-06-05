---
title: 报告系统word插件界面使用培训
date: 2017-06-29 19:05:17
tags: 报告系统
---

### 配置常量

- 点击基本配置

{% asset_img 1.jpg 基本配置 %}

- 看到如下界面，输入如下参数（不要输错），保存即可。

{% asset_img 2.jpg 基本配置 %}

### 文字模板

- 选择需要设置成模板的文字

{% asset_img 4.jpg %}

- 点击添加模板

{% asset_img 5.jpg %}

- 你就可以看到，原先选中的部分就会增加了一个文字模板。

{% asset_img 6.jpg %}

- 之后你需要配置模板

{% asset_img 7.jpg %}

- 打开的对话框如下，分为两个部分。上面定义变量，下面写渲染内容。

{% asset_img 8.jpg %}

- 比如，在这里我们写成：

```python
======Variables=======

p2=v("yuwen_level","4ywstu")|select({"province":pro_code})|which(2)|percent|format({"decimal":1,"multi":100})
p3=v("yuwen_level","4ywstu")|select({"province":pro_code})|which(3)|percent|format({"decimal":1,"multi":100})
p4=v("yuwen_level","4ywstu")|select({"province":pro_code})|which(4)|percent|format({"decimal":1,"multi":100})


=======Content========


{ { p2 + p3+p4 } }

```

- 点击保存按钮

{% asset_img 9.jpg %}

- 点击预览

{% asset_img 10.jpg %}

- 看到预览完毕，点击确定。

{% asset_img 11.jpg %}

- 注意文档要经常保存。

- 快速删除模板

你只需要右键单击文字，然后选择“删除文本控件”即可。

- 表格中的文字模板

很多表格不需要用表格模板，只需要使用文字模板，例如：

{% asset_img 26.jpg %}


### 图表模板

- 先选择图表

{% asset_img 12.jpg %}

- 点击配置模板

{% asset_img 13.jpg %}

- 点击你要修改的序列名，比如这里的【广东省】

{% asset_img 14.jpg %}

- 在左边输入模板，点击中间的按钮就能进行计算，并在右侧看到计算结果

{% asset_img 15.jpg %}

- 你还可以在这里选择已有的模板

{% asset_img 16.jpg %}

- 点击保存

{% asset_img 17.jpg %}

- 还有一个保存

{% asset_img 18.jpg %}

- 点击预览就可以看到图表被渲染后的结果

{% asset_img 19.jpg %}

- 接着处理类似这样的图

{% asset_img 20.jpg %}

序列代码用到了'merge'方法

```
v("yuwen_level","8ywstu")|select({"province":pro_code})|groupby("school_loc3")|which(1)|percent|format({"decimal":1,"multi":100})
|merge|
v("yuwen_level","4ywstu")|select({"province":pro_code})|groupby("school_loc3")|which(1)|percent|format({"decimal":1,"multi":100})
```

- 同时使用广播方法，可以快速复制代码到其他序列

{% asset_img 21.jpg %}

- 使用反向选项，可以使序列值反向排序

{% asset_img 22.jpg %}

- 接下来设置这种图

{% asset_img 23.jpg %}

- 它的序列长度是可变的，就是每个省有多少个区县是不确定的，不过它只有一个序列

{% asset_img 24.jpg %}

- 这这种图需要定义XValues，因为它是随省份的不同而变化的。

{% asset_img 25.jpg %}

- XValues的定义方法是：

代码如下，这种代码几乎不用改，可以直接贴上去用。

```python
v("fakename","dists")|select({"province":pro_code})|key("dist")|value
```

- 类似图形

{% asset_img 27.jpg %}

这种图形和上面介绍的图形是类似的，页需要定义XValues


### 表格模板

