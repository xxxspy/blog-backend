---
title: DataNitro：[2]调用Python的方法
date: 2015-10-01 18:03:19
tags: [python,datanitro]
author: mlln.cn
---
作为入门的第二篇文章，我们还是要讲一些基础的东西，这篇文章我们介绍一下如何在datanitro下使用Python来操作excel。

- 第一种方式，我们可以在Python shell里面运行Python代码，点击它打开

{% asset_img 5327ce160924ab1887e97a6636fae6cd7a890ba0.jpg DataNitro：[2]调用Python的方法 %}

- 一开始我们会看到这个界面，出现了欢迎信息，说明你的datanitro Python shell是可以工作的。

{% asset_img b3f6cea20cf431ad6860d8684836acaf2fdd98f6.jpg DataNitro：[2]调用Python的方法 %}

- 输入一个简单的命令：Cell(1,1).value='hello world'（注意大小写）；按回车就可以执行

{% asset_img adee30dda3cc7cd9279faf883a01213fb90e91f6.jpg DataNitro：[2]调用Python的方法 %}

- 这段代码的效果就是单元格A1赋值为hello world

{% asset_img d002b34bd11373f09dc0f4cea70f4bfbfaed04a0.jpg DataNitro：[2]调用Python的方法 %}

- 我们可以使用Python中已经安装的包：

{% asset_img 7aad4ae736d12f2e0ab735314cc2d562843568f6.jpg DataNitro：[2]调用Python的方法 %}

- 我们可以先建立一个Python的脚本文件**.py，然后引入该文件：点击import

{% asset_img e49cf91190ef76c61b60607a9e16fdfaae5167f6.jpg DataNitro：[2]调用Python的方法 %}

- 找到该Python文件并打开

{% asset_img 42e89c26cffc1e17b84017604990f603728de9a1.jpg DataNitro：[2]调用Python的方法 %}

- 你会看到这个文件已经被引入，点击editor就可以编辑该文件

{% asset_img 8bc3a7014a90f603454f07163a12b31bb151eda1.jpg DataNitro：[2]调用Python的方法 %}

- 编辑器也是够难看的！但是我们可以先输入以下代码试试：注意#号表示注释，没有任何作用，实质上只有一句话有用：Cell(1,3).value=u'中文'

{% asset_img 8cf0d513495409230fdbf82f9158d109b2de49f6.jpg DataNitro：[2]调用Python的方法 %}

- 然后回到excel，点击run，就可以执行命令

{% asset_img 570f8c58d109b3de4b0d7f39cfbf6c81810a4cf6.jpg DataNitro：[2]调用Python的方法 %}

- 用过excel函数的都知道它有多么强大，现在我们有机会写自己的函数了，我们需要先建立一个名字为functions.py的文件

{% asset_img d048adde9c82d1581530c2e0830a19d8bd3e42f6.jpg DataNitro：[2]调用Python的方法 %}

- 在里面写入一个function并保存

{% asset_img a84052086e061d955bb9ac6978f40ad163d9caa1.jpg DataNitro：[2]调用Python的方法 %}

- 记得检查在设置里面是否有允许使用Python自定义函数，如果你没有选，你需要选上他，然后重启excel

{% asset_img 4075890a304e251f7d457fa9a486c9177e3e53f6.jpg DataNitro：[2]调用Python的方法 %}

- 现在在单元格里使用一下该函数，你可以看到效果：

{% asset_img 964b2e4e251f95ca384709e7ca177f3e660952f6.jpg DataNitro：[2]调用Python的方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
