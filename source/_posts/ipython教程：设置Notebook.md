---
title: ipython教程：设置Notebook
date: 2015-05-11 18:03:17
tags: [python]
author: mlln.cn
---
我们有两种方式来设置你的ipython notebook，一种方式是通过命令行启动notebook服务器的时候，在ipython notebook后面添加一个参数来设置notebook服务器；另一种方式是创建一个ipython_notebook_config.py文件来写入你的设置参数。今天我们就讲一下后者。

- 这个文件应该放在你的ipython的文件夹下的profile文件夹。通过命令ipython locate来找到这个ipython_notebook_config.py文件放在哪里。

{% asset_img f35ea0096b63f6248d5e328a8244ebf81b4ca3fd.jpg ipython教程：设置Notebook %}

- 这样你可以打开这个文件夹，看看里面都有什么：所有的配置文件都放在了profile_default文件夹。如果没有看到这个文件夹，你可以使用ipython prifile create来创建

{% asset_img 7c5fcc1b0ef41bd5d9a4e37d54da81cb38db3d00.jpg ipython教程：设置Notebook %}

{% asset_img 9f1011b30f2442a75c22882cd443ad4bd01302cf.jpg ipython教程：设置Notebook %}

- 当然你可以给你的profile文件夹起个名字，比如就叫profile_aaa，你可以这样写命令：ipython profile create aaa

{% asset_img d872d695d143ad4b5802334987025aafa50f06cf.jpg ipython教程：设置Notebook %}

{% asset_img dbf554ed2e738bd41da1c7b8a48b87d6267ff97c.jpg ipython教程：设置Notebook %}

- 如果你想要使用aaa这个profile，我们在启动ipython notebook的时候使用命令：ipython notebook --profile==aaa

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
