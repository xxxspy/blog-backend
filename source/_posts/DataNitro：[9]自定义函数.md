---
title: DataNitro：[9]自定义函数
date: 2015-06-11 18:11:03
tags: [datanitro]
author: mlln.cn
---
之前我们可能讲过用datanitro来自定义一个函数，现在我们回顾一下整个过程，以便把该说的细节都总结在这里，防止以后再走弯路。现在我们从头开始做一个自定义函数。

- 在开始菜单中设定，允许使用自定义函数：

{% asset_img 29790130e924b899a5e7a36b6d061d950b7bf64f.jpg DataNitro：[9]自定义函数 %}

- 建立一个function.py文件，在里面写好我们要用的函数

{% asset_img 0d968f2397dda144f1e0b6e1b1b7d0a20df486bd.jpg DataNitro：[9]自定义函数 %}

- 比如我写一个简单的求和函数：传入的参数应当是一个list，其实在用的时候，传入的是一个CellRange对象

{% asset_img b9d8b7014c086e061273e51801087bf40bd1cb4f.jpg DataNitro：[9]自定义函数 %}

- 在excel里面引入该文件：

{% asset_img 8640bf8b87d6277f9b7bf76b2b381f30e924fc3d.jpg DataNitro：[9]自定义函数 %}

- 现在就可以在excel的单元格里输入公式了：

{% asset_img 0b3a1c087bf40ad1763f1db0542c11dfa8ecce4f.jpg DataNitro：[9]自定义函数 %}

- 好了到此我们就自定义了一个函数，并且能正常使用了，下面是我自己总结的一些心得，肯定以后有用：

- #写自定义函数的步骤：

- #1，新建一个名为function.py的文件

- #2，写一个函数在function.py

- #3，在excel中datanitro插件设置允许用户自定义函数

- #4，引入这个function.py文件

- #5，现在就可以在excel中使用该函数了。

- #注意事项：

- ##1，不能用使用*args和**kwargs

- ##2，可以使用CellRange作为参数输入多个值，传入的参数为一个2纬list，我写一个函数，看看如何遍历所有的元素

- ##    计算所有的元素的和

- ##    def py_sum(x):

- ##        a=0

- ##        for i in range(len(x)):

- ##            for j in x[i]:

- ##                a +=j

- ##        return a

- ##3，在函数里不能调用datanitro的任何excel对象，比如Cell，CellRange，虽然函数在使用的时候我们的确是传入的Cell或者CellRange，

- ##但是我们在函数的代码里，只能把这些参数当作Cell.value来用，比如：

- ##正确的写法是：

- ##    def my_sum(x, y):

- ##        return x + y

- ##

- ##错误的写法是：

- ##    def my_sum(x, y):

- ##        return x.value + y.value

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
