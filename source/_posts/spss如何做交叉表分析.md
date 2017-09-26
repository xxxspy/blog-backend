---
title: spss如何做交叉表分析
date: 2015-06-15 18:23:19
tags: [spss]
author: mlln.cn
---
 交叉表分析主要用来检验两个变量之间是否存在关系，或者说是否独立，其零假设为两个变量之间没有关系。我们在实际的工作中，经常用交叉表来分析比例是否相等。比如我们来分析一下，不同的性别对不同的报纸的选择有什么不同，就是要用交叉表分析了，下面是具体的方法。
方法/步骤


- 在spss中打开数据，然后依次打开：analyze--descriptive--crosstabs，打开交叉表对话框

{% asset_img 7dd98d1001e939013903dcb17bec54e736d1963f.jpg spss如何做交叉表分析 %}

- 将性别放到行列表，将对读物的选择变量放到列，这样就构成了一个交叉表

{% asset_img 4ec2d5628535e5ddc32df45076c6a7efce1b623f.jpg spss如何做交叉表分析 %}

- 接下来我们要设置输出的结果，点击statistics，打开一个新的对话框

{% asset_img 8435e5dde71190ef50fac350ce1b9d16fdfa603f.jpg spss如何做交叉表分析 %}

- 勾选chi-square（卡方检验），勾选phi and cramer's V（衡量交互分析中两个变量关系强度的指标），点击continue，回到交叉表对话框

{% asset_img b812c8fcc3cec3fd9b5bf6fad688d43f869427d3.jpg spss如何做交叉表分析 %}

- 点击cells，设置cell中要展示的数据

{% asset_img f2deb48f8c5494eec0235e962df5e0fe99257e3f.jpg spss如何做交叉表分析 %}

- 在这里勾选observed（各单元格的观测次数），勾选row（行单元格的百分比），点击continue，回到交叉表对话框

{% asset_img 8694a4c27d1ed21b61ac7f6aad6eddc450da3fd3.jpg spss如何做交叉表分析 %}

- 点击ok按钮，输出检验结果

{% asset_img e1fe9925bc315c6003943a608db1cb134954773f.jpg spss如何做交叉表分析 %}

- 先看到的第一个表格就是交叉表，性别为行、选择的读物为列

{% asset_img 9825bc315c6034a866e3e90ecb1349540923763f.jpg spss如何做交叉表分析 %}

- 卡方检验结果：我们主要是看pearson卡方检验，sig值小于0.05，因此我们认为不同的性别的人对周末读物的选择有显著的差别

{% asset_img bd315c6034a85edfb48dafac49540923dd54753f.jpg spss如何做交叉表分析 %}

- 最后一个表格，输出的是phi值和V值，两个都是代表两个变量之间的关系的紧密度的，数值小于0.1说明关系不紧密，即性别与周末读物的选择没有明显的关系，这个结论和上面的卡方检验有出入，所以我们需要进一步进行两两比较。

-  

-  

{% asset_img 4d086e061d950a7bbe531e4b0ad162d9f3d3c9df.jpg spss如何做交叉表分析 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
