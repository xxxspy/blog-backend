---
title: sentimentpy模块进行中文文本情感分类
date: 2018-10-14 18:15:09
tags: [文本挖掘, 情感分析]
---

sentimentpy是我根据R语言的一个文本情感分析包`sentiment`进行开发的, 开发的初衷有:

- R的sentiment已经被弃坑, 没人维护
- Python比R更擅长文本处理
- sentiment包不支持中文

而sentimentpy包有如下特点:

- 使用朴素贝叶斯分类算法
- 利用了情感词典
- 支持中英文
- 支持情绪分类(喜怒哀乐恶惊)
- 支持极性分类(positive/negtive/both)

正在开发的功能:

- 利用语料库训练神经网络进行分类

<!-- more -->

### 用到的词库

具体来说, 中英文的分类类别是不同的, 这受限于中英文使用了不同的情感词库, 英文的情感词库来自于R的sentiment库, 而中文的情感词库是大连理工大学信息检索研究室在林鸿飞教授标注的一个中文情感词库, 在这里有介绍: [传送门](http://mlln.cn/2018/10/11/%E4%B8%AD%E6%96%87%E6%83%85%E6%84%9F%E5%88%86%E6%9E%90%E8%AF%AD%E6%96%99%E5%BA%93%E5%A4%A7%E5%85%A8-%E5%B8%A6%E4%B8%8B%E8%BD%BD%E5%9C%B0%E5%9D%80/)


### 中文情感类别(英文的参考R sentiment库)

具体参考下表, 我们把句子分类下面6个情感大类。

编号	情感大类	情感类	例词
1	乐	快乐(PA)	喜悦、欢喜、笑眯眯、欢天喜地
2		安心(PE)	踏实、宽心、定心丸、问心无愧
3	好	尊敬(PD)	恭敬、敬爱、毕恭毕敬、肃然起敬
4		赞扬(PH)	英俊、优秀、通情达理、实事求是
5		相信(PG)	信任、信赖、可靠、毋庸置疑
6		喜爱(PB)	倾慕、宝贝、一见钟情、爱不释手
7		祝愿(PK)	渴望、保佑、福寿绵长、万寿无疆
8	怒	愤怒(NA)	气愤、恼火、大发雷霆、七窍生烟
9	哀	悲伤(NB)	忧伤、悲苦、心如刀割、悲痛欲绝
10		失望(NJ)	憾事、绝望、灰心丧气、心灰意冷
11		疚(NH)	内疚、忏悔、过意不去、问心有愧
12		思(PF)	思念、相思、牵肠挂肚、朝思暮想
13	惧	慌(NI)	慌张、心慌、不知所措、手忙脚乱
14		恐惧(NC)	胆怯、害怕、担惊受怕、胆颤心惊
15		羞(NG)	害羞、害臊、面红耳赤、无地自容
16	恶	烦闷(NE)	憋闷、烦躁、心烦意乱、自寻烦恼
17		憎恶(ND)	反感、可耻、恨之入骨、深恶痛绝
18		贬责(NN)	呆板、虚荣、杂乱无章、心狠手辣
19		妒忌(NK)	眼红、吃醋、醋坛子、嫉贤妒能
20		怀疑(NL)	多心、生疑、将信将疑、疑神疑鬼
21	惊	惊奇(PC)	奇怪、奇迹、大吃一惊、瞠目结舌

### 中文极性

sentimentpy可以将句子分为四种极性: positive/negtive/neutral/both
英文可以分为三种极性: positive/negtive/neutral

### 中文分词

建议使用`jieba2`, 并加载情感词库以后进行分词, 这样可以尽量把句子按照词库中已有的词进行分词。
sentimentpy这个库已经包含了分词的功能。


### 下面是我的测试:

```python
import unittest
from sentiment import sentiment

class Test(unittest.TestCase):

    def test_chinese(self):
        classifier = sentiment.Classifier('zh')
        # 必须用空格分词
        rtn = classifier.polarity('我 喜欢 这个 手机')
        self.assertEqual(rtn['best_fit_cat'], 'positive')
        rtn = classifier.polarity('我 今天 很 难过')
        self.assertEqual(rtn['best_fit_cat'], 'neutral')
        rtn = classifier.polarity('我 讨厌 你 你 滚开')
        self.assertEqual(rtn['best_fit_cat'], 'negative')

        rtn = classifier.emotion('我 喜欢 这个 手机')
        self.assertEqual(rtn['best_fit_cat'], '好')
        rtn = classifier.emotion('我 今天 很 难过')
        self.assertEqual(rtn['best_fit_cat'], '哀')
        rtn = classifier.emotion('我 讨厌 你 你 滚开')
        self.assertEqual(rtn['best_fit_cat'], '恶')

    
    def test_english(self):
        classifier = sentiment.Classifier('en')
        rtn = classifier.polarity('i love this cellphone')
        self.assertEqual(rtn['best_fit_cat'], 'positive')
        rtn = classifier.polarity('i am so sad today')
        self.assertEqual(rtn['best_fit_cat'], 'negative')
        rtn = classifier.polarity('i hate you fuck away')
        self.assertEqual(rtn['best_fit_cat'], 'negative')

        rtn = classifier.emotion('i love this cellphone')
        self.assertEqual(rtn['best_fit_cat'], 'joy')
        rtn = classifier.emotion('i am so sad today')
        self.assertEqual(rtn['best_fit_cat'], 'sadness')
        rtn = classifier.emotion('i hate you fuck away')
        self.assertEqual(rtn['best_fit_cat'], 'anger')

if __name__ == '__main__':
    unittest.main()

```
