---
title: Python统计分析：[7]混合设计的方差分析
date: 2016-09-23 18:05:15
tags: [python]
author: mlln.cn
---
混合设计的方差分析就是既有组内变量又有组间变量的方差分析。想要进行这样的方差分析，如果还是用python.statsmodels就不太方便了，因此用到了Python的另一个还比较年轻的统计包pyvttbl,它对anova的支持更全面，使用也更方便，这里我们就看看如何用pyvttbl来实现混合设计的方差分析。

- 引入DataFrame对象，注意此Dataframe不是pandas.DataFrame

{% asset_img cebd00178a82b90162ea4c4f708da9773812efcc.jpg Python统计分析：[7]混合设计的方差分析 %}

- 读取数据

{% asset_img b8405490f603738d820d835eb01bb051f919eccc.jpg Python统计分析：[7]混合设计的方差分析 %}

- 我们看一下pyvttbl.DataFrame的结构，有一个变量是必须的——SUBJECT，也就是被试编号，同一个被试有相同的编号，这是我们必须提供的，否则在后面的分析中会出错。

{% asset_img 373bc4b44aed2e73beae09508401a18b86d6facc.jpg Python统计分析：[7]混合设计的方差分析 %}

- 我们用anova方法进行混合设计的方差分析，需要制定因变量score，组间变量group，组内变量test

{% asset_img 2f3295d4b31c870199f13d9a247f9e2f0608ffcc.jpg Python统计分析：[7]混合设计的方差分析 %}

- 打印出来的结果有很多，首先看组间效应的检验，group的F和sig值
与此相对应，我们输出spss中的结果

{% asset_img 9f6e190828381f30d65e02d5aa014c086f06f0cc.jpg Python统计分析：[7]混合设计的方差分析 %}

{% asset_img 5beeba0f4bfbfbedb3cbb9037bf0f736aec31ff8.jpg Python统计分析：[7]混合设计的方差分析 %}

- 接着是组间效应的检验，包括交互效应
以下是spss中的输出结果

{% asset_img 8367d1fc1e178a829eaef0dcf503738da877e8f9.jpg Python统计分析：[7]混合设计的方差分析 %}

{% asset_img 4bd1e803738da97715bd0957b351f8198718e3f9.jpg Python统计分析：[7]混合设计的方差分析 %}

- 最后是边际均值

{% asset_img 8759287adab44aed1adc3198b01c8701a08bfbf9.jpg Python统计分析：[7]混合设计的方差分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
