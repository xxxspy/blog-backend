---
title: Python教程：[57]txt追加模式
date: 2015-08-15 18:03:03
tags: [python]
author: mlln.cn
---
在写入模式下，我们写入txt，会覆盖掉txt中原先保存的内容，所以，我们今天介绍一个追加模式，可以在保留原先内容的前提下，追加新的内容。

- tt.txt文件中已经有了一些内容，我们想要保留这个内容，再追加新的内容
‘

{% asset_img a992e31f4134970a2a695eaf97cad1c8a6865ddc.jpg Python教程：[57]txt追加模式 %}

- 使用追加模式打开该文件，然后用write方法写入新的内容，然后关闭f文件。

{% asset_img 3a86813df8dcd10092a7b6a1708b4710b9122f33.jpg Python教程：[57]txt追加模式 %}

- 现在是写入新的内容，然后保留了已有内容。

{% asset_img cc506c8b4710b912e5dbb87ec1fdfc03934522dc.jpg Python教程：[57]txt追加模式 %}

- 假如我们想要先换一行，然后再输入新的内容，可以用换行符\n

{% asset_img 0fb505d5ad6eddc46ddcfa7b3bdbb6fd52663333.jpg Python教程：[57]txt追加模式 %}

- 新得到的文件就是增加了换行了的。

{% asset_img 7c5fcc1b0ef41bd59749a67453da81cb38db3ddc.jpg Python教程：[57]txt追加模式 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
