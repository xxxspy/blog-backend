---
title: Django教程：[7]网站根目录的设置
date: 2015-04-17 18:01:19
tags: [django]
author: mlln.cn
---
现在我们开启开发服务器，然后访问一下网站根目录，也就是127.0.0.1:8000，你会发现出现了404错误提示，这是因为Django依赖于指定给该路径的模式来返回内容，现在我们并没有给改路径指定返回的内容，我们怎么设置呢？

- 打开你的站点所在文件夹，找到view.py，使用IDLE进行编辑；根据我前面的文章可以知道，view.py是我自己创建的，不是startproject的时候自动创建的，所以你可能创建了不同名称的文件。

{% asset_img 4a77b2af2edda3cca0d8f15a03e93901213f9249.jpg Django教程：[7]网站根目录的设置 %}

- 在该文件中添加一个函数homepage，它只返回一句话“这是首页”

{% asset_img d7c9ca3f8794a4c2482fae510cf41bd5ad6e3978.jpg Django教程：[7]网站根目录的设置 %}

- 接着哦我们打开urls.py

{% asset_img 30ecd5ef76094b3675ae5297a1cc7cd98d109d49.jpg Django教程：[7]网站根目录的设置 %}

- 添加两句话，第一句引用homepage（刚才添加的函数）；第二句将hongpage与url模式相连接

{% asset_img d1571724ab18972b903649b0e4cd7b899e510a78.jpg Django教程：[7]网站根目录的设置 %}

- 这样，我们再访问网站根目录的时候就会得到网站首页

{% asset_img 966aca0735fae6cd3cb8e21b0db30f2442a70f78.jpg Django教程：[7]网站根目录的设置 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
