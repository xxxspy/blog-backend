---
title: 使用textgenrnn生成文本(最后生成中文)
date: 2018-10-16 20:17:55
tags: [keras, tensorflow]
toc: true
xiongzhang: false

---
<span></span>
<!-- more -->


本文代码运行环境:

- windows10
- python3.6
- jupyter notebook

## textgenrnn Demo

改编by [DataScience](http://mlln.cn)

## 简介

`textgenrnn`是一个python库, 用于生成文本, 后端使用tesorflow和keras。下面我们引入用到的库:


```python
from textgenrnn import textgenrnn

textgen = textgenrnn()
```

{% raw %}
<div class="output">
输出(stream):<br>
    Using TensorFlow backend.
    <br />
</div>
{% endraw %}

## 生成文本

使用`generate` 函数生成n个短文:


```python
textgen.generate(5)
```

{% raw %}
<div class="output">
输出(stream):<br>
    I have a post on the world of the most content company to recognize the season by 100% Linux in a console most police of the state of one set of summer and expecting the set of massacress and service offers than the mains of the shit in the PC statue that the players the story of the card for the 
    <br />
    <br />[Humor] I got a programming family for a new day
    <br />
    <br />[AMA Request] Don't even want to stay the world in the first interviewer in the this subreddit and you are the best gift to the plane of the house of some enough to be a little amateur depressed and was the other thing?
    <br />
    <br />The New York Tattoo - The Group Stream
    <br />
    <br />[USA-CA] [H] iPhone 7 Personal Pro [W] Paypal
    <br />
    <br />
</div>
{% endraw %}

另外，你可以设置`temperature`来修改创造性指数（默认为0.5;我不建议设置为1.0以上），设置`prefix`来强制文档以某些字符开头并相应地生成字符，并设置`return_as_list`标志（默认为False）以在应用程序的其他位置使用生成的文本（例如，作为API）


```python
generated_texts = textgen.generate(n=5, prefix="Trump", temperature=0.2, return_as_list=True)
print(generated_texts)
```

{% raw %}
<div class="output">
输出(stream):<br>
    ['Trump is a lot of stories of the same to the post on the show of the best friends and the subreddit is the program and I have a stranger to be a man who was a strange of the picture of the state of the season to the season to the state of the state of the state of the shop to the company in the mo', 'Trump supporters will be a good time to see the survival than they are a good time to be a company to a bad face on the first time to be a player in the same to start and has a stranger that we had a reality of the world?', 'Trump is a beautiful school and should be a good country?', 'Trump companies a book of the results of the season that we should have a stranger to have the person to a strange and the computer is a stranger than the best family of the state of the new people that are the best states of the state with the results of the party to the state of the same time to', 'Trump is a big time and can start a month on a party in the background of the sidewalk and a real person to the story of the posts and they are a little bank of the state of the state of the state of the season that you can see the team and it was to take a picture of the best friends and then he ']
    <br />
</div>
{% endraw %}


使用`generate_samples（）`测试不同'tenperature'模型。


```python
textgen.generate_samples()
```

{% raw %}
<div class="output">
输出(stream):<br>
    ####################
    <br />Temperature: 0.2
    <br />####################
    <br />[Spoiler] The song with the streamer in the first time in the state of the same time to show your favorite parents in the company
    <br />
    <br />What is the best story of the state of the story?
    <br />
    <br />[PS4] [H] 2000 GTX 1080 [W] Paypal
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />This is what the popular posts looks like a friend with the holidays in a police player when you just go to help?
    <br />
    <br />I don't want to see the world with the most program but they should be able to discover them.
    <br />
    <br />What is this bloom at home and here i suck you that was a lot of the talents and fans when they realize how to use the posts of the street services that is a post with a part of a great show of the trip in the wrong school
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />Meditations just got mum supporting where's dragon of his friends depressed.
    <br />
    <br />Channel will [Nuar] and Planned up about the cargoria
    <br />
    <br />Small shot is my boy. He hasn't been but I'm not missed. She would be sure if anymore.
    <br />
    <br />
</div>
{% endraw %}



你也可以`generate_to_file（）`使生成的文本更容易复制/粘贴到其他来源（例如博客/社交媒体）：


```python
textgen.generate_to_file('textgenrnn_texts.txt', n=5)
```

## 使用新的文本训练


如上所示，预训练模型的结果差别很大，因为它是以小形式压缩的大量数据。 `train_on_texts`函数可以在新数据集上对模型进行微调。


```python
texts = ['Never gonna give you up, never gonna let you down',
            'Never gonna run around and desert you',
            'Never gonna make you cry, never gonna say goodbye',
            'Never gonna tell a lie and hurt you']

textgen.train_on_texts(texts, num_epochs=2,  gen_epochs=2)
```

{% raw %}
<div class="output">
输出(stream):<br>
    Training on 174 character sequences.
    <br />Epoch 1/2
    <br />1/1 [==============================] - 1s 1s/step - loss: 1.3999
    <br />Epoch 2/2
    <br />1/1 [==============================] - 0s 144ms/step - loss: 1.3371
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />Never really gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gon
    <br />
    <br />Never really gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gonna gon
    <br />
    <br />Never run and deserts
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />Never really gonna ganna never and run in run and great and gonna gonna gonna desert
    <br />
    <br />Never really never leven givea and you gonnathake
    <br />
    <br />Never really develant, and deserts in and design
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />Never
    <br />
    <br />Never up, let any day, but
    <br />
    <br />Never you guy with
    <br />
    <br />
</div>
{% endraw %}

虽然网络只接受了4个文本的训练，但原始网络仍然学会了所有现代语法的潜在知识，并且可以将这些知识融入生成的文本中，这在较高的`tenperature`下或使用前缀包含原始文件中不存在的字符时你可以看的更明显。


您可以通过调用`reset（）`将训练模型重置回原始状态。


```python
textgen.reset()
```



存储库中包含一个`hacker-news-2000.txt`文件，其中包含按分数提交的Top 2000 [Hacker News]（https://news.ycombinator.com/news）列表。让我们使用该数据集重新训练模型。

对于这个例子，我只使用一个epoch来证明模型只用一次数据传递就可以轻松学习：我建议保留默认的50个epoch，或者为复杂的数据集设置更高的epoch。在我的2016年15“MacBook Pro（四核Skylake CPU）上，数据集每个epoch大约需要1.5分钟。


```python
textgen.train_from_file('./datasets/hacker_news_2000.txt', num_epochs=1)
```

{% raw %}
<div class="output">
输出(stream):<br>
    2,000 texts collected.
    <br />Training on 83,501 character sequences.
    <br />Epoch 1/1
    <br />652/652 [==============================] - 96s 147ms/step - loss: 1.8858
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />A Simple Programmer
    <br />
    <br />A Strip Show HN: Some software company is compand with the programmer
    <br />
    <br />A Startup Startup Startup Startup
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />Progrey and Scott to be not use and string rooted and match in a boot and computer lawden and computer don't there in the beactice about secret activations
    <br />
    <br />A created a computer company cry severe on code, interverse movines over don't command the match to some company and startup
    <br />
    <br />What I'm Computer Satelles
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />Hunakix 164% Visual strucces developers emisome
    <br />
    <br />The ford articles source for and identify the paperse years orders, than everything Noter 00
    <br />
    <br />literals overbights a please adt diverses Amazon's Hirishot case icoprepastic
    <br />
    <br />
</div>
{% endraw %}

现在，我们可以创建非常明显的HN标题，即使只需要很少的培训，这要归功于textgenrnn的预训练性质：


```python
textgen.generate(5, prefix="Apple")
```

{% raw %}
<div class="output">
输出(stream):<br>
    Apple 1016 Google Asking Linux
    <br />
    <br />Apple Peanly Open-Dear Sends Our Paster in Secure Secret Show HN: A website in the movie as here in the website of a programmable
    <br />
    <br />Apple Progrestice Secret Behind Pare Pater of Hearters
    <br />
    <br />Apple to be company to entered the report
    <br />
    <br />Apple stop companies code of a coder on the secret source into a startup for the source
    <br />
    <br />
</div>
{% endraw %}



`train_on_text`和`train_from_file`的其他运行参数是：

- *`num_epochs`：要训练的epoch数（默认值：50）
- *`gen_epochs`：生成样本输出之间运行的时期数;适用于测量模型进度（默认值：1）
- *`batch_size`：训练的批量大小;如果在GPU上运行以加快培训速度，可能需要增加（默认值：128）
- *`train_size`：要保留的序列样本的随机比例：适合控制过度拟合。其余的将用于训练作为验证集。 （默认值：1.0 /全部）。要禁用验证集上的训练（速度），请设置`validation = False`。
- *`dropout`：保留的序列激活比例。适合控制过度拟合/提高对打字错误的抵抗力，但设置过高会导致网络过早收敛。 （默认值：0.0）
- *`is_csv`：如果源文件是单列CSV（例如从BigQuery或Google表格中导出），则使用`train_from_file`以获得正确的换行符。

## 保存和加载模型

模型在每个epoch后自动保存权重，或者您可以调用`save（）`并给出HDF5文件名。然后，通过指定构造中权重的路径，可以将这些权重加载到新的textgenrnn模型中。 （或者对现有的textgenrnn对象使用`load（）`）。


```python
textgen_2 = textgenrnn('textgenrnn_weights.hdf5')
textgen_2.generate_samples()
```

{% raw %}
<div class="output">
输出(stream):<br>
    ####################
    <br />Temperature: 0.2
    <br />####################
    <br />Google is a broke and down
    <br />
    <br />A Starter in Amazering in a Google Startup
    <br />
    <br />The Web Defines Supports For Conternation
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />Good Dropbox Down to die
    <br />
    <br />Playing Source Aid of Adding Program For Operate
    <br />
    <br />Will Claim To So Formate For Founder
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />We was direction factiongend fine and GoDake
    <br />
    <br />John no over relied from new Stude
    <br />
    <br />Leaching A “Yeuari Drawn”
    <br />
    <br />
</div>
{% endraw %}


```python
textgen.model.get_layer('rnn_1').get_weights()[0] == textgen_2.model.get_layer('rnn_1').get_weights()[0]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    array([[ True,  True,  True, ...,  True,  True,  True],
    <br />       [ True,  True,  True, ...,  True,  True,  True],
    <br />       [ True,  True,  True, ...,  True,  True,  True],
    <br />       ...,
    <br />       [ True,  True,  True, ...,  True,  True,  True],
    <br />       [ True,  True,  True, ...,  True,  True,  True],
    <br />       [ True,  True,  True, ...,  True,  True,  True]])

</div>
{% endraw %}



实际上，原始模型和新模型之间的权重是相等的。

您可以使用此功能从其他人那里加载模型，这些模型已经在具有更多历元的更大数据集上进行了训练（并且模型权重足够小以适合电子邮件发送！）。


```python
textgen = textgenrnn('../weights/hacker_news.hdf5')
textgen.generate_samples(temperatures=[0.2, 0.5, 1.0, 1.2, 1.5])
```

{% raw %}
<div class="output">
输出(stream):<br>
    ####################
    <br />Temperature: 0.2
    <br />####################
    <br />A startup’s Firebase bill suddenly increased from $25 to $1750 per month
    <br />
    <br />A Sister’s Eulogy for Steve Jobs
    <br />
    <br />The Website That Got Me Expelled
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />How to Sleep
    <br />
    <br />Ask HN: What are some examples of successful single-person businesses?
    <br />
    <br />Solar Roof
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />Germanā was asked a disappeared to dismay explosions to just work
    <br />
    <br />“Gat Vueal Cities, Weakphad
    <br />
    <br />The New Internet Talk
    <br />
    <br />####################
    <br />Temperature: 1.2
    <br />####################
    <br />In Iraq, for jhilious backg program in a comparn
    <br />
    <br />Solar Rook Point: The NSA-indiepatorogamerace
    <br />
    <br />Ask.jecket shilk
    <br />
    <br />####################
    <br />Temperature: 1.5
    <br />####################
    <br />Nodelover Misses wringless for ununticed processing on Ach destroyer is a watched sysemer 
    <br />
    <br />Police Leeh was ruins to work RTA-a litrame related
    <br />
    <br />A $10K tiny homepage in RSH galace
    <br />
    <br />
</div>
{% endraw %}

## 训练全新模型(生成中文文本)

您可以使用任何现代RNN架构训练新模型，如果提供文本，则调用“train_new_model”，或者如果从文件训练，则添加“new_model = True”参数。如果你这样做，除了权重之外，模型将保存一个`config`文件和一个`vocab`文件，这些文件也必须加载到`textgenrnn`实例中。

可用的配置参数是：

- *`word_level`：是否在单词级别训练模型（默认值：False）
- *`rnn_layers`：模型中循环LSTM层的数量（默认值：2）
- *`rnn_size`：每个LSTM层中的单元数（默认值：128）
- *`rnn_bidirectional`：是否使用双向LSTM，它考虑向前和向后的序列。如果输入文本遵循特定架构，则建议使用。 （默认值：False）
- *`max_length`：在预测下一个标记之前使用的前一个字符/单词的最大数量。对于字级模型，应减少此值（默认值：40）
- *`max_words`：训练时要考虑的最大字数（按频率）（默认值：10000）
- *`dim_embeddings`：字符/单词嵌入的维度（默认值：100）

您还可以在创建textgenrnn实例时指定`name`，这将有助于适当地命名输出权重/配置/词汇。




```python
textgen = textgenrnn(name="chinese_poetry")
```


```python
textgen.reset()
textgen.train_from_file('./datasets/chinese-poetry.txt',
                        new_model=True,
                        batch_size=4,
                        rnn_bidirectional=True,
                        rnn_size=64,
                        dim_embeddings=300,
                        num_epochs=20)

print(textgen.model.summary())
```

{% raw %}
<div class="output">
输出(stream):<br>
    9 texts collected.
    <br />Training new model w/ 2-layer, 64-cell Bidirectional LSTMs
    <br />Training on 117 character sequences.
    <br />Epoch 1/20
    <br />29/29 [==============================] - 3s 101ms/step - loss: 5.0417
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />中中撷撷游中撷中中中中中中撷中中中中中撷中游少中中中中少撷声中中浑
    <br />
    <br />中撷中中头中撷撷中在中中物中撷中中中中中中中中中中中
    <br />
    <br />在撷游撷撷生中中中中中中中中中中中中中发中中中生游中中风浑
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />中晓母在南风生豆晓晓慈风豆中慈当头晓愿风
    <br />
    <br />游游中在生游晓心撷游在中撷少中
    <br />
    <br />采中中搔生晓晓夜白得南短游声三晓游游撷游中晓心落生谁中处浑晓木。衣
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />湿中红母搔撷言游寸夜风晖手浑寸身来撷撷中采夜愿几线。三花最多物谁发上最花风发晖锦看重思短时时簪
    <br />
    <br />风在游在城此白游节
    <br />
    <br />撷在豆官白游言子风多得搔胜来愿采身山湿
    <br />
    <br />Epoch 2/20
    <br />29/29 [==============================] - 1s 29ms/step - loss: 4.0177: 0s - loss:
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />来，，，春。
    <br />
    <br />看国，春春，春。
    <br />
    <br />，，，官春。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />更撷游处线知线。
    <br />
    <br />来
    <br />
    <br />，国发国线发不
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />雨几看来欲晖言
    <br />
    <br />雨，思头相头晖。
    <br />
    <br />最，君短衣谁雨当头，知生春木深重。
    <br />
    <br />Epoch 3/20
    <br />29/29 [==============================] - 1s 29ms/step - loss: 3.6351
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />，国，，春。
    <br />
    <br />国国，春乃乃乃枝。
    <br />
    <br />看看国，，春乃乃乃枝。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />短愿不。
    <br />
    <br />愿慈白采，游胜。
    <br />
    <br />夜看多采多物物最物相物物最最相物物最相物最相相相相。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />愿发君知多
    <br />
    <br />母几不，，官。
    <br />
    <br />白欲线君乃国
    <br />
    <br />Epoch 4/20
    <br />29/29 [==============================] - 1s 29ms/step - loss: 3.0203
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />红红雨红，花多多多，城深深深深深。
    <br />
    <br />国，破河河河，城深深深深深深深深。
    <br />
    <br />头红红，浑不胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜胜
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />夜红白，城春深。
    <br />
    <br />国春枝锦多。
    <br />
    <br />红雨雨雨，上物上深。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />雨风撷国寸衣浑春几河上胜胜锦不胜相不胜胜胜胜胜胜。胜
    <br />
    <br />来生君中言，生草思处，官最思。
    <br />
    <br />看慈胜官浑，城锦上胜晖。
    <br />
    <br />Epoch 5/20
    <br />29/29 [==============================] - 1s 29ms/step - loss: 2.3797
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />国破山河在，城春草草草草草。
    <br />
    <br />国破山在，城春草草草木。
    <br />
    <br />国破山在，城春草草草。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />红南国，春。
    <br />
    <br />慈破知节，花落知多多，。
    <br />
    <br />白夜红湿处花重重锦。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />红南来湿，花知知多多多节，春生发。
    <br />
    <br />头破节春发发多。
    <br />
    <br />国山山看知风花。
    <br />
    <br />Epoch 6/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 1.7550
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />红豆南国春来发几。
    <br />
    <br />白头更短短，浑欲不簪。
    <br />
    <br />白头短短，浑欲不簪。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />白头更短短，浑欲不簪。
    <br />
    <br />好雨雨声，游身身衣。
    <br />
    <br />慈手中线，游身衣。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />头风撷寸草心春晖身晖。
    <br />
    <br />湿欲短短三春，晖三春晖三春生。
    <br />
    <br />子中好雨声在，中身最衣。
    <br />
    <br />Epoch 7/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 1.2185
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />国破山河在，城春草草草草草草草草春。
    <br />
    <br />国破山河在，城春草草草深。
    <br />
    <br />国破山河在，城春草草草草草草草春。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />慈母手中线，游子子子子子上衣。
    <br />
    <br />国破山河在，城春草草草深草深。
    <br />
    <br />国破山河在，春。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />南国山山河在河，城春深深深深。
    <br />
    <br />好雨知时节春发发生生。
    <br />
    <br />豆知多枝。
    <br />
    <br />Epoch 8/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.8539
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />国破山河在，城春木深。
    <br />
    <br />国破山河在，城春木木深。
    <br />
    <br />谁言寸心，报得三春晖。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />国破山河在，城春草木深。
    <br />
    <br />国破山河在，城春木深。
    <br />
    <br />慈母手中线，游子身上。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />红风雨知节春发夜生。
    <br />
    <br />谁言短，浑欲不胜簪。
    <br />
    <br />三破山河生城春木落几枝。
    <br />
    <br />Epoch 9/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.5789
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />国破山河在，城春草木深。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />慈母手中线，游子身上衣。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />愿君多采撷，此物最相相。
    <br />
    <br />愿君多采撷，此物最相。
    <br />
    <br />国破山河在，城春草深。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />谁言寸草，报得三春。
    <br />
    <br />国破山山多采撷，此物最相思。
    <br />
    <br />慈母手中线，游子身晖身上衣。
    <br />
    <br />Epoch 10/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.4246
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />国破山河在，城春草草木深。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />好雨知时节，，当春乃发。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />国破山山在，城春草木深。
    <br />
    <br />白更短浑胜簪。
    <br />
    <br />Epoch 11/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.3293
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />愿君多采撷，此物最相相思。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />愿君多采撷，此物最相思。
    <br />
    <br />夜来风雨声，花落知多少。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />慈母手中线，游子身上衣。
    <br />
    <br />愿君多采撷，此物最相思思。
    <br />
    <br />更不胜簪。
    <br />
    <br />Epoch 12/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.2825
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />国破山河在，城春草木深。
    <br />
    <br />慈母手中线，游子身上衣。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />夜来风雨声，花落知多少。
    <br />
    <br />红豆生南国，春来发几枝。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />母手中线，报得三春晖。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />愿君多采撷，此最思几胜簪。
    <br />
    <br />Epoch 13/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.2709
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />红豆生南国，春来发几枝。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />夜来风雨声，花落知多少。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />夜来风雨声，花落知多少。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />夜来风雨声，花落知多少。
    <br />
    <br />白头搔更短，游浑不胜锦。
    <br />
    <br />愿君多采节，当春乃发几枝。
    <br />
    <br />Epoch 14/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.2547
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />愿君多采撷，此物最相思。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />好雨知时节，当春乃发生。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />红豆生南国，花重锦官城。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />慈母手中线，游子身上衣。
    <br />
    <br />Epoch 15/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.2344
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />慈母手中线，游子身上衣。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />愿君多采撷，此物最相思。
    <br />
    <br />愿君多采撷，此物最思欲不胜簪。
    <br />
    <br />晓看红湿处，花重锦官城春草。
    <br />
    <br />Epoch 16/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.2238
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />愿君多采撷，此物最相思。
    <br />
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />慈母手中线，游子身上衣。
    <br />
    <br />夜来风雨声，花落知多少。
    <br />
    <br />红豆生南国，春来发几枝。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />慈母手中线，游子身上衣。
    <br />
    <br />夜来风雨声，花落知多少。
    <br />
    <br />好雨知时节，当春乃发生。
    <br />
    <br />Epoch 17/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.1942
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />国破山河在，城春草木深。
    <br />
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />好雨知时节，当春乃发生。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />言寸草心，报得三春晖。
    <br />
    <br />红豆生南国，春来发几枝。
    <br />
    <br />谁言寸草心，报报得三春晖。
    <br />
    <br />Epoch 18/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.2101
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />红豆生南国，春来发几枝。
    <br />
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />愿君多采撷，此物最相思。
    <br />
    <br />慈母手中线，游子身上衣。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />夜来风雨声，花落知多少。
    <br />
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />Epoch 19/20
    <br />29/29 [==============================] - 1s 31ms/step - loss: 0.1815
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />夜来风雨声，花落知多少。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />国破山河在，城春草木深。
    <br />
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />夜来风雨声，花落知多少。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />愿君多采撷，此物最相思。
    <br />
    <br />红豆生南国，春来发几枝。
    <br />
    <br />好雨知时节，当春乃发生。
    <br />
    <br />Epoch 20/20
    <br />29/29 [==============================] - 1s 30ms/step - loss: 0.1795
    <br />####################
    <br />Temperature: 0.2
    <br />####################
    <br />国破山河在，城春草木深。
    <br />
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />红豆生南国，春来发几枝。
    <br />
    <br />好雨知时节，当春乃发生。
    <br />
    <br />好雨知时节，当春乃发生。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />谁言寸草心心，报得三春晖。
    <br />
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />__________________________________________________________________________________________________
    <br />Layer (type)                    Output Shape         Param #     Connected to                     
    <br />==================================================================================================
    <br />input (InputLayer)              (None, 40)           0                                            
    <br />__________________________________________________________________________________________________
    <br />embedding (Embedding)           (None, 40, 300)      24000       input[0][0]                      
    <br />__________________________________________________________________________________________________
    <br />rnn_1 (Bidirectional)           (None, 40, 128)      186880      embedding[0][0]                  
    <br />__________________________________________________________________________________________________
    <br />rnn_2 (Bidirectional)           (None, 40, 128)      98816       rnn_1[0][0]                      
    <br />__________________________________________________________________________________________________
    <br />rnn_concat (Concatenate)        (None, 40, 556)      0           embedding[0][0]                  
    <br />                                                                 rnn_1[0][0]                      
    <br />                                                                 rnn_2[0][0]                      
    <br />__________________________________________________________________________________________________
    <br />attention (AttentionWeightedAve (None, 556)          556         rnn_concat[0][0]                 
    <br />__________________________________________________________________________________________________
    <br />output (Dense)                  (None, 80)           44560       attention[0][0]                  
    <br />==================================================================================================
    <br />Total params: 354,812
    <br />Trainable params: 354,812
    <br />Non-trainable params: 0
    <br />__________________________________________________________________________________________________
    <br />None
    <br />
</div>
{% endraw %}

现在可以加载已经训练好的权重/磁带你/配置信息:


```python


textgen_2 = textgenrnn(weights_path='chinese_poetry_weights.hdf5',
                       vocab_path='chinese_poetry_vocab.json',
                       config_path='chinese_poetry_config.json')

textgen_2.generate_samples()
```

{% raw %}
<div class="output">
输出(stream):<br>
    ####################
    <br />Temperature: 0.2
    <br />####################
    <br />夜来风雨声，花落知多少。
    <br />
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />红豆生南国，春来发几枝。
    <br />
    <br />####################
    <br />Temperature: 0.5
    <br />####################
    <br />谁言寸草心，报得三春晖。
    <br />
    <br />夜来风雨声，花落知多少。
    <br />
    <br />晓看红湿处，花重锦官城。
    <br />
    <br />####################
    <br />Temperature: 1.0
    <br />####################
    <br />白头搔更短，浑欲不胜簪。
    <br />
    <br />好时节，当春晖。
    <br />
    <br />国破山河在，城春草木深。
    <br />
    <br />
</div>
{% endraw %}

## 在大型文本文件上训练


尽管textgenrnn旨在对文本文档进行训练，但您可以使用`train_from_largetext_file`（加载整个文件并将其处理为单个文档）在大文本块上训练它，它应该可以正常工作。这类似于更传统的char-rnn教程。

建议训练新模型（默认情况下）。当调用`generate`时，你可能想要增加`max_gen_length`的值。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](textgenrnn-demo.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
