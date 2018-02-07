---
title: gensim lda 文档主题提取实现
date: 2018-02-07 14:49:25
tags: [自然语言处理, 文本挖掘, python]
---

怎么样将一堆文章聚合到不同的主题上, 并且还能提取主题的关键词, 这样我们就能对每个主题有一个大概的感性认识. LDA(Latent Dirichlet Allocation)就是实现这个功能的算法, 今天我们在这里使用python的gensim库来试用一下LDA算法. 但是在使用LDA之前, 我们需要使用pyltp进行分词. 

我的开发环境:

- win10
- python3.6
- gensim
- pyltp

我用到的语料库:



### 安装gensim

    pip install gensim

### 准备语料库

我用的是搜狗新闻语料库, 这个语料库是公开免费的, 网上很多地方可以下载得到, 我放到自己网盘做了备份, 下载链接：https://pan.baidu.com/s/1gg2y3Gf 密码：hk3y. 把语料库下载到本地, 然后解压到一个你方便使用的地方.

### 一些基本配置

```py
import os
from pathlib import Path


#项目文件夹
project_dir = Path('D:\\项目\\lda主题提取')
#搜狗新闻语料库文件夹
source_dir = project_dir / 'source'
#分好词以后语料库文件夹
words_dir = project_dir / 'words'
```

### 分词

我先定义了一个函数`fenci_all`可以将`source_dir`目录下的文件进行遍历, 然后输入到`fenci`函数进行分词, `fenci`函数先读取文件的内容, 然后将篇章分为句子, 句子分为词, 然后将分词结果保存到`words_dir`目录下.

```py
import pyltp
from pyltp import SentenceSplitter
from pyltp import Segmentor
import json

# 分词模型路径
ci_model_path = 'D:\\mysites\\text-characters\\tcharacters\\ltp\\ltp_data\\cws.model'

# 分句器
sspliter = SentenceSplitter()
# 分词器
wspliter = Segmentor()
wspliter.load(ci_model_path)
def fenci(filepath:Path):
    relative=filepath.relative_to(source_dir)
    write_path = words_dir / relative
    # 分句
    try:
        # 这个语料库并不是全部都用gbk编码的, 所以无法解码的我就直接扔掉了
        passage = open(filepath, 'r', encoding='gbk').read()
    except UnicodeDecodeError:
        print('Error to Open file:{}'.format(filepath))
        return 

    sentences = sspliter.split(passage)
    splited = []
    for sent in sentences:
        words = wspliter.segment(sent)
        splited.extend(list(words))
    write_path.parent.mkdir(parents=True, exist_ok=True)   
    f=open(write_path, 'w')
    f.write(json.dumps(splited))
    f.close()

def fenci_all():
    d: Path
    for d in source_dir.iterdir():
        for fpath in d.iterdir():
            print('split {}'.format(fpath))
            fenci(fpath)

fenci_all()
# 释放模型, 节省内存
wspliter.release()

```

### 准备参数

经过上面的步骤, 我们的语料库就是已经分好词的了, 并且所有的预料都保存在了`words_dir`的目录下. 下面我们要考察一下进行LDA需要整理什么数据.

我们写要提个加载数据的函数:

```py
def load_corpus():
    d:Path
    corpus=[]
    for d in words_dir.iterdir():
        for fpath in d.iterdir():
            print('reading {}'.format(fpath))
            passage = json.load(open(fpath, 'r'))
            # 因为我们的句子信息不重要, 所以把所有句子合并成一个
            passage = [word for sentence in passage for word in sentence]
            corpus.append(passage)
    return corpus
```

下面我们就可以通过这个方法来加载数据了:

    corpus = load_corpus()

因为计算机是无法处理文本数据的, 现在在我们的corpus中存储的还是词, 我们需要将词映射到一个数字上, 这就是要建立一个数字和词的对应关系:字典.

```py
from gensim import models, corpora

dic = corpora.Dictionary(corpus)
clean_data = [dic.doc2bow(words) for words in corpus]
```

### 主题提取

```py
lda = models.ldamodel.LdaModel(clean_data, id2word=dic,  num_topics=20)
# 查看主题
for topic in lda.print_topics(num_words=10):
    print(topic[1])
```

输出结果:(星号前面表示权重, 后面表示词)

```cmd
0.029*"," + 0.026*"航空" + 0.021*"飞机" + 0.017*"的" + 0.014*"，" + 0.012*"。" + 0.012*"旅游" + 0.010*"、" + 0.009*"飞" + 0.005*")"
0.024*"，" + 0.021*"的" + 0.020*"》" + 0.017*"《" + 0.015*"&" + 0.015*"nbsp" + 0.014*"。" + 0.008*"、" + 0.007*"：" + 0.005*"为"
0.035*"." + 0.017*"的" + 0.016*"," + 0.016*"，" + 0.014*"防务" + 0.010*"。" + 0.009*")" + 0.007*"a" + 0.005*"A" + 0.004*"、"
0.021*"的" + 0.016*"。" + 0.014*")" + 0.013*"，" + 0.013*"(" + 0.011*"=" + 0.010*"战斗机" + 0.009*"+" + 0.008*"、" + 0.008*"坦克"
0.054*"，" + 0.050*"的" + 0.025*"。" + 0.018*"海军" + 0.017*"训练" + 0.015*"美军" + 0.012*"、" + 0.009*"在" + 0.008*"潜艇" + 0.008*"作战"
0.059*"，" + 0.051*"的" + 0.034*"。" + 0.019*"、" + 0.014*"”" + 0.014*"在" + 0.013*"“" + 0.010*"和" + 0.009*"中国" + 0.008*"了"
0.040*"、" + 0.032*"，" + 0.022*"的" + 0.019*"。" + 0.016*"专业" + 0.014*"考生" + 0.011*"学校" + 0.011*"大学" + 0.010*"考试" + 0.009*"："
0.134*"," + 0.014*"的" + 0.013*")" + 0.013*"、" + 0.013*""" + 0.012*"(" + 0.011*"自卫队" + 0.011*"&" + 0.010*"nbsp" + 0.009*"'"
0.026*"，" + 0.017*"的" + 0.017*"。" + 0.008*"兵力" + 0.007*"师" + 0.007*"编队" + 0.007*"3" + 0.006*"在" + 0.006*"1" + 0.005*"主力"
0.025*"，" + 0.025*"的" + 0.018*"。" + 0.009*"、" + 0.007*"推演" + 0.006*"在" + 0.005*"和" + 0.005*"生产" + 0.005*"断代" + 0.005*"”"
0.125*""" + 0.064*")" + 0.062*"(" + 0.011*"," + 0.010*"。" + 0.008*":" + 0.007*"，" + 0.007*"的" + 0.006*"&" + 0.006*"nbsp"
0.175*";" + 0.168*"&" + 0.168*"nbsp" + 0.014*"的" + 0.013*"：" + 0.010*"，" + 0.010*"。" + 0.006*"、" + 0.004*"1" + 0.004*"2"
0.047*"伊朗" + 0.024*"，" + 0.022*"。" + 0.019*"的" + 0.010*"nbsp" + 0.009*"、" + 0.009*"军费" + 0.008*"&" + 0.007*"公司" + 0.006*"("
0.037*"，" + 0.025*"演习" + 0.025*"（" + 0.024*"）" + 0.019*"。" + 0.016*"、" + 0.009*"的" + 0.009*"在" + 0.009*"部队" + 0.008*"“"
0.075*"，" + 0.065*"的" + 0.030*"。" + 0.018*"是" + 0.012*"在" + 0.012*"“" + 0.011*"”" + 0.009*"和" + 0.009*"、" + 0.007*"不"
0.053*";" + 0.047*"，" + 0.030*"&" + 0.029*"的" + 0.023*"。" + 0.021*"nbsp" + 0.008*"：" + 0.008*"是" + 0.008*"、" + 0.005*"gt"
0.030*"，" + 0.023*"《" + 0.022*"》" + 0.019*"的" + 0.015*"。" + 0.015*"、" + 0.014*"之" + 0.009*"&" + 0.008*"nbsp" + 0.007*"为"
0.041*"，" + 0.028*"。" + 0.021*"解放军" + 0.018*"、" + 0.015*"的" + 0.014*"台军" + 0.009*"空军" + 0.008*"架" + 0.007*"陆军" + 0.007*"）"
0.085*"，" + 0.058*"的" + 0.035*"。" + 0.017*"了" + 0.017*"是" + 0.014*"”" + 0.013*"“" + 0.012*"在" + 0.011*"一" + 0.011*"不"
0.116*"[" + 0.115*"]" + 0.048*":" + 0.043*"-" + 0.031*"，" + 0.017*"防空" + 0.011*"1" + 0.009*"。" + 0.008*"2" + 0.007*"的"
```


### 清理标点和无意义词

上面打印的每个主题的关键词, 有没有发现好多标点符号和各种无意义的词也进入了模型, 这会大大降低我们主题分类的效果, 那么, 我们要事先删除标点符号和无意义词.

我们需要使用pyltp对词性进行标注, 然后只保留词性为`['a', 'b', 'd', 'i', 'j', 'n', 'nh','ni', 'nl', 'ns', 'nt', 'nz', 'v']`的词.

```py

from pyltp import Postagger
poster = Postagger()
poster.load('D:\\mysites\\text-characters\\tcharacters\\ltp\\ltp_data\\pos.model')

def select_word(sentence:list):
    '''只保留词性为['a', 'b', 'd', 'i', 'j', 'n', 'nh',
            'ni', 'nl', 'ns', 'nt', 'nz', 'v']的词, 具体词性意义参考https://www.ltp-cloud.com/intro/#pos_how'''
    keep = ['a', 'b', 'd', 'i', 'j', 'n', 'nh',
            'ni', 'nl', 'ns', 'nt', 'nz', 'v']
    tags = poster.postag(sentence)
    for i in range(len(sentence)-1, -1, -1):
        if tags[i] not in keep:
            del sentence[i]
```

然后在加载数据的时候调用这个方法进行词语筛选, 所以修改一下这个方法:

```py
def load_corpus():
    d:Path
    corpus=[]
    for d in words_dir.iterdir():
        for fpath in d.iterdir():
            print('reading {}'.format(fpath))
            passage = json.load(open(fpath, 'r'))
            for sentence in passage:
                select_word(sentence)
            # 因为我们的句子信息不重要, 所以把所有句子合并成一个
            passage = [word for sentence in passage for word in sentence]
            corpus.append(passage)
    return corpus
```

### 最终结果

```cmd
0.010*"工作" + 0.010*"专业" + 0.008*"是" + 0.007*"大学" + 0.007*"解放军" + 0.006*"教育" + 0.005*"能力" + 0.005*"发展" + 0.005*"建设" + 0.005*"技术"
0.031*"是" + 0.019*"不" + 0.014*"也" + 0.011*"人" + 0.011*"有" + 0.011*"就" + 0.009*"都" + 0.009*"说" + 0.007*"没有" + 0.007*"到"
0.014*"航母" + 0.014*"我军" + 0.009*"是" + 0.007*"建设" + 0.006*"发展" + 0.005*"教育部" + 0.005*"毛" + 0.005*"主权" + 0.005*"大" + 0.005*"为"
0.012*"师" + 0.009*"军" + 0.009*"直播员" + 0.008*"战斗力" + 0.006*"球" + 0.005*"拦截" + 0.004*"5月" + 0.004*"为" + 0.003*"指挥" + 0.003*"退役"
0.017*"伊朗" + 0.013*"空军" + 0.013*"飞机" + 0.009*"旅游" + 0.009*"考生" + 0.008*"志愿" + 0.008*"军事" + 0.008*"是" + 0.007*"录取" + 0.006*"陈水扁"
0.015*"将" + 0.015*"美国" + 0.010*"是" + 0.008*"中国" + 0.007*"航空" + 0.007*"为" + 0.006*"目前" + 0.006*"台" + 0.006*"飞机" + 0.006*"到"
0.013*"战争" + 0.010*"防务" + 0.006*"文章" + 0.006*"是" + 0.005*"为" + 0.005*"考研" + 0.005*"蒋介石" + 0.005*"有" + 0.003*"师团" + 0.003*"作者"
0.011*"为" + 0.010*"农民" + 0.007*"政权" + 0.006*"农村" + 0.006*"是" + 0.005*"斯大林" + 0.004*"有" + 0.003*"不" + 0.003*"大" + 0.003*"历史"
0.030*"是" + 0.024*"不" + 0.016*"有" + 0.014*"就" + 0.013*"人" + 0.009*"都" + 0.009*"也" + 0.008*"要" + 0.008*"说" + 0.007*"会"
0.018*"公司" + 0.013*"银行" + 0.009*"贷款" + 0.007*"北京" + 0.007*"投资" + 0.006*"市场" + 0.006*"毛泽东" + 0.005*"会计" + 0.005*"中国" + 0.005*"集团"
0.024*"部队" + 0.014*"防空" + 0.013*"官兵" + 0.009*"台军" + 0.008*"军队" + 0.007*"战士" + 0.007*"图" + 0.006*"指挥" + 0.005*"球" + 0.004*"兵力"
0.015*"是" + 0.012*"不" + 0.008*"有" + 0.007*"人" + 0.005*"就" + 0.005*"也" + 0.005*"时" + 0.004*"吃" + 0.004*"都" + 0.004*"可"
0.025*"中国" + 0.021*"是" + 0.012*"美国" + 0.009*"日本" + 0.007*"有" + 0.006*"也" + 0.006*"大" + 0.005*"导弹" + 0.005*"文化" + 0.005*"最"
0.040*"公司" + 0.023*"美国" + 0.016*"雷达" + 0.010*"英国" + 0.006*"隐形" + 0.006*"系统" + 0.005*"进行" + 0.005*"时间" + 0.005*"机动" + 0.005*"将"
0.044*"训练" + 0.006*"干部" + 0.005*"职工" + 0.005*"工资" + 0.005*"军区" + 0.005*"兵团" + 0.004*"规定" + 0.004*"不" + 0.004*"野战" + 0.004*"沈阳"
0.045*"是" + 0.016*"有" + 0.014*"不" + 0.012*"就" + 0.011*"要" + 0.010*"也" + 0.007*"问题" + 0.007*"可以" + 0.006*"会" + 0.006*"能"
0.023*"演习" + 0.022*"海军" + 0.013*"是" + 0.010*"潜艇" + 0.010*"有" + 0.008*"美军" + 0.007*"军演" + 0.007*"舰队" + 0.006*"军事" + 0.005*"直升机"
0.016*"武器" + 0.015*"发射" + 0.015*"导弹" + 0.012*"是" + 0.008*"试验" + 0.006*"不" + 0.006*"系统" + 0.006*"卫星" + 0.006*"弹道导弹" + 0.005*"将"
0.022*"俄" + 0.020*"俄罗斯" + 0.010*"自卫队" + 0.010*"将" + 0.006*"系统" + 0.005*"进行" + 0.005*"是" + 0.004*"主席" + 0.004*"编队" + 0.004*"拦截"
0.014*"为" + 0.005*"是" + 0.004*"右派" + 0.004*"大" + 0.004*"有" + 0.003*"位" + 0.003*"夏" + 0.003*"义和团" + 0.003*"不" + 0.003*"将"
```

以下是完整的源码:

```py
# encoding:utf8
import os
from pathlib import Path
import json


#项目文件夹
project_dir = Path('D:\\项目\\lda主题提取')
#搜狗新闻语料库文件夹
source_dir = project_dir / 'source'
#分好词以后语料库文件夹
words_dir = project_dir / 'words'

########### 分词 ##################

import pyltp
from pyltp import SentenceSplitter
from pyltp import Segmentor

# 分词模型路径
ci_model_path = 'D:\\mysites\\text-characters\\tcharacters\\ltp\\ltp_data\\cws.model'

# 分句器
sspliter = SentenceSplitter()
# 分词器
wspliter = Segmentor()
wspliter.load(ci_model_path)
def fenci(filepath:Path):
    relative=filepath.relative_to(source_dir)
    write_path = words_dir / relative
    # 分句
    try:
        passage = open(filepath, 'r', encoding='gbk').read()
    except UnicodeDecodeError:
        print('Error to Open file:{}'.format(filepath))
        return 

    sentences = sspliter.split(passage)
    splited = []
    for sent in sentences:
        words = wspliter.segment(sent)
        splited.append(list(words))
    write_path.parent.mkdir(parents=True, exist_ok=True)   
    f=open(write_path, 'w')
    f.write(json.dumps(splited))
    f.close()

def fenci_all():
    d: Path
    for d in source_dir.iterdir():
        for fpath in d.iterdir():
            print('split {}'.format(fpath))
            fenci(fpath)

fenci_all()
wspliter.release()



# lda
from pyltp import Postagger
poster = Postagger()
poster.load('D:\\mysites\\text-characters\\tcharacters\\ltp\\ltp_data\\pos.model')

def select_word(sentence:list):
    '''只保留词性为['a', 'b', 'd', 'i', 'j', 'n', 'nh',
            'ni', 'nl', 'ns', 'nt', 'nz', 'v']的词, 具体词性意义参考https://www.ltp-cloud.com/intro/#pos_how'''
    keep = ['a', 'b', 'd', 'i', 'j', 'n', 'nh',
            'ni', 'nl', 'ns', 'nt', 'nz', 'v']
    tags = poster.postag(sentence)
    for i in range(len(sentence)-1, -1, -1):
        if tags[i] not in keep:
            del sentence[i]


def load_corpus():
    d: Path
    corpus = []
    for d in words_dir.iterdir():
        for fpath in d.iterdir():
            print('reading {}'.format(fpath))
            passage = json.load(open(fpath, 'r'))
            for sentence in passage:
                select_word(sentence)
            # 因为我们的句子信息不重要, 所以把所有句子合并成一个
            passage = [word for sentence in passage for word in sentence]
            corpus.append(passage)
    return corpus

corpus = load_corpus()




from gensim import models, corpora

dic = corpora.Dictionary(corpus)
clean_data = [dic.doc2bow(words) for words in corpus]
lda = models.ldamodel.LdaModel(clean_data, id2word=dic,  num_topics=20)

# 查看主题

for topic in lda.print_topics(num_words=10):
    print(topic[1])

```