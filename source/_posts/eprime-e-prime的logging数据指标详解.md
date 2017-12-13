---
title: eprime/e-prime的logging数据指标详解
date: 2017-11-19 09:46:15
tags: [e-prime, eprime]
---

eprime有几十个数据指标, 但是 很多新手不清楚里面的指标是什么意思, 这里特别总结到一起, 可能不太全, 会逐步补充到里面. 如果里面有什么错误, 或者有需要补充的内容, 请在下面留言.

### 几个概念:

- 时间戳: 从实验开始到某个时间点之间的毫秒数.

<!--more-->

### 常见指标

- RESP: 被试的反应, 可以是鼠标也可以是键盘按键.
- CRESP: 主试设置的正确反应. 如果你在程序中没有设置正确反应, 这个值是没有的.
- ACC: 代表被试反应的准确性, 反应正确数值为1, 反应错误数值为0. 
- RT: 反应时, 这是我们常用的指标, 就是刺激出现到被试按键的反应时间.
- RTTime: 反应时间戳, 代表从实验开始到被试按键这个时间长度, 单位是毫秒.
- StartTime: 开始时间戳, 代表刺激开始的时间点到实验开始的时间点之间的时间长度.
- FinishTime: 和StartTime类似, 参考上面.
- TargetOnsetTime: 刺激开始执行动作的理论时间戳, 是通过计算得到的, 代表着你想让刺激绘制的时间.
- OnsetTime: 刺激实际开始执行动作的时间戳, 代表刺激实际开始绘制到屏幕的开始时间点.
- OnsetDelay: 代表着TargetOnsetTime和OnsetTime的时间差, 因为你的理论时间往往不能精确执行, 计算机执行下来会有一个时间延迟. 
- ActionTime: 刺激完成动作的时间戳, 其实就是绘制到屏幕上的时间, 但是不代表被试看到刺激的时间, 因为程序完成绘制到刺激完整出现中间是有一定时间差的, 虽然很小.
- ActionDelay: ActionTime和OnsetTime的差值. 动作开始执行到动作执行完毕之间有一个略微的差异.
- Duration: 刺激的持续时间, 单位是毫秒.
- OffsetTime: 结束动作开始的时间点, 不懂计算机语言的人可能疑惑为什么结束还需要时间. 因为程序创建了很多变量/对象需要清理, 这些动作也是需要时间的.
- TargetOffsetTime: 理论的结束动作开始时间. 这个时间通常是根据你设置的刺激持续时间(Duration)计算得到的.
- OffsetDelay: 结束的延迟时间, 也就是TargetOffsetTime和OffsetTime之间的差异.
- CustomOnsetTime: 自定义Onset时间, 如果你设置了CustomOnsetTime, 程序会等到这个时间点才执行Onset动作.
- CustomOffsetTime: 参考CustomOnsetTime, 程序等待到这个时间点才执行Offset动作.
- DurationError: 持续时间误差, 这个时间指的是实际的持续时间(OffsetTime-OnsetTime)和你设置的持续时间之间的误差.

> Erime这个软件已经很老了, 因为各种遗留原因, 有些人还是选择用Eprime, 但是我个人是更喜欢Psychopy, 用起来更简单, 大家可以试一试.