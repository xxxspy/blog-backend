
---

title: spss计算平均方差提取量AVE和组合信度CR的方法
date: 2019-09-06 12:44:03
mathjax: true
tags: [spss, ]

---


这篇文章主要介绍了如何使用SPSS计算平均提取方差值AVE(Average Variance Extracted)和组合信度CR( Composite Reliability)的方法, 并且提供了计算他们的小程序, 帮助你在线计算。

<!-- more -->

在统计学（经典测量理论）中，提取的平均方差（AVE）是因子包含题目的的方差量的量度，与测量误差引起的方差量有关。  在下图中`$\lambda$`

### spss操作

在spss中, 我们可以这样去计算每个题目(变量)的因子载荷:

<img src="imgs/factor-analysis-menue.png">

注意我们需要用到因子旋转后的因子载荷, 所以要设置旋转方法:

<img src="imgs/factor-analysis-dialog.png">

运行命令以后, 可以输出旋转后因子成分矩阵, 下图中, 红色方框中的因子载荷就是第一个因子的因子载荷, 利用这些数据就可以计算第一个因子的平均提取方差值(AVE)和组合信度(CR):

<img src="imgs/rotated-component-matrix.png">

### 计算公式

假设`$\lambda$`代表题目的因子载荷, 那么平均方差提取量(Average Variance Extracted)`$l_{AVE}$`的计算步骤是:

`$$
$l_{AVE}$ = {( \sum \lambda^2) \over N}
$$`

那么组合信度( Composite Reliability)的计算公式是:

`$$
l_{CR} = {( \sum \lambda)^2 \over {( \sum \lambda)^2 + \sum \varepsilon}}
$$`

### 在线计算器

为了方便广大童鞋能够正确的计算AVE和CR值, 我在这里写了一个小程序, 你需要输入某个因子的因子载荷,
多个数值之间使用英文逗号","隔开, 例如"0.5,0.7,0.8,0.9", 
然后点击"计算"!

{% raw %}

<script>
console.log('hello')
</script>

<table class="table">
    <tr>
        <td>输入因子载荷(英文逗号隔开)</td>
        <td>
           <input id="loads" class="form-control" placeholder="输入因子载荷, 然后点击计算按钮" type="text">
        </td>
    </tr>
    <tr><td>AVE=</td><td> <input readonly class="form-control" id="ave" type="number"></td>
    </tr>
    <tr><td>CR=</td><td ><input readonly class="form-control" id="cr" type="number"></td></tr>
    <tr><td colspan="2"><button onclick="cal_cr()" class="btn btn-default">计算</button></td></tr>
</table>

<script>
    function cal_cr(){
        let loadsIpt = $('#loads')
        $('#ave').val('')
        $('#cr').val('')

        let loads = []
        let loadvalues = loadsIpt.val()
        if(!loadvalues){
            alert('没有因子载荷')
            return
        }
        let sm = 0
        let sm2 = 0
        let epsm = 0
        let n_item = 0
        loadvalues.split(',').forEach(v=>{
            n_item += 1
            let load = parseFloat(v)
            loads.push(load)
            sm += load
            sm2 += load * load
            epsm += 1 - load*load
        })
        let ave = sm2 / n_item
        let cr = sm * sm / (sm*sm + epsm)
        $('#ave').val(ave)
        $('#cr').val(cr)
    }
</script>

{% endraw %}

### 视频教程

<iframe src="//player.bilibili.com/player.html?aid=95343967&cid=162769024&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="width: 800px;height: 600px;"> </iframe>

> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](spss计算平均方差提取量AVE和组合信度CR的方法.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
