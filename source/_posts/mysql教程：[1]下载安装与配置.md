---
title: mysql教程：[1]下载安装与配置
date: 2016-08-05 18:03:05
tags: [mysql]
author: mlln.cn
---
这是mysql教程第一篇，我介绍一下自己的平台：windows7 64位，安装mysql版本是5.6，mysql 5.6的32位和64位的下载链接都在文章最下面的参考资料里（下载密码就是在链接后面），大家可以看文章的下面下载适合自己的版本，我就用的是64位。

- 第一步我们先在C:Program Files路径下，建立一个新文件夹，命名为mysql

{% asset_img 58af236d55fbb2fbbfba776d4d4a20a44723dcf9.jpg mysql教程：[1]下载安装与配置 %}

- 将下载下来的压缩包解压到mysql文件夹汇总

{% asset_img f76575600c338744fb550003530fd9f9d62aa0f9.jpg mysql教程：[1]下载安装与配置 %}

- 最后我解压得到的mysql就是酱紫了：注意看地址栏，看看和你是不是一样；当然你可以和我不一样，但是在后面的步骤中我是需要用到mysql的解压路径的，所以，希望你注意一下啦。了

{% asset_img 7787b9efce1b9d16a98eb51ef1deb48f8d5464c0.jpg mysql教程：[1]下载安装与配置 %}

- 我们打开计算机的【属性】面板，你可能叫【我的电脑】，随便啦

{% asset_img 148f28d3d539b6001b5e20c8eb50352ac75cb7f9.jpg mysql教程：[1]下载安装与配置 %}

- 打开【高级系统设置】，，，哎，过程很繁琐呀

{% asset_img 9864a2315c6034a83cab97fec9134954082376c0.jpg mysql教程：[1]下载安装与配置 %}

- 切换到【高级】标签下，打开环境变量

{% asset_img 906289dda144ad346a2fa8f8d2a20cf430ad85f9.jpg mysql教程：[1]下载安装与配置 %}

- 新建一个系统该变量，点击【新建】

{% asset_img 310f3b1f95cad1c8d8f2d3587d3e6709c83d51c0.jpg mysql教程：[1]下载安装与配置 %}

- 变量名设置为【MYSQL_HOME】，变量值设置为mysql的解压路径【C:Program Filesmysql】

{% asset_img 4e0b3ea4462309f791cd836d700e0cf3d6cad6eb.jpg mysql教程：[1]下载安装与配置 %}

- 接着找到path，编辑一下，点击【编辑】

{% asset_img ae10eddeb48f8c54cd43ea5038292df5e1fe7ff9.jpg mysql教程：[1]下载安装与配置 %}

- 将新的路径添加进去，注意是添加不是覆盖，添加的路径是【%MYSQL_HOME%in】，注意与其他路径用分号隔开

{% asset_img 5d212aa85edf8db1afbe531b0b23dd54574e74f9.jpg mysql教程：[1]下载安装与配置 %}

- 打开dos窗口（win+r，输入cmd，点击确定）

{% asset_img cc506c8b4710b9124651d981c1fdfc03934522f9.jpg mysql教程：[1]下载安装与配置 %}

- 我们将路径重新定位到mysqlin下，用到了cd命令，你可以看我写的文章【dos命令：[1]cd用法】来直到cd的意义。我们现在输入的命令是【cd /d c:Program Filesin】

{% asset_img 4abae5edab64034fc384ed79adc379310b551dc0.jpg mysql教程：[1]下载安装与配置 %}

- 接着我们输入命令【mysqld install MySQL --defaults-file="D:Program Filesmysqlmy-default.ini"】，看到成功安装的提示了没？这说明已经安装成功了。欢呼吧，你可以开始mysql开发了。下一篇文章我们会讲到如何运行mysql服务器。

{% asset_img a583631ed21b0ef48178b721dfc451da80cb3ef9.jpg mysql教程：[1]下载安装与配置 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
