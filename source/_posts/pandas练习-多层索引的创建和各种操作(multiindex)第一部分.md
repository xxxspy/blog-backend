
---
title: pandas练习-多层索引的创建和各种操作(multiindex)第一部分
date: 2019-01-22 20:17:55
tags: [pandas]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---

<span></span>
<!-- more -->

分层/多级索引非常令人兴奋，因为它为一些非常复杂的数据分析和操作提供了可能性，特别是对于处理更高维度的数据。从本质上讲，它使你能在较低维度的数据结构(如Series（1d）和DataFrame（2d）)中存储和操作具有任意数量维度的数据。

在这篇文章中, 你将会学到什么是"MultiIndex", 以及如何创建和操作MultiIndex。


### 创建MultiIndex

MultiIndex对象是标准Index对象的扩展, 你可以将MultiIndex视为元组构成的列表，其中每个元组都是唯一的, 它与Index的区别是, Index可以视为数字或者字符串构成的列表。可以从数组列表（使用MultiIndex.from_arrays），元组列表（使用MultiIndex.from_tuples）或交叉迭代集（使用MultiIndex.from_product）创建MultiIndex。当构造函数传递元组列表时，它将尝试返回MultiIndex。以下示例演示了创建MultiIndexes的不同方法。

#### from_tuples

下面先创建一个元祖构成的列表:


```python
import pandas as pd

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
            ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

tuples = list(zip(*arrays))
tuples
```




{% raw %}
<div class="output">
输出(plain):<br/>

    [('bar', 'one'),
    <br /> ('bar', 'two'),
    <br /> ('baz', 'one'),
    <br /> ('baz', 'two'),
    <br /> ('foo', 'one'),
    <br /> ('foo', 'two'),
    <br /> ('qux', 'one'),
    <br /> ('qux', 'two')]

</div>
{% endraw %}



使用from_tuples来创建MultiIndex:


```python
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index
```




{% raw %}
<div class="output">
输出(plain):<br/>

    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
    <br />           labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
    <br />           names=['first', 'second'])

</div>
{% endraw %}



创建一个series, 并设置它的index:


```python
import numpy as np
s = pd.Series(np.random.randn(8), index=index)
s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    first  second
    <br />bar    one       1.457857
    <br />       two       0.999506
    <br />baz    one      -1.556818
    <br />       two       1.716127
    <br />foo    one      -1.562564
    <br />       two       0.313624
    <br />qux    one       0.537644
    <br />       two       1.178401
    <br />dtype: float64

</div>
{% endraw %}



#### from_arrays

如果说from_tuples接受的参数是"行"的列表, 那么 from_arrays接受的参数是就是"列"的列表:


```python
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
            ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

index = pd.MultiIndex.from_arrays(arrays)
s = pd.Series(np.random.randn(8), index=index)
s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    bar  one   -1.754944
    <br />     two    1.111560
    <br />baz  one   -1.291416
    <br />     two    1.556595
    <br />foo  one    0.147699
    <br />     two    1.379124
    <br />qux  one   -0.981192
    <br />     two    0.292709
    <br />dtype: float64

</div>
{% endraw %}



不过为了简便, 我们通常可以直接在Series的构造函数中使用:


```python
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
            ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]

s = pd.Series(np.random.randn(8), index=arrays)
s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    bar  one    0.507618
    <br />     two   -2.190117
    <br />baz  one   -0.138124
    <br />     two   -2.175832
    <br />foo  one   -0.570554
    <br />     two   -0.851560
    <br />qux  one   -0.784552
    <br />     two    0.003748
    <br />dtype: float64

</div>
{% endraw %}



#### from_product

假如我们有两个list, 这两个list内的元素相互交叉, 两两搭配, 这就是两个list的product:


```python
lists = [['bar', 'baz', 'foo', 'qux'], ['one', 'two']]

index = pd.MultiIndex.from_product(lists, names=['first', 'second'])
s = pd.Series(np.random.randn(len(index)), index=index)
s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    first  second
    <br />bar    one      -1.209379
    <br />       two       0.497207
    <br />baz    one       0.592290
    <br />       two      -0.769594
    <br />foo    one      -0.935071
    <br />       two       0.201014
    <br />qux    one      -0.176715
    <br />       two      -0.183346
    <br />dtype: float64

</div>
{% endraw %}



### MultiIndex.names

你可以为MultiIndex的各个层起名字, 这就是names属性:


```python
# 我们还没有设置名称
s.index.names
```




{% raw %}
<div class="output">
输出(plain):<br/>

    FrozenList([None, None])

</div>
{% endraw %}




```python
s.index.names = ['FirstLevel', 'SecondLevel']

s.index
```




{% raw %}
<div class="output">
输出(plain):<br/>

    MultiIndex(levels=[['bar', 'baz', 'foo', 'qux'], ['one', 'two']],
    <br />           labels=[[0, 0, 1, 1, 2, 2, 3, 3], [0, 1, 0, 1, 0, 1, 0, 1]],
    <br />           names=['FirstLevel', 'SecondLevel'])

</div>
{% endraw %}



### MultiIndex可以作为列名称

Series和DataFrame的列名称属性就是columns, 他也可以是一个MultiIndex对象:


```python
df = pd.DataFrame(np.random.randn(3, 8), index=['A', 'B', 'C'], columns=index)
df
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>FirstLevel</th>
      <th colspan="2" halign="left">bar</th>
      <th colspan="2" halign="left">baz</th>
      <th colspan="2" halign="left">foo</th>
      <th colspan="2" halign="left">qux</th>
    </tr>
    <tr>
      <th>SecondLevel</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1.014034</td>
      <td>1.464162</td>
      <td>-0.753476</td>
      <td>-0.163394</td>
      <td>-0.198990</td>
      <td>0.116046</td>
      <td>-0.555008</td>
      <td>-0.965797</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.314244</td>
      <td>-1.263142</td>
      <td>1.523974</td>
      <td>0.541391</td>
      <td>-0.217874</td>
      <td>0.019695</td>
      <td>1.188791</td>
      <td>-1.003912</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-1.175155</td>
      <td>-0.587370</td>
      <td>0.352587</td>
      <td>-0.047469</td>
      <td>-0.896502</td>
      <td>0.280792</td>
      <td>0.806554</td>
      <td>0.132662</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 获取各水平的值

方法get_level_values将返回特定级别的每个位置的标签向量：


```python
index.get_level_values(0)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    Index(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], dtype='object', name='FirstLevel')

</div>
{% endraw %}



如果你给index设置了名称, 那么你可以直接使用名称来获取水平值:


```python
index.get_level_values('FirstLevel')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    Index(['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], dtype='object', name='FirstLevel')

</div>
{% endraw %}



### 选择数据

这可能是MultiIndex最重要的功能之一。

先看下我们的df的结构:


```python
df
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>FirstLevel</th>
      <th colspan="2" halign="left">bar</th>
      <th colspan="2" halign="left">baz</th>
      <th colspan="2" halign="left">foo</th>
      <th colspan="2" halign="left">qux</th>
    </tr>
    <tr>
      <th>SecondLevel</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1.014034</td>
      <td>1.464162</td>
      <td>-0.753476</td>
      <td>-0.163394</td>
      <td>-0.198990</td>
      <td>0.116046</td>
      <td>-0.555008</td>
      <td>-0.965797</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.314244</td>
      <td>-1.263142</td>
      <td>1.523974</td>
      <td>0.541391</td>
      <td>-0.217874</td>
      <td>0.019695</td>
      <td>1.188791</td>
      <td>-1.003912</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-1.175155</td>
      <td>-0.587370</td>
      <td>0.352587</td>
      <td>-0.047469</td>
      <td>-0.896502</td>
      <td>0.280792</td>
      <td>0.806554</td>
      <td>0.132662</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



获取FirstLevel是bar的所有数据:


```python
df['bar']
```




{% raw %}
<div class="output" contenteditable="true">
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
      <th>SecondLevel</th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1.014034</td>
      <td>1.464162</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.314244</td>
      <td>-1.263142</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-1.175155</td>
      <td>-0.587370</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



获取FirstLevel是bar, SecondLevel是one的所有数据:


```python
df['bar', 'one']
```




{% raw %}
<div class="output">
输出(plain):<br/>

    A    1.014034
    <br />B   -1.314244
    <br />C   -1.175155
    <br />Name: (bar, one), dtype: float64

</div>
{% endraw %}



我更喜欢这样来用, 意义更明确:


```python
df['bar']['one']
```




{% raw %}
<div class="output">
输出(plain):<br/>

    A    1.014034
    <br />B   -1.314244
    <br />C   -1.175155
    <br />Name: one, dtype: float64

</div>
{% endraw %}



需要注意的是, 结果选择输出的结果的columns已经改变:


```python
df['bar'].columns
```




{% raw %}
<div class="output">
输出(plain):<br/>

    Index(['one', 'two'], dtype='object', name='SecondLevel')

</div>
{% endraw %}



如果你要选择第二层的列名为one的所有数据, 你需要借助xs方法:


```python
df.xs('one', level=1, axis=1)
```




{% raw %}
<div class="output" contenteditable="true">
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
      <th>FirstLevel</th>
      <th>bar</th>
      <th>baz</th>
      <th>foo</th>
      <th>qux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1.014034</td>
      <td>-0.753476</td>
      <td>-0.198990</td>
      <td>-0.555008</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.314244</td>
      <td>1.523974</td>
      <td>-0.217874</td>
      <td>1.188791</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-1.175155</td>
      <td>0.352587</td>
      <td>-0.896502</td>
      <td>0.806554</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



或者使用名称代替数字:


```python
df.xs('one', level='SecondLevel', axis='columns')
```




{% raw %}
<div class="output" contenteditable="true">
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
      <th>FirstLevel</th>
      <th>bar</th>
      <th>baz</th>
      <th>foo</th>
      <th>qux</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1.014034</td>
      <td>-0.753476</td>
      <td>-0.198990</td>
      <td>-0.555008</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.314244</td>
      <td>1.523974</td>
      <td>-0.217874</td>
      <td>1.188791</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-1.175155</td>
      <td>0.352587</td>
      <td>-0.896502</td>
      <td>0.806554</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}


我喜欢xs的原因是, 它不仅可以用来选择列, 也可以用来选择行:

```python
s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    FirstLevel  SecondLevel
    <br />bar         one           -1.754944
    <br />            two            1.111560
    <br />baz         one           -1.291416
    <br />            two            1.556595
    <br />foo         one            0.147699
    <br />            two            1.379124
    <br />qux         one           -0.981192
    <br />            two            0.292709
    <br />dtype: float64

</div>
{% endraw %}




```python
s.xs('one', level='SecondLevel', axis='index')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    FirstLevel
    <br />bar   -1.754944
    <br />baz   -1.291416
    <br />foo    0.147699
    <br />qux   -0.981192
    <br />dtype: float64

</div>
{% endraw %}



### 选择行

下面我们把df进行转置, 然后看看一些选择行的操作:


```python
df = df.T

df
```




{% raw %}
<div class="output" contenteditable="true">
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
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>FirstLevel</th>
      <th>SecondLevel</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>1.014034</td>
      <td>-1.314244</td>
      <td>-1.175155</td>
    </tr>
    <tr>
      <th>two</th>
      <td>1.464162</td>
      <td>-1.263142</td>
      <td>-0.587370</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>-0.753476</td>
      <td>1.523974</td>
      <td>0.352587</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.163394</td>
      <td>0.541391</td>
      <td>-0.047469</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.198990</td>
      <td>-0.217874</td>
      <td>-0.896502</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.116046</td>
      <td>0.019695</td>
      <td>0.280792</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">qux</th>
      <th>one</th>
      <td>-0.555008</td>
      <td>1.188791</td>
      <td>0.806554</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.965797</td>
      <td>-1.003912</td>
      <td>0.132662</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



选择FirstLevel是bar, SecondLevel是two的数据:


```python
df.loc[('bar', 'two')]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    A    1.464162
    <br />B   -1.263142
    <br />C   -0.587370
    <br />Name: (bar, two), dtype: float64

</div>
{% endraw %}



下面的用法是等效的:


```python
df.loc['bar'].loc['two']
```




{% raw %}
<div class="output">
输出(plain):<br/>

    A    1.464162
    <br />B   -1.263142
    <br />C   -0.587370
    <br />Name: two, dtype: float64

</div>
{% endraw %}



选择行的同时也能选择列:


```python
df.loc[('bar', 'two'), 'A']
```




{% raw %}
<div class="output">
输出(plain):<br/>

    1.4641615518687836

</div>
{% endraw %}



我们还能使用切片操作:


```python
df.loc['baz': 'foo']
```




{% raw %}
<div class="output" contenteditable="true">
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
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>FirstLevel</th>
      <th>SecondLevel</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>-0.753476</td>
      <td>1.523974</td>
      <td>0.352587</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.163394</td>
      <td>0.541391</td>
      <td>-0.047469</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">foo</th>
      <th>one</th>
      <td>-0.198990</td>
      <td>-0.217874</td>
      <td>-0.896502</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.116046</td>
      <td>0.019695</td>
      <td>0.280792</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



或许, 使用更多的是这样:


```python
df.loc[('bar', 'two'): ('baz', 'two')]
```




{% raw %}
<div class="output" contenteditable="true">
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
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>FirstLevel</th>
      <th>SecondLevel</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <th>two</th>
      <td>1.464162</td>
      <td>-1.263142</td>
      <td>-0.587370</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>-0.753476</td>
      <td>1.523974</td>
      <td>0.352587</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-0.163394</td>
      <td>0.541391</td>
      <td>-0.047469</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



当然, 我还是推荐大家使用xs, 它可以使你的代码更容易被别人理解, 而且选择行和列都用统一的方式:


```python
df.xs('two', level='SecondLevel', axis='index')
```




{% raw %}
<div class="output" contenteditable="true">
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
    <tr>
      <th>FirstLevel</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>1.464162</td>
      <td>-1.263142</td>
      <td>-0.587370</td>
    </tr>
    <tr>
      <th>baz</th>
      <td>-0.163394</td>
      <td>0.541391</td>
      <td>-0.047469</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>0.116046</td>
      <td>0.019695</td>
      <td>0.280792</td>
    </tr>
    <tr>
      <th>qux</th>
      <td>-0.965797</td>
      <td>-1.003912</td>
      <td>0.132662</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 数据对齐

如果你需要对数据进行运算, 那么设置好了index可以给你带来很多便利:


```python
s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    FirstLevel  SecondLevel
    <br />bar         one           -1.754944
    <br />            two            1.111560
    <br />baz         one           -1.291416
    <br />            two            1.556595
    <br />foo         one            0.147699
    <br />            two            1.379124
    <br />qux         one           -0.981192
    <br />            two            0.292709
    <br />dtype: float64

</div>
{% endraw %}



假设我们只需要对第二个元素之后的数据进行运算, 我们的pandas为我们做了按照index的自动数据对齐:


```python
s + s[2:]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    FirstLevel  SecondLevel
    <br />bar         one                 NaN
    <br />            two                 NaN
    <br />baz         one           -2.582832
    <br />            two            3.113191
    <br />foo         one            0.295398
    <br />            two            2.758247
    <br />qux         one           -1.962383
    <br />            two            0.585417
    <br />dtype: float64

</div>
{% endraw %}



或许下面这个看起来更有用:


```python
s + s[::2]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    FirstLevel  SecondLevel
    <br />bar         one           -3.509889
    <br />            two                 NaN
    <br />baz         one           -2.582832
    <br />            two                 NaN
    <br />foo         one            0.295398
    <br />            two                 NaN
    <br />qux         one           -1.962383
    <br />            two                 NaN
    <br />dtype: float64

</div>
{% endraw %}




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas练习-多层索引的创建和各种操作(multiindex)第一部分.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
