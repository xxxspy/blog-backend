---
title: CR和AVE计算器Excel版下载和使用教程
date: 2023-08-16 02:17:03
tags: [spss]
---

CR指的是组合信度（Composite Reliability）， AVE指的是平均方差提取量（Average Variance Extraction），
我们已经在本网站开发了一个计算器（在这里[spss计算平均方差提取量AVE和组合信度CR的方法](https://mlln.cn/2019/09/06/spss%E8%AE%A1%E7%AE%97%E5%B9%B3%E5%9D%87%E6%96%B9%E5%B7%AE%E6%8F%90%E5%8F%96%E9%87%8FAVE%E5%92%8C%E7%BB%84%E5%90%88%E4%BF%A1%E5%BA%A6CR%E7%9A%84%E6%96%B9%E6%B3%95/) ，
但是很多人认为还是用Excel计算CR和AVE比较方便， 而且结果可以直接复制到表格， 方便论文里的表格制作。

所以我们决定做一个Excel版本的AVE和CR计算器。

<!-- more -->

# 下载方法

因为我们想要可持续的贡献有价值的内容， 
所以我们决定对这些资源提供小偿下载，
这里我们提示， 网页版计算器是免费的，
大家可以直接打开网页使用，
Excel版在这里下载： [CR和AVE计算器Excel版下载](https://gf.bilibili.com/item/detail/1103271046)

# 使用方法

当你下载好了Excel计算器， 打开这个Excel文件，
你会看到下面这个表格， 这个表格只有“粘贴Mplus结果”列才是你需要填写的。

<img src="cr&ave01.png">

输入区只能输入直接从Mplus复制的标准化因子在乎部分，如下图：

<img src="mplus.png">


然后AVE和CR是自动计算的， 只要因子载荷更改了，AVE和CR就会自动更新。

注意你一次只能计算一个因子的AVE和CR， 不要把多个因子的因子载荷同时录入到这个表格中，
会导致错误的结论。

另外， 对于AVE和CR有一些建议：

- CR建议超过0.7( Hair,1997) ,
- Fornell and Larcker (1981) 建议 CR 最低0.6
- Fornell and Larcker(1981) 建议 AVE最低 0.5

# 视频教程

https://www.bilibili.com/video/BV1fN411z78X/

<iframe src="//player.bilibili.com/player.html?bvid=BV1fN411z78X&page=1" style="width:800px;height:600px" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>