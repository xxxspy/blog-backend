---
title: SPSS实例：[21]调节效应检验方法
date: 2016-01-15 18:17:11
tags: [spss]
author: mlln.cn
---
经常给人做数据分析，似乎大家遇到的一个瓶颈就是调节效应怎么做，我也不怕砸自己的饭碗，就将方法分享给大家，希望大家受用。

- 在spss中，打开线性回归的菜单，如图所示

{% asset_img 3853ad1bb051f819fde94644d8b44aed2f73e7b5.jpg SPSS实例：[21]调节效应检验方法 %}

- 我们先将因变量【职业探索】、自变量【自我概念】、调节变量【社会支持】放入各自的框框。

{% asset_img a992e31f4134970a15dc552197cad1c8a6865dd5.jpg SPSS实例：[21]调节效应检验方法 %}

- 点击下一层，设置第二个方程

{% asset_img b110e6198618367aa7453ad32c738bd4b21ce5b5.jpg SPSS实例：[21]调节效应检验方法 %}

- 这第二层比第一层增加了一个交互项

{% asset_img 8759287adab44aed5182fbeab11c8701a08bfbb5.jpg SPSS实例：[21]调节效应检验方法 %}

- 点击statistic，设置输出什么参数

{% asset_img a6c7d7177f3e6709e4af00f139c79f3df9dc55d5.jpg SPSS实例：[21]调节效应检验方法 %}

- 一定要选择R方改变量，点击continue，然后点击ok

{% asset_img c856613e6709c93d5e5d4bf99d3df8dcd00054d5.jpg SPSS实例：[21]调节效应检验方法 %}

{% asset_img 310f3b1f95cad1c88e14b9297d3e6709c83d51d5.jpg SPSS实例：[21]调节效应检验方法 %}

- 我们可以看r方的该变量，第二个方程，sig F change值小于0.05，证明调节效应存在

{% asset_img 6648d73d70cf3bc7afaf88e2d300baa1cc112ad5.jpg SPSS实例：[21]调节效应检验方法 %}

- 我们看输出的结果，第一个红框是系数，也就是前面介绍的abcc'，sig值是他们的显著性水平，交互项系数的sig值小于0.05，说明存在调节效应。

{% asset_img 373bc4b44aed2e730b25c3228501a18b86d6fab5.jpg SPSS实例：[21]调节效应检验方法 %}

{% asset_img b853d6fcc3cec3fdc791e27bd488d43f869427d5.jpg SPSS实例：[21]调节效应检验方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
