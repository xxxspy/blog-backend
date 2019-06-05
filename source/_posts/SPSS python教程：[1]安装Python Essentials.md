---
title: SPSS python教程：[1]安装Python Essentials
date: 2015-08-11 18:03:05
tags: [python,spss]
author: mlln.cn
---
这个系列教程是用来教大家如何使用python脚本来操作spss，使用脚本的好处是可以批量处理，如果你有很多数据要处理，他们的处理方法类似，那就需要用到脚本，可以自动化、智能化处理数据，大大减少数据分析的工作量，关于更多好处，你们可以参考spss的官方文档，这里不多少，开始介绍如何设置spss中的python插件：SPSS Python Essentials。

- 我用的spss版本是22.0，也是最近为了使用SPSS Python Essentials才安装的这个版本，大家可以参考这篇文章，以便正确安装spss 22.0。【http://jingyan.baidu.com/article/3d69c55187d5faf0cf02d73f.html】

- 安装好了spss22.0以后，如果你按照上面的安装教程进行的安装，SPSS Python Essentials就自动的安装在了你的spss22.0的安装目录下。接下来我们要进行必要的设置。

- 打开spss22的界面，打开编辑菜单下的【选项】

{% asset_img ea85a94543a982266fc821b18882b9014b90ebd8.jpg SPSS python教程：[1]安装Python Essentials %}

- 切换到脚本选项下，我们设置一下缺省脚本语言为python，点击【应用】

{% asset_img f9589818367adab4e5d911d589d4b31c8601e4d8.jpg SPSS python教程：[1]安装Python Essentials %}

- 切换到【文件位置】选项下，设置python的位置，我们有两个选项，一个是随IBM SPSS安装的位置，这就是说，spss22在安装的时候自动安装了python2.7，如果我们想要使用这个python，就选择第一个选项；但是我现在有一个更好的建议，使用我们自己安装的python，也就是说在安装spss之前就有一个python安装好了，我现在想使用这个python，我们可以设置python的其他安装，然后找到这个python安装的目录，最后点击确定就可以了。为什么我建议使用第二种选择呢？因为我的python下有很多安装好的扩展包，需要在处理数据的时候调用，以后安装新的扩展包也很方便。如果使用是、随spss安装的python，还需要另行安装这些扩展包

{% asset_img 8a95ad1c8701a18b32e218d99c2f07082938fed8.jpg SPSS python教程：[1]安装Python Essentials %}

- 设置完成以后，我们想要启动python的编辑窗口，需要在开始菜单中启动，如图所示。不能直接从python的安装目录里启动。

{% asset_img d35a10f41bd5ad6eaacc6e7c83cb39dbb6fd3c2b.jpg SPSS python教程：[1]安装Python Essentials %}

- 另外，spss22还有一个bug，我们虽然设置了Python的主目录，但是在新建脚本的时候，还是用的随spss安装的python的shell。所以想要使用python脚本，你就从上面那个方面里启动python shell

{% asset_img 90cebeec08fa513df4a366483f6d55fbb3fbd9d8.jpg SPSS python教程：[1]安装Python Essentials %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
