
---
title: pandas数据分析100道练习题-第四部分
date: 2018-08-23 17:54:31
tags: [python, pandas]
toc: true
repl: "https://repl.it/@xxxspy/learn-pandas?lite=true"

---

<span></span>
<!-- more -->





这篇文章收集了网友们使用pandas进行数据分析时经常遇到的问题, 这些问题也可以检验你使用pandas的熟练程度, 所以他们更像是一个学习教材, 掌握这些技能, 可以使你数据数据分析的工作事半功倍。

- 第一部分pandas练习题请访问: [pandas数据分析100道练习题-第一部分](http://mlln.cn/2018/08/13/pandas%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90100%E9%81%93%E7%BB%83%E4%B9%A0%E9%A2%98-%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86/)
- 第二部分pandas练习题请访问: [pandas数据分析100道练习题-第二部分](http://mlln.cn/2018/08/15/pandas数据分析100道练习题-第二部分/)
- 第三部分pandas练习题请访问: [pandas数据分析100道练习题-第三部分](http://mlln.cn/2018/08/16/pandas数据分析100道练习题-第三部分/)
- 第四部分pandas练习题请访问: [pandas数据分析100道练习题-第三部分](http://mlln.cn/2018/08/23/pandas数据分析100道练习题-第四部分/)

下面是第四部分:

### 如何计算列之间的最大相关系数


```python
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randint(1,100, 80).reshape(8, -1), 
    columns=list('pqrstuvwxy'),
    index=list('abcdefgh')
)

abs_corrmat = np.abs(df.corr())
print(abs_corrmat)
max_corr = abs_corrmat.apply(lambda x: sorted(x)[-2])
print('Maximum Correlation possible for each column: ', np.round(max_corr.tolist(), 2))
```

{% raw %}
<div class="output">
输出(stream):<br>
              p         q         r         s         t         u         v  \
    <br />p  1.000000  0.268096  0.000000  0.552086  0.147951  0.229566  0.312353   
    <br />q  0.268096  1.000000  0.881994  0.169709  0.124291  0.542839  0.351897   
    <br />r  0.000000  0.881994  1.000000  0.254703  0.014796  0.335214  0.331702   
    <br />s  0.552086  0.169709  0.254703  1.000000  0.373359  0.355978  0.042473   
    <br />t  0.147951  0.124291  0.014796  0.373359  1.000000  0.564365  0.001794   
    <br />u  0.229566  0.542839  0.335214  0.355978  0.564365  1.000000  0.179641   
    <br />v  0.312353  0.351897  0.331702  0.042473  0.001794  0.179641  1.000000   
    <br />w  0.697658  0.343943  0.566769  0.424458  0.014227  0.489756  0.274991   
    <br />x  0.254656  0.431052  0.539917  0.434953  0.368824  0.275014  0.056530   
    <br />y  0.106323  0.121851  0.179469  0.236219  0.228056  0.141275  0.468257   
    <br />
    <br />          w         x         y  
    <br />p  0.697658  0.254656  0.106323  
    <br />q  0.343943  0.431052  0.121851  
    <br />r  0.566769  0.539917  0.179469  
    <br />s  0.424458  0.434953  0.236219  
    <br />t  0.014227  0.368824  0.228056  
    <br />u  0.489756  0.275014  0.141275  
    <br />v  0.274991  0.056530  0.468257  
    <br />w  1.000000  0.065845  0.124048  
    <br />x  0.065845  1.000000  0.364810  
    <br />y  0.124048  0.364810  1.000000  
    <br />Maximum Correlation possible for each column:  [0.7  0.88 0.88 0.55 0.56 0.56 0.47 0.7  0.54 0.47]
    <br />
</div>
{% endraw %}

### 计算每一行的最小值与最大值的比值


```python
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Solution 1
min_by_max = df.apply(lambda x: np.min(x)/np.max(x), axis=1)
min_by_max
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    0.074468
    <br />1    0.013514
    <br />2    0.101010
    <br />3    0.457447
    <br />4    0.040404
    <br />5    0.081633
    <br />6    0.024096
    <br />7    0.163265
    <br />dtype: float64

</div>
{% endraw %}



### 找到每行第二大的值

创建一个新列'penultimate'，它具有每行df的第二大值。


```python
# Input
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Solution
out = df.apply(lambda x: x.sort_values().unique()[-2], axis=1)
df['penultimate'] = out
print(df)
```

{% raw %}
<div class="output">
输出(stream):<br>
        0   1   2   3   4   5   6   7   8   9  penultimate
    <br />0  89  42  65  63   4  24  41  72  79  66           79
    <br />1  76  28  17  53  42  21  93  81   5  39           81
    <br />2  66  92  18  93  99  74  71  85  84  42           93
    <br />3  59  53  72  13   1  88  95  92  70  68           92
    <br />4  97  56  64  76  78  36  80  10  94  14           94
    <br />5  48  92  39  42   1  26  32   7  48  90           90
    <br />6  17   4  70  22  44  52  39  84  67  52           70
    <br />7  38  44  46  12  24  23  28  85  87  82           85
    <br />
</div>
{% endraw %}

### 如何正态化dataframe中的所有列


```python
# Input
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Solution Q1
out1 = df.apply(lambda x: ((x - x.mean())/x.std()).round(2))
print('Solution Q1\n',out1)

# Solution Q2
out2 = df.apply(lambda x: ((x.max() - x)/(x.max() - x.min())).round(2))
print('Solution Q2\n', out2)  
```

{% raw %}
<div class="output">
输出(stream):<br>
    Solution Q1
    <br />       0     1     2     3     4     5     6     7     8     9
    <br />0  0.25  1.05  1.21  0.39 -0.57  0.34 -0.42 -0.79 -1.18  0.90
    <br />1 -0.11 -0.12  1.24  0.07  1.15 -1.18  1.16  0.53  1.10 -0.32
    <br />2 -0.78  1.53 -1.54 -1.24  1.20  1.72  0.27  1.00  0.42  0.06
    <br />3 -0.04  0.81 -0.41 -1.14 -0.99 -0.40 -1.05 -1.06 -1.45 -1.28
    <br />4 -0.75 -1.05 -1.12 -0.05  1.20 -1.14 -1.22 -0.62 -0.09  0.15
    <br />5 -0.53 -0.63  0.43  1.48 -0.69 -0.40 -0.16 -1.10 -0.16  1.07
    <br />6  2.31 -0.60  0.01  1.17 -0.91  0.94  1.65  0.63 -0.09  0.95
    <br />7 -0.36 -1.02  0.18 -0.68 -0.40  0.12 -0.23  1.41  1.44 -1.54
    <br />Solution Q2
    <br />       0     1     2     3     4     5     6     7     8     9
    <br />0  0.67  0.19  0.01  0.40  0.81  0.48  0.72  0.88  0.91  0.06
    <br />1  0.78  0.64  0.00  0.52  0.02  1.00  0.17  0.35  0.12  0.53
    <br />2  1.00  0.00  1.00  1.00  0.00  0.00  0.48  0.16  0.35  0.39
    <br />3  0.76  0.28  0.59  0.97  1.00  0.73  0.94  0.99  1.00  0.90
    <br />4  0.99  1.00  0.85  0.56  0.00  0.99  1.00  0.81  0.53  0.35
    <br />5  0.92  0.84  0.29  0.00  0.87  0.73  0.63  1.00  0.55  0.00
    <br />6  0.00  0.83  0.44  0.11  0.97  0.27  0.00  0.31  0.53  0.05
    <br />7  0.86  0.99  0.38  0.79  0.73  0.55  0.66  0.00  0.00  1.00
    <br />
</div>
{% endraw %}

### 如何计算每行与上一行的相关？


```python
# Input
df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))

# Solution
[df.iloc[i].corr(df.iloc[i+1]).round(2) for i in range(df.shape[0])[:-1]]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    [-0.51, 0.11, -0.05, 0.02, 0.46, -0.69, -0.23]

</div>
{% endraw %}



### 如何用0填充dataframe的对角线上的数


```python
df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))

# Solution
for i in range(df.shape[0]):
    df.iat[i, i] = 0
    df.iat[df.shape[0]-i-1, i] = 0
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
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>71</td>
      <td>61</td>
      <td>38</td>
      <td>97</td>
      <td>22</td>
      <td>93</td>
      <td>36</td>
      <td>47</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11</td>
      <td>0</td>
      <td>11</td>
      <td>86</td>
      <td>46</td>
      <td>20</td>
      <td>60</td>
      <td>60</td>
      <td>0</td>
      <td>38</td>
    </tr>
    <tr>
      <th>2</th>
      <td>71</td>
      <td>88</td>
      <td>0</td>
      <td>11</td>
      <td>92</td>
      <td>25</td>
      <td>98</td>
      <td>0</td>
      <td>17</td>
      <td>69</td>
    </tr>
    <tr>
      <th>3</th>
      <td>27</td>
      <td>57</td>
      <td>2</td>
      <td>0</td>
      <td>49</td>
      <td>83</td>
      <td>0</td>
      <td>27</td>
      <td>3</td>
      <td>94</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>33</td>
      <td>61</td>
      <td>52</td>
      <td>0</td>
      <td>0</td>
      <td>50</td>
      <td>71</td>
      <td>96</td>
      <td>29</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>52</td>
      <td>32</td>
      <td>90</td>
      <td>0</td>
      <td>0</td>
      <td>59</td>
      <td>53</td>
      <td>15</td>
      <td>52</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>41</td>
      <td>90</td>
      <td>0</td>
      <td>42</td>
      <td>52</td>
      <td>0</td>
      <td>14</td>
      <td>17</td>
      <td>39</td>
    </tr>
    <tr>
      <th>7</th>
      <td>42</td>
      <td>87</td>
      <td>0</td>
      <td>51</td>
      <td>54</td>
      <td>84</td>
      <td>29</td>
      <td>0</td>
      <td>94</td>
      <td>99</td>
    </tr>
    <tr>
      <th>8</th>
      <td>29</td>
      <td>0</td>
      <td>64</td>
      <td>64</td>
      <td>7</td>
      <td>99</td>
      <td>47</td>
      <td>39</td>
      <td>0</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>71</td>
      <td>1</td>
      <td>20</td>
      <td>27</td>
      <td>54</td>
      <td>37</td>
      <td>99</td>
      <td>31</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### dataframe分组后获取某个组的数据


```python
df = pd.DataFrame({'col1': ['apple', 'banana', 'orange'] * 3,
                   'col2': np.random.rand(9),
                   'col3': np.random.randint(0, 15, 9)})

df_grouped = df.groupby(['col1'])

# Solution 1
df_grouped.get_group('apple')
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
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apple</td>
      <td>0.861407</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>apple</td>
      <td>0.407644</td>
      <td>14</td>
    </tr>
    <tr>
      <th>6</th>
      <td>apple</td>
      <td>0.974718</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 分组后获取某组中的第n大的值


```python
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'taste': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})

n=2
# Solution
df_grpd = df['taste'].groupby(df.fruit)
df_grpd.get_group('banana').sort_values().iloc[-n]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0.31660034951387783

</div>
{% endraw %}



### 分组后获取每组平均值, 并且保持分组列不是index


```python
df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})

# Solution
out = df.groupby('fruit', as_index=False)['price'].mean()
print(out)
```

{% raw %}
<div class="output">
输出(stream):<br>
        fruit  price
    <br />0   apple      6
    <br />1  banana      7
    <br />2  orange      5
    <br />
</div>
{% endraw %}

### 参照两列合并两个dataframe, 并且只保留两个dataframe都有的行


```python
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

# Solution
pd.merge(df1, df2, how='inner', left_on=['fruit', 'weight'], right_on=['pazham', 'kilo'], suffixes=['_left', '_right'])
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
      <th>fruit</th>
      <th>weight</th>
      <th>price_left</th>
      <th>pazham</th>
      <th>kilo</th>
      <th>price_right</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>apple</td>
      <td>high</td>
      <td>14</td>
      <td>apple</td>
      <td>high</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>apple</td>
      <td>high</td>
      <td>9</td>
      <td>apple</td>
      <td>high</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>apple</td>
      <td>high</td>
      <td>10</td>
      <td>apple</td>
      <td>high</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>orange</td>
      <td>low</td>
      <td>7</td>
      <td>orange</td>
      <td>low</td>
      <td>11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>orange</td>
      <td>low</td>
      <td>8</td>
      <td>orange</td>
      <td>low</td>
      <td>11</td>
    </tr>
    <tr>
      <th>5</th>
      <td>orange</td>
      <td>low</td>
      <td>14</td>
      <td>orange</td>
      <td>low</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 如何从dataframe中删除另一个dataframe中存在的行


```python
df1 = pd.DataFrame({'fruit': ['apple', 'orange', 'banana'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.arange(9)})

df2 = pd.DataFrame({'fruit': ['apple', 'orange', 'pine'] * 2,
                    'weight': ['high', 'medium'] * 3,
                    'price': np.arange(6)})


# Solution
print(df1[~df1.isin(df2).all(1)])

df1.isin(df2)
```

{% raw %}
<div class="output">
输出(stream):<br>
        fruit  weight  price
    <br />2  banana     low      2
    <br />3   apple    high      3
    <br />4  orange  medium      4
    <br />5  banana     low      5
    <br />6   apple    high      6
    <br />7  orange  medium      7
    <br />8  banana     low      8
    <br />
</div>
{% endraw %}




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
      <th>fruit</th>
      <th>weight</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>7</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 如何获得两列值匹配的位置


```python
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                    'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})

# Solution
np.where(df.fruit1 == df.fruit2)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    (array([1, 2, 5, 6, 7, 8], dtype=int64),)

</div>
{% endraw %}



### 时间序列如何前后移动时间步

创建新的列是已有列的滞后列或者前向列


```python
df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd'))

# Solution
df['a_lag1'] = df['a'].shift(1)
df['b_lead1'] = df['b'].shift(-1)
print(df)
```

{% raw %}
<div class="output">
输出(stream):<br>
        a   b   c   d  a_lag1  b_lead1
    <br />0  90  49  33  17     NaN     11.0
    <br />1  84  11  34  16    90.0     66.0
    <br />2  78  66  63   6    84.0     34.0
    <br />3  84  34  53  15    78.0     30.0
    <br />4  12  30  44  22    84.0      NaN
    <br />
</div>
{% endraw %}

### 获取整个dataframe值的计数


```python
df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))
# Solution

pd.value_counts(df.values.ravel())
```




{% raw %}
<div class="output">
输出(plain):<br/>

    2    4
    <br />8    3
    <br />5    3
    <br />1    3
    <br />4    2
    <br />3    2
    <br />9    1
    <br />7    1
    <br />6    1
    <br />dtype: int64

</div>
{% endraw %}



### 字符串列的分割


```python
df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])

# Solution
df.row.str.split(',|\t', expand=True)


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
      <td>STD</td>
      <td>City    State</td>
    </tr>
    <tr>
      <th>1</th>
      <td>33</td>
      <td>Kolkata    West Bengal</td>
    </tr>
    <tr>
      <th>2</th>
      <td>44</td>
      <td>Chennai    Tamil Nadu</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>Hyderabad    Telengana</td>
    </tr>
    <tr>
      <th>4</th>
      <td>80</td>
      <td>Bangalore    Karnataka</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas数据分析100道练习题-第四部分.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
