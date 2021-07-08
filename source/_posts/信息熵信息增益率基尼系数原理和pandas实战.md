
---
title: 信息熵信息增益率基尼系数原理和pandas实战
date: 2018-09-18 19:17:55
tags: [pandas]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---
<span></span>
<!-- more -->

信息增益(Info Gain), 信息增益率(Info Gain Ratio)和 基尼指数(Gini Index)都是在做决策树时试用的分支选择策略, 下面我们试用numpy来实现这几个指标, 以便加深对这些指标的理解。

下面我们来引入用到的库:


```python
import numpy as np
# 进行数据整理
import pandas as pd
# 数据
import io
# 验证结果
from scipy import stats
```

### 案例和数据集

学习决策树常用的一个数据集就是"机器学习（周志华）》 西瓜数据集3.0", 下面我把数据粘贴出来, 你们就不必下载了, 直接硬编码到python种使用:


```python
data_str = output = io.StringIO('''编号,色泽,根蒂,敲声,纹理,脐部,触感,密度,含糖率,好瓜
1,青绿,蜷缩,浊响,清晰,凹陷,硬滑,0.697,0.46,是  
2,乌黑,蜷缩,沉闷,清晰,凹陷,硬滑,0.774,0.376,是  
3,乌黑,蜷缩,浊响,清晰,凹陷,硬滑,0.634,0.264,是  
4,青绿,蜷缩,沉闷,清晰,凹陷,硬滑,0.608,0.318,是  
5,浅白,蜷缩,浊响,清晰,凹陷,硬滑,0.556,0.215,是  
6,青绿,稍蜷,浊响,清晰,稍凹,软粘,0.403,0.237,是  
7,乌黑,稍蜷,浊响,稍糊,稍凹,软粘,0.481,0.149,是  
8,乌黑,稍蜷,浊响,清晰,稍凹,硬滑,0.437,0.211,是  
9,乌黑,稍蜷,沉闷,稍糊,稍凹,硬滑,0.666,0.091,否  
10,青绿,硬挺,清脆,清晰,平坦,软粘,0.243,0.267,否  
11,浅白,硬挺,清脆,模糊,平坦,硬滑,0.245,0.057,否  
12,浅白,蜷缩,浊响,模糊,平坦,软粘,0.343,0.099,否  
13,青绿,稍蜷,浊响,稍糊,凹陷,硬滑,0.639,0.161,否  
14,浅白,稍蜷,沉闷,稍糊,凹陷,硬滑,0.657,0.198,否  
15,乌黑,稍蜷,浊响,清晰,稍凹,软粘,0.36,0.37,否  
16,浅白,蜷缩,浊响,模糊,平坦,硬滑,0.593,0.042,否  
17,青绿,蜷缩,沉闷,稍糊,稍凹,硬滑,0.719,0.103,否''')

data = pd.read_csv(data_str)
data.set_index('编号', inplace=True)
data
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
      <th>色泽</th>
      <th>根蒂</th>
      <th>敲声</th>
      <th>纹理</th>
      <th>脐部</th>
      <th>触感</th>
      <th>密度</th>
      <th>含糖率</th>
      <th>好瓜</th>
    </tr>
    <tr>
      <th>编号</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>青绿</td>
      <td>蜷缩</td>
      <td>浊响</td>
      <td>清晰</td>
      <td>凹陷</td>
      <td>硬滑</td>
      <td>0.697</td>
      <td>0.460</td>
      <td>是</td>
    </tr>
    <tr>
      <th>2</th>
      <td>乌黑</td>
      <td>蜷缩</td>
      <td>沉闷</td>
      <td>清晰</td>
      <td>凹陷</td>
      <td>硬滑</td>
      <td>0.774</td>
      <td>0.376</td>
      <td>是</td>
    </tr>
    <tr>
      <th>3</th>
      <td>乌黑</td>
      <td>蜷缩</td>
      <td>浊响</td>
      <td>清晰</td>
      <td>凹陷</td>
      <td>硬滑</td>
      <td>0.634</td>
      <td>0.264</td>
      <td>是</td>
    </tr>
    <tr>
      <th>4</th>
      <td>青绿</td>
      <td>蜷缩</td>
      <td>沉闷</td>
      <td>清晰</td>
      <td>凹陷</td>
      <td>硬滑</td>
      <td>0.608</td>
      <td>0.318</td>
      <td>是</td>
    </tr>
    <tr>
      <th>5</th>
      <td>浅白</td>
      <td>蜷缩</td>
      <td>浊响</td>
      <td>清晰</td>
      <td>凹陷</td>
      <td>硬滑</td>
      <td>0.556</td>
      <td>0.215</td>
      <td>是</td>
    </tr>
    <tr>
      <th>6</th>
      <td>青绿</td>
      <td>稍蜷</td>
      <td>浊响</td>
      <td>清晰</td>
      <td>稍凹</td>
      <td>软粘</td>
      <td>0.403</td>
      <td>0.237</td>
      <td>是</td>
    </tr>
    <tr>
      <th>7</th>
      <td>乌黑</td>
      <td>稍蜷</td>
      <td>浊响</td>
      <td>稍糊</td>
      <td>稍凹</td>
      <td>软粘</td>
      <td>0.481</td>
      <td>0.149</td>
      <td>是</td>
    </tr>
    <tr>
      <th>8</th>
      <td>乌黑</td>
      <td>稍蜷</td>
      <td>浊响</td>
      <td>清晰</td>
      <td>稍凹</td>
      <td>硬滑</td>
      <td>0.437</td>
      <td>0.211</td>
      <td>是</td>
    </tr>
    <tr>
      <th>9</th>
      <td>乌黑</td>
      <td>稍蜷</td>
      <td>沉闷</td>
      <td>稍糊</td>
      <td>稍凹</td>
      <td>硬滑</td>
      <td>0.666</td>
      <td>0.091</td>
      <td>否</td>
    </tr>
    <tr>
      <th>10</th>
      <td>青绿</td>
      <td>硬挺</td>
      <td>清脆</td>
      <td>清晰</td>
      <td>平坦</td>
      <td>软粘</td>
      <td>0.243</td>
      <td>0.267</td>
      <td>否</td>
    </tr>
    <tr>
      <th>11</th>
      <td>浅白</td>
      <td>硬挺</td>
      <td>清脆</td>
      <td>模糊</td>
      <td>平坦</td>
      <td>硬滑</td>
      <td>0.245</td>
      <td>0.057</td>
      <td>否</td>
    </tr>
    <tr>
      <th>12</th>
      <td>浅白</td>
      <td>蜷缩</td>
      <td>浊响</td>
      <td>模糊</td>
      <td>平坦</td>
      <td>软粘</td>
      <td>0.343</td>
      <td>0.099</td>
      <td>否</td>
    </tr>
    <tr>
      <th>13</th>
      <td>青绿</td>
      <td>稍蜷</td>
      <td>浊响</td>
      <td>稍糊</td>
      <td>凹陷</td>
      <td>硬滑</td>
      <td>0.639</td>
      <td>0.161</td>
      <td>否</td>
    </tr>
    <tr>
      <th>14</th>
      <td>浅白</td>
      <td>稍蜷</td>
      <td>沉闷</td>
      <td>稍糊</td>
      <td>凹陷</td>
      <td>硬滑</td>
      <td>0.657</td>
      <td>0.198</td>
      <td>否</td>
    </tr>
    <tr>
      <th>15</th>
      <td>乌黑</td>
      <td>稍蜷</td>
      <td>浊响</td>
      <td>清晰</td>
      <td>稍凹</td>
      <td>软粘</td>
      <td>0.360</td>
      <td>0.370</td>
      <td>否</td>
    </tr>
    <tr>
      <th>16</th>
      <td>浅白</td>
      <td>蜷缩</td>
      <td>浊响</td>
      <td>模糊</td>
      <td>平坦</td>
      <td>硬滑</td>
      <td>0.593</td>
      <td>0.042</td>
      <td>否</td>
    </tr>
    <tr>
      <th>17</th>
      <td>青绿</td>
      <td>蜷缩</td>
      <td>沉闷</td>
      <td>稍糊</td>
      <td>稍凹</td>
      <td>硬滑</td>
      <td>0.719</td>
      <td>0.103</td>
      <td>否</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



该数据集通常是使用前几个西瓜属性预测最后一个指标"好瓜".

### 信息熵怎么算

要计算信息增益的话, 首先要知道怎么算信息熵, 它的公式是:

`$$
H(X) = \sum_{i \in X} p_i log p_i
$$`


```python
def entropy(data, att_name):
    '''
    data: 数据集
    att_name: 属性名
    '''
    levels = data[att_name].unique()
    # 信息熵
    ent = 0
    for lv in levels:
        pi = sum(data[att_name]==lv) / data.shape[0]
        ent += pi*np.log(pi)
    return -ent
print('好瓜的信息熵:')
entropy(data, '好瓜')
```

{% raw %}
<div class="output">
输出(stream):<br>
    好瓜的信息熵:
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    0.8760918930634294

</div>
{% endraw %}



使用scipy内置的`stats.entropy`验证我们的函数:


```python
def entropy_scipy(data, att_name):
    n = data.shape[0]
    values = data[att_name].value_counts()
    return stats.entropy(values/n)

assert entropy(data, '好瓜')==entropy_scipy(data, '好瓜')
```

### 条件信息熵怎么算

已知条件Y, 求X的概率就是P(X|Y), 知道的信息越多，随机事件的不确定性就越小。
书中定义：在Y条件X的条件熵：（二元模型）

引自维基百科:

<img src="imgs/conditional_entropy.png">


因为我们已经有了交叉熵的公式, 所以我们其实可以直接算出`$H(Y|X=x)$`


```python
def conditional_entropy(data, xname, yname):
    xs = data[xname].unique()
    ys = data[yname].unique()
    p_x = data[xname].value_counts() / data.shape[0]
    ce = 0
    for x in xs:
        ce += p_x[x]*entropy(data[data[xname]==x], yname)
    return ce

print('触感条件下, 好瓜的信息熵:')
conditional_entropy(data, '触感', '好瓜')
```

{% raw %}
<div class="output">
输出(stream):<br>
    触感条件下, 好瓜的信息熵:
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    0.8462465738213797

</div>
{% endraw %}



### 信息增益

理论上我们可以证明`$H(Y)>=H(Y|X)$`


```python
def gain(data, xname, yname):
    en = entropy(data, yname)
    ce = conditional_entropy(data, xname, yname)
    return en - ce

print('触感的引入导致的信息增益:')
gain(data, '触感', '好瓜')
```

{% raw %}
<div class="output">
输出(stream):<br>
    触感的引入导致的信息增益:
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    0.029845319242049695

</div>
{% endraw %}



### 属性的信息增益与属性的类别数的关系


属性的类别越多, 根据该属性就可以把数据切分的更细, 这样往往导致信息的混乱程度降低, 所以类别多的属性的信息增益较大, 我们可以用代码实验一下:



```python
data['testCol'] = 0
data.iloc[10:, -1] = 1
print(gain(data, 'testCol', '触感'))
data.iloc[14:, -1] = 2
print(gain(data, 'testCol', '触感'))
print(gain(data, '密度', '触感'))
```

{% raw %}
<div class="output">
输出(stream):<br>
    0.00011925580490779186
    <br />0.0018253756129741339
    <br />0.605797499372304
    <br />
</div>
{% endraw %}

### 信息增益率

信息增益率的提出是为了规避信息增益种属性类别数目造成的影响, 它的计算公式是:

`$$
GainRatio(Y, X) = {Gain(Y, X) \over SplitInfo(X)}
$$`

其中:

`$$
SplitInfo(X)= \sum_{i \in X} p_i log p_i = H(X)
$$`


```python
def gain_ratio(data, xname, yname):
    g = gain(data, xname, yname)
    si = entropy(data, xname)
    return g / si
print('信息增益率:')
gain_ratio(data, '触感', '好瓜')
```

{% raw %}
<div class="output">
输出(stream):<br>
    信息增益率:
    <br />
</div>
{% endraw %}




{% raw %}
<div class="output">
输出(plain):<br/>

    0.04926616447405919

</div>
{% endraw %}




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](信息熵信息增益率基尼系数原理和pandas实战.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
