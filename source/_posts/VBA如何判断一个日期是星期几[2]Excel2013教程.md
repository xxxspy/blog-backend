---
title: VBA如何判断一个日期是星期几[2]Excel2013教程
date: 2015-10-19 18:17:03
tags: [excel]
author: mlln.cn
---
我们经常要将日期转换成星期，这个在Excel中很容易实现，但是如何使用vba来转换，这个可能大家就不熟悉了，今天就来给大家演示一下如何使用vba来进行日期到星期的转换：

- 首先打开Excel，如图所示，有一列日期，我们在第二列输入周几，作为星期列

{% asset_img 310f3b1f95cad1c8d1cbed4f7e3e6709c93d5122.jpg VBA如何判断一个日期是星期几[2]Excel2013教程 %}

- 我们切换到vb界面，如图所示，在菜单栏上执行：开发工具--vb

{% asset_img 814b07d8bc3eb13558cfa6d3a71ea8d3fd1f440a.jpg VBA如何判断一个日期是星期几[2]Excel2013教程 %}

- 双击模块，打开模块，在这个模块中定义一个函数，如图所示：在下面的参考资料里有这个Excel文件的下载链接

{% asset_img c28fddfdfc0392455cc5f0678694a4c27d1e2522.jpg VBA如何判断一个日期是星期几[2]Excel2013教程 %}

- 接着我们选中b2单元格，输入公式：=周几（a2），这样就可以计算周几了

{% asset_img d57e9994a4c27d1e5d562aac1ad5ad6eddc43822.jpg VBA如何判断一个日期是星期几[2]Excel2013教程 %}

- 拖动b2单元格的右下角，快速填充下面的单元格，到此我们就完成了所有的日期的转换

{% asset_img 3a86813df8dcd1003a94e949738b4710b9122f0a.jpg VBA如何判断一个日期是星期几[2]Excel2013教程 %}

{% asset_img cc506c8b4710b9124dc9e796c2fdfc039245220a.jpg VBA如何判断一个日期是星期几[2]Excel2013教程 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
