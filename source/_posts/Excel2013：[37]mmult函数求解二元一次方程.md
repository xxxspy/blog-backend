---
title: Excel2013：[37]mmult函数求解二元一次方程
date: 2015-01-11 18:19:23
tags: [excel]
author: mlln.cn
---
已知一个二元一次方程，怎样求出方程的解？我们可以规划求解，也可以使用矩阵函数，这里就用mmult函数求解二元一次方程，还用到的辅助函数MINVERSE，下面看看具体的求解过程吧。

- 已知条件是两个方程，我们需要进行调整，使方程的形式如图所示，常数项在等号的右边，未知数在等号的左边，且未知数XY的顺序是一致的。

{% asset_img a28d62d98d1001e95c5dd76aba0e7bec54e79737.jpg Excel2013：[37]mmult函数求解二元一次方程 %}

- 建立一个表格，我们整理一下各个系数和常数，如图所示，注意它是如何同方程一一对应的

{% asset_img 8759287adab44aedd7427d81b11c8701a18bfb0d.jpg Excel2013：[37]mmult函数求解二元一次方程 %}

- 在解这一栏，我们选中这两个单元格，注意是两个啊哦！

{% asset_img 2e6fa7389b504fc2ba3e7360e7dde71190ef6d37.jpg Excel2013：[37]mmult函数求解二元一次方程 %}

- 在公式栏输入公式=MMULT(MINVERSE(A8:B9),C8:C9)，注意两个参数A8：B9 和C8：C9代表那两个区域

{% asset_img 62667cd0f703918fb8defeaf533d269759eec40d.jpg Excel2013：[37]mmult函数求解二元一次方程 %}

- 按下Ctrl+shift+回车键，这样就得到了公式的解

{% asset_img d56b3634349b033b64873fbf17ce36d3d539bd0d.jpg Excel2013：[37]mmult函数求解二元一次方程 %}

- 你可以验证一下，这个解是不是正确，将求得的解带入方程，看等式是否成立

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
