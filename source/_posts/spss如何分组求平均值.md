---
title: spss如何分组求平均值
date: 2016-09-15 18:01:23
tags: [spss]
author: mlln.cn
---
分组求均值，举个俩字来说就是，一个数据分为男生和女生，那么分别求男生和女生的平均值就是分组均值，要求分组均值就要确定总共有多少分组，比如我们要求不同性别的人不同的学历的人他们每周花费在报纸上的钱有多少，这样有性别和学历两个变量进行分组了。
方法/步骤


-  打开数据文件以后，打开平均数对话框，在菜单栏上执行：analyze--compare means --means

{% asset_img 622762d0f703918fc8e5ce44513d269759eec40c.jpg spss如何分组求平均值 %}

- 将每周买报纸花费的钱作为因变量，将性别作为自变量，如图所示，然后点击next，我们来设置第二层自变量

{% asset_img 6159252dd42a2834b9bfc5855bb5c9ea15cebf27.jpg spss如何分组求平均值 %}

- 将最好学历作为第二层自变量，放到independent list，如果你还有要求分组均值的自变量，你可以继续点击next，不过我这里已经不用了

{% asset_img 359b033b5bb5c9ea84eaf06dd539b6003af3b327.jpg spss如何分组求平均值 %}

- 点击options来设置要输出的参数

{% asset_img 37d3d539b6003af3aca32fee352ac65c1038b627.jpg spss如何分组求平均值 %}

- 系统给出的默认值有：平均数、数据记录数、标准差。如果你需要其他的参数，还可以从左侧的列表里选择，然后点击continue

{% asset_img 3bf33a87e950352a5f78d6865343fbf2b2118b27.jpg spss如何分组求平均值 %}

- 回到了平均数对话框，点击ok即可输出不同分组的平均数。

{% asset_img 472309f7905298220a07ca4dd7ca7bcb0a46d40c.jpg spss如何分组求平均值 %}

- 这就是输出的结果：

-  

{% asset_img 9213b07eca806538aef3579d97dda144ad348227.jpg spss如何分组求平均值 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
