---
title: SPSS实例：[2]卡方检验百分比差异
date: 2016-10-23 18:19:15
tags: [spss]
author: mlln.cn
---
今天讲的卡方检验只是多种卡方检验中的一种，你还看一去看我最新的几篇文章讲分层卡方、相关样本卡方、kappa一致性系数等，这里【http://jingyan.baidu.com/season/33651?pn=26】

- 第一步是录入数据，我们录入数据的方式如下图：class是分组变量，0值代表A组，1代表B组，effect是是否敏感变量，0代表不敏感，1代表敏感，num是频次，也就是各个组的个案数目。你可以比对上面的交叉表来看看spss数据结构

{% asset_img 5beeba0f4bfbfbed4aedf0be79f0f736aec31f78.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 接着，我们要对数据进行加权，很多人问为什么要加权，实际上我们采用上图所示的数据结构就决定了我们必须用频次进行加权，这样可以让上面的那种数据结构表示呈交叉表。如果没有加权的话，会出现错误，我们待会会看到一个错误的结果，就是没有加权的结果。加权的方法是data--weight cases

{% asset_img 2f9cbdcc7cd98d10692ecaf0203fb80e7aec903e.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 将频次放入变量框，然后点击ok按钮，加权成成功

{% asset_img 3790312eb9389b503d0526938435e5dde6116e3e.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 接着在菜单栏上执行：analyse--descriptive statistics--crosstabs，打开交叉表对话框

{% asset_img 08b68e529822720e2134243b7acb0a46f31fab3e.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 在这个对话框中，我们需要将行和列变量放入各自的框中，注意看行和列变量不要弄颠倒了，回顾上面的数据结构，你自己对比一下，哪一个是行变量

{% asset_img 8759287adab44aedd3fa7825b21c8701a08bfb79.jpg SPSS实例：[2]卡方检验百分比差异 %}

{% asset_img 263e802f0708283818ba1ad5b999a9014d08f179.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 点击statistic按钮，设置卡方统计量

{% asset_img 246cca2a2834349b41fca844c8ea15ce37d3be3e.jpg SPSS实例：[2]卡方检验百分比差异 %}

{% asset_img b74124f33a87e95079ed35ad11385343faf2b43e.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 点击cells按钮，选择输出的参数

{% asset_img 62667cd0f703918fbc66fb0b503d269758eec479.jpg SPSS实例：[2]卡方检验百分比差异 %}

{% asset_img 3c2c4bfbb2fb431648a8bcbb21a4462308f7d379.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 最后出现的是卡方检验的结果了，第一个表格是交叉表，显示了期望值和实际值

{% asset_img 246cca2a2834349b41b1a844c8ea15ce37d3be79.jpg SPSS实例：[2]卡方检验百分比差异 %}

- 接着是卡方检验表，这是最关键的结果。我们根据样本量的大小来决定看哪一行的指标

- 假如我们的总样本数N》40且交叉表中每一个cells中频数均大于5，卡方检验的结果是精确的，可以参考第一行的指标，也就是pearson-chi-square（显然我们的案例满足这个条件）sig值小于.05，说明差异显著，说明两组病人对药物的反应是不同的；假如样本总量N<40，或者cells中有一个频数小于5，我们只能看校正后的卡方值，也就是第二行数据，或者我们看fisher精确概率法获得的值，也就是第四行，这两行都得到了显著的结果；

{% asset_img 3bb22487e950352a8bd6e3c95243fbf2b3118b79.jpg SPSS实例：[2]卡方检验百分比差异 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
