---
title: Python教程：[3]input和raw_input函数
date: 2016-10-03 18:03:01
tags: [python]
author: mlln.cn
---
今天使用python3.2来编辑程序的时候，突然发现一个错误name 'raw_input' is not defined，原因是从版本3.0 开始去掉了raw_input 函数，改用input。所以两个函数合并在了一起，所以今天只讲input函数就可以了。input函数用于弹出一个对话框，提示用户输入内容，输入的内容可以直接显示出来，也可以赋值给某个变量。

- 基本用法是：input('输入要显示的文字')

{% asset_img f7426d8da97739129adc0f4bfa198618377ae2e7.jpg Python教程：[3]input和raw_input函数 %}

- 弹出一个对话框，让你输入，假如我们输入“你好”

{% asset_img a8362712b31bb051d3de3902347adab44bede0e7.jpg Python教程：[3]input和raw_input函数 %}

- 立刻会出现这个输入的内容。

{% asset_img 4bac30738bd4b31cb4c61e9185d6277f9f2ff8e7.jpg Python教程：[3]input和raw_input函数 %}

- 我们输入

{% asset_img ca5257540923dd54952c2d42d309b3de9c82487a.jpg Python教程：[3]input和raw_input函数 %}

- 弹出对话框，假如我们输入“www”

{% asset_img ac2fc3c451da81cbc3f609e75066d0160924314d.jpg Python教程：[3]input和raw_input函数 %}

- a的值就是“www”

{% asset_img a28d62d98d1001e9a225e125ba0e7bec54e79744.jpg Python教程：[3]input和raw_input函数 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
