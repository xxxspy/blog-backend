---
title: spss分层聚类的操作方法和分析方法
date: 2015-02-05 18:01:19
tags: [spss]
author: mlln.cn
---
聚类是一个将case分类的数据，它不是一个严格的统计方法，所以是一个很有争议的方法。但是因为没有可以替代他的方法，所以现在大家也都在用。
方法/步骤


- 依次点击：analyse--classify--hierarchical cluster，打开分层聚类对话框

{% asset_img f7246b600c33874428699da8510fd9f9d62aa0b2.jpg spss分层聚类的操作方法和分析方法 %}

- 在聚类分析对话框中，
将聚类用到的变量都放到variables中

{% asset_img d009b3de9c82d158eccce465800a19d8bd3e4293.jpg spss分层聚类的操作方法和分析方法 %}

- 将地区变量放入case标签中，他的意思是每一个数据都用地区这个值来命名

{% asset_img 6f061d950a7b0208e175823562d9f2d3562cc8a2.jpg spss分层聚类的操作方法和分析方法 %}

- 点击plot按钮，打开对话框，设置要输出的图

{% asset_img 54fbb2fb43166d22e049a940462309f79052d22c.jpg spss分层聚类的操作方法和分析方法 %}

- 在打开的对话框中，勾选dendrogram，然后点击continue按钮。这个dendrogram是层次聚类谱系图，最后我们还会分析这个图

{% asset_img 5243fbf2b21193136c14436465380cd790238d8b.jpg spss分层聚类的操作方法和分析方法 %}

- 点击method按钮，设置聚类的方法

{% asset_img 8cb1cb1349540923cacddcaa9258d109b2de49b9.jpg spss分层聚类的操作方法和分析方法 %}

- 如图所示，通常我们用到的聚类方法是wards method，接着我们需要把变量转换成z分数，点击continue按钮

{% asset_img 4b90f603738da97744dc39ffb051f8198718e377.jpg spss分层聚类的操作方法和分析方法 %}

- 点击save按钮，填写希望保存的聚类类别数范围3--8，据此选项，spss将在数据编辑窗口中添加7个变量，分别标明聚类数位3--8类情况下各省市所属的类

{% asset_img 314e251f95cad1c8883943f37f3e6709c83d5167.jpg spss分层聚类的操作方法和分析方法 %}

- 设置输出的聚类类别数范围3--8，点击continue按钮

{% asset_img 5882b2b7d0a20cf4d4b7470b76094b36acaf993b.jpg spss分层聚类的操作方法和分析方法 %}

- 点击ok按钮，开始输出数据处理的结果

{% asset_img 63d0f703918fa0ecabc1ddd9269759ee3c6ddbe4.jpg spss分层聚类的操作方法和分析方法 %}

- 你看到的下面的这个表格叫做聚类过程表，其内容并不是经常被关注，因为大部分实际应用中，聚类的具体过程是被忽略的。但是聚类系数可以帮助我们判断将数据分为几类最合适，判断的方法是，相邻的两个数据变化的幅度显著大于前面的系数的变化范围，这时候分类在这里就是最好的

{% asset_img ac345982b2b7d0a2e8d5bd49cbef76094a369ac2.jpg spss分层聚类的操作方法和分析方法 %}

- 最后是层次聚类谱系图，从这个图中可看到聚类的过程，根据你的需求选择分类的组数

{% asset_img 32fa828ba61ea8d3d90dcfd0970a304e251f5832.jpg spss分层聚类的操作方法和分析方法 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
