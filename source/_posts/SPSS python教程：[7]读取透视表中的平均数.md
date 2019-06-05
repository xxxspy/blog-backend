---
title: SPSS python教程：[7]读取透视表中的平均数
date: 2016-10-11 18:17:11
tags: [python,spss]
author: mlln.cn
---
由于经常有人问怎么将数据中心化，笨方法就是手工去算，但是我打算用点高级的东西，从描述性统计的输出的透视表中，读取平均数，然后再用变量的每一个值减去平均数。这篇文章介绍一下最关键的一个步骤，那就是从输出的描述性统计中读取平均数。

- 先看一下所有的代码。然后我们再逐步解释

{% asset_img f677b1c379310a5540f30c74b54543a983261018.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- 首先是BEGIN PROGRAM和END PROGRAM,这两者之间插入python代码，也就是说python代码必须在这两者之间才能正确执行，之前有讲过

{% asset_img 245e8bcad1c8a7867b2d978e6509c93d71cf50e8.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- 装载spss和apssaux模块，spss模块很熟悉，但是spssaux模块是一个附加模块，在帮助文件中，没有关于它的，只能去自己搜索了。或者在python中使用help(spssaux)

{% asset_img f392492c11dfa9eca8f8849760d0f703908fc119.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- fpath中保存数据文件路径

{% asset_img 6391e903918fa0ec2011b68d249759ee3c6ddb19.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- spss打开该数据文件，注意这里用到了一些syntax命令，这些都是基本的。如果你不会写syntax也无妨，你可以在spss中手动操作一下，得到描述性统计，在结果输出文档中，就能看到用到的syntax，你再将其粘贴过来就可以了。

{% asset_img b7bc4c66d01609247d227f9bd60735fae7cd34e8.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- 然后cmd中存有进行描述性统计的syntax命令

{% asset_img d5462bfae6cd7b89426be7030d2442a7d8330ee8.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- spssaux.createxmloutput将执行cmd命令，然后将结果保存在xml工作空间中，可以设置visible为True来看到输出结果

{% asset_img 476217f79052982245e5eb43d5ca7bcb0b46d419.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- 读取透视表中的的某个以数值，注意观察参数，对照着透视表你就能理解了。

{% asset_img 6a2112338744ebf85ea7b6bfdbf9d72a6159a719.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- 最后将读取得到的平均数值打印出来，成功！

{% asset_img a54e55fbfbedab64ef759040f536afc378311ee8.jpg SPSS python教程：[7]读取透视表中的平均数 %}

- 最近在进行spss的自动化处理数据，有兴趣的可以联系我。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
