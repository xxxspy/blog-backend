---
title: SPSS实例：[23]如何对数据进行排序
date: 2016-10-19 18:05:17
tags: [spss]
author: mlln.cn
---
我们今天来学习一个简单的功能，在spss中如何对数据进行排序，虽然简单，但是很重要。我刚才处理的数据是从Excel中导入的，接着还有其他Excel中的数据要粘贴到spss中，我需要先让spss中的数据按照年级、专业排序，然后才能保证粘贴数据的时候能够按照年级和专业的顺序去粘贴，下面我们来看看如何排序吧。

- 在菜单中执行：data-sort cases，打开排序对话框

{% asset_img 58af236d55fbb2fb93e62b704d4a20a44723dc40.jpg SPSS实例：[23]如何对数据进行排序 %}

- 我们想要让spss按照年级排序，当case与case的年级相同的时候，按照专业进行排序，如图所示，将年级和专业按照先后顺序放入sort by框中

{% asset_img bf487563f6246b60eed4c116e9f81a4c500fa2bf.jpg SPSS实例：[23]如何对数据进行排序 %}

- 设置排序的方式是【升序】，如图所示，选择ascending，相反你可以选择desceding来降序

{% asset_img 7787b9efce1b9d16d51fe903f1deb48f8d5464bc.jpg SPSS实例：[23]如何对数据进行排序 %}

- 接着，我们其实可以点击ok来完成排序，但是没用一次spss就看一下它的syntax是非常好的习惯，这样你很快就能学会基本的syntax操作，学会syntax好处就是你比别人处理数据的速度大大提升，十倍百倍的速度提升，点击paste可以看到syntax

{% asset_img b5ce925494eef01f15cc6ba7e2fe9925bd317dbc.jpg SPSS实例：[23]如何对数据进行排序 %}

- 你看到了，其实只需要用两句简单的代码就能实现排序的功能

{% asset_img 95afee1f3a292df5d11bdf77be315c6035a873bc.jpg SPSS实例：[23]如何对数据进行排序 %}

- 我们还是回到界面中，点击ok

{% asset_img 9864a2315c6034a8683acbe3c9134954082376bc.jpg SPSS实例：[23]如何对数据进行排序 %}

- 排序好了以后，你最好保存一下结果

{% asset_img 5f9e93b1cb13495433c69b06544e9258d0094abc.jpg SPSS实例：[23]如何对数据进行排序 %}

- 现在的数据就是按照年级和专业进行的排序，你学会了吗？请关注我的系列教程：spss实例教程，你将看到一个专业的数据分析员是如何在工作中使用spss的。

{% asset_img d019d2bf6c81800a5c3dfa6cb33533fa838b47bc.jpg SPSS实例：[23]如何对数据进行排序 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
