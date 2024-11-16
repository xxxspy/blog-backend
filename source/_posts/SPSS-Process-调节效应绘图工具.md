---
title: SPSS Process 调节效应绘图工具
date: 2023-03-25 16:34:43
tags: [spss, process]
---
SPSS的Process做完调节效应分析以后， 给我们输出了一段代码帮助我们做简单斜率的图，
但是使用spss绘制简单斜率呢比较丑，所以我们做了一个便捷的工具， 可以帮助你快速绘制简单斜率图。

这个工具用于可视化简单效应图， 
并且主要用于spss的process插件所产生的可视化数据。
在文章最后还提供了使用Excel绘图的方法，并且提供了Excel绘图模板，支持一键绘图，非常简单。

<!-- more -->

## 方法

首先找到SPSS Process的输出结果， 具体是下面选中的（黑色背景）的部分：

<img src="spss-process-简单斜率图.png">

将这部分数据复制到下面的数据输入框中， 立刻就会看到图已经绘制好了。
如果你发生问题， 可以看视频教程。

## 简单斜率绘图工具

<script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/5.4.2/echarts.min.js" integrity="sha512-VdqgeoWrVJcsDXFlQEKqE5MyhaIgB9yXUVaiUa8DR2J4Lr1uWcFm+ZH/YnzV5WqgKf4GPyHQ64vVLgzqGIchyw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<style>

    td {
        color: #d7ecff;
    }
    td > input {
        color: black;

    }
    td > textarea {
        color: black;

    }
</style>
<div id="main" style="width: 100%;height:600px;background-color:white"></div>
<div id="config" style="height:400px">
    <table style="color:black">
        <tr>
            <td>数据</td><td colspan="3"><textarea rows="10" cols="50"  onchange="draw()">
                 -.8976    -1.4802     2.4567 
                .0000    -1.4802     2.2899 
                .8976    -1.4802     2.1231 
                -.8976      .0000     2.2448 
                .0000      .0000     2.1287 
                .8976      .0000     2.0127 
                -.8976     1.4802     2.0328 
                .0000     1.4802     1.9675 
                .8976     1.4802     1.9023
            </textarea></td>
        </tr>
        <tr>
            <td>横坐标名称</td><td><input type="text" id="xname" value="时间压力" onchange="draw()"></td>
            <td>纵坐标名称</td><td><input type="text" id="yname" value="挑战性" onchange="draw()"></td>
        </tr>
        <tr>
            <td>坐标轴名称大小</td><td><input type="number" id="axis-name-size" value="20" onchange="draw()"></td>
            <td>调节变量名称</td><td><input type="text" id="zname" value="积极语言" onchange="draw()"></td>
        </tr>
        <tr>
            <td>下边距</td><td><input type="number" id="ymin" value="0.1" onchange="draw()"></td>
            <td>上边距</td><td><input type="number" id="ymax" value="0.1" onchange="draw()"></td>
        </tr>
    </table>
</div>

<script>
function parseData(){
    let rawdata = $('textarea').val();
    let data = [];
    rawdata.split('\n').forEach(line=>{
        console.log(line);
        let lastNum=undefined;
        line.split(' ').forEach(n=>{
            n = parseFloat(n);
            console.log('n='+n)
            if(!isNaN(n)){lastNum=n}
        })
        if(!isNaN(lastNum)){
            data.push(lastNum)
        }
        
    })
    return data
}

function draw(){
    let data = parseData();
    let option = {
    legend: {
        show: true,
        top: 'bottom',
    },
    xAxis: {
        name: $('#xname').val(),
        type: 'category',
        nameLocation: 'center',
        nameTextStyle: {
            fontSize:$('#axis-name-size').val(),
            verticalAlign: 'top',
            padding: [10,10,10,10],
        },
        data: ['M-SD', 'M', 'M+SD', ]
    },
    yAxis: {
        name: $('#yname').val(),
        type: 'value',
        nameLocation: 'center',
        min: function (value) {
            return value.min - parseFloat($('#ymin').val());
        },
        max: function (value) {
            return value.max + parseFloat($('#ymax').val());
        },
        nameTextStyle: {
            fontSize: $('#axis-name-size').val(),
            verticalAlign: 'bottom',
            padding: [10,10,10,10],
        },
    },
    series: [
        {
        name: '低' + $('#zname').val(),
        data: data.slice(0,3),
        type: 'line',
        color: 'black',
        symbol: 'rect',
        symbolSize: 8,
        lineStyle: {
            normal: {
            width: 2,
            type: 'dotted'
            },
        
        }
        },
        {
        name: '中' + $('#zname').val(),
        data: data.slice(3,6),
        type: 'line',
        symbol: 'triangle',
        symbolSize: 8,
        color: 'black',
        lineStyle: {
            normal: {
            width: 2,
            type: 'dotted'
            },

        }
        },
        {
        name: '高' + $('#zname').val(),
        data: data.slice(6,9),
        type: 'line',
        color: 'black',
        lineStyle: {
            normal: {
            width: 2,
            type: 'dotted'
            },

        }
        },
    ]
    };
    console.log( data.slice(0,3))
    console.log( data.slice(3,6))
    console.log( data.slice(6,9))
    var myChart = echarts.init(document.getElementById('main'));
    myChart.setOption(option);
}
setTimeout(()=>{
    draw()
}, 500)
</script>


## 视频教程

<iframe src="//player.bilibili.com/player.html?aid=526561374&bvid=BV1VM411g7mR&cid=1070494623&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="width:800px;height:600px"> </iframe>

## 如何使用Excel绘制SPSS Process的简单斜率图

下载Excel地址： https://afdian.com/item/6eb619fccb0011ed868452540025c377


