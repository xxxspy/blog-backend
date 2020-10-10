---
title: P值显著性计算器
date: 2020-10-10 09:04:43
tags: [spss, 显著性]
---

<script src="/tfstats/tfstats.js"></script>

这是计算卡方分布/T分布/F分布P值(显著性)的计算器, 做这个小程序的目的是因为现在很多学生学习统计的时候会自己计算一些统计量, 比如卡方和t分数等, 
我们知道这些值以后需要根据统计书上的附录查表才能知道这些值对应的P值, 比较麻烦, 所以我就想, 既然P值是可以直接计算得到, 
我们就做一个计算器吧!

<!-- more -->

### 卡方计算器

{% raw %}
<table>
    <tr>
        <td>自由度</td><td>卡方值</td><td>P值</td>
    </tr>
    <tr>
        <td><input class="form-control" type="number" id="df1" step="1"></td>
        <td><input class="form-control" type="number" id="chi1"></td>
        <td><input class="form-control" type="number" id="p1" disabled></td>
    </tr>
    <tr>
        <td>
            <button class="btn btn-block" onclick="calculateChi()">计算</button>
        </td>
        <td colspan="2">
        </td>
    </tr>
</table>
<script>
    function calculateChi(){
        let df = $('#df1').val()
        let chi = $('#chi1').val()
        if(df!="" && chi!=""){
            try{
                df = parseInt(df)
                chi = parseFloat(chi)
                let cdf = tfstats.utils.jstat.chisquare.cdf;
                let p = 1-cdf(chi, df)
                $('#p1').val(p)

            }catch(e){
                console.log(e)
                alert('计算过程发生错误')
            }
        }else{
            alert('数据不全')
        }
    }
</script>
{% endraw %}

### T检验计算器


{% raw %}
<table>
    <tr>
        <td>自由度</td><td>T值</td><td>单侧</td><td>P值</td>
    </tr>
    <tr>
        <td><input class="form-control" type="number" id="df2" step="1"></td>
        <td><input class="form-control" type="number" id="t2"></td>
        <td><input class="form-control" type="checkbox" id="side2"></td>
        <td><input class="form-control" type="number" id="p2" disabled></td>
    </tr>
    <tr>
        <td>
            <button class="btn btn-block" onclick="calculateTtest()">计算</button>
        </td>
        <td colspan="3">
        </td>
    </tr>
</table>
<script>
    function calculateTtest(){
        let df = $('#df2').val()
        let t = $('#t2').val()
        let side = $('#side2').prop('checked') ? 1:2 ;
        if(df!="" && t!=""){
            try{
                df = parseInt(df)
                t = parseFloat(t)
                console.log(`t:${t}, df:${df}, type:${typeof df}`)
                let cdf = tfstats.utils.jstat.studentt.cdf;
                console.log('cdf:'+cdf(t, df))
                let p = 1-cdf(t, df)
                if(side==2){
                    p = p*2
                }
                $('#p2').val(p)

            }catch(e){
                console.log(e)
                alert('计算过程发生错误')
            }
        }else{
            alert('数据不全')
        }
    }
</script>
{% endraw %}

### F检验

  


{% raw %}
<table>
    <tr>
        <td>自由度1</td><td>自由度2</td><td>F值</td><td>P值</td>
    </tr>
    <tr>
        <td><input class="form-control" type="number" id="df13" step="1"></td>
        <td><input class="form-control" type="number" id="df23" step="1"></td>
        <td><input class="form-control" type="number" id="f3"></td>
        <td><input class="form-control" type="number" id="p3" disabled></td>
    </tr>
    <tr>
        <td>
            <button class="btn btn-block" onclick="calculateFtest()">计算</button>
        </td>
        <td colspan="3">
        </td>
    </tr>
</table>
<script>
    function calculateFtest(){
        let df1 = $('#df13').val()
        let df2 = $('#df23').val()
        let f = $('#f3').val()
        if(df1!="" && df2!="" && f!=""){
            try{
                df1 = parseInt(df1)
                df2 = parseInt(df2)
                f = parseFloat(f)
                let cdf = tfstats.utils.jstat.centralF.cdf;
                let p = 1-cdf(f, df1, df2)
                $('#p3').val(p)
            }catch(e){
                console.log(e)
                alert('计算过程发生错误')
            }
        }else{
            alert('数据不全')
        }
    }
</script>
{% endraw %}