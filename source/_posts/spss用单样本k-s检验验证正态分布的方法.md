---
title: spss用单样本k-s检验验证正态分布的方法
date: 2016-09-05 18:03:15
tags: [spss]
author: mlln.cn
---
 k-s检验是用来检验数据是否符合正态分布的，因为在检验之前我们并不知道该数据是否符合正态分布，所以这种检验属于非参数检验。对要检验的数据也没有限制，只要数据量够大就可以，数据量偏少会造成检验不准确。下面来具体介绍k-s检验的过程和结果分析。
方法/步骤


-  在spss中打开数据，怎么打开就不介绍了，打开数据以后，在菜单栏上执行：analyze--非参检验--legacy disalogs--1 sample k-s

-  

{% asset_img d439b6003af33a87c56f04ebc65c10385243b5c4.jpg spss用单样本k-s检验验证正态分布的方法 %}

- 将你要检验正态的变量放到test variables list，勾选下面的normal，这是正态的意思。

{% asset_img adaf2edda3cc7cd9c51530283901213fb80e9102.jpg spss用单样本k-s检验验证正态分布的方法 %}

- 点击exact，进入选择检验方法的对话框

{% asset_img a2cc7cd98d1001e9730410feb80e7bec54e79702.jpg spss用单样本k-s检验验证正态分布的方法 %}

- 这里有三个选项可以选择，第一个asymptotic的意思是基于渐进分布的显著性水平的检验指标，适于大样本，如果样本过小或者分布不好，就会影响检验的效力；monte carlo适用于精确显著性水平的无偏估计，如果样本过大，数据处理过程太长，就应该使用这个选项；exact精确计算概率值，可以设定数据处理的时间，如果数据处理时间超过了你设定时间30分钟，就应该使用monte carlo

-  

{% asset_img e850352ac65c1038637cca33b2119313b17e89c4.jpg spss用单样本k-s检验验证正态分布的方法 %}

- 回到k-s检验对话框，点击options按钮，设置输出的参数

{% asset_img 3801213fb80e7bec1ae207102f2eb9389b506b02.jpg spss用单样本k-s检验验证正态分布的方法 %}

- 勾选descriptive和quartiles，这两个的意思分别是输出描述性统计和四分位数，点击continue按钮

{% asset_img 5243fbf2b21193138441fb4165380cd790238dc4.jpg spss用单样本k-s检验验证正态分布的方法 %}

- 我们可以看到对数据的检验结果，最后的显著性检验值为0.000，非常显著。我们首先要知道在做显著性检验的时候虚无假设是数据符合正态分布，因为检验显著，所以否定虚无假设，所以数据是不符合显著性的要求的。

{% asset_img 7aec54e736d12f2ee83daa914fc2d56285356802.jpg spss用单样本k-s检验验证正态分布的方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
