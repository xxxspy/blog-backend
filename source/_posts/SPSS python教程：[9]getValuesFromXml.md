---
title: SPSS python教程：[9]getValuesFromXml
date: 2016-04-05 18:23:05
tags: [python,spss]
author: mlln.cn
---
前两篇文章介绍了如何获取透视表中的平均数，现在更深入的探讨一下其中用到的spssaux.GetValuesFromXMLWorkspace方法。在这篇文章中【http://jingyan.baidu.com/article/c275f6bac03a22e33c75674c.html】，可以看到我使用该方法。现在我们具体探讨一下：

- 先看一个数据透视表，想办法获取IAI的平均数

{% asset_img 9304c888d43f8794096a7eafd01b0ef41ad53a5e.jpg SPSS python教程：[9]getValuesFromXml %}

- 我们使用spssaux.GetValuesFromXMLWorkspace，如下图那样写一段代码就能得到IAI的平均数。其中用到了很多参数，下面我们分析一下这些参数都是什么：

{% asset_img 99636c0e0cf3d7ca66ea0ef7f01fbe096a63a9d7.jpg SPSS python教程：[9]getValuesFromXml %}

- 首先是handle参数，它是结果项目的句柄，也就是上面的透视表的句柄。你要从中获取数据。而你怎么知道它的句柄的？是在创建该透视表的时候得到的，具体请看上篇文章【http://jingyan.baidu.com/article/cb5d6105088fe2005d2fe04d.html】

- 其次是tablesubtype参数，我们可以在这里看到透视表的subtype

{% asset_img cc506c8b4710b9126b11c67fc1fdfc039345221b.jpg SPSS python教程：[9]getValuesFromXml %}

- rowcategory参数：行类别，它标识出行坐标，rowcategory="IAI"就表示成下图

{% asset_img 9e7ce6dcd100baa15390743a4510b912c9fc2eb7.jpg SPSS python教程：[9]getValuesFromXml %}

- columncategory参数：列类别，标志出列坐标，colCategory='Mean'可以表示为下图

{% asset_img bf487563f6246b602ece81f5e9f81a4c500fa22b.jpg SPSS python教程：[9]getValuesFromXml %}

- cellAttrib单元格属性：任何一个单元格都有text和number两个属性，我们想要获得text的值就用cellAttrib='text'

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
