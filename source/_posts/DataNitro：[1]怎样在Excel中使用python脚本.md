---
title: DataNitro：[1]怎样在Excel中使用python脚本
date: 2015-05-23 18:05:05
tags: [python,excel,datanitro]
author: mlln.cn
---
怎么在Excel中运行python脚本？这个问题由来已久，很多pythoner都希望直接用python控制Excel，但是只能从外部调用，有没有一个VBA的东西可以直接在Excel中运行呢？答案是有，DataNitro就是这么一个东西，看看下面Excel中的界面，他就是了，可以直接点击‘run'来运行一个Python脚本。下面我们来看看它是如何安装与配置的。

- 先安装python2.7，其他版本不知道行不行，但是这个肯定行，然后配置环境变量，保证python在该环境中，打开开始菜单，找到计算机，然后右键单击它，选择【属性】

{% asset_img 00a82701213fb80e416877e135d12f2eb938940f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 找到高级系统设置

{% asset_img 4e83cb628535e5dda375b3e975c6a7efce1b626f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 找到环境变量，点击该按钮，打开环境变量设置窗口

{% asset_img ae10eddeb48f8c54db6ad31939292df5e0fe7f0f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 找到Path系统变量，然后点击【编辑】

{% asset_img 3b6833f5e0fe9925e9557f6637a85edf8db1716f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 在这里，确保python的安装目录在，没有的话，添加进去

{% asset_img 5d212aa85edf8db191976a520a23dd54564e740f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 下面就可以安装该插件了，去官网下载一个；或者百度一下，各大下载网站都有

{% asset_img 8cf0d51349540923803775489158d109b3de496e.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 双击即可安装，安装过程就是一路点击’下一步，不过有一步需要注意

{% asset_img b13fd48065380cd7b447b4dba244ad345982816f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

{% asset_img c87c6ecf3bc79f3d85bff206b9a1cd11728b296e.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

{% asset_img 78701455b319ebc40f2660af8126cffc1e17166e.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

{% asset_img 29790130e924b89971826f0e6d061d950a7bf60f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 在这里，不要勾选python，如果通过这种方式安装python，你原先安装的python就无法使用了

{% asset_img eab9044c510fd9f9ddae435f262dd42a2834a40f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

- 最后安装完成，打开Excel就可以看到datanitro了

{% asset_img 969cbf44ad34598298d3f3a40ff431adcbef846f.jpg DataNitro：[1]怎样在Excel中使用python脚本 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
