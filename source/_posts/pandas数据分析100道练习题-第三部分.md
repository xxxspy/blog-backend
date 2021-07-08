
---
title: pandas数据分析100道练习题-第三部分
date: 2018-08-16 18:17:55
tags: [python, pandas]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---
<span></span>
<!-- more -->


这篇文章收集了网友们使用pandas进行数据分析时经常遇到的问题, 这些问题也可以检验你使用pandas的熟练程度, 所以他们更像是一个学习教材, 掌握这些技能, 可以使你数据数据分析的工作事半功倍。

- 第一部分pandas练习题请访问: [pandas数据分析100道练习题-第一部分](http://mlln.cn/2018/08/13/pandas%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90100%E9%81%93%E7%BB%83%E4%B9%A0%E9%A2%98-%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86/)
- 第二部分pandas练习题请访问: [pandas数据分析100道练习题-第二部分](http://mlln.cn/2018/08/15/pandas数据分析100道练习题-第二部分/)

下面是第三部分:

### 检查dataframe是否有缺失值


```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'a':[1.2,2,3,4],
    'b':list('abcd')
})

print('缺失:', df.isnull().values.any())
df.iat[0,0] = np.nan
print('缺失:', df.isnull().values.any())

```

{% raw %}
<div class="output">
输出(stream):<br>
    缺失: False
    <br />缺失: True
    <br />
</div>
{% endraw %}

### 统计dataframe中每列缺失值的数量


```python
df.apply(lambda x: x.isnull().sum())
```




{% raw %}
<div class="output">
输出(plain):<br/>

    a    1
    <br />b    0
    <br />dtype: int64

</div>
{% endraw %}



### dataframe用每列的平均值取代缺失值


```python
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df[['Min.Price', 'Max.Price']].head()
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
      <th>Min.Price</th>
      <th>Max.Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>12.9</td>
      <td>18.8</td>
    </tr>
    <tr>
      <th>1</th>
      <td>29.2</td>
      <td>38.7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>25.9</td>
      <td>32.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>44.6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
# 仅使用['Min.Price', 'Max.Price']这两列演示
df[['Min.Price', 'Max.Price']].apply(lambda x: x.fillna(x.mean())).head()
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
      <th>Min.Price</th>
      <th>Max.Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>12.900000</td>
      <td>18.800000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>29.200000</td>
      <td>38.700000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>25.900000</td>
      <td>32.300000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17.118605</td>
      <td>44.600000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.118605</td>
      <td>21.459091</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 从dataframe中获取某一列, 并返回一个dataframe


```python
# 只要传入一个list作为切片
df[['Manufacturer']].head()
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
      <th>Manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Acura</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Audi</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Audi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BMW</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### dataframe如何改变列的顺序


```python
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
df.head()
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
df[list('cbdae')]
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
      <th>c</th>
      <th>b</th>
      <th>d</th>
      <th>a</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>6</td>
      <td>8</td>
      <td>5</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12</td>
      <td>11</td>
      <td>13</td>
      <td>10</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>16</td>
      <td>18</td>
      <td>15</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 设置dataframe输出的行数和列数


```python
# 设置之前
df
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
pd.set_option('display.max_columns', 4)
pd.set_option('display.max_rows', 4)
# 设置之后
df
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
      <th>...</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>...</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>...</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>...</td>
      <td>18</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 5 columns</p>
</div>
</div>
{% endraw %}




```python
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)
```

### 设置dataframe输出时不使用科学记数法


```python
pd.DataFrame(np.random.random(4)**10, columns=['random'])
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
      <th>random</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.285027e-07</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.580650e-05</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.049461e-01</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6.873938e-06</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.DataFrame(np.random.random(4)**10, columns=['random'])
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
      <th>random</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.9207</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0209</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0000</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
# 恢复默认值
pd.set_option('display.float_format', None)
pd.DataFrame(np.random.random(4)**10, columns=['random'])
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
      <th>random</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.004970</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.018763</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.000058</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.252180</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 设置dataframe输出百分比数据


```python
df = pd.DataFrame(np.random.random(4), columns=['random'])
df
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
      <th>random</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.343280</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.700357</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.885307</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.932272</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
df.style.format({'random':'{0:.2%}'.format})
```




{% raw %}
<div class="output">
输出(html):<br>
<style  type="text/css" >
</style>  
<table id="T_fd251854_a0e2_11e8_a730_001a7dda7111" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >random</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_fd251854_a0e2_11e8_a730_001a7dda7111level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_fd251854_a0e2_11e8_a730_001a7dda7111row0_col0" class="data row0 col0" >34.33%</td> 
    </tr>    <tr> 
        <th id="T_fd251854_a0e2_11e8_a730_001a7dda7111level0_row1" class="row_heading level0 row1" >1</th> 
        <td id="T_fd251854_a0e2_11e8_a730_001a7dda7111row1_col0" class="data row1 col0" >70.04%</td> 
    </tr>    <tr> 
        <th id="T_fd251854_a0e2_11e8_a730_001a7dda7111level0_row2" class="row_heading level0 row2" >2</th> 
        <td id="T_fd251854_a0e2_11e8_a730_001a7dda7111row2_col0" class="data row2 col0" >88.53%</td> 
    </tr>    <tr> 
        <th id="T_fd251854_a0e2_11e8_a730_001a7dda7111level0_row3" class="row_heading level0 row3" >3</th> 
        <td id="T_fd251854_a0e2_11e8_a730_001a7dda7111row3_col0" class="data row3 col0" >93.23%</td> 
    </tr></tbody> 
</table> 
</div>
{% endraw %}



> 知识点:

> 使用百分号可以自动将数据转换为百分比格式:
> `'{0:.2%}'.format(0.555555)`

更多字符串格式化问题,可以看这篇专题: [python3字符串format最佳实践](http://mlln.cn/2018/07/19/python3%E5%AD%97%E7%AC%A6%E4%B8%B2format%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)

### 使用多个列创建唯一索引(index)


```python
df = pd.read_csv(
    'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', 
    usecols=[0,1,2,3,5])
```


```python
df[['Manufacturer', 'Model', 'Type']] = df[['Manufacturer', 'Model', 'Type']].fillna('missing')
df.index = df.Manufacturer + '_' + df.Model + '_' + df.Type
print(df.index.is_unique)
```

{% raw %}
<div class="output">
输出(stream):<br>
    True
    <br />
</div>
{% endraw %}

### 获取第n大的数所在行


```python
df = pd.DataFrame(
    np.random.randint(1, 30, 30).reshape(10,-1), 
    columns=list('abc'))
df['a']

```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    21
    <br />1    17
    <br />2    19
    <br />3     3
    <br />4     2
    <br />5     3
    <br />6    10
    <br />7     5
    <br />8    25
    <br />9    12
    <br />Name: a, dtype: int32

</div>
{% endraw %}




```python
# 使用行号排序
df['a'].argsort()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    4
    <br />1    3
    <br />2    5
    <br />3    7
    <br />4    6
    <br />5    9
    <br />6    1
    <br />7    2
    <br />8    0
    <br />9    8
    <br />Name: a, dtype: int64

</div>
{% endraw %}




```python
# 可以这样看到原始数据的排序

df['a'][df['a'].argsort()]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    4     2
    <br />3     3
    <br />5     3
    <br />7     5
    <br />6    10
    <br />9    12
    <br />1    17
    <br />2    19
    <br />0    21
    <br />8    25
    <br />Name: a, dtype: int32

</div>
{% endraw %}




```python
n = 5
df['a'].argsort()[::-1][n]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    3

</div>
{% endraw %}



### dataframe获取行之和大于100的数据, 并返回最后的两行


```python
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rowsums = df.apply(np.sum, axis=1)
last_two_rows = df.iloc[np.where(rowsums > 100)[0][-2:], :]
last_two_rows
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13</th>
      <td>39</td>
      <td>31</td>
      <td>35</td>
      <td>15</td>
    </tr>
    <tr>
      <th>14</th>
      <td>30</td>
      <td>22</td>
      <td>25</td>
      <td>31</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 如何从系列或数据框列中查找和限制异常值

用相应的5％分位数和95％分位数值替换低于5％分位数和大于95％分位数的所有值


```python
# Input
ser = pd.Series(np.logspace(-2, 2, 30))

# Solution
def cap_outliers(ser, low_perc, high_perc):
    low, high = ser.quantile([low_perc, high_perc])
    print(low_perc, '%ile: ', low, '|', high_perc, '%ile: ', high)
    ser[ser < low] = low
    ser[ser > high] = high
    return(ser)

capped_ser = cap_outliers(ser, .05, .95)
```

{% raw %}
<div class="output">
输出(stream):<br>
    0.05 %ile:  0.016049294076965887 | 0.95 %ile:  63.876672220183934
    <br />
</div>
{% endraw %}

### 如何在删除负值后将dataframe重新整形为最大可能的正方形


将df重塑为最大可能的正方形，并删除负值。如果需要，删除最小值。结果中正数的顺序应保持与原始顺序相同。


```python
df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
print(df)
```

{% raw %}
<div class="output">
输出(stream):<br>
        0   1   2   3   4   5   6   7   8   9
    <br />0  12  -6 -15  14  33  -9 -14  46   7   6
    <br />1  23  -5  13  22 -10  35  -8   8 -20  34
    <br />2  19  49  18  -1   5  22  38  -5  27  34
    <br />3 -12  47  21   9  45  18   3 -10  27  42
    <br />4  48  32  41 -14   5  40  33  -3  10  11
    <br />5  17  -2  13  47  28   5  24  26  -7  10
    <br />6  49  21  14 -16  12 -17   3  43   8 -10
    <br />7  17 -19 -14   2  -8 -10   1  25  -9  48
    <br />8  25  46  -7  36 -13  18  42  31  49  37
    <br />9   2  25  47  28   9  49  10  44 -15  12
    <br />
</div>
{% endraw %}


```python
# 步骤1:删除负数

arr = df[df > 0].values.flatten()
arr_qualified = arr[~np.isnan(arr)]
arr_qualified
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([12., 14., 33., 46.,  7.,  6., 23., 13., 22., 35.,  8., 34., 19.,
    <br />       49., 18.,  5., 22., 38., 27., 34., 47., 21.,  9., 45., 18.,  3.,
    <br />       27., 42., 48., 32., 41.,  5., 40., 33., 10., 11., 17., 13., 47.,
    <br />       28.,  5., 24., 26., 10., 49., 21., 14., 12.,  3., 43.,  8., 17.,
    <br />        2.,  1., 25., 48., 25., 46., 36., 18., 42., 31., 49., 37.,  2.,
    <br />       25., 47., 28.,  9., 49., 10., 44., 12.])

</div>
{% endraw %}




```python
# 步骤2: 计算正方形的边长

n = int(np.floor(arr_qualified.shape[0]**.5))
n
```




{% raw %}
<div class="output">
输出(plain):<br/>

    8

</div>
{% endraw %}




```python
# 步骤3: 整形为要求的正方形
top_indexes = np.argsort(arr_qualified)[::-1]
output = np.take(arr_qualified, sorted(top_indexes[:n**2])).reshape(n, -1)
print(output)
```

{% raw %}
<div class="output">
输出(stream):<br>
    [[12. 14. 33. 46.  7. 23. 13. 22.]
    <br /> [35.  8. 34. 19. 49. 18. 22. 38.]
    <br /> [27. 34. 47. 21.  9. 45. 18. 27.]
    <br /> [42. 48. 32. 41. 40. 33. 10. 11.]
    <br /> [17. 13. 47. 28. 24. 26. 10. 49.]
    <br /> [21. 14. 12. 43.  8. 17. 25. 48.]
    <br /> [25. 46. 36. 18. 42. 31. 49. 37.]
    <br /> [25. 47. 28.  9. 49. 10. 44. 12.]]
    <br />
</div>
{% endraw %}

### 交换dataframe的两行

把第一行和第二行数据交换


```python
df = pd.DataFrame(np.arange(25).reshape(5, -1))
df
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
a, b = df.iloc[1, :].copy(), df.iloc[2, :].copy()
df.iloc[1, :], df.iloc[2, :] = b, a
df
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### dataframe行倒序排序


```python
df.iloc[::-1, :]
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 对分类数据进行one-hot编码

经常用于逻辑回归


```python
df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))
df
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
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
pd.concat([pd.get_dummies(df['a']), df[list('bcde')]], axis=1)
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
      <th>0</th>
      <th>5</th>
      <th>10</th>
      <th>15</th>
      <th>20</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
      <td>14</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>16</td>
      <td>17</td>
      <td>18</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>21</td>
      <td>22</td>
      <td>23</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 哪个列包含每行的最大值

求行最大值所在的列


```python
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1))
df.apply(np.argmax, axis=1)
```

{% raw %}
<div class="output">
输出(stream):<br>
    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\numpy\core\fromnumeric.py:52: FutureWarning: 'argmax' is deprecated, use 'idxmax' instead. The behavior of 'argmax'
    <br />will be corrected to return the positional maximum in the future.
    <br />Use 'series.values.argmax' to get the position of the maximum now.
    <br />  return getattr(obj, method)(*args, **kwds)
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    0    3
    <br />1    1
    <br />2    3
    <br />3    0
    <br />4    2
    <br />5    0
    <br />6    0
    <br />7    2
    <br />8    2
    <br />9    0
    <br />dtype: int64

</div>
{% endraw %}



### 计算 每行的最近行(使用欧几里得距离)


```python
nearest = {}
for i, row in df.iterrows():
    c = ((df - row)**2).sum(axis = 1).argsort()
    for j in c:
        if j != i:
            break
    nearest[i] = j
print(nearest)
```

{% raw %}
<div class="output">
输出(stream):<br>
    {0: 7, 1: 7, 2: 6, 3: 5, 4: 8, 5: 4, 6: 2, 7: 0, 8: 4, 9: 3}
    <br />
</div>
{% endraw %}

今天的教程就到此为止了, 希望大家关注我的小站mlln.cn, 后面还会有关于pandas系列的练习题, 希望这些工作能帮助你学习pandas. 如果你有什么意见或者建议, 请在微博@该用户已经被封, 并附带本文链接。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas数据分析100道练习题-第三部分.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
