
---

title: pandas1.0新功能试用
date: 2020-03-11 12:44:03
tags: [pandas]

---


python最著名的数据科学工具包pandas正式发布了1.0版本, 这是一个里程碑, 我们都知道软件版本从0.x到1.x的升级就说明该软件基本成熟, 各项功能基本稳定了, 为了纪念这个升级, 我在这里介绍一下pandas1.0有哪些新功能。



<!--more-->

新功能的介绍在这里:https://dev.pandas.io/docs/whatsnew/v1.0.0.html , 英文好的可以自行前往。

### 安装环境

pandas1.0不在支持python2.x, 因此为了能够安装pandas1.0, 你需要使用python3, 那么怎么查看你的python版本呢:

```
$ python --version
Python 3.6.5
```

### 从旧版本升级到1.0

升级pandas要小心, 尤其是对一些重度用户, 因为这次升级可能会导致之前的代码不能运行, 如果你的代码很重要, 就不要轻易升级, 或者你可以使用虚拟环境给新版本创建一个全新的运行环境, 需要旧版本的时候可以自由切换版本环境。

我们直接使用pip命令就能升级pandas, 方法如下:

```
pip install --upgrade pandas==1.0
```

安装完了以后你就可以查看一下你的pandas版本了:


```python
import pandas as pd
pd.__version__
```




{% raw %}
<div class="output">
输出(plain):<br/>

    '1.0.0'

</div>
{% endraw %}



### 新特性:DataFrame.info升级

info方法的可读性进一步提高, 大大提高我们查看数据的体验:


```python
df = pd.DataFrame({
   'A': [1,2,3], 
   'B': ["goodbye", "cruel", "world"], 
   'C': [False, True, False]
})
```


```python
df.info()
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   A       3 non-null      int64 
 1   B       3 non-null      object
 2   C       3 non-null      bool  
dtypes: bool(1), int64(1), object(1)
memory usage: 179.0+ bytes

</div>
{% endraw %}

### 新特性:支持markdown格式的表格

程序员经常使用markdown写文章, 那么DataFrame支持markdown输出以后, 我们可以方便的输出表格数据, 并且粘贴到自己的博客上:


```python
df.to_markdown()
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-4-5196b8168295> in <module>
    ----> 1 df.to_markdown()
    

    d:\venv\.common\lib\site-packages\pandas\core\frame.py in to_markdown(self, buf, mode, **kwargs)
       2015         kwargs.setdefault("headers", "keys")
       2016         kwargs.setdefault("tablefmt", "pipe")
    -> 2017         tabulate = import_optional_dependency("tabulate")
       2018         result = tabulate.tabulate(self, **kwargs)
       2019         if buf is None:
    

    d:\venv\.common\lib\site-packages\pandas\compat\_optional.py in import_optional_dependency(name, extra, raise_on_missing, on_version)
         90     except ImportError:
         91         if raise_on_missing:
    ---> 92             raise ImportError(msg) from None
         93         else:
         94             return None
    

    ImportError: Missing optional dependency 'tabulate'.  Use pip or conda to install tabulate.


上面的程序运行报错了, 因为我们缺少了一个生成markdown代码的依赖包, 只要安装上它就行:

```
!pip install tabulate
```


```python
df.to_markdown()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    '|    |   A | B       | C     |\n|---:|----:|:--------|:------|\n|  0 |   1 | goodbye | False |\n|  1 |   2 | cruel   | True  |\n|  2 |   3 | world   | False |'

</div>
{% endraw %}



### 新特性:string数据格式

以前, 字符串格式的数据在pandas中使用的数据格式是"object", 现在pandas新增了string格式的数据, 下面我们创建一个字符串格式的Series:


```python
sser = pd.Series('hello,world,!'.split(','), dtype='string')

sser.dtype
```




{% raw %}
<div class="output">
输出(plain):<br/>

    StringDtype

</div>
{% endraw %}




```python
df['B'] = df['B'].astype("string")
df.dtypes
```




{% raw %}
<div class="output">
输出(plain):<br/>

    A     int64
    <br />B    string
    <br />C      bool
    <br />dtype: object

</div>
{% endraw %}



有这个格式以后, 我们可以快速筛选出string格式的列:


```python
df.select_dtypes('string')
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
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>goodbye</td>
    </tr>
    <tr>
      <th>1</th>
      <td>cruel</td>
    </tr>
    <tr>
      <th>2</th>
      <td>world</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 新特性: 布尔数据格式




```python
bser = pd.Series([1,1,0], dtype='boolean')

bser.dtype
```




{% raw %}
<div class="output">
输出(plain):<br/>

    BooleanDtype

</div>
{% endraw %}




```python
df['D'] = bser

df.dtypes
```




{% raw %}
<div class="output">
输出(plain):<br/>

    A      int64
    <br />B     string
    <br />C       bool
    <br />D    boolean
    <br />dtype: object

</div>
{% endraw %}



### 新特性:pd.NA

在pandas0.25中, 我们可以使用`numpy.nan`和`None`以及`pd.NaT`来表示缺失值, 这造成一些困难。比如一列数据都是整数, 但是有一个数字缺失, 用`numpy.nan`代填, 那么这列数据的数据格式就不得不转换成浮点数, 下面是一个例子:


```python
import numpy as np

ser = pd.Series([1,2,3], dtype='int')
ser
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    1
    <br />1    2
    <br />2    3
    <br />dtype: int32

</div>
{% endraw %}




```python
ser[0] = np.nan

ser
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    NaN
    <br />1    2.0
    <br />2    3.0
    <br />dtype: float64

</div>
{% endraw %}



这种不符合常识的行为会造成很多困扰, 所以现在我们可以这样设置缺失值:


```python
ser2 = pd.Series([1,2,3], dtype='int')

ser2[0] = pd.NA
ser2
```




{% raw %}
<div class="output">
输出(plain):<br/>

    0    <NA>
    <br />1       2
    <br />2       3
    <br />dtype: object

</div>
{% endraw %}



虽然ser2的数据格式仍然改变了, 变成了object类型, 但是里面的整数数字没有更改, 还是整数, 这更符合我们的意愿。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas1.0有哪些新功能.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
