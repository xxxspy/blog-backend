---
title: spss中k-means聚类的操作方法
date: 2016-02-11 18:19:17
tags: [spss]
author: mlln.cn
---
k-means聚类是聚类方法中的一种，通常我们要预先确定case到底可以分为几类，然后才能进行这个聚类分析。另外，注意查看各个变量的量纲、平均数、方差齐性，如果不满足同质性，需要进行正太化转变，当然，数据要满足正态分布才可以啊哦。
工具/原料


- 这种聚类方法不能自动的计算变量的Z分数，如果数据差异过大，量纲不同，需要进行z分数的转换，下面的操作没有告诉你如何转换z分数，你需要注意

- k-means的聚类的原理是迭代，迭代本身是无限的过程，如果没有命令，计算机就一直迭代下去，这样计算会很慢，所以我们设置一个迭代次数，比如100，那么迭代100次就必须停止。活着spss中有迭代停止的标准

- spss20.0
方法/步骤


- 准备好数据，在菜单栏上执行：analyse--classify--k-means cluster，打开k平均数对话框

{% asset_img f636afc379310a5527e38d21b74543a98326101b.jpg spss中k-means聚类的操作方法 %}

- 将聚类用到的指标变量放入variables，将客户的编码放到label cases by当中，把客户编号作为case的标签

{% asset_img 7c1ed21b0ef41bd5c367ba2151da81cb39db3d2a.jpg spss中k-means聚类的操作方法 %}

- 接着要设置聚类的类别数目，如图所示，这个数目不是随便给的，他有两个来源：要么是你根据工作经验，认为数据分为几类是最合理的；要么是你有前人的研究证明分为几类。

{% asset_img d50735fae6cd7b89e3a368560f2442a7d8330e13.jpg spss中k-means聚类的操作方法 %}

- 在主对话框中，点击iterate按钮，打开迭代对话框

{% asset_img 29381f30e924b8991cff2bed6e061d950b7bf620.jpg spss中k-means聚类的操作方法 %}

- 将最大迭代次数设置为100，下图你看到的默认的迭代次数为10，但是数据量越大，迭代次数就应该越多，所以我们设置为100.点击continue按钮，返回到主对话框。

{% asset_img 902397dda144ad345c32da52d0a20cf430ad8551.jpg spss中k-means聚类的操作方法 %}

- 点击save按钮，因为我们想要保存分类的结果，并将结果保存到一个变量当中

{% asset_img 95eef01f3a292df5cefcf0c0bc315c6034a87323.jpg spss中k-means聚类的操作方法 %}

- 打开一个自对话框，勾选cluster membership，点击continue返回到主对话框

{% asset_img 5bafa40f4bfbfbed216e6aaa78f0f736afc31f2b.jpg spss中k-means聚类的操作方法 %}

- 点击ok，开始运行数据，并输出数据结果

{% asset_img 0eb30f2442a7d93348dbb8a6ad4bd11372f001f7.jpg spss中k-means聚类的操作方法 %}

- 我们看到的第一个表格叫做初始聚类中心，它列出每一个类别初始的中心点，这些中心点都是spss自动生成的。因为case的顺序会影响到中心点的位置，所以我们需要让case的顺序是随机的，有必要的时候要进行随机化处理

{% asset_img 3812b31bb051f819244a5f9fdab44aed2f73e7fc.jpg spss中k-means聚类的操作方法 %}

- 下面的两个表格是迭代过程表，你可以看到每一次迭代中心点的变化值，当中心点的变化小于初始类别中心最小距离的2%的时候，迭代就停止了，你看到的第二幅图在迭代35次以后就停止了迭代

{% asset_img 79f0f736afc379319a9ddafcebc4b74542a91169.jpg spss中k-means聚类的操作方法 %}

{% asset_img 7dd98d1001e939013292d1eb7bec54e737d19656.jpg spss中k-means聚类的操作方法 %}

- 下面这个表格叫做最终聚类中心，也就是各个类别在各个变量上的平均值，它可以帮助我们根据变量的平均值来给分类赋予实际的意义

{% asset_img dcc451da81cb39dbc6cc3883d0160924aa1830d2.jpg spss中k-means聚类的操作方法 %}

- 最后的表格叫做各个类别case数，你可以读出在每一个类别中有多少case

{% asset_img b3b7d0a20cf431adc32d1cec4b36acaf2fdd9863.jpg spss中k-means聚类的操作方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
