
---
title: pandas数据分析100道练习题-第二部分
date: 2018-08-15 18:17:55
tags: [python, pandas]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---
<span></span>
<!-- more -->


这篇文章收集了网友们使用pandas进行数据分析时经常遇到的问题, 这些问题也可以检验你使用pandas的熟练程度, 所以他们更像是一个学习教材, 掌握这些技能, 可以使你数据数据分析的工作事半功倍。第一部分pandas练习题请访问: [pandas数据分析100道练习题-第一部分](http://mlln.cn/2018/08/13/pandas%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90100%E9%81%93%E7%BB%83%E4%B9%A0%E9%A2%98-%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86/), 下面是第二部分:

### series如何将一日期字符串转换为时间


```python
import pandas as pd
ser = pd.Series(['01 Jan 2010', 
                '02-02-2011', 
                 '20120303', 
                 '2013/04/04', 
                 '2014-05-05', 
                 '2015-06-06T12:20'])

pd.to_datetime(ser)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0   2010-01-01 00:00:00
    <br />1   2011-02-02 00:00:00
    <br />2   2012-03-03 00:00:00
    <br />3   2013-04-04 00:00:00
    <br />4   2014-05-05 00:00:00
    <br />5   2015-06-06 12:20:00
    <br />dtype: datetime64[ns]

</div>
{% endraw %}



### series如何从时间序列中提取年/月/天/小时/分钟/秒


```python
date = pd.Series(['01 Jan 2010', 
                '02-02-2011', 
                 '20120303', 
                 '2013/04/04', 
                 '2014-05-05', 
                 '2015-06-06T12:20'])
date = pd.to_datetime(date)
date.dt.year
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    2010
    <br />1    2011
    <br />2    2012
    <br />3    2013
    <br />4    2014
    <br />5    2015
    <br />dtype: int64

</div>
{% endraw %}




```python
date.dt.month
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    1
    <br />1    2
    <br />2    3
    <br />3    4
    <br />4    5
    <br />5    6
    <br />dtype: int64

</div>
{% endraw %}




```python
date.dt.day
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    1
    <br />1    2
    <br />2    3
    <br />3    4
    <br />4    5
    <br />5    6
    <br />dtype: int64

</div>
{% endraw %}




```python
date.dt.hour
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0     0
    <br />1     0
    <br />2     0
    <br />3     0
    <br />4     0
    <br />5    12
    <br />dtype: int64

</div>
{% endraw %}



### 从series中找出包含两个以上元音字母的单词


```python
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])

def count(x):
    aims = 'aeiou'
    c= 0
    for i in x:
        if i in aims:
            c += 1
    return c

counts = ser.map(lambda x: count(x))
ser[counts>=2]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    1    Orange
    <br />4     Money
    <br />dtype: object

</div>
{% endraw %}



### 如何过滤series中的有效电子邮件


```python
emails = pd.Series(['buying books at amazom.com', 
                    'rameses@egypt.com', 
                    'matt@t.co',
                    'narendra@modi.com'])

import re
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
valid = emails.str.findall(pattern, flags=re.IGNORECASE)
[x[0] for x in valid if len(x)]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    ['rameses@egypt.com', 'matt@t.co', 'narendra@modi.com']

</div>
{% endraw %}



### series A 以series B为分组依据, 然后计算分组后的平均值


```python
import numpy as np
fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

weights.groupby(fruit).mean()

```




{% raw %}
<div class="output">
输出(plain):<br/>

    apple     9.00
    <br />banana    4.75
    <br />carrot    3.00
    <br />dtype: float64

</div>
{% endraw %}



### 如何计算两个系列之间的欧氏距离


```python
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

sum((p - q)**2)**.5
```




{% raw %}
<div class="output">
输出(plain):<br/>

    18.16590212458495

</div>
{% endraw %}



### 如何在数字系列中查找所有局部最大值（或峰值）


```python
ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])
dd = np.diff(np.sign(np.diff(ser)))
peak_locs = np.where(dd == -2)[0] + 1
peak_locs
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([1, 5, 7], dtype=int64)

</div>
{% endraw %}



### 如何创建一个以'2000-01-02'开始包含10个周六的TimeSeries


```python
pd.Series(np.random.randint(1,10,10), 
          pd.date_range('2000-01-02', 
                        periods=10, 
                        freq='W-SAT'))
```




{% raw %}
<div class="output">
输出(plain):<br/>

    2000-01-08    5
    <br />2000-01-15    4
    <br />2000-01-22    2
    <br />2000-01-29    1
    <br />2000-02-05    4
    <br />2000-02-12    8
    <br />2000-02-19    1
    <br />2000-02-26    6
    <br />2000-03-04    6
    <br />2000-03-11    2
    <br />Freq: W-SAT, dtype: int32

</div>
{% endraw %}



### 如何填补TimeSeires的缺失日期


```python
ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01',
                                                       '2000-01-03', 
                                                       '2000-01-06', 
                                                       '2000-01-08']))
# 使用前一个日期的数据填补
ser.resample('D').ffill()
# 如果使用后一个日期的数据填补, 可以使用bfill方法
```




{% raw %}
<div class="output">
输出(plain):<br/>

    2000-01-01     1.0
    <br />2000-01-02     1.0
    <br />2000-01-03    10.0
    <br />2000-01-04    10.0
    <br />2000-01-05    10.0
    <br />2000-01-06     3.0
    <br />2000-01-07     3.0
    <br />2000-01-08     NaN
    <br />Freq: D, dtype: float64

</div>
{% endraw %}



### 如何计算series的自相关


```python
ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))
autocorrelations = [ser.autocorr(i).round(2) for i in range(11)]

autocorrelations
```




{% raw %}
<div class="output">
输出(plain):<br/>

    [1.0, 0.38, 0.12, 0.17, 0.44, 0.48, 0.25, -0.31, -0.1, 0.65, 0.05]

</div>
{% endraw %}



### 读取csv时, 间隔几行读取数据


```python
# 生成用于测试的csv
fpath = 'testt.csv'
df = pd.DataFrame({'a': range(100), 
                   'b':np.random.choice(['apple', 'banana', 'carrot'], 100)})
df.to_csv(fpath, index=None)
```


```python
### 隔行读取csv
import csv

with open(fpath, 'r') as f:
    reader = csv.reader(f)
    out = []
    for i, row in enumerate(reader):
        if i%20 ==0:
            out.append(row)
pd.DataFrame(out[1:], columns=out[0])
```




{% raw %}
<div class="output">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>19</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39</td>
      <td>carrot</td>
    </tr>
    <tr>
      <th>2</th>
      <td>59</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>3</th>
      <td>79</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>4</th>
      <td>99</td>
      <td>apple</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 读取csv时进行数据转换


```python
pd.read_csv(fpath, 
            converters={
                'a':lambda x: 'low' if int(x) < 50 else 'high'
            }).head()
```




{% raw %}
<div class="output">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>low</td>
      <td>carrot</td>
    </tr>
    <tr>
      <th>1</th>
      <td>low</td>
      <td>carrot</td>
    </tr>
    <tr>
      <th>2</th>
      <td>low</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>3</th>
      <td>low</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>4</th>
      <td>low</td>
      <td>apple</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 读取csv时只读取某列


```python
pd.read_csv(fpath, usecols=['a']).head()
```




{% raw %}
<div class="output">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 读取dataframe每列的数据类型


```python
df=pd.DataFrame(
    {
        'a':range(100),
        'b':np.random.rand(100),
        'c':[1,2,3,4]*25,
        'd':['apple', 'banana', 'carrot']*33 + ['apple']
    }
)

df.dtypes
```




{% raw %}
<div class="output">
输出(plain):<br/>

    a      int64
    <br />b    float64
    <br />c      int64
    <br />d     object
    <br />dtype: object

</div>
{% endraw %}



### 读取dataframe的行数和列数


```python
df.shape
```




{% raw %}
<div class="output">
输出(plain):<br/>

    (100, 4)

</div>
{% endraw %}



### 获取dataframe每列的基本描述统计


```python

df.describe()
```




{% raw %}
<div class="output">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>100.000000</td>
      <td>100.000000</td>
      <td>100.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>49.500000</td>
      <td>0.515885</td>
      <td>2.500000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>29.011492</td>
      <td>0.281679</td>
      <td>1.123666</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000605</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>24.750000</td>
      <td>0.280289</td>
      <td>1.750000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>49.500000</td>
      <td>0.545348</td>
      <td>2.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>74.250000</td>
      <td>0.736113</td>
      <td>3.250000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>99.000000</td>
      <td>0.992075</td>
      <td>4.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 从dataframe中找到a列最大值对应的行


```python
df.loc[df.a==np.max(df.a)]
```




{% raw %}
<div class="output">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>99</th>
      <td>99</td>
      <td>0.598169</td>
      <td>4</td>
      <td>apple</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 从dataframe中获取c列最大值所在的行号


```python
np.where(df.c==np.max(df.c))
```




{% raw %}
<div class="output">
输出(plain):<br/>

    (array([ 3,  7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67,
    <br />        71, 75, 79, 83, 87, 91, 95, 99], dtype=int64),)

</div>
{% endraw %}



### 在dataframe中根据行列数读取某个值


```python
row = 4
col = 0
print(f'行{row}列{col}的值是: {df.iat[row, col]}')
row = 4
col = 2
print(f'行{row}列{col}的值是: {df.iat[row, col]}')
row = 0
col = 0
print(f'行{row}列{col}的值是: {df.iat[row, col]}')
row = 33
col = 3
print(f'行{row}列{col}的值是: {df.iat[row, col]}')
```

{% raw %}
<div class="output">
输出(stream):<br>
    行4列0的值是: 4
    <br />行4列2的值是: 1
    <br />行0列0的值是: 0
    <br />行33列3的值是: apple
    <br />
</div>
{% endraw %}

### 在dataframe中根据index和列名称读取某个值


```python
index = 0
col = 'd'
print(f'index={index}, col={col} : {df.at[index, col]}')
index = 2
col = 'd'
print(f'index={index}, col={col} : {df.at[index, col]}')
index = 4
col = 'd'
print(f'index={index}, col={col} : {df.at[index, col]}')
index = 5
col = 'c'
print(f'index={index}, col={col} : {df.at[index, col]}')
```

{% raw %}
<div class="output">
输出(stream):<br>
    index=0, col=d : apple
    <br />index=2, col=d : carrot
    <br />index=4, col=d : banana
    <br />index=5, col=c : 2
    <br />
</div>
{% endraw %}

### dataframe中重命名某一列


```python
df.rename(columns={'d':'fruit'}).head()
```




{% raw %}
<div class="output">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>fruit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.406456</td>
      <td>1</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.607407</td>
      <td>2</td>
      <td>banana</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.197953</td>
      <td>3</td>
      <td>carrot</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.279180</td>
      <td>4</td>
      <td>apple</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.193107</td>
      <td>1</td>
      <td>banana</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



今天的教程就到此为止了, 希望大家关注我的小站mlln.cn, 后面还会有关于pandas系列的练习题, 希望这些工作能帮助你学习pandas, 或者在面试的时候应付面试题。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas数据分析100道练习题-第二部分.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
