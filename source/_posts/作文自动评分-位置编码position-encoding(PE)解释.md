
---
title: 作文自动评分-位置编码position-encoding(PE)解释
date: 2018-07-05 20:17:55
tags: [tensorflow, 深度学习, 作文评分]
toc: true
xiongzhang: true
mathjax: true

---
<span></span>
<!-- more -->

> 声明: 本文由[DataScience](http://mlln.cn)原创发表, 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.

本文代码运行环境:

- windows10
- python3.6
- jupyter notebook
- tensorflow 1.x

### position-encoding

这是用词向量计算句子向量的一种算法, 在[End-to-end Memory Network](https://arxiv.org/pdf/1503.08895.pdf)这篇论文中被提出来。在这篇论文中比较了另一种计算句子向量的模型--词袋模型, 下面我们分别来说一下这两种方法。

#### 词袋模型

假设我们用`$x_{ij}$`表示第i个句子的第j个词, 一个句子的所有词可以表示为`$x_i = \{x_{i1}，x_{i2}，...，x_{ij} \}$`，嵌入每个单词并对得到的向量求和：
`$$
m_i = \sum x_{ij}
$$`


```python
import numpy as np
def position_encoding(sentence_size, embedding_size):
    """
    Position Encoding 
    """
    # sentence_size = J
    # embedding_size = d
    # i = k
    # j = j
    J = sentence_size
    d = embedding_size
    encoding = np.ones((embedding_size, sentence_size), dtype=np.float32)
    ls = sentence_size+1
    le = embedding_size+1
    for k in range(1, le):
        for j in range(1, ls):
            encoding[k-1, j-1] = (2*k/d-1)*(2*j/J - 1)
    encoding += 1
    return np.transpose(encoding)/2


```

或者我在其他论文里见过别人这样做, 但是我还没搞清楚原因, 如果你知道, 请留言告诉我。


```python

def position_encoding(sentence_size, embedding_size):
    """
    Position Encoding described in section 4.1 [1]
    """
    encoding = np.ones((embedding_size, sentence_size), dtype=np.float32)
    ls = sentence_size+1
    le = embedding_size+1
    for i in range(1, le):
        for j in range(1, ls):
            encoding[i-1, j-1] = (i - (le-1)/2) * (j - (ls-1)/2)
    encoding = 1 + 4 * encoding / embedding_size / sentence_size
    return np.transpose(encoding)

```

### 参考文献

Sainbayar Sukhbaatar, Arthur Szlam, Jason Weston, and Rob Fergus. 2015. End-To-End Memory Networks. In Advances in Neural Information Processing Systems 28, C Cortes, N D Lawrence, D D Lee, M Sugiyama, and R Garnett (Eds.). Curran Associates, Inc., 2440–2448.


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](作文自动评分-位置编码position-encoding(PE)解释.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
