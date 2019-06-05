---
title: spss利用count计算指定变量值的出现次数
date: 2015-02-15 18:05:03
tags: [spss]
author: mlln.cn
---
 count可以统计频数，并将频数生成一个新的变量，比如说，有10道题是问你是否赞同某个说法，5级评分，分别为：非常赞同、赞同、不知道、反对、非常反对。我们要知道某个人的综合的态度，就要统计出来这个人赞同的数量，用count就可以实现了。
方法/步骤


- 打开数据以后，在菜单栏上执行：transform--count ，打开count对话框

{% asset_img c2fdfc039245d688d4db4928a4c27d1ed31b2464.jpg spss利用count计算指定变量值的出现次数 %}

- 在打开的对话框中，在目标变量中输入态度，并将填写变量的标签，将要统计的态度a1--a10都添加到numeric variables

{% asset_img 9345d688d43f8794a5e2b2a2d21b0ef41bd53a18.jpg spss利用count计算指定变量值的出现次数 %}

- 点击define value，对变量进行条件限制

{% asset_img 9345d688d43f8794a626b3a2d21b0ef41ad53a64.jpg spss利用count计算指定变量值的出现次数 %}

- 勾选range这个选项，然后在两个文本框中分别输入1和2，也就是限定了分数的范围是1到2，然后点击continue

{% asset_img d53f8794a4c27d1ed13bc1481bd5ad6eddc43818.jpg spss利用count计算指定变量值的出现次数 %}

- 返回到了count对话框，点击ok按钮，运行

{% asset_img a5c27d1ed21b0ef41ef562d2ddc451da81cb3e18.jpg spss利用count计算指定变量值的出现次数 %}

- 我们看到这里已经多了一个态度变量

{% asset_img d31b0ef41bd5ad6ed5209f6681cb39dbb7fd3c64.jpg spss利用count计算指定变量值的出现次数 %}

- 最后在菜单栏上执行：analyze--descriptive statistic--frequencies，对不同态度进行统计

-  

{% asset_img dcc451da81cb39dbbddd9ddad0160924ab183018.jpg spss利用count计算指定变量值的出现次数 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
