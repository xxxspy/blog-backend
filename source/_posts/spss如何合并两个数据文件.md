---
title: spss如何合并两个数据文件
date: 2015-04-03 18:19:23
tags: [spss]
author: mlln.cn
---
spss录入数据是个非常繁琐的事情，所以我们经常会几个人同时录入，然后将录入的数据进行合并，这里介绍的经验就是如何合并两个数据文件，有时候两个文件是完全相同的，有一样的变量，有时候是有差别的，这时候就看你需要文件如何合并了。
方法/步骤


- 我们先要在数据库中打开第一个数据文件，在菜单栏上执行：file--open--data

{% asset_img cf1b9d16fdfaaf51fd3836328c5494eef11f7a67.jpg spss如何合并两个数据文件 %}

- 通过浏览窗口，打开第一个数据网文件以后，我们来合并第二个数据文件，在菜单栏上执行：data--merge file--add cases

{% asset_img 7e3e6709c93d70cf060b1d80f8dcd100bba12b4d.jpg spss如何合并两个数据文件 %}

- 打开合并文件对话框，点击浏览按钮，找到你要合并的第二个数据文件

{% asset_img fcfaaf51f3deb48f9cb21653f01f3a292cf57867.jpg spss如何合并两个数据文件 %}

- 点击open按钮，返回数据合并对话框

{% asset_img b58f8c5494eef01f29cfaf48e0fe9925bd317d67.jpg spss如何合并两个数据文件 %}

- 在这里检查一下要合并的文件，如何确认无误，点击continue，继续

{% asset_img 9e3df8dcd100baa18fddf0364710b912c9fc2e4d.jpg spss如何合并两个数据文件 %}

- 看到这个对话框了，我们看到右侧的列表是相同的变量，也就是两个数据文件有相同的变量，左侧的列表是只有一个数据文件中有的变量，右边标有 * 号 的为第一个数据文件中有二第二个数据文件没有的变量，标有+号的是第二个数据文件有而第一个数据文件没有的变量，根据你的需要，为了保留数据的所有信息，我们可以将左侧列表里所有的变量都添加到右侧，记住出现在右侧列表里的变量才会被保存下来，左边变量都会被删除

{% asset_img bba1cd11728b4710fcde4a41c3cec3fdfd03234d.jpg spss如何合并两个数据文件 %}

- 使用shift键选中所有的变量，天机添加按钮

{% asset_img cc11728b4710b9128e304173c3fdfc039345224d.jpg spss如何合并两个数据文件 %}

- 我们看到这就是合并文件以后的数据了，由于年龄段这个变量只有一个数据文件有，所以另一个数据文件中的数据在这个变量上就是空白的了。

-  

{% asset_img c9fcc3cec3fdfc03d8895435d43f8794a5c2264d.jpg spss如何合并两个数据文件 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
