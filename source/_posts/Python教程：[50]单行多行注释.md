---
title: Python教程：[50]单行多行注释
date: 2015-09-05 18:11:23
tags: [python]
author: mlln.cn
---
python注释用的是符号#，但只能注释一行，如果要写一大片文字，最好还是使用三个单引号进行注释，另外，如果你用的是中文注释，还需要在文件头部声明编码方式，下面我们看看几个例子：

- 首先在第一行必须声明编码方式

{% asset_img 3bc6f750352ac65cc7bb3ae3f9f2b21192138aa1.jpg Python教程：[50]单行多行注释 %}

- 单行注释，用一个#就可以了，同时被注释的文字显示为红色（不一样的编辑器显示的颜色不同）

{% asset_img 570f8c58d109b3de81f4b8f8cebf6c81810a4c93.jpg Python教程：[50]单行多行注释 %}

- 多行注释就用三个单引号，注意要在注释首位都用三个单引号

{% asset_img b3508d13b07eca80bbbb6577932397dda04483a1.jpg Python教程：[50]单行多行注释 %}

- 现在我写了这些代码，按下F5运行一下

{% asset_img 814b07d8bc3eb135168ceb2ba41ea8d3fc1f4493.jpg Python教程：[50]单行多行注释 %}

- 你会看到只输出了ok

{% asset_img 58c3acb7d0a20cf4d92ea24f74094b36adaf99a1.jpg Python教程：[50]单行多行注释 %}

- 假如我们删掉首行的编码声明

{% asset_img 2f9cbdcc7cd98d10f06a50a1233fb80e7aec90a1.jpg Python教程：[50]单行多行注释 %}

- 再按下F5就会提示你生命编码方式，点击edit my file就会自动添加一个编码方式。

{% asset_img c87c6ecf3bc79f3dc0aab8a0b8a1cd11738b2993.jpg Python教程：[50]单行多行注释 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
