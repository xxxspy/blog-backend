
---

title: SPSS做简单调节效应分析Model-1-Of-Process(视频教程+可视化工具)
date: 2020-03-22 12:44:03
tags: [spss, 调节效应, process]
mathjax: true

---


Process是spss中处理中介和调节模型的插件, 我们今天要讲一下process中的model1, 也就是最简单的调节模型, 视频教程已经放在文章末尾。

文章主要使用两种方法进行调节效应的检验, SPSS的回归方法和process的方法。

如果你不关心统计理论, 你可以直接跳转到下面的"SPSS分析过程"。



<!--more-->
<!-- toc -->

<img src="model-1-wen.png">

上图中, 使用X表示自变量, Z表示调节变量, Y表示因变量, XZ表示自变量和调节变量的乘积。

使用Spss可以做调节效应分析吗? 当然可以! 而且你不需要任何插件就可以做, 具体做法是这样的流程:

- 将自变量和调节变量进行中心化
- 计算自变量和调节变量的乘积
- 使用回归检验一下方程中系数c的显著性:


`$$
Y = i + aX + bZ + cXZ + e
$$`

具体做之前需要先回答两个问题:

- 1.为什么要中心化?
- 2.为什么乘积项的系数显著就可以证明存在调节效应?

### 为什么要中心化

温中林在他的论文《基于多元回归的调节效应分析》已经讲的很清楚, 因为中心化以后, 回归系数a和系数b的意义更加明确, 因而spss的回归结果更易于理解! 并且他还在文章中说, 我们以前以为中心化是为了降低变量之间的共线性, 这只降低了非本质的共线性, 也对回归结果没有本质影响, 因而不能当作我们变量中心化的理由。

也就是说, 中心化强制的将调节变量X的均值设置为0, 当Z为均值时, 回归方程变为我们最常见的多元回归形式:

`$$
Y = i + aX + e
$$`

这时候a的意义就是: 当调节变量取均值时的回归系数。这时候如果SPSS的计算结果显示系数a显著不为0, 说明当Z为均值时, X对Y有影响。

如果我们没有将变量进行中心化, 那么我们只能将方程写为:

`$$
Y = i + (a+\bar Z)X + b \bar Z + e ; (\bar Z ≠ 0)
$$`

###  为什么乘积项的系数显著就可以证明存在调节效应

我们可以对比一下系数c显著和不显著的两种方程, 注意c显著意思就是统计上不为0。

当`c≠0`显著时, 方程如下, 实际上`a+cZ`就是以X为自变量, 以Y为因变量的回归方程的斜率, c不为0, 说明斜率会因为Z的改变而改变:

`$$
Y = i + (a+cZ)X + bZ + e
$$`

当`c=0`时, 方程如下, 也就是说Z的变化只引起了方程的截距的改变, 但是并没有影响方程的斜率:

`$$
Y = i + aX + bZ + e
$$`

### SPSS分析过程

上面已经介绍了主要流程, 下面再细说一下:

- 计算自变量和调节变量的均值和标准差
- 中心化
- 求乘积
- 做两个回归模型

#### 计算自变量和调节变量的均值和标准差

使用描述统计:

<img src="description-menue.png" class="img-thumbnail">

设置如下:
<img src="description-options.png" class="img-thumbnail">

输出结果:
<img src="description-output.png" class="img-thumbnail">


#### 中心化变量

计算变量的功能在这里:

<img src="calculate-menue.png" class="img-thumbnail">

让变量减去平均值即可, 注意生成新的变量用"M"打头:

<img src="calculate-options.png" class="img-thumbnail">


#### 计算交互项(乘积)

注意交互项的变量名要体现他时谁跟谁的乘积。

<img src="calculate-interation.png" class="img-thumbnail">



最后你计算一下各个变量的均值, 看是否如你所愿:

<img src="calculate-output.png" class="img-thumbnail">

#### 做回归

我们需要做如下两个回归:

$$
𝑌=𝑖+𝑎𝑋+𝑏𝑍+𝑒
𝑌=𝑖+𝑎𝑋+𝑏𝑍+𝑐𝑋𝑍+𝑒
$$

他们的区别仅仅是第二个模型增加了交互项, 具体步骤如下:

**Step1: 菜单**

<img src="regression-menue.png" class="img-thumbnail">

**Step2:第一个回归模型**

<img src="regression-model1.png" class="img-thumbnail">

**Step3:第二个回归模型**

<img src="regression-model2.png" class="img-thumbnail">

**Step4:配置选项**

<img src="regression-options.png" class="img-thumbnail">

**Step4:输出结果**

首先看R方的改变量, 从Model1到Model2, R方改变量是显著的, 说明增加交互项可以提高回归模型的拟合度。

<img src="regression-output1.png" class="img-thumbnail">

再看交互项的系数是显著的, 证明调节作用显著。

<img src="regression-output2.png" class="img-thumbnail">

### Process做简单交互效应

Process能帮助你更快的检验交互效应, 因为它自动化处理了上面的过程, 下面我们来演示一下如何使用Process插件:

#### 操作方法

找到process菜单:

<img src="process-menue.png" class="img-thumbnail">

**设置变量:**

<img src="process-options2.png" class="img-thumbnail">

**配置参数:**

注意我们勾选了一下两个选项:

- Generate code for visualizing interactions(生成可视化交互效应的代码)
- all variables that define products(变量中心化处理)

并且, 我们希望计算调节变量在三个点值(conditioning values)时回归方程的参数, 
这三个点可以时百分位数, 也可以是标准差为单位的三个值, 我们更倾向于选择后者。

<img src="process-options2.png" class="img-thumbnail">




#### 结果解读

主要看下面两个结果, 首先是交互项(Int_1)的系数是否显著, 下面的结果是显著的;
然后看R方的改变量, 这个值从模型1到模型2改变了0.024, 这与上面使用SPSS的回归方法计算的值一模一样。

<img src="process-output.png" class="img-thumbnail">

接下来我们可以看到调节变量(工作量)取三个值(负一个标准差/均值/正一个标准差)时回归方程的斜率(自变量的系数):

<img src="process-output2.png" class="img-thumbnail">


#### 结果可视化

最后我们使用process提供的数据进行可视化绘图, 这个数据有3列, 第一列是工作资源的三个值(分别是均值和它上下一个标准差), 第二列是工作量的三个值(分别是均值和它上下一个标准差),  最后一列是在工作起源和工作量在不同值时计算得到的工作投入的值。

<img src="process-output3.png" class="img-thumbnail">

我们将这些数字贴到excel, 经过整理就可以绘制得到一个调节效应的可视化折线图:
注意, 整理过程中, 我们将自变量和调节变量的三种值都进行了命名, 名字为两个字母, 第一个字母表示自变量(X)或者调节变量(M),
第二个字母表示均值(M), 均值以上一个标准差(H), 均值以下一个标准差(L)。


<img src="visualization.png" class="img-thumbnail">


### 可视化工具

<div id="visual" style="border-style: groove;text-align: center;width: 800px;">

根据下面的公式, 我们来对号入座的填入数据, 这样就可以可视化我们的交互效应。

`$$ 
𝑌=𝑖+𝑎𝑋+𝑏𝑍+𝑐𝑋𝑍+𝑒 
$$`
<div>
i = <input onchange="onChange()" value="4.262" placeholder="常量" name="pi" type="number" style="width: 110px;background-color: transparent;text-align: left;"><br>
a = <input onchange="onChange()"  value="0.126" name="pa" type="number" style="width: 110px;background-color: transparent;text-align: left;"><br>
b = <input  onchange="onChange()" value="1.06" name="pb" type="number" style="width: 110px;background-color: transparent;text-align: left;"><br>
c = <input  onchange="onChange()" value="0.287" name="pc" type="number" style="width: 110px;background-color: transparent;text-align: left;"><br>
自变量名称、均值和标准差 = <input  onchange="onChange()" name="xn" placeholder="名称" value="X" type="text" style="width: 110px;background-color: transparent;text-align: left;"><input  onchange="onChange()" value="0" name="xm" placeholder="均值" type="number" style="width: 110px;background-color: transparent;text-align: left;"><input  onchange="onChange()" value="0.661" placeholder="标准差" name="xs" type="number" style="width: 110px;background-color: transparent;text-align: left;"><br>

调节变量名称、均值和标准差 = <input  onchange="onChange()" name="mn" placeholder="名称" value="M" type="text" style="width: 110px;background-color: transparent;text-align: left;"><input  onchange="onChange()" value="0" name="mm" placeholder="均值" type="number" style="width: 110px;background-color: transparent;text-align: left;"><input  onchange="onChange()" value="0.996" placeholder="标准差" name="ms" type="number" style="width: 110px;background-color: transparent;text-align: left;"><br>
</div>

<div id="line-chart" style="width: 100%;height:600px;"></div>
<div id="d3-chart" style="width: 100%;height:600px;"></div>

</div>

### Process快捷可视化

我们将process生成的可视化代码, 粘贴到下面的文本框, 就可以自动可视化:

<textarea id="visual-codes" onchange="onCodeChange()" style="width:100%;color:black;" rows="15"></textarea>
<div id="line-chart-codes" style="width: 100%;height:600px;"></div>



### 总结

- 我们这篇文章介绍了两种方法来检验调节效应, 两种方法本质上都是做了两次回归, 结果也是一样的。
- Process的好处是大大简化了我们的操作步骤


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](SPSS做简单调节效应分析Model-1-Of-Process.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn

<script src="https://cdn.bootcss.com/echarts/4.7.0/echarts.js"></script>
<script src="/js/echarts-gl.min.js"></script>
<script>
    function get_eles(){
        let eles = {
            'pi': $('input[name="pi"]'),
            'pa': $('input[name="pa"]'),
            'pb': $('input[name="pb"]'),
            'pc': $('input[name="pc"]'),
            'xn': $('input[name="xn"]'),
            'xm': $('input[name="xm"]'),
            'xs': $('input[name="xs"]'),
            'mn': $('input[name="mn"]'),
            'mm': $('input[name="mm"]'),
            'ms': $('input[name="ms"]'),
        }
        return eles
    };
    

    function get_values(){
        let eles = get_eles();
        let values = {}
        Object.keys(eles).forEach((name, _)=>{
            console.log(name)
            let v = eles[name].val()
            if(name == 'xn' || name == 'mn'){
                values[name] = v
            }else if(v.length>0){
                values[name] = parseFloat(v)
            }
        })
        console.log('values')
        console.log(values)
        return values
    }
    
    function calculate_data(){
        let values = get_values()
        let series = []
        let xvalues = [values['xm'] - values['xs'], values['xm'], values['xm'] + values['xs']]
        let mvalues = [values['mm'] - values['ms'], values['mm'], values['mm'] + values['ms']]
        let levels = ['M-SD', 'M', 'M+SD']
        let i = values.pi;
        let a = values.pa;
        let b = values.pb;
        let c = values.pc;
        let names = [];
        mvalues.forEach((x, order)=>{
            let name = `${values["mn"]}(${levels[order]})`;
            let line = {
                name: name,
                type: 'line',
                data: []
            }
            names.push(name);
            xvalues.forEach(m=>{
                console.log(`${i} + ${a*x} + ${b*m} + ${c*x*m}`)
                line.data.push(
                    i + a*x + b*m + c*x*m
                )
            })
            series.push(line)
        })
        console.log('==================')
        console.log(series)
        return {
            series: series,
            legend: names,
            xname: values.xn,
            mname: values.mn,
            values: values,
            xaxis: [
                `${values['xn']}(M-SD)`, `${values['xn']}(M)`, `${values['xn']}(M+SD)`
            ],
        }
    }
</script>
<script>
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('line-chart'));



        var option = {
            backgroundColor: 'rgb(255, 255, 255)',
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: ['M-SD', 'M', 'M+SD', ],
                show: true,
            },
            grid: {
                left: '13%',
                right: '14%',
                bottom: '13%',
                containLabel: true
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: true,
                data: ['XL','XM','XH']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                    name: 'M-SD',
                    type: 'line',
                    data: [3.6246,
                            4.1366,
                            4.6486,
                            ]
                },
                {
                    name: 'M',
                    type: 'line',
                    data: [3.5607,
                            4.262,
                            4.9632,
                            ]
                },
                {
                    name: 'M+SD',
                    type: 'line',
                    data: [3.4969,
                        4.3874,
                        5.2778,
                        ]
                },
                
            ]
        };


        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        
        function resetChart(){
            let d = calculate_data();
            option.xAxis.data = d.xaxis;
            option.series = d.series;
            option.legend.data = d.legend;
            console.log(option)
            myChart.setOption(option)
            reset_3d(d.values)
        }
        
        // 侦听修改事件
        function onChange(){
            console.log('change')
            resetChart()
        }
</script>

<script>
    // 3D显示
d3Option = {
    tooltip: {
        trigger: 'axis'
    },
    backgroundColor: '#fff',
    visualMap: {
        show: false,
        dimension: 2,
        min: -1,
        max: 1,
        inRange: {
            color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        }
    },
    xAxis3D: {
        type: 'value',
        name: '自变量',
    },
    yAxis3D: {
        type: 'value',
        name: '调节变量',
    },
    zAxis3D: {
        type: 'value',
        name: '因变量',
    },
    grid3D: {
        viewControl: {
            // projection: 'orthographic'
        }
    },
    series: [{
        type: 'surface',
        wireframe: {
            // show: false
        },
        equation: {
            x: {
                step: 0.05
            },
            y: {
                step: 0.05
            },
            z: function (x, y) {
                return 1 + x + y + x*y
            }
        }
    }]
}
        var d3Chart = echarts.init(document.getElementById('d3-chart'));
        d3Chart.setOption(d3Option);

        function reset_3d(values){
            d3Option.xAxis3D.name = values.xn,
            d3Option.yAxis3D.name = values.mn,
            d3Option.series[0].equation.x.max = values.xm + 2 * values.xs;
            d3Option.series[0].equation.y.max = values.mm + 2 * values.ms;
            d3Option.series[0].equation.x.min = values.xm - 2 * values.xs;
            d3Option.series[0].equation.y.min = values.mm - 2 * values.ms;
            d3Option.series[0].equation.z = function(x, y){
                return values.pi + values.pa * x + values.pb * y + values.pc * x * y
            }
            d3Chart.setOption(d3Option);

        }
</script>

<script>
        var myCodeChart = echarts.init(document.getElementById('line-chart-codes'));
        var codeOption = {
            backgroundColor: 'rgb(255, 255, 255)',
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: ['M-SD', 'M', 'M+SD', ],
                show: true,
            },
            grid: {
                left: '13%',
                right: '14%',
                bottom: '13%',
                containLabel: true
            },
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            xAxis: {
                type: 'category',
                boundaryGap: true,
                data: ['XL','XM','XH']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                    name: 'M-SD',
                    type: 'line',
                    data: [3.6246,
                            4.1366,
                            4.6486,
                            ]
                },
                {
                    name: 'M',
                    type: 'line',
                    data: [3.5607,
                            4.262,
                            4.9632,
                            ]
                },
                {
                    name: 'M+SD',
                    type: 'line',
                    data: [3.4969,
                        4.3874,
                        5.2778,
                        ]
                },
                
            ]
        };


        // 使用刚指定的配置项和数据显示图表。
        myCodeChart.setOption(codeOption);

        function parseData(){
            let text = $('#visual-codes').val()
            let cols = [];
            let rows = []
            text.split('\n').forEach((line, i)=>{
                console.log(line)
                line = line.trim()
                if(line == 'BEGIN DATA.'){
                    return
                }

                line = line.split(/\s+/)
                if(cols.length==0 && line.length==4){
                    cols = [line[0], line[1], line[2]]
                    console.log(cols);
                    return cols
                }
                let row = []
                line.forEach((val, j)=>{
                    row.push(parseFloat(val))
                })
                rows.push(row)
                
            })
            return {
                'cols': cols,
                'rows': rows,
            }
        }

        
        
        // 侦听修改事件
        function onCodeChange(){
            console.log('change')
            let d = parseData()
            console.log('dddddddddddddddddd:')
            console.log(d)
            let xn = d.cols[0]
            let mn = d.cols[1];
            let yn = d.cols[2]
            let legend = [
                `${mn}(M-SD)`,
                `${mn}(M)`,
                `${mn}(M+SD)`,
            ]
            let xaxis= [
                `${xn}(M-SD)`, `${xn}(M)`, `${xn}(M+SD)`
            ]
            let series = [
                {
                    name: legend[0],
                    type: 'line',
                    data: [d.rows[0][2], d.rows[1][2], d.rows[2][2], ],
                },
                {
                    name: legend[1],
                    type: 'line',
                    data: [d.rows[3][2], d.rows[4][2], d.rows[5][2], ],
                },
                {
                    name: legend[2],
                    type: 'line',
                    data: [d.rows[6][2], d.rows[7][2], d.rows[8][2], ],
                },
            ]
            codeOption.xAxis.data = xaxis;
            codeOption.series = series;
            codeOption.legend.data = legend;
            myCodeChart.setOption(codeOption)
            console.log(series)
            
        }
</script>