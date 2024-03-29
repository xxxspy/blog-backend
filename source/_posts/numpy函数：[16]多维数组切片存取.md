---
title: numpy函数：[16]多维数组切片存取
date: 2016-01-17 18:23:03
tags: [numpy]
author: mlln.cn
---
多维数组和一维数组的存取方法类似，我们这篇文章介绍使用切片来存取一个二维数组，多维数组道理一样，你自己尝试一下即可。

- 先从numpy中引入所有

{% asset_img 6a22e8246b600c335b90a648184c510fd8f9a102.jpg numpy函数：[16]多维数组切片存取 %}

- 创建一个一维数组

{% asset_img eab9044c510fd9f936fe2de9272dd42a2934a402.jpg numpy函数：[16]多维数组切片存取 %}

- 将一维数组重新组织成一个二维数组

{% asset_img f9589818367adab4eaff60c389d4b31c8601e4c0.jpg numpy函数：[16]多维数组切片存取 %}

- 使用切片来读取第一行中的第二和第三个数，我们看下标【0,2:4】,其中逗号前的数字表示第0轴下标取值范围，逗号之后表示第1维下标取值范围，2:4就表示2-4之间

{% asset_img 8a95ad1c8701a18b21c469cf9c2f07082938fec0.jpg numpy函数：[16]多维数组切片存取 %}

- 我们可以返回一个二维的数组

{% asset_img e8112b2ac65c1038a797b642b0119313b17e8902.jpg numpy函数：[16]多维数组切片存取 %}

- 只读取第3列的元素（逗号前只有一个冒号，表示所有）

{% asset_img 9252ae7eca806538f703dc9395dda144ac348202.jpg numpy函数：[16]多维数组切片存取 %}

- 也可以设置步长（两个逗号后面的2表示步长为2）

{% asset_img 647912d7912397dd5f90e0845b82b2b7d1a28702.jpg numpy函数：[16]多维数组切片存取 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
