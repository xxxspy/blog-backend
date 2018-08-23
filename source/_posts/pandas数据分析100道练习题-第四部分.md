---
title: pandas数据分析100道练习题-第四部分
date: 2018-08-23 07:54:31
tags: [python, pandas]
toc: true
repl: "https://repl.it/@xxxspy/FoolishTechnologicalIntegers?lite=true"
---

<span></span>
<!-- more -->


这篇文章收集了网友们使用pandas进行数据分析时经常遇到的问题, 这些问题也可以检验你使用pandas的熟练程度, 所以他们更像是一个学习教材, 掌握这些技能, 可以使你数据数据分析的工作事半功倍。

- 第一部分pandas练习题请访问: [pandas数据分析100道练习题-第一部分](http://mlln.cn/2018/08/13/pandas%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90100%E9%81%93%E7%BB%83%E4%B9%A0%E9%A2%98-%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86/)
- 第二部分pandas练习题请访问: [pandas数据分析100道练习题-第二部分](http://mlln.cn/2018/08/15/pandas数据分析100道练习题-第二部分/)
- 第三部分pandas练习题请访问: [pandas数据分析100道练习题-第三部分](http://mlln.cn/2018/08/15/pandas数据分析100道练习题-第三部分/)

下面是第三部分:

### 如何计算列之间的最大相关系数

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randint(1,100, 80).reshape(8, -1), 
    columns=list('pqrstuvwxy'),
    index=list('abcdefgh')
)
df

abs_corrmat = np.abs(df.corr())
max_corr = abs_corrmat.apply(lambda x: sorted(x)[-2])
print('Maximum Correlation possible for each column: ', np.round(max_corr.tolist(), 2))
```

### 如何计算列之间的最大相关系数

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randint(1,100, 80).reshape(8, -1), 
    columns=list('pqrstuvwxy'),
    index=list('abcdefgh')
)
df

abs_corrmat = np.abs(df.corr())
max_corr = abs_corrmat.apply(lambda x: sorted(x)[-2])
print('Maximum Correlation possible for each column: ', np.round(max_corr.tolist(), 2))
```