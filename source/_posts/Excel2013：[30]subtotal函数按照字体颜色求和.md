---
title: Excel2013：[30]subtotal函数按照字体颜色求和
date: 2016-04-03 18:19:05
tags: [excel]
author: mlln.cn
---
给别人做数据，别人的数据经常是五颜六色的，为了突出某些数据，我们经常使用各种字体颜色，那么我们突然想要知道某种颜色的数字之和，怎么办？或者想知道他们的平均数怎么办？下面介绍一下SUBTOTAL函数的用法，看完你就知道如何根据字体颜色来求各种数。

- 这里有一列数据，你可以看到红色字体，我现在想要知道红色字体的和，选中数据如图所示

{% asset_img d019d2bf6c81800a44429275b33533fa838b47e2.jpg Excel2013：[30]subtotal函数按照字体颜色求和 %}

- 在【数据】菜单下，我们点击【筛选】

{% asset_img 6dc09e0a19d8bc3eeeaf1db1808ba61ea9d345e2.jpg Excel2013：[30]subtotal函数按照字体颜色求和 %}

- 你可以看到这个下拉箭头，我们打开它的下拉菜单

{% asset_img 373bc4b44aed2e7349259d578501a18b86d6faba.jpg Excel2013：[30]subtotal函数按照字体颜色求和 %}

- 菜单中有一个选项是【按颜色筛选】，好的，选择它，然后在次级菜单中选择红色

{% asset_img 4075890a304e251ffc50ff83a586c9177e3e53e2.jpg Excel2013：[30]subtotal函数按照字体颜色求和 %}

- 接着，我们随便找一个存放总数的单元格，我们输入公式=SUBTOTAL(，这时候你会看到一个下拉菜单提示你可选参数，因为我们要求和，所以我们使用第九个参数9，然后输入一个逗号，再选择求和的区域

{% asset_img 263e802f07082838d4c1c76fba99a9014d08f1ba.jpg Excel2013：[30]subtotal函数按照字体颜色求和 %}

- 最后输入的公式是这样的：

{% asset_img 38403f3fb80e7bec650e189a2d2eb9389a506bb1.jpg Excel2013：[30]subtotal函数按照字体颜色求和 %}

- 最后看到了吧，总数是不是正确呀。

{% asset_img 1e71f724b899a90183f9404d1f950a7b0308f5ba.jpg Excel2013：[30]subtotal函数按照字体颜色求和 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
