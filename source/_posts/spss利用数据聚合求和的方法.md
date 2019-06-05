---
title: spss利用数据聚合求和的方法
date: 2015-10-23 18:19:15
tags: [spss]
author: mlln.cn
---
 有时候我们拿到的数据是不规范的，比如从数据库中直接导出的数据就是。我们举个例子，每个记者每发一篇文章就会增加一条记录，在统计每个月的工作绩效的时候，需要统计每个记者到底发了多少稿件，我们就用到了数据聚合aggregate。
方法/步骤


-  打开数据以后，我们在菜单栏上执行：data--aggregate，打开数据聚合对话框

{% asset_img 0824ab18972bd407592d93707b899e510eb30950.jpg spss利用数据聚合求和的方法 %}

- 将记者姓名放到分组变量，然后将稿件数量和字数都放到聚合变量里，这时候你看到了，系统默认是求均值，我们要求的其实是总和，所以，先选中其中一个变量，比如选中稿件数量，然后点击function

{% asset_img 7dd98d1001e9390126a9cdb37bec54e737d19697.jpg spss利用数据聚合求和的方法 %}

- 在打开的function对话框中，勾选sum，然后点击continue，这样就将均值转换成了求和

{% asset_img 203fb80e7bec54e73d475a93b9389b504ec26a97.jpg spss利用数据聚合求和的方法 %}

- 同样的方法，勾选字数，点击function按钮

{% asset_img 43a7d933c895d143db9ca4ae73f082025baf0750.jpg spss利用数据聚合求和的方法 %}

- 勾选sum，然后点击continue，返回数据聚合对话框

{% asset_img 203fb80e7bec54e73d475a93b9389b504ec26a97.jpg spss利用数据聚合求和的方法 %}

- 这时候我们所有的设置已经基本完成，点击ok即可开始转换数据

{% asset_img c995d143ad4bd1130b27f7bf5aafa40f4afb0550.jpg spss利用数据聚合求和的方法 %}

- 最后看到数据结果了，最后生成了两列变量，分别求出了每个记者的稿件数量和字数总数

-  

{% asset_img 72f082025aafa40f372c8e50ab64034f79f01950.jpg spss利用数据聚合求和的方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
