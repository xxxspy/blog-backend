

```python
# -*- coding: utf-8 -*-
# author: Yabin Zheng
# Email: sczhengyabin@hotmail.com

%matplotlib inline

import pandas as pd
import numpy as np

import datetime

import matplotlib.pyplot as plt
```


```python
df = df_origin = pd.read_excel("./成都小区信息_20170323.xlsx", sheetname="成交记录")
df_i = pd.read_excel("./成都小区信息_20170323.xlsx", sheetname="小区信息")
```

## 时间段设置


```python
df = df_origin[df_origin['季度'] >= '2013Q1']
# df = df_origin[df_origin['成交月份'] >= '2013.01']
```

## 行政区域成交情况


```python
ss_district = df['区域'].value_counts()
```


```python
ss_district.plot(kind="bar", title="区域销量图")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1d179421ba8>




![png](output_6_1.png)


## 成交量与房屋量比


```python
ss_district_trade_house_ratio = ss_district.copy()
for district in ss_district.index:
    ss_district_trade_house_ratio.set_value(label=district,
                                            value=df_i[df_i['区域'] == district]['总户数'].sum())
ss_district_trade_house_ratio = (ss_district / ss_district_trade_house_ratio.values).sort_values(ascending=False)
```


```python
ss_district_trade_house_ratio.plot(kind='bar', title="区域成交房屋数量比")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1d10000bd68>




![png](output_9_1.png)


## 季度成交统计


```python
ss_season = df['季度'].value_counts().sort_index()
```


```python
ss_season.plot(kind="bar")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1d10055cef0>




![png](output_12_1.png)


## 月销量直方图


```python
ss_month = df[df['成交月份'].astype(str) >= "2015.01"]['成交月份'].value_counts().sort_index()
```


```python
ss_month.plot(kind="bar")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1d176aba940>




![png](output_15_1.png)


## 销量同比增速


```python
count_districts = len(ss_district)
count_seasons = len(ss_season)
df_district_season = pd.DataFrame(columns=ss_district.index.astype(str))
```


```python
for season in ss_season.index:
    ss_district_season = df[df['季度'] == season]['区域'].value_counts().sort_index()
    ss_district_season.name = season
    df_district_season = df_district_season.append(ss_district_season)
```


```python
df_district_season_acc = df_district_season.drop(["2013Q1", "2013Q2", "2013Q3", "2013Q4"], axis=0)
for i in range(0, len(df_district_season) - 4):
    df_district_season_acc.ix[i] = 100 * (df_district_season.ix[i+4] / df_district_season.ix[i] - 1)
```


```python
df_district_season_acc.plot().legend(loc='center left', bbox_to_anchor=(1, 0.5))
```




    <matplotlib.legend.Legend at 0x1d178d8fa90>




![png](output_20_1.png)


## 热门小区


```python
ss_xiaoqu = df['小区名称'].value_counts()[:20]
```


```python
ss_xiaoqu.plot(kind="bar")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1d1786ffb38>




![png](output_23_1.png)


## 保存新的excel
**注意，只会生成一个sheet，因此先保存成不一样的文件，再手工拷贝过去**


```python
writer = pd.ExcelWriter("./成都小区信息_new.xlsx")
df.to_excel(writer, "成交记录")
writer.save()
```
