
---
title: gensim生成长本文中文摘要
date: 2018-06-20 8:17:55
tags: [gensim, python, 摘要生成]
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

### 介绍

随着今日头条/微信公众号等通过推送文章让用户阅读的信息获取方式的繁荣，为长文本生成智能和准确摘要的任务已经成为流行的研究以及行业问题。自动摘要可以提高用户获取信息的效率, 并且可以降低编辑的劳动成本。

文本摘要有两种基本方法：抽取和抽象。前者从原始文本中提取单词和单词短语以创建摘要。后者学习了一种内部语言表达方式，以产生更多像人类一样的摘要，并转述了原文的意图。

今天的教程主要介绍如何用gensim自动实现摘要生成, 以后的文章也会逐一介绍其他一些python工具用于实现同样的目的, 但是效果不同.

### gensim文本摘要技术解释

`gensim.summarization`模块实现了TextRank算法，一种基于Mihalcea等人的论文的加权图的无监督算法。它被另一个学生Olavur Mortensen添加在他的博客上。这种算法的灵感来自google用于网页排名的算法。 TextRank的工作原理如下：

- 预处理文本：删除停用词或其他词。
- 创建一个顶点是句子的图。
- 通过边缘将每个句子连接到每个其他句子。边缘的权重是两个句子的相似程度。
- 在图上运行PageRank算法。
- 选择具有最高PageRank分数的顶点（句子）

### 代码实现

由于`gensim`通常是用在英文的主题提取, 所以`gensim.summarization`模块很多文本预处理的方法都假设我们的语料是英文的, 总的来说有以下假设:

- 句号是英文符号`.`, 这会影响断句.
- 词以空格分隔, 这会影响分词

今天我们想要使用gensim来进行中文的摘要生成, 怎么办? 我首先想到的是修改gensim源码, 但是工程比较大, 不适合在教程中讲解, 所以我最终选了一种绕行方式, 就是将中文语料转换成英文格式. 比如:

`gensim可以实现中文的文章主题生成。`

转换成:

`gensim 可以 实现 中文 的 文章 主题 生成。. `

这样才能正确的被`gensim.summarization`模块所接受.

#### 分句分词和文本转换

我们使用`pyltp`模块进行句子分割和词分割, 只有这样才能实现文本格式转换. 如果你用的是linux系统, 安装pyltp很简单, 如果你用的是windows系统, 我建议你看这篇文章来安装pyltp模块: <a href="/2018/02/03/pyltp%E5%AE%89%E8%A3%85%E5%92%8C%E5%B0%8F%E7%99%BD%E5%85%A5%E9%97%A8/">pyltp windows下的安装</a>.

(下面的教程假设你已经安装好了pyltp.)

下面我们就来实现这个文本转换过程:


```python
from pyltp import Segmentor
from pyltp import SentenceSplitter


_segmentor = None
_sent_splitter = None

def split(content):
    '''分句和分词'''
    global _segmentor, _sent_splitter
    if _segmentor is None:
        model_path = r'D:\mysites\text-characters\tcharacters\ltp\ltp_data\cws.model'
        segmentor = Segmentor()  # 初始化实例
        segmentor.load(model_path) # 加载分词模型
        _segmentor = segmentor  # 设置全局变量, 避免每次都重新加载模型, 耗时
        _sent_splitter = SentenceSplitter() # 句子分割模型
    sents = _sent_splitter.split(content)  # 先进行分句
    _sents = []
    for sent in sents:
        words = _segmentor.segment(sent) # 分词
        sent = ' '.join(words) # 用空格把词隔开
        _sents.append(sent)
    content = '. '.join(_sents)  # 用.把句子隔开
    return content
    
```

#### 测试分句分词


```python
content = '本模块提供文本摘要的功能。基于TextRank算法来计算文本句子的等级。'
result = split(content)
print(f'转换前: {content}')
print(f'转换后: {result}')
```

{% raw %}
<div class="output">
输出:
    转换前: 本模块提供文本摘要的功能。基于TextRank算法来计算文本句子的等级。
    转换后: 本 模块 提供 文本 摘要 的 功能 。. 基于 TextRank 算法 来 计算 文本 句子 的 等级 。
    
</div>
{% endraw %}

#### gensim实现文本摘要

这个过程很简单, 因为我们并不介绍算法, 只是调用接口.


```python
from gensim.summarization.summarizer import summarize
content = '''
使用51篇文章的Opinion数据集进行比较。
每篇文章都是关于产品的功能，例如iPod的电池寿命等，并且是购买该产品的客户的评论集合。
数据集中的每篇文章都有5个手动编写的“黄金”摘要。
通常5金总结是不同的，但它们也可以是相同的文本重复5次。
LexRank是这里的赢家，因为它产生了更好的ROUGE和BLEU分数。
不幸的是，我们发现由Gensim的TextRank和Luhn模型产生的摘要信息比摘要要少。
此外，LexRank并不总是在ROUGE评分中击败TextRank  - 例如，TextRank在DUC 2002数据集上的表现稍好于LexRank。
因此，LexRank和TextRank之间的选择取决于您的数据集，值得一试。
数据的另一个结论是Gensim的Textrank优于普通的PyTextRank。
因为它在明文TextRank中使用BM25函数而不是余弦IDF。
表中的另一点是Luhn的算法具有较低的BLEU分数。
这是因为它提取了更长的摘要，因此涵盖了更多的产品评论。
不幸的是，我们不能缩短它，因为Sumy中Luhn算法的封装不提供参数来改变字数限制。
'''
tokens = split(content)
summarize(tokens)
```




{% raw %}
<div class="output">
输出:
    '. LexRank 是 这里 的 赢家 ， 因为 它 产生 了 更 好 的 ROUGE 和 BLEU 分数 。.\n. 不幸 的 是 ， 我们 发现 由 Gensim 的 TextRank 和 Luhn 模型 产生 的 摘要 信息 比 摘要 要 少 。.'
</div>
{% endraw %}



至此, 我们生成的摘要还算可以, 但是多了一些空格和句子分隔符. 那么, 我们就来清理以下这些无意义的符号.


```python
def clean(content):
    content = content.replace('.', '') # 删除句子分隔符
    content = content.replace(' ', '') # 删除空格
    return content
```

测试以下效果:


```python
result = summarize(tokens)
result = clean(result)
print(result)
```

{% raw %}
<div class="output">
输出:
    LexRank是这里的赢家，因为它产生了更好的ROUGE和BLEU分数。
    不幸的是，我们发现由Gensim的TextRank和Luhn模型产生的摘要信息比摘要要少。
    
</div>
{% endraw %}


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](gensim生成长本文中文摘要.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
