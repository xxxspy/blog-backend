---
title: Q-learning实现flappyBird永不坠落
date: 2018-03-06 21:02:47
tags: [机器学习, 游戏]
---

这篇文章用于展示我自己学习Q-learning算法的一个成果. 简单来说, 使用机器学习算法Q-learning 来让电脑自己学会玩flappyBird这款游戏. 下面展示的是一个真正的游戏, 你点点击鼠标可以出发小鸟的飞行动作, 不过, 在恰当的时机, 电脑会自己触发动作.

<!--more-->


{% raw %}
<iframe  width="100%" height="650" src="skip_render/game.html"></iframe>
{% endraw %}

本篇文章是我根据视频教程写的, 大部分代码源自该教程: https://www.youtube.com/watch?v=kmLT_HMk9Hw&index=10&list=PLO5e_-yXpYLD31AteKWxbXL1UKVjlZkib