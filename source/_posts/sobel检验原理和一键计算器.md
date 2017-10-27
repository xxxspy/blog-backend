---
title: sobel检验原理和一键计算器
date: 2017-10-10 08:19:30
tags: spss
---

sobel-test是在中介效应检验的过程中用到的，所以本文假设你已经理解了中介效应的原理，如果不懂，可以去看这2篇文章——{% post_link SPSS实例：[16]中介效应的检验过程 %}和{% post_link SPSS实例：[20]检验中介效应的操作方法 %}。

<!-- more -->

这里我们回顾一下中介效应涉及到的系数及其标准误：

{% asset_img mediation.jpg %}

图中变量的意义：

- IV 代表自变量
- DV 代表因变量
- Mediator 代表中介变量
- a 代表IV预测Mediator时的回归系数
- b 代表IV和Mediator预测DV时的Mediator的回归系数
- 图中的s都代表标准误(standard error)

三种test的公式如下：

```python
#Sobel test equation
z-value = a*b/SQRT(b2*sa2 + a2*sb2)

#Aroian test equation
z-value = a*b/SQRT(b2*sa2 + a2*sb2 + sa2*sb2)

#Goodman test equation
z-value = a*b/SQRT(b2*sa2 + a2*sb2 - sa2*sb2)
```

根据这三种公式，我们把相应的数据填入表格中，就可以计算得到z和p值。

{% raw %}
<form>
  <table cellpadding="1" cellspacing="1" border="1" bgcolor="#D7D7D7">
    <tbody><tr>
      <td>
        <table cellpadding="1" cellspacing="1" border="0" bgcolor="#D7D7D7">

          <tbody><tr><td colspan="1"></td>
              <td colspan="1"><center>Input:</center></td>
              <td colspan="1"></td>
              <td colspan="1"><center>Test statistic:</center></td>
              <td colspan="1"><center>Std. Error:</center></td>
              <td colspan="1"><center><i>p</i>-value:</center></td></tr>
          <tr><td colspan="1" align="right" style="vertical-align: middle"><center><i>a</i></center></td>
              <td colspan="1"><input type="text" class="form-control" name="a" size="4" tabindex="1" style="width: 95px"></td>
              <td colspan="1" align="right" style="vertical-align: middle">Sobel test:</td>
              <td colspan="1"><input type="text" class="form-control" name="sobel" size="5" tabindex="5" style="width: 95px"></td>
              <td colspan="1"><input type="text" class="form-control" name="sobelse" size="5" tabindex="8" style="width: 95px"></td>
              <td colspan="1"><input type="text" class="form-control" name="sobelp" size="5" tabindex="11" style="width: 95px"></td></tr>
          <tr><td colspan="1" align="right" style="vertical-align: middle"><center><i>b</i></center></td>
              <td colspan="1"><input type="text" class="form-control" name="b" size="4" tabindex="2" style="width: 95px"></td>
              <td colspan="1" align="right" style="vertical-align: middle">Aroian test:</td>
              <td colspan="1"><input type="text" class="form-control" name="goodi" size="5" tabindex="6" style="width: 95px"></td>
              <td colspan="1"><input type="text" class="form-control" name="goodise" size="5" tabindex="9" style="width: 95px"></td>
              <td colspan="1"><input type="text" class="form-control" name="goodip" size="5" tabindex="12" style="width: 95px"></td></tr>
          <tr><td colspan="1" align="right" style="vertical-align: middle"><center><i>s</i><sub>a</sub></center></td>
              <td colspan="1"><input type="text" class="form-control" name="sa" size="4" tabindex="3" style="width: 95px"></td>
              <td colspan="1" align="right" style="vertical-align: middle">Goodman test:</td>
              <td colspan="1"><input type="text" class="form-control" name="goodii" size="5" tabindex="7" style="width: 95px"></td>
              <td colspan="1"><input type="text" class="form-control" name="goodiise" size="5" tabindex="10" style="width: 95px"></td>
              <td colspan="1"><input type="text" class="form-control" name="goodiip" size="5" tabindex="13" style="width: 95px"></td></tr>
          <tr><td colspan="1" align="right" style="vertical-align: middle"><center><i>s</i><sub>b</sub></center></td>
              <td colspan="1"><input type="text" class="form-control" name="sb" size="4" tabindex="4" style="width: 95px"></td>
              <td colspan="1"><input class="btn btn-default" type="RESET" value="Reset all" tabindex="15" style="width: 100%"></td>
              <td colspan="3"><input type="BUTTON" class="btn btn-primary" value="Calculate" tabindex="14" onclick="Calc(this.form)" style="width: 100%"></td></tr>

        </tbody></table>
      </td>
    </tr>
  </tbody></table>
</form>
<script language="JavaScript">

var Pi=Math.PI; var PiD2=Pi/2; var PiD4=Pi/4; var Pi2=2*Pi
function Sqrt(x) { return Math.sqrt(x) }
function Power(x,y) { return Math.pow(x,y) }
function ChiSq(x,n) { 
   if(n==1 & x>1000) {return 0} 
   if(x>1000 | n>1000) { 
       var q=ChiSq((x-n)*(x-n)/(2*n),1)/2 
       if(x>n) {return q} {return 1-q} 
       } 
   var p=Math.exp(-0.5*x); if((n%2)==1) { p=p*Math.sqrt(2*x/Pi) } 
   var k=n; while(k>=2) { p=p*x/k; k=k-2 } 
   var t=p; var a=n; while(t>0.0000000001*p) { a=a+2; t=t*x/a; p=p+t } 
   return 1-p 
   } 
function Norm(z) { return ChiSq(z*z,1) }
//This script and many more are available free online at
//The JavaScript Source!! http://javascript.internet.com

function round(number,X) {
// rounds number to X decimal places, defaults to 8
X = (!X ? 8 : X);
return Math.round(number*Math.pow(10,X))/Math.pow(10,X);
}
function Calc(form){ 
	{
		form.sobel.value = round((form.a.value)*(form.b.value)/Sqrt(Power(form.a.value,2)*Power(form.sb.value,2)+Power(form.b.value,2)*Power(form.sa.value,2)));
		form.goodi.value = round((form.a.value)*(form.b.value)/Sqrt(Power(form.a.value,2)*Power(form.sb.value,2)+Power(form.b.value,2)*Power(form.sa.value,2)+Power(form.sa.value,2)*Power(form.sb.value,2)));
		form.goodii.value = round((form.a.value)*(form.b.value)/Sqrt(Power(form.a.value,2)*Power(form.sb.value,2)+Power(form.b.value,2)*Power(form.sa.value,2)-Power(form.sa.value,2)*Power(form.sb.value,2)));
		form.sobelse.value = round(Sqrt(Power(form.a.value,2)*Power(form.sb.value,2)+Power(form.b.value,2)*Power(form.sa.value,2)));
		form.goodise.value = round(Sqrt(Power(form.a.value,2)*Power(form.sb.value,2)+Power(form.b.value,2)*Power(form.sa.value,2)+Power(form.sa.value,2)*Power(form.sb.value,2)));
		form.goodiise.value = round(Sqrt(Power(form.a.value,2)*Power(form.sb.value,2)+Power(form.b.value,2)*Power(form.sa.value,2)-Power(form.sa.value,2)*Power(form.sb.value,2)));
		form.sobelp.value = round(Norm(form.sobel.value));
		form.goodip.value = round(Norm(form.goodi.value));
		form.goodiip.value = round(Norm(form.goodii.value));
	}
}
function Calc2(form){ 
	{
	  form.sobel.value = round(1/Sqrt((1/(Power(form.tb.value,2)))+(1/(Power(form.ta.value,2)))));
		form.goodi.value = round(1/Sqrt((1/(Power(form.tb.value,2)))+(1/(Power(form.ta.value,2)))+(1/(Power(form.ta.value,2)*Power(form.tb.value,2)))));
		form.goodii.value = round(1/Sqrt((1/(Power(form.tb.value,2)))+(1/(Power(form.ta.value,2)))-(1/(Power(form.ta.value,2)*Power(form.tb.value,2)))));
		form.sobelp.value = round(Norm(form.sobel.value));
		form.goodip.value = round(Norm(form.goodi.value));
		form.goodiip.value = round(Norm(form.goodii.value));
	}
}
function Calc3(form){ 
	{
    sab=form.sab.value/1
	  if (Power((sab/((form.sa.value)*(form.sb.value))),2)>1) {
	    if (sab<0) {
	      sab=(form.sa.value)*(form.sb.value)*(-1)
      }
	    if (sab>0) {
	      sab=(form.sa.value)*(form.sb.value)
      }
	 }
	form.sobel.value = round(((form.a.value)*(form.b.value)+(form.sab.value))/Sqrt(Power(form.b.value,2)*Power(form.sa.value,2)+Power(form.a.value,2)*Power(form.sb.value,2)+Power(form.sa.value,2)*Power(form.sb.value,2)+2*(form.a.value)*(form.b.value)*sab+Power(sab,2)),4);
		form.sobelp.value = round(Norm(form.sobel.value));
	}
}
</script>
{% endraw %}