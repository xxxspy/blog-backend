
---
title: pandas文本数据转整数分类编码的最佳实践
date: 2018-09-18 20:17:55
tags: [pandas]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---
<span></span>
<!-- more -->

### 问题描述

在许多实际的数据处理工作中，数据集通常包含分类变量。这些变量通常存储为表示各种特征的文本值。一些示例包括颜色（“红色”，“黄色”，“蓝色”），尺寸（“小”，“中”，“大”）或地理名称（州或国家）。无论使用何种值，挑战在于确定如何在分析中使用此数据。许多机器学习算法可以支持分类值而无需进一步操作，但还有许多算法不支持。因此，分析师面临的挑战是如何将这些文本属性转换为数值以便进一步处理。

与数据科学世界的许多其他方面一样，关于如何解决这个问题没有单一的答案。每种方法都需要权衡，并对分析结果产生潜在影响。幸运的是，pandas和scikit-learn的python工具提供了几种方法，可用于将分类数据转换为合适的数值。本文将对一些常见的（以及一些更复杂的）方法进行汇总，希望它能帮助其他人将这些技术应用于他们的现实世界问题。

### 数据集

在本文中，我在UCI机器学习库中找到一个好的数据集。这个特定的汽车数据集包括分类值和连续值的组合，并且作为相对容易理解的有用示例。由于在决定如何编码各种分类值时，领域知识是一个重要方面 - 这个数据集是一个很好的个案研究。

在我们开始编码各种值之前，我们需要载入数据并进行一些小的清理。幸运的是，pandas使这简单明了：


```python
import pandas as pd
import numpy as np

# 定义数据的列名称, 因为这个数据集没有包含列名称
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# 读取在线的数据集, 并将?转换为缺失NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
df.head()[df.columns[:10]]
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
      <th>symboling</th>
      <th>normalized_losses</th>
      <th>make</th>
      <th>fuel_type</th>
      <th>aspiration</th>
      <th>num_doors</th>
      <th>body_style</th>
      <th>drive_wheels</th>
      <th>engine_location</th>
      <th>wheel_base</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>NaN</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>NaN</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>NaN</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>94.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>164.0</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>164.0</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.4</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



看一下所有列的数据类型:


```python
df.dtypes
```




{% raw %}
<div class="output">
输出(plain):<br/>

    symboling              int64
    <br />normalized_losses    float64
    <br />make                  object
    <br />fuel_type             object
    <br />aspiration            object
    <br />num_doors             object
    <br />body_style            object
    <br />drive_wheels          object
    <br />engine_location       object
    <br />wheel_base           float64
    <br />length               float64
    <br />width                float64
    <br />height               float64
    <br />curb_weight            int64
    <br />engine_type           object
    <br />num_cylinders         object
    <br />engine_size            int64
    <br />fuel_system           object
    <br />bore                 float64
    <br />stroke               float64
    <br />compression_ratio    float64
    <br />horsepower           float64
    <br />peak_rpm             float64
    <br />city_mpg               int64
    <br />highway_mpg            int64
    <br />price                float64
    <br />dtype: object

</div>
{% endraw %}



因为我们只关心文本数据, 所以我们选出类型为"object"的列, 而pandas提供了`select_dtypes`方法可以快速达到目的:


```python
df2 = df.select_dtypes('object').copy()
df2.head()
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
      <th>make</th>
      <th>fuel_type</th>
      <th>aspiration</th>
      <th>num_doors</th>
      <th>body_style</th>
      <th>drive_wheels</th>
      <th>engine_location</th>
      <th>engine_type</th>
      <th>num_cylinders</th>
      <th>fuel_system</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>dohc</td>
      <td>four</td>
      <td>mpfi</td>
    </tr>
    <tr>
      <th>1</th>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>dohc</td>
      <td>four</td>
      <td>mpfi</td>
    </tr>
    <tr>
      <th>2</th>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>ohcv</td>
      <td>six</td>
      <td>mpfi</td>
    </tr>
    <tr>
      <th>3</th>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>ohc</td>
      <td>four</td>
      <td>mpfi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>4wd</td>
      <td>front</td>
      <td>ohc</td>
      <td>five</td>
      <td>mpfi</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



因为数据集种包括缺失数据, 这会增加后续处理的难度, 我们为了简单起见, 将缺失值删除即可:


```python
df2.dropna(inplace=True)
```

### 方案Ⅰ:替换字符串

最简单的方式就是, 查找列中所有的字符串, 然后给不同的字符串一个编号, 然后用编号替换字符串:

- 使用`vlaue_counts`获取所有的字符串:


```python
col = 'body_style'

strs = df2[col].value_counts()
strs
```




{% raw %}
<div class="output">
输出(plain):<br/>

    sedan          94
    <br />hatchback      70
    <br />wagon          25
    <br />hardtop         8
    <br />convertible     6
    <br />Name: body_style, dtype: int64

</div>
{% endraw %}



- 将所有字符串映射为数字:


```python
value_map = dict((v, i) for i,v in enumerate(strs.index))
value_map
```




{% raw %}
<div class="output">
输出(plain):<br/>

    {'sedan': 0, 'hatchback': 1, 'wagon': 2, 'hardtop': 3, 'convertible': 4}

</div>
{% endraw %}



- 使用`replace`方法替换字符串


```python
df2.replace({col:value_map})[col].head()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    4
    <br />1    4
    <br />2    1
    <br />3    0
    <br />4    0
    <br />Name: body_style, dtype: int64

</div>
{% endraw %}



你会看到, 不仅仅字符串被替换, 而且series的数据类型变成了int64

### 方案Ⅱ:标签编码

编码分类值的另一种方法是使用称为标签编码的技术。标签编码只是将列中的每个值转换为数字。例如，body_style列包含5个不同的值。我们可以选择像这样编码：

- convertible -> 0
- hardtop -> 1
- hatchback -> 2
- sedan -> 3
- wagon -> 4

- 首先你可以将列的数据格式转换为`category`


```python
bs = df2['body_style'].astype('category')
bs.head()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    convertible
    <br />1    convertible
    <br />2      hatchback
    <br />3          sedan
    <br />4          sedan
    <br />Name: body_style, dtype: category
    <br />Categories (5, object): [convertible, hardtop, hatchback, sedan, wagon]

</div>
{% endraw %}



- 然后你只需要使用标签的编码作为真正的数据就可以了:


```python
bs.cat.codes.head()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    0
    <br />1    0
    <br />2    2
    <br />3    3
    <br />4    3
    <br />dtype: int8

</div>
{% endraw %}



### 方案三: 转换成哑变量, 或者叫one-hot编码

标签编码的优点是它很简单，但它的缺点是数值可能被算法“误解”。例如，0的值显然小于4的值，但这是否真的与现实生活中的数据集相对应？在我们的计算中，旅行车的重量是否比敞篷车重4倍？在这个例子中，我不这么认为。所以我们需要将数据转换为哑变量(onehot), 在pandas中, 这个转变只需要一行代码:


```python
pd.get_dummies(df[['drive_wheels', 'body_style']]).head()
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
      <th>drive_wheels_4wd</th>
      <th>drive_wheels_fwd</th>
      <th>drive_wheels_rwd</th>
      <th>body_style_convertible</th>
      <th>body_style_hardtop</th>
      <th>body_style_hatchback</th>
      <th>body_style_sedan</th>
      <th>body_style_wagon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 方案四: 自定义二分类

根据数据集，您可以使用标签编码和one-hot来创建满足进一步分析需求的二分类列

在此特定数据集中，有一个名为engine_type的列包含几个不同的值：


```python
df2['engine_type'].value_counts()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    ohc      146
    <br />ohcf      15
    <br />ohcv      13
    <br />dohc      12
    <br />l         12
    <br />rotor      4
    <br />dohcv      1
    <br />Name: engine_type, dtype: int64

</div>
{% endraw %}



为了便于讨论，我们可能关心的是发动机是否是顶置凸轮（OHC）。换句话说，OHC的各种版本对于该分析都是相同的。如果是这种情况，那么我们可以使用str accessor创建一个新列，指示汽车是否有OHC引擎。


```python
df2["engine_type"].str.contains("ohc").map(int).value_counts()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    1    187
    <br />0     16
    <br />Name: engine_type, dtype: int64

</div>
{% endraw %}



### Scikit-Learn

除了pandas方法，scikit-learn还提供类似的功能。就个人而言，我发现使用pandas有点简单，但我认为重要的是要知道如何在scikit-learn中执行这些过程。

例如，如果我们想对汽车的品牌进行标签编码，我们需要实例化LabelEncoder对象并fit_transform数据：


```python
from sklearn.preprocessing import LabelBinarizer

lb_style = LabelBinarizer()
lb_results = lb_style.fit_transform(df2["body_style"])
pd.DataFrame(lb_results, columns=lb_style.classes_).head()
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
      <th>convertible</th>
      <th>hardtop</th>
      <th>hatchback</th>
      <th>sedan</th>
      <th>wagon</th>
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
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas文本数据转整数分类编码的最佳实践.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
