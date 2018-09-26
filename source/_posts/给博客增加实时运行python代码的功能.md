---
title: 给博客增加实时运行python代码的功能
date: 2018-09-14 20:17:55
tags: [python, hexo]
toc: true
xiongzhang: true

---

DataCamp Light 是DataCamp公司提供的网页代码高亮和运行的前端插件, 目前只支持R和python, 下面我们用示例来说明如何把博客改造成可以实时运行代码的REPL。

> 注意: 我近日发现DataCamp被-墙， 所以你们可能看不到代码编辑器和结果输出， 我在学校是可以看到的， 不明白好东西为什么总是被-墙。

<!-- more -->

### DataCamp Light特点

- 将任何网站或博客转换为互动学习平台。
- 适用于R和Python。会话在DataCamp的服务器上维护。
- 使用教程包将现有的文档转换为交互式课程。
- 查看演示R和Python示例。
- 利用Submission Correctness Tests检查代码运行的正确性

### 怎样安装

在你的网页中添加脚本就可以了:

```js
<script type="text/javascript" src="//cdn.datacamp.com/dcl-react.js.gz"></script>
```

页面在加载完毕后, 上面的js模块会检查页面上的特定区域, 决定是否转换为可运行的代码编辑器。


### 页面配置

引用上面的JavaScript库后，您可以开始以下面的格式编写HTML块。这些将动态转换为可运行的代码编辑器。

```html
<div data-datacamp-exercise data-lang="r">
	<code data-type="pre-exercise-code">
		# 这部分代码是在初始化的时候自动运行的
		b = 6
	</code>
	<code data-type="sample-code">
		# 这里是示例代码


		# Print out a


	</code>
	<code data-type="solution">
		# 这里是答案
		a <- 5

		# Print out a
		print(a)
	</code>
	<code data-type="sct">
		test_object("a")
		test_function("print")
		success_msg("Great job!")
	</code>
	<div data-type="hint">Use the assignment operator (code<-</code>) to create the variable codea</code>.</div>
</div>
```

正如我们在示例中所看到的，代码包含在一个div标签中, 带有两个数据属性data-datacamp-exercise和data-lang。第一个属性data-datacamp-exercise表示<div>应该被视为DataCamp Light的代码块，而另一个属性data-lang指定应该使用哪种编程语言, 目前只支持R和python。还有一个可选的属性data-height，它可以设置div的px高度（最小高度为300px），或者根据示例代码行的数量设置大小：data-height =“auto”。


下面我们展示一下真正的效果:

{% raw %}
<div data-datacamp-exercise data-lang="python">
	<code data-type="pre-exercise-code">
		# 这部分代码是在初始化的时候自动运行的
		b = 6
	</code>
	<code data-type="sample-code">
		# 这里是示例代码


		# Print out a


	</code>
	<code data-type="solution">
		# 这里是答案
		a=5

		# Print out a
		print(a)
	</code>
	<code data-type="sct">
		test_object("a")
		test_function("print")
		success_msg("Great job!")
	</code>
	<div data-type="hint">Use the assignment operator (code<-</code>) to create the variable codea</code>.</div>
</div>
<script type="text/javascript" src="//cdn.datacamp.com/dcl-react.js.gz"></script>

{% endraw %}


### 默认运行

初始化R / Python会话时执行的代码。您可以使用它为学生预加载数据集，包等。指定此方法的方法是定义一个包含初始化代码的code标记，并将data-type属性设置为pre-exercise-code，如下所示：

```html
<code data-type="pre-exercise-code">
	# This will get executed each time the exercise gets initialized
	b = 6
</code>
```

### 示例代码

要设置最初将出现在代码编辑器中的示例代码，应定义包含示例代码的code标记，并将data-type属性设置为示例代码，如下所示：

```html
<code data-type="sample-code">
	# Create a variable a, equal to 5


	# Print out a


</code>

```

### 答案

要设置解决方案代码，应定义包含解决方案代码的code标记，并将data-type属性设置为如下解决方案：

```html
<code data-type="solution">
	# Create a variable a, equal to 5
	a <- 5

	# Print out a
	print(a)
</code>
```

### 正确答案检查器

正确性测试用于检查用户提交的代码是否正确解决了问题。有关这方面的详细信息，您可以查看R的文档和Python的文档。指定SCT的方法是定义包含SCT代码的code标记，并将data-type属性设置为sct，如下所示：

```html
<code data-type="sct">
	test_object("a")
	test_function("print")
	success_msg("Great job!")
</code>
```

### 提示信息

要指定提示，应定义包含提示的标记，并且应将data-type属性设置为提示，如下所示：

```html
<div data-type="hint">
    Use the assignment operator (<code><-</code>) to create the variable <code>a</code>.
</div>
```

### 高级功能展示

你可以看到, 我们不仅仅可以运行python内置模块, 还有一些第三方模块, 而且支持matplotlib绘图。


{% raw %}

<div data-datacamp-exercise data-lang="python">

	<code data-type="sample-code">
        import numpy as np
        import matplotlib.pyplot as plt

        x = np.arange(0, 5, 0.1);
        y = np.sin(x)
        plt.plot(x, y)
        plt.show()
	</code>
</div>
{% endraw %}
