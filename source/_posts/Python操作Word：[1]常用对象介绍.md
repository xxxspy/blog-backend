---
title: Python操作Word：[1]常用对象介绍
date: 2015-05-01 18:03:05
tags: [python]
author: mlln.cn
---
前面已经介绍过了试用win32com类库来进行Word开发，系列文章《Python操作Word》是继承了前面的文章，所以，你应该先查看前面的文章，其实只有两篇，文章地址列在最下面的参考资料了。

- 段落：这是我蕞常用的类，可以给不同的段落设置格式，也可以插入内容，比如读取段落的数目，使用Paragraph.Count。选择特定的锻炼可使用Paragraph[]

{% asset_img 0db52fadcbef7609263e4b902cdda3cc7cd99e4d.jpg Python操作Word：[1]常用对象介绍 %}

- 图片、图表：Shapes对象，获取图片的数目使用Count，获取第N个图片使用Shapes[N]

{% asset_img bd70426034a85edf1a4b2d2c4b540923dc5475bf.jpg Python操作Word：[1]常用对象介绍 %}

- 表格：Tables对象，获取Tables的数目使用Count,获取第N个表格使用Tables[N]

{% asset_img 8474fbdde71190eff5ce40d0cc1b9d16fdfa604d.jpg Python操作Word：[1]常用对象介绍 %}

- 范围：Range对象是最重要的对象，我们经常使用range()来取得文档的所有范围；使用rang(i,j)可以获得第i行第j个字的位置；

{% asset_img 95afee1f3a292df570f67e1abe315c6034a8734d.jpg Python操作Word：[1]常用对象介绍 %}

- 还可以使用Start 和End来标注开始和结尾。

{% asset_img bbe0d311728b471078e82ec3c1cec3fdfd0323bf.jpg Python操作Word：[1]常用对象介绍 %}

- 文字：Words对象，想要知道有多少个字？看下面。

{% asset_img d57e9994a4c27d1e1ee1e8cb19d5ad6edcc438bf.jpg Python操作Word：[1]常用对象介绍 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
