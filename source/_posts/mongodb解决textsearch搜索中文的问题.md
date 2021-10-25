
---

title: mongodb解决textsearch搜索中文的问题
date: 2019-06-21 12:44:03
tags: [mongodb, python, jieba, mongoengine]

---

这篇文章我主要介绍一下自己是如何在mongodb中实现中文的全文搜索功能的!

<!-- more -->

我们都知道, mongodb有textsearch的功能, 也就是文本搜索, 但是实际上它并没有对中文提供很好的支持, 因为中文并没有像英文那样的词干和分词符号(空格), 所以你在使用mongodb的文本搜索功能的时候难免会发现--根本没卵用!!!

为了解决这个问题, 我们其实可以给mongodb预先分好词, 为了简单起见, 我并不太追求分词的准确性, 使用的是最简单的jieba分词库, 这是python里的一个自然语言处理第三方库!

为了实现以上目标, 我们的工作分为两步:


- 将搜索字段进行分词, 并以空格为词的分隔符形成新的字符串
- 在mongodb中设置文本索引

### 安装和使用jieba

我们使用pip安装jieba:


```python
!pip install jieba
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Collecting jieba
  Using cached https://files.pythonhosted.org/packages/71/46/c6f9179f73b818d5827202ad1c4a94e371a29473b7f043b736b4dab6b8cd/jieba-0.39.zip
Building wheels for collected packages: jieba
  Building wheel for jieba (setup.py): started
  Building wheel for jieba (setup.py): finished with status 'done'
  Stored in directory: C:\Users\syd\AppData\Local\pip\Cache\wheels\c9\c7\63\a9ec0322ccc7c365fd51e475942a82395807186e94f0522243
Successfully built jieba
Installing collected packages: jieba
Successfully installed jieba-0.39

</div>
{% endraw %}

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
You are using pip version 19.0.3, however version 19.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

</div>
{% endraw %}

jieba中有专门为搜索而设的分词接口: cut_for_search


```python
import jieba

words = jieba.cut_for_search('你好mlln.cn, 我可以被分词吗?')
for w in words:
    print(w)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Building prefix dict from the default dictionary ...
Dumping model to file cache C:\Users\syd\AppData\Local\Temp\jieba.cache
Loading model cost 1.273 seconds.
Prefix dict has been built succesfully.

</div>
{% endraw %}

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
你好
mlln
.
cn
,
 
我
可以
被
分词
吗
?

</div>
{% endraw %}

### 设置mongodb的文本索引

我使用的是python中的mongoengine模块, 它可以帮助我们用类的方式组织Document, 我的其中一个需要搜索的Document的定义是这样的:


```python
class Questionaire(Document):
    qtype = StringField(required=True)
    source_id = StringField(required=True, unique=True)
    title = StringField(required=True)
    title_words = StringField(required=False)
    des = StringField(required=False)
    des_words = StringField(required=False)
    has_factor = BooleanField(default=False)
    has_data = BooleanField(default=False)
    meta = {
        'indexes': [
            'source_id', 
            {
                'fields': ['$title_words', "$des_words"],
                'default_language': 'english',
                'weights': {'title_words': 10, 'des_words': 2}
            }
        ]
    }
```

你不需要理解上面的代码, 你只需要看meta这个成员, 它定义了索引, 第二个索引就是一个文本索引:
```
    {
        'fields': ['`$title_words', "$`

### 分词

使用jieba将需要分词的字段进行分词, 然后重新组合成分词后的字符串, 伪代码是这样的:


```python
def fenci(sentence: str)->str:
    words = jieba.lcut_for_search(sentence)
    return ' '.join(words)
```

我们使用上面的方法分词以后, 将分词后的字符串保存到mongodb, 然后就可以进行搜索了:

### 搜索

核心的方式就是使用search_text方法进行搜索, 排序的话使用text_score, 这个text_score的定义就要看我们在构建索引的时候定义的计算权重:` 'weights': {'title_words': 10, 'des_words': 2}`, 它的意思是title_words占10分, des_words占2分, 以这样的权重来计算text_score。


```python
from itembank import models as M 
from itembank import settings

M.get_cnn(settings.DBNAME)
qs = M.Questionaire.objects.search_text('生活').order_by('$text_score')
print(qs)
```

搜索得到的结果就是:
```
[<Questionaire: <Questionaire 大学生生活体验调查问卷>>]
```


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](mongodb解决textsearch搜索中文的问题.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
