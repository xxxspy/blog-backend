
---

title: Amos结构方程模型数据分析入门教程
date: 2022-06-12 12:44:03
tags: [结构方程, amos]

---

### 模型


<img src="imgs/model.png">

这是一个中介和调节模型, 领导力是自变量, 组织绩效是因变量, 效能感是中介变量, 调节变量是情绪智力, 情绪智力调节了效能感与组织绩效的关系, 简单来说, 情绪智力越高, 效能感对组织绩效的预测作用越强, 这是一个正向调节的变量。

### 数据

数据由问卷采集而来, 总共采集了473名员工作为样本。

- 领导力有11个题目, 在数据中变量名是A1-A11;
- 效能感有11个题目, 在数据中变量名是B1-B11;
- 组织绩效有13个题目, 在数据中变量名是C1-C13;
- 情绪智力有6个题目, 在数据中变量名是D1-D6;

数据保存在spss数据中, 文件名是data.sav;

### 验证性因子分析

#### 模型图绘制

<img src="imgs/cfa.png">

#### 模型拟合

模型的整体拟合优度主要指标：卡方为1485.53，df=773，RMSEA=0.044<0.08，CFI=0.958>0.90，TLI=0.955>0.90，IFI=0.958>0.90，NFI=0.916>0.90，PCFI=0.903>0.50，PNFI=0.864>0.50，GFI=0.868<0.90，模型基本可以接受。

<img src="imgs/modelfit.png">

#### 因子载荷

从下面表格中"Estimate"表示因子载荷的估计，"STD_Estimate"是标准化的因子载荷，"P"表示显著性，如果P为一颗以上"*"或者小于0.05表示该载荷是显著的，也就是说统计上不为0。依据标准化载荷值可以计算因子的平均方差提取值AVE，AVE通常大于0.5且建构信度CR大于0.7就认为该潜变量的构建效度良好。

<img src="imgs/factorloading.png">

#### 区分效度

对角线上的数值是AVE的平方根, 其他数值是因子之间的相关系数, 当AVE大于该因子与其他因子的相关系数时, 我们认为区分效度良好。

<img src="imgs/discrimenent.png">

### 结构方程模型

#### 绘制模型图

<img src="imgs/sem.png">



#### 模型拟合

模型的整体拟合优度主要指标为：chi-square为1189.93，df=557，RMSEA=0.049<0.08，CFI=0.958>0.90，TLI=0.955>0.90，IFI=0.958>0.90，NFI=0.924>0.90，PCFI=0.897>0.50，PNFI=0.865>0.50，GFI=0.876<0.90，模型基本可以接受。

<img src="imgs/modelfit2.png">



#### 路径系数

我们关心的路径系数有三个, P值显著就证明路径系数不为零, 在此之前, 你肯定对结果做了假设, 比如"领导力正向影响效能感", 如果这条路径显著, 就证明你的假设成立。

<img src="imgs/coefficience.png">

#### 中介效应

这是一个典型的中介模型, 所以我们需要对中介效应做一个检验, 目前检验中介效应最常用的方法就是使用bootstraping抽样来计算中介效应的分布, 
amos支持这个操作, 最终我们整理成如下的表格:

<img src="imgs/mediation.png">

有些人质疑为什么直接效应和间接效应之和不等于总效应, 因为这是bootstrap抽样, 估计值是样本均值, 所以总效应的均值未必等于直接效应和间接效应均值之和。

#### 调节效应

使用分组比较的方法来做调节效应分析, 将调节变量按照高低分划分样本, 两组样本可以分别估计模型, 如果两组结果有差异(主要是路径系数), 就可以证明调节变量在该路径上具有调节效应。

还有一种思路, 设置模型的参数限制, 说起来比较复杂, 我们在视频里细聊。

具体步骤:

- 合成调节变量
- 高低分组
- 设置模型
- 整理结果

##### 模型拟合

<img src="imgs/moderfit.png">

##### 路径系数

<img src="imgs/modelcoff.png">

### 视频教程

<iframe 
style="width:800px;height:600px" 
src="//player.bilibili.com/player.html?aid=555736434&bvid=BV17v4y1M7Kk&cid=767005266&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

<iframe 
style="width:800px;height:600px" 
src="//player.bilibili.com/player.html?aid=555736434&bvid=BV1cY4y1J7rt&cid=767005266&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

<iframe 
style="width:800px;height:600px" 
src="//player.bilibili.com/player.html?aid=555736434&bvid=BV16r4y1u7tc&cid=767005266&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>


### 视频完整版及数据下载

https://afdian.net/item?plan_id=d72215a6fe7111eca07a52540025c377


> **注意**
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的, 不论什么模型都可以, 只限制于1个研究内. 
> 跟我学统计可以代做分析, 每单几百元不等. 
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](Amos结构方程数据分析案例教程.ipynb)
> 可以在微博上@mlln-cn向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
