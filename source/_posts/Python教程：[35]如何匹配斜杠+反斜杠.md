---
title: Python教程：[35]如何匹配斜杠+反斜杠
date: 2016-09-01 18:01:23
tags: [python]
author: mlln.cn
---
今天用python采集数据的时候遇到了已给问题，就是这个字符串怎么匹配：“\/”,其实就是一个反斜杠一个斜杠，我用的是正则表达式来匹配，因为反斜杠是转义字符，我们还是看看具体的教程吧。

- 我们先来看看反斜杠+斜杠在python中的存放的方式，将下面的一堆绿色字符传递给txt这个变量

{% asset_img 2f3295d4b31c87015a337ff1257f9e2f0608ffe6.jpg Python教程：[35]如何匹配斜杠+反斜杠 %}

- 我们直接显示的字符和print出来的字符是不一样的。注意看http:后面的字符，直接显示出来的是“\\/”而print出来的是“\/”，那我们匹配的时候是按照“\\/”还是“\/”来匹配呢？

{% asset_img 1f569482b9014a901a7d8baaab773912b31bee2c.jpg Python教程：[35]如何匹配斜杠+反斜杠 %}

{% asset_img 263e802f070828381e891103ba99a9014d08f1e6.jpg Python教程：[35]如何匹配斜杠+反斜杠 %}

- 我们先给出正确的答案，我们需要匹配“\\/”

{% asset_img 373bc4b44aed2e73736c4b3b8501a18b86d6fae6.jpg Python教程：[35]如何匹配斜杠+反斜杠 %}

- 假如我们想要匹配“\/”，实际上得到的是“/”

{% asset_img 3853ad1bb051f8197566ce5dd8b44aed2e73e72c.jpg Python教程：[35]如何匹配斜杠+反斜杠 %}

- 如我们不使用r，也就是raw string，同样无法正确匹配

{% asset_img f9589818367adab4bc93d65489d4b31c8701e42c.jpg Python教程：[35]如何匹配斜杠+反斜杠 %}

- 当然，下面这种情况也是错误的。

{% asset_img 6f4703950a7b0208714df2f660d9f2d3562cc8e6.jpg Python教程：[35]如何匹配斜杠+反斜杠 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
