
---
title: pandas数据分析100道练习题-第一部分
date: 2018-08-13 18:17:55
tags: [python, pandas]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---
<span></span>
<!-- more -->


这篇文章收集了网友们使用pandas进行数据分析时经常遇到的问题, 这些问题也可以检验你使用pandas的熟练程度, 所以他们更像是一个学习教材, 掌握这些技能, 可以使你数据数据分析的工作事半功倍。

### 如何引入pandas并查看版本


```python
import pandas as pd
print(pd.__version__)
print(pd.show_versions(as_json=True))
```

{% raw %}
<div class="output">
输出(stream):<br>
    0.23.0
    <br />{'system': {'commit': None, 'python': '3.6.4.final.0', 'python-bits': 64, 'OS': 'Windows', 'OS-release': '10', 'machine': 'AMD64', 'processor': 'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel', 'byteorder': 'little', 'LC_ALL': 'None', 'LANG': 'None', 'LOCALE': 'None.None'}, 'dependencies': {'pandas': '0.23.0', 'pytest': None, 'pip': '9.0.1', 'setuptools': '28.8.0', 'Cython': None, 'numpy': '1.14.3', 'scipy': '1.1.0', 'pyarrow': None, 'xarray': None, 'IPython': '6.4.0', 'sphinx': None, 'patsy': None, 'dateutil': '2.7.3', 'pytz': '2018.4', 'blosc': None, 'bottleneck': None, 'tables': None, 'numexpr': None, 'feather': None, 'matplotlib': '2.2.2', 'openpyxl': None, 'xlrd': '1.1.0', 'xlwt': '1.3.0', 'xlsxwriter': None, 'lxml': None, 'bs4': None, 'html5lib': '0.9999999', 'sqlalchemy': None, 'pymysql': None, 'psycopg2': None, 'jinja2': '2.10', 's3fs': None, 'fastparquet': None, 'pandas_gbq': None, 'pandas_datareader': None}}
    <br />None
    <br />
</div>
{% endraw %}

### list或numpy array或dict转pd.Series


```python
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
```


```python
# 方法
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)
print(ser3.head())
```

{% raw %}
<div class="output">
输出(stream):<br>
    a    0
    <br />b    1
    <br />c    2
    <br />e    3
    <br />d    4
    <br />dtype: int64
    <br />
</div>
{% endraw %}

### series的index转dataframe的column


```python
ser3.head()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    a    0
    <br />b    1
    <br />c    2
    <br />e    3
    <br />d    4
    <br />dtype: int64

</div>
{% endraw %}




```python
df = ser3.to_frame().reset_index()
print(df.head())
```

{% raw %}
<div class="output">
输出(stream):<br>
      index  0
    <br />0     a  0
    <br />1     b  1
    <br />2     c  2
    <br />3     e  3
    <br />4     d  4
    <br />
</div>
{% endraw %}

### 多个series合并成一个dataframe


```python
df = pd.DataFrame({'col1': ser1, 'col2': ser2})
print(df.head())
```

{% raw %}
<div class="output">
输出(stream):<br>
      col1  col2
    <br />0    a     0
    <br />1    b     1
    <br />2    c     2
    <br />3    e     3
    <br />4    d     4
    <br />
</div>
{% endraw %}

### 根据index, 多个series合并成dataframe


```python
# 选择部分数据进行合并, 便与看到合并效果
s1 = ser1[:16]
s2 = ser2[14:]
s1
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0     a
    <br />1     b
    <br />2     c
    <br />3     e
    <br />4     d
    <br />5     f
    <br />6     g
    <br />7     h
    <br />8     i
    <br />9     j
    <br />10    k
    <br />11    l
    <br />12    m
    <br />13    n
    <br />14    o
    <br />15    p
    <br />dtype: object

</div>
{% endraw %}




```python
pd.concat([s1, s2], axis=1)
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>e</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>f</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>g</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>h</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>i</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>j</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>k</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>l</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>m</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>n</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>o</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>p</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>NaN</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>NaN</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>NaN</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>NaN</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>NaN</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>NaN</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>NaN</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>23.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>NaN</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>NaN</td>
      <td>25.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 头尾拼接两个series


```python
pd.concat([s1, s2], axis=0)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0      a
    <br />1      b
    <br />2      c
    <br />3      e
    <br />4      d
    <br />5      f
    <br />6      g
    <br />7      h
    <br />8      i
    <br />9      j
    <br />10     k
    <br />11     l
    <br />12     m
    <br />13     n
    <br />14     o
    <br />15     p
    <br />14    14
    <br />15    15
    <br />16    16
    <br />17    17
    <br />18    18
    <br />19    19
    <br />20    20
    <br />21    21
    <br />22    22
    <br />23    23
    <br />24    24
    <br />25    25
    <br />dtype: object

</div>
{% endraw %}



### 找到元素 在series A中不在series B中


```python
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser1[~ser1.isin(ser2)]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    1
    <br />1    2
    <br />2    3
    <br />dtype: int64

</div>
{% endraw %}



### 两个seiries的并集


```python
np.union1d(ser1, ser2)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([1, 2, 3, 4, 5, 6, 7, 8], dtype=int64)

</div>
{% endraw %}



### 两个series的交集


```python
np.intersect1d(ser1, ser2)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([4, 5], dtype=int64)

</div>
{% endraw %}



### 两个series的非共有元素


```python
u = pd.Series(np.union1d(ser1, ser2))
i = pd.Series(np.intersect1d(ser1, ser2))
u[~u.isin(i)]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    1
    <br />1    2
    <br />2    3
    <br />5    6
    <br />6    7
    <br />7    8
    <br />dtype: int64

</div>
{% endraw %}



### 如何获得series的最小值，第25百分位数，中位数，第75位和最大值？


```python
ser = pd.Series(np.random.normal(10, 5, 25))
np.random.RandomState(100)
np.percentile(ser, q=[0, 25, 50, 75, 100])
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([-1.2740299 ,  5.82920931,  8.64214184, 10.8035798 , 18.08081406])

</div>
{% endraw %}



### 如何获得系列中唯一项目的频率计数？


```python
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

ser.value_counts()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    g    5
    <br />b    5
    <br />e    4
    <br />f    4
    <br />d    4
    <br />a    4
    <br />c    2
    <br />h    2
    <br />dtype: int64

</div>
{% endraw %}



### series中计数排名前2的元素


```python
v_cnt = ser.value_counts()
cnt_cnt=v_cnt.value_counts().index[:2]
cnt_cnt
```




{% raw %}
<div class="output">
输出(plain):<br/>

    Int64Index([4, 5], dtype='int64')

</div>
{% endraw %}




```python
index = v_cnt[v_cnt.isin(cnt_cnt)].index
index
```




{% raw %}
<div class="output">
输出(plain):<br/>

    Index(['g', 'b', 'e', 'f', 'd', 'a'], dtype='object')

</div>
{% endraw %}



### 如何将数字系列分成10个相同大小的组


```python
ser = pd.Series(np.random.random(20))
ser.head()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    0.888218
    <br />1    0.938604
    <br />2    0.859850
    <br />3    0.434301
    <br />4    0.851859
    <br />dtype: float64

</div>
{% endraw %}




```python
groups = pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1], 
        labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th'])
groups.head()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0     8th
    <br />1    10th
    <br />2     7th
    <br />3     4th
    <br />4     6th
    <br />dtype: category
    <br />Categories (10, object): [1st < 2nd < 3rd < 4th ... 7th < 8th < 9th < 10th]

</div>
{% endraw %}



### 如何将numpy数组转换为给定形状的dataframe


```python
ser = pd.Series(np.random.randint(1, 10, 35))
df = pd.DataFrame(ser.values.reshape(7,5))
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
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>7</td>
      <td>3</td>
      <td>6</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>5</td>
      <td>4</td>
      <td>7</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>8</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>8</td>
      <td>7</td>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>5</td>
      <td>9</td>
      <td>9</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 如何从一系列中找到2的倍数的数字位置


```python
ser = pd.Series(np.random.randint(1, 10, 7))
ser
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    8
    <br />1    9
    <br />2    8
    <br />3    5
    <br />4    3
    <br />5    6
    <br />6    3
    <br />dtype: int32

</div>
{% endraw %}




```python
np.argwhere(ser % 2==0)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([[0],
    <br />       [2],
    <br />       [5]], dtype=int64)

</div>
{% endraw %}



### 如何从系列中的给定位置提取项目


```python
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
ser.take(pos)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0     a
    <br />4     e
    <br />8     i
    <br />14    o
    <br />20    u
    <br />dtype: object

</div>
{% endraw %}



### 获取元素的位置


```python
aims = list('adhz')
[pd.Index(ser).get_loc(i) for i in aims]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    [0, 3, 7, 25]

</div>
{% endraw %}



### 如何计算真值和预测序列的均方误差


```python
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
np.mean((truth-pred)**2)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0.18571414723876128

</div>
{% endraw %}



### 如何将系列中每个元素的第一个字符转换为大写


```python
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
ser.map(lambda x: x.title())
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0     How
    <br />1      To
    <br />2    Kick
    <br />3    Ass?
    <br />dtype: object

</div>
{% endraw %}



### 如何计算系列中每个单词的字符数


```python
ser.map(lambda x: len(x))
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    3
    <br />1    2
    <br />2    4
    <br />3    4
    <br />dtype: int64

</div>
{% endraw %}



### 如何计算时间序列数据的差分


```python
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

# 一级差分
ser.diff()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    NaN
    <br />1    2.0
    <br />2    3.0
    <br />3    4.0
    <br />4    5.0
    <br />5    6.0
    <br />6    6.0
    <br />7    8.0
    <br />dtype: float64

</div>
{% endraw %}




```python
# 二级差分
ser.diff().diff()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    NaN
    <br />1    NaN
    <br />2    1.0
    <br />3    1.0
    <br />4    1.0
    <br />5    1.0
    <br />6    0.0
    <br />7    2.0
    <br />dtype: float64

</div>
{% endraw %}




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas数据分析100道练习题-第一部分.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
