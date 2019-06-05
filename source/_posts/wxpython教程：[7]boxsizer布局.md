---
title: wxpython教程：[7]boxsizer布局
date: 2016-05-03 18:19:17
tags: [python,wxpython]
author: mlln.cn
---
今天我们说一下使用boxsizer进行布局的方法，这种布局方式更适合制作有很多不同种类控件的界面。boxsizer分为横向和纵向两种，如果你想要把控件水平排列，就使用横向boxsizer，如果你想让控件都垂直排列，就使用纵向boxsizer，当然很多界面既有横向排列又有纵向排列的控件，我们就可以使用boxsizer的嵌套。

- 这是我们今天用到的第一部分代码，你运行它的话就可以看到一个界面，有一个标签和文本框，他们是水平排列的。下面我们逐句解释。

{% asset_img f76575600c3387447d6a8929520fd9f9d62aa0fd.jpg wxpython教程：[7]boxsizer布局 %}

- 这三句话很简单，首先创建了一个panel面板，然后创建一个纵向box，最后创建一个横向box，我们的目的是创建一个既有横向排列的控件又有纵向排列的控件，所以先创建两个不同box，然后再让他们嵌套起来。

{% asset_img 5202e5f2b211931301af59e566380cd790238dbc.jpg wxpython教程：[7]boxsizer布局 %}

- 创建一个标签，然后将标签添加到hbox1当中。flag和border结合使用，border是边框的宽度，flag表明哪一个边框。proportion是比例的意思，假如在一个横向box中有两个控件，两个控件的proportion相等，那么Frame大小改变的时候，两个控件大小保持相同。如果proportion=0，那么大小不变。
flag可以用的值有：

{% asset_img 310f3b1f95cad1c8a2455a727c3e6709c83d51ad.jpg wxpython教程：[7]boxsizer布局 %}

{% asset_img 6648d73d70cf3bc794a66cb9d200baa1cc112a85.jpg wxpython教程：[7]boxsizer布局 %}

- 再向hbox1中添加一个文本框控件，注意proportion

{% asset_img a1ad16fa513d26972434a90856fbb2fb4216d845.jpg wxpython教程：[7]boxsizer布局 %}

- 最后是将横向文本框嵌套于纵向文本框。可以设置边框。目前我们还看不到为什么要做这样一个嵌套，因为控件还很少，仅有的两个控件是水平排列的。如果我们想再增加几个控件，并且控件位于这两个控件下方，我们就需要再创建一个横向box，并将横向box添加到纵向box中。

{% asset_img 3790312eb9389b50818940078635e5dde7116e36.jpg wxpython教程：[7]boxsizer布局 %}

- 代码的最后是配置box：如果没有该命令，我们之前设置的sizer都是不起作用的

{% asset_img a75fb6d3fd1f41346997a52b261f95cad0c85e80.jpg wxpython教程：[7]boxsizer布局 %}

- 这是最后完成的效果：

{% asset_img 48151723dd54564e7e76476cb0de9c82d1584f11.jpg wxpython教程：[7]boxsizer布局 %}

- 下面我们再添加2个横向的box，并且其中增加—个控件

{% asset_img 58c3acb7d0a20cf488945c8a75094b36acaf9924.jpg wxpython教程：[7]boxsizer布局 %}

- 最终的全部代码：

{% asset_img a1ad16fa513d26972387aa0856fbb2fb4216d8d4.jpg wxpython教程：[7]boxsizer布局 %}

- 生成的界面：

{% asset_img d56b3634349b033bc6d85e8f16ce36d3d439bdd0.jpg wxpython教程：[7]boxsizer布局 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
