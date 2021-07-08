
---
title: keras教程-n-10分钟入门LSTM
date: 2018-09-02 20:17:55
tags: [keras教程]
toc: true
xiongzhang: false

---
<span></span>
<!-- more -->


本文代码运行环境:

- windows10
- python3.6
- jupyter notebook
- tensorflow 1.x
- keras 2.x

用过keras的人可能都遇到过这个问题: 怎么用keras来实现一个序列到序列的LSTM网络, 因为这个网络相对于简单的多层感知机要复杂很多。今天我们就用10分钟来实现一个lstm神经网络。前提是你对这个网络结构已经有一些了解。 

### 什么是seq2seq模型(序列到序列的模型)

序列到序列的模型指的是模型的输入和输出都是一个序列, 比如机器翻译, 输入是中文的句子, 输出是英文的句子。这样的模型还可以被用于对话机器人或者一些文字生成的场景。

#### 简单模型:输入的序列和输出序列长度都相同

当输入序列和输出序列具有相同的长度时，您可以使用Keras LSTM或GRU层简单地实现这些模型。这个示例脚本就是这种情况，它显示了如何教RNN学习数字加法：

<img src="images/add-nums.png" />

这种方法的一个警告是，它假设有了输入就能产生输出。这在某些情况下有效（数字字符串加法），但对大多数用例不起作用。在一般情况下，关于整个输入序列的信息是必要的，以便开始生成目标序列。

#### 更通用的模型:输入和输出长度不同

在一般情况下，输入序列和输出序列具有不同的长度（例如机器翻译），并且需要整个输入序列以便开始预测目标。这需要更高级的设置，这是人们在提及没有进一步上下文的“序列到序列模型”时通常所指的。以下是它的工作原理：

- RNN层充当“编码器”：它处理输入序列并返回其自己的内部状态。注意，我们丢弃编码器RNN的输出，仅使用状态信息。该状态将用作下一步骤中解码器的“上下文”。
- 另一个RNN层（或其堆栈）充当“解码器”：在给定目标序列的先前字符的情况下，训练它以预测目标序列的下一个字符。具体而言，训练模型将目标序列转换为相同的序列但偏移一个时间步骤，在此上下文中称为“教师强制”的训练过程。重要的是，解码器使用来自编码器的状态向量作为初始状态，这是解码器获得应该生成什么的信息。

<img src="images/seq2seq.png" />


在预测阶段, 也就是在解码未知输入序列时, 我们经过的步骤有所不同:

1）将输入序列编码为状态向量。
2）从大小为1的目标序列开始（只是序列开始字符）。
3）将状态向量和1-char目标序列馈送到解码器以产生对下一个字符的预测。
4）使用这些预测对下一个字符进行采样（我们只使用argmax）。
5）将采样的字符附加到目标序列
6）重复，直到我们生成序列结束字符或我们达到序列最长限制。

### keras案例

我们用代码来加强理解。

对于我们的示例，我们将使用成对的英语句子及其中文翻译的数据集，您可以从[网站(mlln.cn)下载](http://mlln.cn/2018/08/26/机器翻译语料库大全(免费下)) 。要下载的文件名为 cmn-eng.zip。我们将实现一个字符级的序列到序列模型，逐个字符地处理输入并逐个字符地生成输出。另一种选择是单词级模型，这对于机器翻译而言更为常见。在本文的最后，您将找到一些关于使用嵌入层将模型转换为单词级模型的注释。

#### 总的流程

- 1）将句子转换为3个Numpy数组，encoder_input_data，decoder_input_data，decoder_target_data：
    - encoder_input_data是包含英语句子的one-hot向量的三维数组, 形状为（num_pairs，max_english_sentence_length，num_english_characters）。
    - decoder_input_data是一个形状为（num_pairs，max_chi_sentence_length，num_chi_characters）的3D数组，包含中文句子的one-hot向量。
    - decoder_target_data与decoder_input_data相同，但偏移一个timestep。 decoder_target_data [：，t，：]与decoder_input_data [：，t + 1，：]相同。
    
- 2）训练基本的基于LSTM的Seq2Seq模型以预测给出encoder_input_data和decoder_input_data的decoder_target_data。我们的模型使用"teacher forcing"。

- 3）翻译一些句子以检查模型是否正常工作（将来自encoder_input_data的样本从decoder_target_data转换成相应的样本）。

由于训练过程和推理过程（解码句子）完全不同，我们对两者使用不同的模型，尽管它们都利用相同的内层。

这是我们的训练模型, 它利用了keras的三个关键参数:

- return_state参数，配置RNN层以返回列表，其中第一个是输出，下一个是内部RNN状态。这用于恢复编码器的状态。
- inital_state参数，指定RNN的初始状态。这用于将编码器状态作为初始状态传递给解码器。
- return_sequences参数，配置RNN以返回其完整的输出序列（而不仅仅是最后一个输出，默认行为）。这用于解码器。


```python
from keras.models import Model
from keras.layers import Input, LSTM, Dense

# 定义输入序列
encoder_inputs = Input(shape=(None, num_encoder_tokens))
# 构建LSTM单元
encoder = LSTM(latent_dim, return_state=True)
# 获取输出和状态h和状态c
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
# 我们抛弃 `encoder_outputs` 只保留states.
encoder_states = [state_h, state_c]

# 配置解码器`的初始状态为encoder_states` 
decoder_inputs = Input(shape=(None, num_decoder_tokens))
# 我们让编码器返回全部的output 序列,
# 并且返回内部状态, 在训练阶段我们不使用内部状态信息
# 但是在推断阶段会用到
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs,
                                     initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)

# Define the model that will turn
# `encoder_input_data` & `decoder_input_data` into `decoder_target_data`
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
```

用两行代码来实现训练模型，同时监控20％样本中的loss。


```python
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.2)
```

训练大概一小时以后, 我们可以做推断了。

- 1）对输入句子进行编码并获取初始解码器状态
- 2）以该初始状态和“序列开始”标记作为目标运行解码器的一步。输出将是下一个目标字符。
- 3）附加预测的目标字符并重复。


```python
encoder_model = Model(encoder_inputs, encoder_states)

decoder_state_input_h = Input(shape=(latent_dim,))
decoder_state_input_c = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
decoder_outputs, state_h, state_c = decoder_lstm(
    decoder_inputs, initial_state=decoder_states_inputs)
decoder_states = [state_h, state_c]
decoder_outputs = decoder_dense(decoder_outputs)
decoder_model = Model(
    [decoder_inputs] + decoder_states_inputs,
    [decoder_outputs] + decoder_states)
```

我们用它来实现一个生成句子的循环:


```python
def decode_sequence(input_seq):
    # Encode the input as state vectors.
    states_value = encoder_model.predict(input_seq)

    # Generate empty target sequence of length 1.
    target_seq = np.zeros((1, 1, num_decoder_tokens))
    # Populate the first character of target sequence with the start character.
    target_seq[0, 0, target_token_index['\t']] = 1.

    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict(
            [target_seq] + states_value)

        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = reverse_target_char_index[sampled_token_index]
        decoded_sentence += sampled_char

        # Exit condition: either hit max length
        # or find stop character.
        if (sampled_char == '\n' or
           len(decoded_sentence) > max_decoder_seq_length):
            stop_condition = True

        # Update the target sequence (of length 1).
        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sampled_token_index] = 1.

        # Update states
        states_value = [h, c]

    return decoded_sentence
```

### 结果

我们的结果似乎出奇的好, 但是这并不让我吃惊, 因为我们的测试数据就是训练数据!

```
Input sentence: Be nice.
Decoded sentence: Soyez gentil !
-
Input sentence: Drop it!
Decoded sentence: Laissez tomber !
-
Input sentence: Get out!
Decoded sentence: Sortez !
```

### 彩蛋

#### 如果我想用GRU层而不是LSTM怎么办?

使用GRU更简单, 因为LSTM有两个状态向量, 而GRU只有一个。
下面是修改的代码:

```python
encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder = GRU(latent_dim, return_state=True)
encoder_outputs, state_h = encoder(encoder_inputs)

decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_gru = GRU(latent_dim, return_sequences=True)
decoder_outputs = decoder_gru(decoder_inputs, initial_state=state_h)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')
decoder_outputs = decoder_dense(decoder_outputs)
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
```

#### 如果用词而不是字母作为输入单元, 用数字代表这些词, 该怎么做

如果你的输入时数字序列(用数字代表词)你可以使用keras的Embedding 层, 下面是具体做法:

```python
# Define an input sequence and process it.
encoder_inputs = Input(shape=(None,))
x = Embedding(num_encoder_tokens, latent_dim)(encoder_inputs)
x, state_h, state_c = LSTM(latent_dim,
                           return_state=True)(x)
encoder_states = [state_h, state_c]

# Set up the decoder, using `encoder_states` as initial state.
decoder_inputs = Input(shape=(None,))
x = Embedding(num_decoder_tokens, latent_dim)(decoder_inputs)
x = LSTM(latent_dim, return_sequences=True)(x, initial_state=encoder_states)
decoder_outputs = Dense(num_decoder_tokens, activation='softmax')(x)

# Define the model that will turn
# `encoder_input_data` & `decoder_input_data` into `decoder_target_data`
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# Compile & run training
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
# Note that `decoder_target_data` needs to be one-hot encoded,
# rather than sequences of integers like `decoder_input_data`!
model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.2)
```

#### 如果我不想使用'teacher forcing'来训练

在某些特殊情况下，可能无法使用'teacher forcing'，因为你无法访问完整的目标序列，例如：如果你正在对很长的序列进行在线培训，那么缓冲完整的输入目标对是不可能的。在这种情况下，你可能希望通过将解码器的输出重新注入解码器的输入来进行训练，就像我们在推理阶段做的那样。

你可以通过构建硬编码输出重新注入循环的模型来实现此目的：

```python
from keras.layers import Lambda
from keras import backend as K

# The first part is unchanged
encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder = LSTM(latent_dim, return_state=True)
encoder_outputs, state_h, state_c = encoder(encoder_inputs)
states = [state_h, state_c]

# Set up the decoder, which will only process one timestep at a time.
decoder_inputs = Input(shape=(1, num_decoder_tokens))
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_dense = Dense(num_decoder_tokens, activation='softmax')

all_outputs = []
inputs = decoder_inputs
for _ in range(max_decoder_seq_length):
    # Run the decoder on one timestep
    outputs, state_h, state_c = decoder_lstm(inputs,
                                             initial_state=states)
    outputs = decoder_dense(outputs)
    # Store the current prediction (we will concatenate all predictions later)
    all_outputs.append(outputs)
    # Reinject the outputs as inputs for the next loop iteration
    # as well as update the states
    inputs = outputs
    states = [state_h, state_c]

# Concatenate all predictions
decoder_outputs = Lambda(lambda x: K.concatenate(x, axis=1))(all_outputs)

# Define and compile model as previously
model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')

# Prepare decoder input data that just contains the start character
# Note that we could have made it a constant hard-coded in the model
decoder_input_data = np.zeros((num_samples, 1, num_decoder_tokens))
decoder_input_data[:, 0, target_token_index['\t']] = 1.

# Train model as previously
model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.2)
```

### 本教程的全部代码


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](keras教程-n-10分钟入门LSTM.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
