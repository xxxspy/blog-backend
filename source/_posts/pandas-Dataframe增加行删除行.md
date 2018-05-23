
---
title: pandas-Dataframe增加行删除行
date: 2018-05-23 8:17:55
tags: [python, dataframe, 数据分析]
toc: true
xiongzhang: true

---
<span></span>
<!-- more -->

> 声明: 本文由[DataScience](http://mlln.cn)原创发表, 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.

本文代码运行环境:

- windows10
- python3.6
- jupyter notebook

我使用pandas有很长时间了, 一个经常被问道的问题是, 如何增加或删除行, 今天我在这里做一个总结, 希望能帮助一部分人. 下面我们先引入用到的库, 并进行一些初始化的操作.


```python
import pandas as pd
import random
```


```python
df = pd.DataFrame({'a':list(range(100)), 'b':[random.random() for i in range(100)]})
index = pd.MultiIndex.from_product([list('abcd'), list(range(25))])
df.index = index
df.head()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">a</th>
      <th>0</th>
      <td>0</td>
      <td>0.579633</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.220929</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.729217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.183624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.088332</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 增加行

如果你确定知道要增加的行的索引是什么, 并且这个索引不在df.index中, 那么用如下方法是最简单的.


```python
df.loc[('a', -1), :]=None 
df.tail()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">d</th>
      <th>21</th>
      <td>96.0</td>
      <td>0.869157</td>
    </tr>
    <tr>
      <th>22</th>
      <td>97.0</td>
      <td>0.443904</td>
    </tr>
    <tr>
      <th>23</th>
      <td>98.0</td>
      <td>0.946893</td>
    </tr>
    <tr>
      <th>24</th>
      <td>99.0</td>
      <td>0.787945</td>
    </tr>
    <tr>
      <th>a</th>
      <th>-1</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



但是, 很多时候, 我们并不确定索引是否已经存在, 只想追加数据, 那么最好是使用`DataFrame.append`方法. 但是你需要事先创建一个dataframe实例, 用于存放被追加的数据.


```python
data = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})
data.index = pd.MultiIndex.from_tuples([('a', 1), ('b', 1), ('c', 1)])
data
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <th>1</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>b</th>
      <th>1</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>c</th>
      <th>1</th>
      <td>3</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
new_df = df.append(data)
new_df.tail()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>d</th>
      <th>24</th>
      <td>99.0</td>
      <td>0.787945</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>-1</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>b</th>
      <th>1</th>
      <td>2.0</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>c</th>
      <th>1</th>
      <td>3.0</td>
      <td>6.000000</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 删除行

很多时候我们没必要做频繁的数据操作, 只需要建立一个DataFrame的视图即可, 比如选择a<10的所有数据:


```python
df[df['a']<10]
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="9" valign="top">a</th>
      <th>0</th>
      <td>0.0</td>
      <td>0.579633</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.0</td>
      <td>0.729217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>0.183624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
      <td>0.088332</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5.0</td>
      <td>0.757389</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6.0</td>
      <td>0.621999</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7.0</td>
      <td>0.907589</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8.0</td>
      <td>0.493122</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9.0</td>
      <td>0.884472</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



我们并没有删除这些行, 只是选择出了我们需要的行, 并建立了一个视图, 这个概念可以类比与mysql数据库的查询视图.

但是, 如果想要删除某些行, 那怎么办? 我常用的方法是`DataFrame.drop`, 它既可以删除行, 也可以删除列. 具体看代码:


```python
# 删除index为('a', -1)的行
df.drop(('a', -1)).tail()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>to_delete</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">d</th>
      <th>20</th>
      <td>95.0</td>
      <td>0.599706</td>
      <td>1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>96.0</td>
      <td>0.869157</td>
      <td>1</td>
    </tr>
    <tr>
      <th>22</th>
      <td>97.0</td>
      <td>0.443904</td>
      <td>1</td>
    </tr>
    <tr>
      <th>23</th>
      <td>98.0</td>
      <td>0.946893</td>
      <td>1</td>
    </tr>
    <tr>
      <th>24</th>
      <td>99.0</td>
      <td>0.787945</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
# 删除指定行
# 删除倒数第一行
df.drop(df.index[-1]).tail()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">d</th>
      <th>20</th>
      <td>95.0</td>
      <td>0.599706</td>
    </tr>
    <tr>
      <th>21</th>
      <td>96.0</td>
      <td>0.869157</td>
    </tr>
    <tr>
      <th>22</th>
      <td>97.0</td>
      <td>0.443904</td>
    </tr>
    <tr>
      <th>23</th>
      <td>98.0</td>
      <td>0.946893</td>
    </tr>
    <tr>
      <th>24</th>
      <td>99.0</td>
      <td>0.787945</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
# 删除多行

df.drop([('a', -1), ('d', 24)]).tail()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>to_delete</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">d</th>
      <th>19</th>
      <td>94.0</td>
      <td>0.593349</td>
      <td>1</td>
    </tr>
    <tr>
      <th>20</th>
      <td>95.0</td>
      <td>0.599706</td>
      <td>1</td>
    </tr>
    <tr>
      <th>21</th>
      <td>96.0</td>
      <td>0.869157</td>
      <td>1</td>
    </tr>
    <tr>
      <th>22</th>
      <td>97.0</td>
      <td>0.443904</td>
      <td>1</td>
    </tr>
    <tr>
      <th>23</th>
      <td>98.0</td>
      <td>0.946893</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
# 删除连续的多行
# 删除最后5行
df.drop(df.index[-5:]).tail()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">d</th>
      <th>16</th>
      <td>91.0</td>
      <td>0.838718</td>
    </tr>
    <tr>
      <th>17</th>
      <td>92.0</td>
      <td>0.334192</td>
    </tr>
    <tr>
      <th>18</th>
      <td>93.0</td>
      <td>0.110082</td>
    </tr>
    <tr>
      <th>19</th>
      <td>94.0</td>
      <td>0.593349</td>
    </tr>
    <tr>
      <th>20</th>
      <td>95.0</td>
      <td>0.599706</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
# 删除列
df.drop('to_delete', axis=1).head()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">a</th>
      <th>0</th>
      <td>0.0</td>
      <td>0.579633</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.0</td>
      <td>0.729217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>0.183624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
      <td>0.088332</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



当然, 这些操作并没有真的删除这些数据, 想要在`df`上删除, 你需要使用参数`inplace=True`, 如:


```python
df.drop('to_delete', axis=1, inplace=True)
df.head()
```




{% raw %}
<div class="output">
输出:
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
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">a</th>
      <th>0</th>
      <td>0.0</td>
      <td>0.579633</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.0</td>
      <td>0.729217</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.0</td>
      <td>0.183624</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.0</td>
      <td>0.088332</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



好啦, 这就是我用python pandas时删除和增加行的方法, 如果你有更好的方法, 请在这里留言.


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas-Dataframe增加行删除行.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
