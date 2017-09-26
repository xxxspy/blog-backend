---
title: Django教程：[4]制作第一个网页
date: 2016-10-23 18:19:01
tags: [django]
author: mlln.cn
---
通过前面的三篇文章，我们现在已经有能力创建一个网页了。Django就是那么的有效率。我们创建第一个页面的目的是让你理解Django是如何工作的。不信往下看。进行下面的教程之前，如果你没有看我以前写的文章，可能会有疑惑。我前面的文章创建了一个站点djangoweb文件夹，下面要用到

- 第一步要在我们创建的站点文件夹下面新建一个view.py文件，如图所示。当然你创建文件的名称是任意的，你可以叫别的名字。但是要跟后面要写的代码一致，后面还会用到view.py，如果你的文件名不是view，后面你需要做出相应的调整

{% asset_img b3508d13b07eca80277f099d932397dda1448316.jpg Django教程：[4]制作第一个网页 %}

- 我们将该文件写入代码：如图所示。代码的意义是，首先引入HttpResponse类，后面我们会详细介绍这个类，现在我们只知道它用于返回网页中显示的代码。接着我们定义了一个名为hello的函数，它有一个参数为req，这个参数是django.http.HttpRequest的一个实例，我们暂时用不到这个参数，但是它却是一个必须的参数，参数的名称可以任意。hello函数它仅仅返回一个HttpResponse对象，这个对象包含了文本“Hello world”

{% asset_img d8b8c92a6059252df86d2d7e369b033b5bb5b916.jpg Django教程：[4]制作第一个网页 %}

- 现在保存好这个view文件

{% asset_img 148f28d3d539b6000cb43fcdeb50352ac65cb716.jpg Django教程：[4]制作第一个网页 %}

- 接下来我们需要修改urls.py文件，这个文件可以将url和调用的函数对应起来。比如，我想当我在浏览器地址栏输入http://127.0.0.1:8001/hello/的时候就能调用view.hello方法，那么我们必须在urls.py中进行添加

{% asset_img 8b527d2762d0f7039674a6a60afa513d2797c542.jpg Django教程：[4]制作第一个网页 %}

- 首先要引用我们企图调用的方法，然后在urlpatterns中添加url(r'^hello/$',hello),；注意最后面的逗号不能省略。这个代码就是将url同调用的函数联系起来。

{% asset_img 0db2c9ca7bcb0a46efc6b8436963f6246a60afa0.jpg Django教程：[4]制作第一个网页 %}

- 最后，我们在dos下开启开发服务器，如果你还不知道如何开启开发服务器，你需要看下面的参考资料里的传送门。

{% asset_img 08b68e529822720e1677d28079cb0a46f31fabcb.jpg Django教程：[4]制作第一个网页 %}

- 打开浏览器，地址栏输入地址：127.0.0.1:8001/hello/，你就会看到我们制作的第一个页面了。你学会了吗？

{% asset_img 21e5582309f7905280a677440ef3d7ca7acbd5cb.jpg Django教程：[4]制作第一个网页 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
