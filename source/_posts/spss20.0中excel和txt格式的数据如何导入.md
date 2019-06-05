---
title: spss20.0中excel和txt格式的数据如何导入
date: 2016-08-17 18:03:05
tags: [excel,spss]
author: mlln.cn
---
excel和txt是我们存放数据的两种基本格式，这两种格式不能在spss中直接打开，需要我们进行设置，尤其是txt文件，因为它的数据组织形式很多，spss需要进行更多的设置才能成功导入数据，下面分别介绍了导入excel和txt文件的方法。
方法一：导入excel数据


-  打开spss，然后在菜单栏上执行：file--open--data

{% asset_img 9345d688d43f8794c79d10abd21b0ef41ad53ad0.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 打开open data对话框，选择files type为excel，否则你看不到excel文件

{% asset_img d53f8794a4c27d1eb74463411bd5ad6edcc438d0.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 选中你要导入的excel，然后点击open按钮

{% asset_img f703738da97739122854dde4f8198618377ae2c1.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 因为excel文件中有很多工作表，我们需要选择你要导入的工作表

{% asset_img 80cb39dbb6fd5266bf496491ab18972bd50736d0.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 这接着我们看到这里问你变量名是否包含在excel数据中，假如excel表格中有标题，我们就勾选这个选项，假如表格没有标题，直接就是数据，那么不需要勾选这个选项，点击ok按钮

{% asset_img 38dbb6fd5266d016797bc6ad972bd40734fa35d0.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 我们可以看到数据导入成功，并且变量名设置成了excel的表格的标题

-  

{% asset_img 8718367adab44aed8c3ce661b31c8701a08bfbc1.jpg spss20.0中excel和txt格式的数据如何导入 %}
方法二：导入txt数据


-  打开spss ，在菜单栏上执行：file--open--data

{% asset_img a686c9177f3e6709861a1e7a3bc79f3df8dc5518.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 选择文件类型为text

{% asset_img 9e3df8dcd100baa19b361c3e4710b912c8fc2e18.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 找到要导入的数据，然后点击open按钮

{% asset_img 7af40ad162d9f2d3ef027f6aa9ec8a136327cc20.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 打开一个对话框，先选择是否预先设定的格式，我们没有预定的格式，否则你也不会看到这个文章，勾选no，然后点击next

{% asset_img f3d3572c11dfa9ec313d0d9262d0f703918fc120.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 选择你的变量是如何组织的，我们看看excel中的数据，一个变量和另一个变量中间隔着一个空格，所以我们要选择格式的时候选择第一个【delimited】，任意的一种符号隔开的数据都要选择这个选项

{% asset_img b812c8fcc3cec3fda124fcf0d688d43f87942718.jpg spss20.0中excel和txt格式的数据如何导入 %}

{% asset_img 8b13632762d0f7032ea1ce5908fa513d2697c520.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 接着打开一个对话框，设置你的第一条数据是从第几行开始的，我们刚才看到txt中的数据了，是从第一行开始的，所以填写1

{% asset_img 908fa0ec08fa513de5b9375b3d6d55fbb2fbd920.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 接着你要设置你的数据是如何呈现的，一般就死每一行一个case，也就是txt文件中，一行存放一条数据

{% asset_img d31b0ef41bd5ad6eb5e33f6f81cb39dbb6fd3c18.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 最后选择要导入多少数据，勾选【all of the cases】，意思是导入所有的数据

{% asset_img 38dbb6fd5266d0166603c5ad972bd40735fa3518.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 选择哪个符号将数据隔开了，在本案例中，是空格隔开了数据，所以选择space或者tab

{% asset_img 21a4462309f79052570c1cbb0cf3d7ca7bcbd520.jpg spss20.0中excel和txt格式的数据如何导入 %}

- 最后设定变量的名称，从data preview中选择一个变量，然后在变量名称这一栏填写变量的名称，依此方法给所有的变量都命名，最后点击finish完成数据的导入。

-  

{% asset_img 962bd40735fae6cd0eaef0e40fb30f2442a70f18.jpg spss20.0中excel和txt格式的数据如何导入 %}

{% asset_img 0df3d7ca7bcb0a462731d0bc6b63f6246b60af20.jpg spss20.0中excel和txt格式的数据如何导入 %}

{% asset_img f31fbe096b63f624b24e62868744ebf81a4ca320.jpg spss20.0中excel和txt格式的数据如何导入 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
