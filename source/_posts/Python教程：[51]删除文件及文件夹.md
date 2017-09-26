---
title: Python教程：[51]删除文件及文件夹
date: 2016-05-17 18:17:05
tags: [python]
author: mlln.cn
---
假如有一个txt文件，我想要使用python命令删除它，怎么弄？这里用到了Python的os模块，我们使用例子来说明如何如何删除文件及目录。

- 在d盘下有一个tt文本文件，我们来删除它

{% asset_img 8697397f9e2f0708688ca795eb24b899a801f25f.jpg Python教程：[51]删除文件及文件夹 %}

- 首先引入os模块

{% asset_img e865a699a9014c0828b2a530087b02087af4f45f.jpg Python教程：[51]删除文件及文件夹 %}

- 使用os下的remove命令来删除该文件，参数是r'd:/tt.txt’，通常路径字符串都是用r字符串

{% asset_img 1e71f724b899a90109c1d6a31f950a7b0308f574.jpg Python教程：[51]删除文件及文件夹 %}

- 现在改文件已经被删除，现在我们再运行一下该命令，看看有什么提示错误

{% asset_img 0b3a1c087bf40ad12e6d4a76552c11dfa8ecce5f.jpg Python教程：[51]删除文件及文件夹 %}

- 这就是提示的错误，为了写出更见健壮的程序，我们通常要在删除文件前，先检验该文件是否存在。

{% asset_img 48151723dd54564e598869acb1de9c82d0584f73.jpg Python教程：[51]删除文件及文件夹 %}

- 使用path.exists命令来检验文件是否存在，参数仍然是路径字符串

{% asset_img 6dc09e0a19d8bc3e64e58b5f808ba61ea9d34573.jpg Python教程：[51]删除文件及文件夹 %}

- 配合if语句，我们就可以写出一个健壮的删除文件的命令。

{% asset_img 83cab81ea8d3fd1f9ae42faf324e251f94ca5f73.jpg Python教程：[51]删除文件及文件夹 %}

- 上面讲到了如何删除文件，下面说一下如何删除文件夹。我们用到了rmdir方法，它可以直接删除空文件夹

{% asset_img 814b07d8bc3eb135e7b4382ea41ea8d3fc1f44f1.jpg Python教程：[51]删除文件及文件夹 %}

- 假如文件夹非空，会提示这样的错误：

- Traceback (most recent call last):

-   File "<pyshell#8>", line 1, in <module>

-     os.rmdir(r'd:/tt/')

- WindowsError: [Error 145] : 'd:/tt/'

{% asset_img 9252ae7eca80653882d42b8695dda144ad34822e.jpg Python教程：[51]删除文件及文件夹 %}

- 假如文件夹不存在，会提示这样的错误：

- Traceback (most recent call last):

-   File "<pyshell#16>", line 1, in <module>

-     os.rmdir(r'd:/tt/')

- WindowsError: [Error 2] : 'd:/tt/'

{% asset_img 5beeba0f4bfbfbedb239b9ea7af0f736aec31f87.jpg Python教程：[51]删除文件及文件夹 %}

- 怎么删除非空文件夹？我们用到了shutil模块

{% asset_img 32bb9c8ba61ea8d32551fb91950a304e241f58f1.jpg Python教程：[51]删除文件及文件夹 %}

- 用rmtree命令可以直接删除文件夹，包括内部文件

{% asset_img 83cab81ea8d3fd1f987a2daf324e251f94ca5ff1.jpg Python教程：[51]删除文件及文件夹 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
