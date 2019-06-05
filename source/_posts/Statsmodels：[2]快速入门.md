---
title: Statsmodels：[2]快速入门
date: 2015-03-11 18:15:23
tags: [statsmodels]
author: mlln.cn
---
这是Python.statsmodels系列文章的第二篇，为了让大家快速入门，理解statsmodels工作的整个过程，我找到了一个很好的例子，在这里介绍给大家。下面我们来一步步介绍这个例子。

- 引入相关模块，pandas主要用到了他的DataFrame，sm用到了回归分析，patsy.dmatrices用于生成design matrix

{% asset_img 7a8a1446f21fbe09d996846668600c338644adbd.jpg Statsmodels：[2]快速入门 %}

- 先获取数据，本例子用到的数据保存在网上的csv文件，我们可以使用pandas.read_csv方便的读取数据（url='http://vincentarelbundock.github.com/Rdatasets/csv/HistData/Guerry.csv'）

{% asset_img 6a22e8246b600c3331b199ba194c510fd8f9a1bd.jpg Statsmodels：[2]快速入门 %}

- 查看一下数据的前五行，有很多列，显示有点混乱

{% asset_img eab9044c510fd9f96cdf121b262dd42a2934a4bd.jpg Statsmodels：[2]快速入门 %}

{% asset_img b25d9901a18b87d6a669ed6d040828381f30fd5e.jpg Statsmodels：[2]快速入门 %}

- 下面筛选出我们需要的列：
这是最后得到的数据：

{% asset_img 246cca2a2834349bc2ce29f7caea15ce37d3bebd.jpg Statsmodels：[2]快速入门 %}

{% asset_img 91ae68c6a7efce1b67e38fb8ac51f3deb58f65bd.jpg Statsmodels：[2]快速入门 %}

- 由于最后一行有NaN值，所以需要使用dropna删除该行数据

{% asset_img 718e25c79f3df8dcff16c9e3ce11728b4710285d.jpg Statsmodels：[2]快速入门 %}

- 生成design matrix，我们建立的模型是y=BX，因此需要分别求得y和X矩阵，而dmatrices就是干这个的
这是y
这是X矩阵：我们会发现分类变量自动的转换成了哑变量

{% asset_img 3792cb39b6003af3f3729b12362ac65c1138b6bd.jpg Statsmodels：[2]快速入门 %}

{% asset_img b5ce925494eef01f38df5fb7e3fe9925bd317dbd.jpg Statsmodels：[2]快速入门 %}

{% asset_img 109eb7ec8a136327f5c68441928fa0ec08fac75e.jpg Statsmodels：[2]快速入门 %}

- OLS指的是一般最小二乘，fit方法对回归方程进行估计，summary保存着计算的结果
这是输出的模型的估计结果：

{% asset_img a583631ed21b0ef45bc3de2cdec451da81cb3e5d.jpg Statsmodels：[2]快速入门 %}

{% asset_img 27d647ee3d6d55fb13ed30546e224f4a20a4dd5e.jpg Statsmodels：[2]快速入门 %}

{% asset_img 4e0b3ea4462309f73844eb60710e0cf3d7cad65e.jpg Statsmodels：[2]快速入门 %}

- 现在我们要进一步检验数据是不是适合使用OLS，我们暂且先检验一下数据是否为线性，虚无假设是线性的，采用Rainbow test
输出结果为：第一个为F值，第二个为P值，显然未能拒绝虚无假设

{% asset_img 0e655ca7d933c8958755de09d21373f08202005d.jpg Statsmodels：[2]快速入门 %}

{% asset_img 6648d73d70cf3bc7b2cb8a9ed200baa1cc112abd.jpg Statsmodels：[2]快速入门 %}

- 接着，我们绘制偏回归线观察数据点是否分布在估计得到的直线的附近（图为控制了Rgion和Literacy后wealth对lottery的回归关系）

{% asset_img b258f5c4b74543a9e830bcbe1d178a82b901145d.jpg Statsmodels：[2]快速入门 %}

{% asset_img b110e6198618367aa3a239af2d738bd4b31ce55e.jpg Statsmodels：[2]快速入门 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
