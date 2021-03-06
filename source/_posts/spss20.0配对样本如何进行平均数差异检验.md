---
title: spss20.0配对样本如何进行平均数差异检验
date: 2015-09-03 18:01:15
tags: [spss]
author: mlln.cn
---
用这个方法之前先要确定你的数据是否适用于配对样本t检验，一般这样的数据来自同一个人，但是是分两次测量得到的，或者虽然是来自两个人，但是他们是经过匹配的，可以认为两个人在研究的变量上没有差异。
方法/步骤


-  打开spss导入数据，然后在菜单栏上执行：analyse--compare means--paired samples t test

{% asset_img 29381f30e924b8996cf21bbd6e061d950b7bf66d.jpg spss20.0配对样本如何进行平均数差异检验 %}

- 你会看到如下所示的对话框，这里我们要看好了怎么对变量进行配对，先从左侧的列表里选择一个变量，比如选择triglyceride这个变量，点击如图所示的箭头，添加到右侧的列表

{% asset_img 6f061d950a7b0208b0075d6462d9f2d3562cc86d.jpg spss20.0配对样本如何进行平均数差异检验 %}

- 接下来找到与上面的那个变量相配对的另一个变量final triglyceride，添加到variable2

{% asset_img 060828381f30e9247c62feb44c086e061c95f775.jpg spss20.0配对样本如何进行平均数差异检验 %}

- 同样的方法，把体重这个配对变量放到配对变量列表

{% asset_img 63d0f703918fa0ecd0090688269759ee3c6ddb6d.jpg spss20.0配对样本如何进行平均数差异检验 %}

- 点击ok按钮，开始进行数据处理

{% asset_img 03087bf40ad162d93c28009911dfa9ec8b13cd75.jpg spss20.0配对样本如何进行平均数差异检验 %}

- 你会看到下面的这个统计结果，先来分析第一个表格，关键的数据是均值，你会看到triglyceride这个变量前后的值的变化，从138到124大概下降了14，这是大概的一个数字，并不能说明这个差值是有效的

{% asset_img 279759ee3d6d55fb6c0814a36d224f4a21a4dd6d.jpg spss20.0配对样本如何进行平均数差异检验 %}

- 第二个表格展示的是配对样本之间的相关系数，我们可以看到体重的相关系数为0.996，而且sig值达到了0.000，这是一个非常完美的数据，这说明实验处理对体重的影响是一致的。但是上面的这对变量却没有显示出相关关系。

{% asset_img a8ec8a13632762d022f8c63aa0ec08fa503dc675.jpg spss20.0配对样本如何进行平均数差异检验 %}

- 最后我们要看第三个表格，先看均值的差异表明实验前后数据发生了变化，而后面的sig值则说明这个变化是否有效，因为第一个sig值超过了0.05，所以结果是不显著的，不能认为实验是有效的。而第二个sig为0.000，这说明实验的处理效果显著，可以认为该处理方法能够有效的减轻体重

-  

{% asset_img 908fa0ec08fa513dfc6c0e5b3d6d55fbb3fbd975.jpg spss20.0配对样本如何进行平均数差异检验 %}

{% asset_img 21a4462309f790527ed125bb0cf3d7ca7acbd56d.jpg spss20.0配对样本如何进行平均数差异检验 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
