---
title: SVN教程：[5]部署django到SAE全过程
date: 2015-02-05 18:23:23
tags: [django]
author: mlln.cn
---
之前写过一篇在SAE上部署django的教程，现在返回来看犯了很多错误，所以在这里更正一篇，希望大家见谅，其实我也不是什么高手，难免有错误，下面看看在新浪sae上部署django的完整过程吧。

- 先去新浪sae上登陆，找到你建立的应用，然后点击【创建一个版本】，如果你没有创建过版本，可能只有一个版本

{% asset_img 1899a23eb13533fa86fe2d63aad3fd1f40345bf7.jpg SVN教程：[5]部署django到SAE全过程 %}

- 输入版本号，这个数字是任意的，我就按照版本3来做

{% asset_img a992e31f4134970a3a3bae6297cad1c8a6865df7.jpg SVN教程：[5]部署django到SAE全过程 %}

- 回到Deltatest文件夹，如果你看过前面的文章就知道这个文件夹是什么，如果你没有跟着做，你看一下这篇文章就知道：http://jingyan.baidu.com/article/6525d4b135bb1dac7d2e94ad.html看完这篇文章，右键单击这个文件夹，然后选择【svn更新】

{% asset_img a6c7d7177f3e6709db48fbb239c79f3df9dc55f7.jpg SVN教程：[5]部署django到SAE全过程 %}

- 更新完毕以后，你会看到这里多了一个文件夹3，这个文件夹就跟sae上的版本3相同了。

{% asset_img 718e25c79f3df8dcc67531dccf11728b461028f7.jpg SVN教程：[5]部署django到SAE全过程 %}

- 点击进入文件夹3，可以看到有这两个文件。

{% asset_img c87c6ecf3bc79f3dee1f5a7db8a1cd11738b2945.jpg SVN教程：[5]部署django到SAE全过程 %}

- 打开cmd命令窗口，我们先进入文件夹3，如图所示的命令：

{% asset_img 9e7ce6dcd100baa1d4d2f9f64510b912c9fc2e45.jpg SVN教程：[5]部署django到SAE全过程 %}

- 接着，我们在该文件夹下面创建一个新工程，比如工程名称叫做Deltatest

{% asset_img cc506c8b4710b912d53f48b3c1fdfc0393452245.jpg SVN教程：[5]部署django到SAE全过程 %}

- 回到文件夹3，这里就会多了一个文件夹deltatest，双击进入deltatest文件夹

{% asset_img 9304c888d43f87948101f663d01b0ef41ad53a45.jpg SVN教程：[5]部署django到SAE全过程 %}

- 这里面还有一个Deltatest文件夹
这是deltatest文件夹内的文件

{% asset_img a583631ed21b0ef432a02613dfc451da80cb3ef7.jpg SVN教程：[5]部署django到SAE全过程 %}

{% asset_img 1a94b36eddc451daacbeb2a6b4fd5266d11632f7.jpg SVN教程：[5]部署django到SAE全过程 %}

- 我们将这两个文件剪切

{% asset_img aa59892bd40735fad1b8f0f49c510fb30e2408f7.jpg SVN教程：[5]部署django到SAE全过程 %}

- 复制到这里，也就是文件夹3下面

{% asset_img 1f569482b9014a90afc0f8f0ab773912b21bee46.jpg SVN教程：[5]部署django到SAE全过程 %}

- 好了后面就简单了，我们要配置一下两个文件，第一个是index.wsgi文件，里面写这些内容：

{% asset_img 6391e903918fa0ec88c3de40249759ee3d6ddb3c.jpg SVN教程：[5]部署django到SAE全过程 %}

- 第二个文件是config.yawm

{% asset_img 9f6e190828381f30826237e4ab014c086f06f0c1.jpg SVN教程：[5]部署django到SAE全过程 %}

- 最后，提交一下

{% asset_img f7426d8da9773912ea023f2cfa198618367ae21c.jpg SVN教程：[5]部署django到SAE全过程 %}

- 注意点选【全部】，不然漏掉某些文件，你就失败了。

{% asset_img 79b1e936afc3793140603c64e9c4b74543a91137.jpg SVN教程：[5]部署django到SAE全过程 %}

- 在浏览器输入你的app的网址，看看能不能出现django的欢迎界面吧！！有问题可以在下面留言奥。

{% asset_img dbf554ed2e738bd4d5690c7ca38b87d6267ff9f0.jpg SVN教程：[5]部署django到SAE全过程 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
