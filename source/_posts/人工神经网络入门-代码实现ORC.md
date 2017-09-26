---
title: 人工神经网络入门+代码实现ORC
date: 2017-06-11 23:52:31
tags: [ORC, 神经网络, 3djs, synaptic]
d3js: true
synaptic: true
mathjax: true
---

{% raw %}
<div class="row" id="content-body">
    <div id="orc-container" class="col-md-6 col-lg-6 col-sm-12"></div>
    <div class="controls col-md-6 col-lg-6 col-sm-12">
        在表格里写入一个一个数字(0-9)<br />
        <button class="clear btn btn-default"> 清空 </button>
        <button class="recognize btn btn-default">识别</button>
        <div>预测结果： <span class="prediction"> ?? </span> </div>
        信度：<div class="confidence"></div>
        <div class="confidences">
        </div>
    </div>
</div>
<div class="row" id="network-container"></div>
<div class="row btn-group" id="network-buttons">
    <button class="btn btn-lg btn-default" id="reduce-neuron">减少神经元</button>
    <input id="num-nodes" type="number" class="btn btn-default btn-large form-group" value="25" title="隐层神经元个数" height="100%">
    <button class="btn btn-lg btn-default" id="add-neuron">增加神经元</button>
    <button class="btn btn-lg btn-default" id="network-run">训练</button>
</div>
{% endraw %}

{% raw %}
<!-- orc -->
   <style>
        body {
          margin: 0;
          font-family: Helvetica;
          font-weight: 100;
        }
        svg {
          shape-rendering: crispEdges;
          cursor: pointer;
        }
        .controls {
        }
    </style>
    
    <!-- draw a grid -->
    <script type="text/javascript">

        if ('d3' in window){
            var gL=50, gridN=8, boxLength=gL * gridN
            var svg=d3.select('#orc-container').append('svg').attr("width",boxLength)
                .attr("height",boxLength)
            var data=d3.range(gridN*gridN).map(function(d){
                return {i: d%gridN, j:Math.floor(d/gridN), id: d, active:0}
            })

            var grids=svg.append('g').attr('class', 'grids')
                .selectAll('rect').data(data).enter().append('rect')
                .attr("width", gL).attr("height", gL)
                .attr('x', function(d){return gL*d.i})
                .attr('y', function(d){return gL*d.j})
                .style('stroke', 'rgba(255, 255, 255, 0.2)')

            function updateGrid(g){
                g.style('fill', function(d){
                    return d.active ? 'rgba(255,255,255,1)':'black'
                })

            }
            var conf = d3.select('.confidences').selectAll('div')
                .data(d3.range(10)).enter()
                .append('div').text(function(d){return d + ': '})

            var bar=conf.append('div').attr('class', 'bg')
                .style("width",'60px')
                .style("height", '20px')
                .style("display", 'inline-block')

            bar.append('div').attr('class', 'fg')
                .style("width", '20%')
                .style("height", '100%')
                .style('background-color', 'rgba(0, 0, 0, 0.8)')

            svg.on('mousedown', function(){
                grids.on('mousemove',function(d){
                    d.active=1
                    updateGrid(d3.select(this))
                })
            }).on('mouseup',function(){
                grids.on('mousemove',null)
            })

            function updateState(){
                var input = data.map(function(d){return d.active})
                var output = window.network.activate(input)
                var max = -1, maxId = -1
                output.forEach(function(d, i) { if (d > max) max = d, maxId = i })
                conf.data(output).select('.fg')
                    .style('width', function(d) { return d * 100 + '%' })
                d3.select('.prediction').text(maxId)
                d3.select('.confidence').text(max)

            }
            d3.select('button.clear').on('click', resetBlocks)
            d3.select('button.recognize').on('click', updateState)

            function resetBlocks() {
              grids.each(function(d) { d.active = 0 }).call(updateGrid)
            }
        }else{
            document.getElementById('content-body').innerHTML='本篇文章内容特殊，只有打开文章才能看到。'
            document.getElementById('network-buttons').innerHTML=''
        }
    </script>

{% endraw %}

{% raw %}
   <!-- network graph -->
    <style type="text/css">
        text {
          pointer-events: none;
        }

        .node:hover {
          stroke: #999;
          stroke-opacity: .6;
          stroke-width: 4px;
        }

        .link {
          stroke: #999;
          stroke-opacity: .6;
        }
    </style>
    <script type="text/javascript">
    if ('d3' in window){
        var width = 960,
            height = 1400,
            nodeSize = 10;

        var color = d3.scaleOrdinal(d3.schemeCategory20);

        var svg = d3.select("#network-container").append("svg")
            .attr("width", width)
            .attr("height", height);


        window.show_network=function(network) {
            
            svg.selectAll('*').remove()
            // get network size
            var netsize = {}
            allLayers=[network.layers.input]
            network.layers.hidden.forEach(function(l){
                allLayers.push(l)
            })
            allLayers.push(network.layers.output)

            // calc distances between nodes
            largestLayerSize=0
            allLayers.forEach(function(d){if(d.size>largestLayerSize){
                largestLayerSize=d.size
            }})

            var xdist = width / allLayers.length,
                ydist = height / largestLayerSize;

            // create node locations
            layerCount=0
            var links = [];
            allLayers.map(function(layer) {
                layerCount +=1
                layer.layerCount=layerCount
                neurons=layer.neurons()
                nNeurons=neurons.length
                maxYDistance=nNeurons * ydist
                startY=(height-maxYDistance)/2
                neuCount=0
                neurons.forEach(function(neuron){
                    neuCount +=1
                    neuron.x=(layerCount - 0.5) * xdist
                    neuron.y=(neuCount - 0.5 ) * ydist + startY
                    connections=neuron.connections.projected
                    keys=Object.keys(connections)
                    keys.forEach(function(id){
                        links.push(connections[id])
                    })
                })
            });

            // draw links
            var link = svg.selectAll(".link")
                .data(links)
              .enter().append("line")
                .attr("class", "link")
                .attr("x1", function(d) { return d.from.x; })
                .attr("y1", function(d) { return d.from.y; })
                .attr("x2", function(d) { return d.to.x; })
                .attr("y2", function(d) { return d.to.y; })
                .style("stroke-width", function(d) { return d.weight * 10; });

            // draw nodes
            console.log(network.neurons())
            var node = svg.selectAll(".node")
                .data(network.neurons())
              .enter().append("g")
                .attr("transform", function(d) {
                    return "translate(" + d.neuron.x + "," + d.neuron.y + ")"; }
                );

            var circle = node.append("circle")
                .attr("class", "node")
                .attr("r", nodeSize)
                .style("fill", function(d) { return color(d.layer.layerCount); });


            node.append("text")
                .attr("dx", "-.35em")
                .attr("dy", ".35em")
                .text(function(d, i) { return i; })
        }

        var numInput=document.getElementById('num-nodes')
        var addBtn=d3.select('#add-neuron').on('click', function(){
            value=numInput.value
            console.log(value)
            value = parseInt(value)
            // numInput.attr('value', value + 1)  #这个方法不能动态显示更改后的数据
            numInput.value=value +1
        })
        var reduceBtn=d3.select('#reduce-neuron').on('click', function(){
            value= parseInt(numInput.value)
            value = (value > 1)? value -1 : 0
            numInput.value=value
            
        })
        var runBtn= d3.select('#network-run').on('click', function(){
            num=parseInt(numInput.value)
            if(num>0){
                myNetwork=new synaptic.Architect.Perceptron(64, num, 10)
                trainer=new synaptic.Trainer(myNetwork)
                window.train(trainer)
                window.show_network(myNetwork)
                window.network=myNetwork
                window.trainer=trainer
                alert('训练完成')
            }else{
                alert('神经元的数量必须大于0')
            }
        })
    }
    </script>

{% endraw %}

{% raw %}
    <script type="text/javascript">
        if('synaptic' in window){
            var myNetwork = new synaptic.Architect.Perceptron(64, 25, 10)
            var trainer = new synaptic.Trainer(myNetwork)

            function train(trainer){
                d3.text('data', function(err, data) {
                  if (err) {
                    throw err
                  }
                  var ts, te, idx
                  data = d3.csvParseRows(data, function(row) { return row.map(Number) })
                    .map(function(d) {
                    // Expected output.
                    var t = d3.range(10).map(function() { return 0 })
                    t[d[0]] = 1
                    return { input: d.slice(1), output: t }
                  })
                    ts=Date.now()
                    trainer.train(data)
                    te=Date.now()
                    console.log('Time Spend: '+ (te-ts))
                })
            }
            window.train=train
            train(trainer)
            window.network=myNetwork
            window.trianer=trainer
            window.show_network(myNetwork)
        }
    </script>
{% endraw %}


### 计算计算过程

#### 输入和输出

假设网络中所有的参数已知，根据一个输入向量x，求输出向量y。

首先输入是一个64维向量：

`\[ x=\left[ x_1, x_2,\dots x_d \right] \](d=64)`

而输出向量应该是一个10维的向量，用来表征10个数字的识别概率。

`\[ \hat y=\left [ \hat y_1, \hat y_2,\dots \hat y_l \right](l=10) \]`

#### 已知条件：

- 输入层到隐层神经元之间的链接权重`v`：

`\[ v=\left| { \begin{array}{c}
v_{11} & v_{12} & \dots & v_{1d}\\
v_{21} & v_{22} & \dots & v_{2d}\\
\vdots & \vdots & \ddots & \vdots\\
v_{q1} & v_{q2} & \dots & v_{qd}
\end{array} }\right| (d=64, q=\text{count of hidden layer neurons})\]
`

- 隐层神经元的阈值b

`\[ b=[b_1, b_2, \dots, b_q](q=\text{count of hidden layer neurons}) \]`

- 隐层到输出层的权重`w`：

`\[
w=\left| { \begin{array}{c}
w_{11} & w_{12} & \dots & w_{1q}\\
w_{21} & w_{22} & \dots & w_{2q}\\
\vdots & \vdots & \ddots & \vdots\\
w_{l1} & w_{l2} & \dots & w_{lq}
\end{array} }\right| (l=10, q=\text{count of hidden layer neurons})
\]`


- 输出层的阈值`\( \theta \)`

`\[ \theta=[\theta_1, \theta_2,\dots,\theta_l](l=10) \]`

- 激活函数

`\[ f(x)={ 1 \over { 1 + e^{-x} } } \]`

#### 计算结果

- 隐层神经元的输入

`\[ \alpha = v · x^T + b  \]`

- 隐层神经元的激活

`\[ \beta=f(\alpha) \]`

- 输出神经元输入

`\[\gamma = w · \beta + \theta\]`

- 输出神经元的激活

`\[f(\gamma)\]`

### synaptic.js实现神经网络

为了演示我们就用一个前端库来做一个神经网络。

```javascript
var myNetwork = new synaptic.Architect.Perceptron(64, 25, 10)
var trainer = new synaptic.Trainer(myNetwork)
data=[
    {input: [0,0,0,0,1,...,0], output: 1},
    {input: [0,0,0,0,1,...,0], output: 1},
    {input: [0,0,0,0,1,...,0], output: 1},
    {input: [0,0,0,0,1,...,0], output: 1},
    {input: [0,0,0,0,1,...,0], output: 1},
    {input: [0,0,0,0,1,...,0], output: 1},
    {input: [0,0,0,0,1,...,0], output: 1}
]
trainer.train(data)
new_input=[0,0,1,...,0]
var output = network.activate(new_input)
```

### 