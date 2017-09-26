---
title: SVN教程：[4]SAE上部署django
date: 2015-10-15 18:17:17
tags: [django]
author: mlln.cn
---
这篇文章写的不是很详细，所以我又补充了一个详细版教程，你可以相互结合着看：http://jingyan.baidu.com/article/7082dc1c569f18e40a89bd21.html

- 我们先来创建一个文件夹deltatest（这是我在sae上创建的应用名称），如图所示，用于存放我们的django创建的站点

{% asset_img cc506c8b4710b9124dbfe0bbc1fdfc039245223d.jpg SVN教程：[4]SAE上部署django %}

- 在deltatest文件夹上面右键单击，然后选择SVN检出，建立与SAE的链接

{% asset_img b13fd48065380cd7b755b4a8a344ad34588281e8.jpg SVN教程：[4]SAE上部署django %}

- 这里大家都应该知道怎么设置，不会的看我上一篇文章【SVN教程[3]SEA代码部署】，点击确定

{% asset_img 263e802f07082838c90dca51ba99a9014c08f130.jpg SVN教程：[4]SAE上部署django %}

- 我们使用django在deltatest文件夹下面创建一个站点，用了下面两个命令。如果你不会，可以参考这篇经验：Django教程：[2]创建一个站点

{% asset_img 90cebeec08fa513dc8ec7a9b3f6d55fbb3fbd9f6.jpg SVN教程：[4]SAE上部署django %}

- 这样就在deltatest文件夹下面多了一个文件夹deltatest，将这个文件夹重命名为1

{% asset_img 61183b2dd42a283424ed204e59b5c9ea14cebfe8.jpg SVN教程：[4]SAE上部署django %}

{% asset_img 346bd85c10385343e48491649113b07ecb8088e8.jpg SVN教程：[4]SAE上部署django %}

- 我们右键单击文件夹，然后选择提交

{% asset_img 8474fbdde71190ef31b0849acc1b9d16fcfa60e8.jpg SVN教程：[4]SAE上部署django %}

- 打开浏览器，输入你的应用的域名，这个在你申请应用的时候设置的，你会看到django的欢迎界面，这说明django部署成功，还是不会的请在下面留言。

{% asset_img c87c6ecf3bc79f3d86aaf275b8a1cd11738b29e8.jpg SVN教程：[4]SAE上部署django %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
