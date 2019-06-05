---
title: python 线性代数：[19]行列式求解
date: 2016-10-05 18:03:15
tags: [python]
author: mlln.cn
---
行列式是线性代数里最重要的概念之一，今天我们使用Python的numpy和sympy包计算几个三阶行列式。下面的计算过程用excel存放矩阵的数据，而用excel里面的datanitro插件来运行Python代码，所以你可能要熟悉一下datanitro这个插件，关于这个插件的全部教程，我都写在了这个系列里：http://jingyan.baidu.com/season/43508

- 熟悉了这个插件以后，我们看看我们要解决的这四个矩阵：这些练习题来自《线性代数，同济大学第五版第一张课后题》。

{% asset_img 73ca5910b912c8fc4c2adbe7f8039245d78821fb.jpg python 线性代数：[19]行列式求解 %}

- 这接着我们将这些矩阵录入到excel当中。

{% asset_img f15e24292df5e0fec472a52b586034a85edf7276.jpg python 线性代数：[19]行列式求解 %}

- 接着我们把代码写到1.1.py文件中。

{% asset_img 4abae5edab64034fc2b2ee2cabc379310a551d59.jpg python 线性代数：[19]行列式求解 %}

- 接着，我们在excel的datanitro插件中，引入1.1.py文件，然后run一下就可以看到计算结果：

{% asset_img c28fddfdfc03924559e0c8258394a4c27d1e2507.jpg python 线性代数：[19]行列式求解 %}

- 以上是大概的流程，接下来具体讲解一下代码的意义。

- 引入需要的两个模块

{% asset_img 11794d43fbf2b211ba8ca964ce8065380cd78e3e.jpg python 线性代数：[19]行列式求解 %}

- 先看看第一题，这是计算第一个矩阵的行列式：

- a,CellRange是datanitro的内置对象，表示excel里面的一个单元格区域，通过它我们可以将这个区域内的值读取出来，存放到lst这个列表里，也就是Python中的list对象；接着用numpy模块的reshap方法，将list转换为3x3的矩阵，然后用刀了det方法计算行列式，最后结果为-4

{% asset_img 647912d7912397dd8e08b72e5d82b2b7d0a28763.jpg python 线性代数：[19]行列式求解 %}

- 第二题：红色字体都是注释，没有实际功能。跟第一题相比，第二题用字母代替了数字，所以，我们要用到Python的符号计算包sympy，我们可以看到E就是一个3x3的矩阵，但是需要将E转换为符号矩阵，用到了sp.Matrix，得到M，然后使用m的det方法计算得到行列式，结果是：

{% asset_img d56b3634349b033b4ce6d5f011ce36d3d539bd6a.jpg python 线性代数：[19]行列式求解 %}

{% asset_img d089b986c9177f3e181dd22774cf3bc79f3d56ab.jpg python 线性代数：[19]行列式求解 %}

- 第三题，与第二题类似，用到了sp.Matrix，但是我们还用到了sp.factor，这个方法可以将结果提取公因式，最后的计算结果为：

{% asset_img a6c7d7177f3e6709b76b6dd53fc79f3df8dc5575.jpg python 线性代数：[19]行列式求解 %}

{% asset_img b110e6198618367a153456f72a738bd4b31ce518.jpg python 线性代数：[19]行列式求解 %}

- 如果前三题你都搞懂了，第四题就简单了，没有新知识：

{% asset_img 6a2112338744ebf816254c15ddf9d72a6059a700.jpg python 线性代数：[19]行列式求解 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
