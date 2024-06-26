
---

title: jamovi模块开发教程
date: 2021-08-19 12:44:03
tags: [jamovi]

---

本篇文章主要介绍如何为jamovi开发统计模块。jamovi统计分析咨询请加qq: 2726725926

<!--more-->
<!-- toc -->

## 起飞

在开始之前，jamovi 中的分析模块是用R 编程语言编写的。本教程假设您有一些 R 知识，最好有一些编写 R 包的经验。

为jamovi 开发模块需要这个jmvtools包。在本教程中，我们将：

- 安装 jmvtools
- 确保jmvtools可以找到jamovi
- 从 GitHub 构建和安装 jamovi 模块

### 安装 jmvtools

jmvtools 可以从 jamovi 仓库获得，并且可以通过以下方式安装在 R 中：

```r

install.packages('jmvtools', repos=c('https://repo.jamovi.org', 'https://cran.r-project.org'))
```

### 检查jmvtools可以找到jamovi

现在你已经jmvtools安装好了，我们可以检查它是否可以找到你的jamovi安装：

```r
jmvtools::check()
```

jmvtools 在可能被视为“常见地点”的地方搜索 jamovi，例如：

- /Applications
- /usr/lib/jamovi
- C:\Program Files

如果jmvtools找不到，您可以在调用中指定路径check()：

```r
jmvtools::check(home='C:\\Users\\jonathon\\Documents\\jamovi')
```

注意代码中的路径需要根据你自己的电脑来设置

当然, 如果你想自己手动设置jamovi的路径, 也是可以的, 只需要执行下面的命令:

```r
options(jamovi_home='jamovi的安装路径')
```

### 安装模块

现在我们已经安装好了jmvtools，我们可以用它来构建和安装一个jamovi模块。接下来，我们将从 GitHub 下载一个模块，构建并安装它。我们将使用Base R模块 - 您可以使用此处的直接链接下载它:https://github.com/jamovi/jmvbaseR/archive/master.zip  , 这是一个实验性的模块。

 下载到的文件是一个压缩包, 先解压到文件夹, RStudio 中打开该文件夹（或将您的工作目录设置为该目录）。现在我们可以调用install()函数：
 
 ```r
jmvtools::install()   # not to be mistaken for devtools::install()
```

这将构建模块，并将其安装到 jamovi 中。

如果您现在转到打开的 jamovi 窗口，您会看到功能区上出现了一个新的“Base R”菜单，其中包含一组新的分析。从 R 安装和更新 jamovi 分析的能力非常棒，因为我们将在下一节中看到，我们可以对分析进行更改，jmvtools::install()再次运行，并立即看到这些更改反映在 jamovi 中。这使得开发和测试 jamovi 模块变得轻而易举！

## 创建模块

在本节中，我们将从头开始创建一个 jamovi 模块，并将其安装到 jamovi 中。

为 jamovi 创建模块的最简单方法是使用包中的create()函数jmvtools：

```r
jmvtools::create('SuperAwesome')
```

这将创建一个SuperAwesome目录。如果我们现在查看刚出炉的 SuperAwesome 的内容，我们会发现：

```
SuperAwesome/
├── DESCRIPTION
├── NAMESPACE
├── jamovi/
|   └── 0000.yaml
└── R/
```

对于以前从事过 R 包开发工作的人来说，这应该看起来很熟悉。那是因为 jamovi 模块是R 包，但带有附加`jamovi/0000.yaml`文件。有了这个文件，
这个包就变成了双重公民：它可以构建到 R 包中，也可以构建到 jamovi 模块中。

如果您查看该`0000.yaml`文件，您会注意到它包含的内容与`DESCRIPTION`文件非常相似。但是，当我们向模块添加分析时，
它们也会列在此文件中。在开发的早期阶段，这个文件先不管他，我们稍后会回到它。

## 创建分析

一个独立样本t检验通常用于确定两个分组是否在一些变量均值上有显著差异。例如，您可能对一个街区的儿童与另一街区的儿童的身高是否不同感兴趣。在这种情况下，数据集将为每个孩子分配一行, 总共有两列数据, 一列代表身高, 一列代表街区。

对于那些熟悉t.testR 内置函数的人，如果两个变量分别是height和neighbourhood，则可以运行t检验：

```
t.test(height ~ neighbourhood, data=data)
```

在下一节中，我们将创建一个使用此函数的 t 检验 jamovi 分析。

jamovi 模块的最简单方法是使用jmvtools的函数`addAnalysis()`。首先我们将工作目录设置为SuperAwesome目录，然后调用addAnalysis()

```R
setwd('SuperAwesome') # 设置工作目录
jmvtools::addAnalysis(name='ttest', title='Independent Samples T-Test')
```

然后如果我们现在查看SuperAwesome模块的目录树，我们有：

```
SuperAwesome/
├── DESCRIPTION
├── NAMESPACE
├── jamovi/
|   ├── ttest.a.yaml
|   ├── ttest.r.yaml
|   ├── ttest.u.yaml
|   └── 0000.yaml
└── R/
    ├── ttest.h.R
    └── ttest.b.R
```

说到这里我有点不好意思说, 每次分析有5个文件。这种结构确实使事情更易于管理，因此尽管乍一看似乎有些过分，但背后有很好的理由。请耐心等待，它并不像看起来那么复杂。

<img src="imgs/file-list.png">

yaml 是一种用于结构化数据的简单易读的文本格式。如果您不熟悉 yaml，可以在[此处](http://yaml.org/spec/1.2/spec.html)阅读有关格式的更多信息，但这可能不是必需的。它直观且易读，您可能会毫不费力地拿起它。

- ttest.a.yaml: 该文件包含了所有分析的元信息，说明它接收到的参数和用户界面选项等。我们将在接下来的教程涵盖这一点。
- ttest.r.yaml: 该文件包含有关分析结果的显示方式。
- ttest.u.yaml: 根据`ttest.a.yaml`的内容自动生成的。对于许多分析，这将产生良好的结果，并且不需要进一步编辑。
- ttest.h.R: 这是一个头文件, 也是从`ttest.a.yaml`和`ttest.r.yaml`自动生成的, 你不需要看这个文件, 也不需要修改它
- ttest.b.R: 实现分析的代码文件, 也是你花费最多时间的文件, 决定了你的分析是如何进行的



### `ttest.a.yaml`的定义

jmvtools::addAnalysis()创建一个.a.yaml带有一些基本选项的默认文件。令人高兴的是，对于本教程，这些恰好对应于 t 检验所需的选项。我们生成的ttest.a.yaml文件如下：

```yaml
---
name:  ttest
title: Independent Samples T-Test
jas:     "1.1"
version: "1.0.0"

options:
    - name: data
      type: Data

    - name: dep
      title: Dependent Variable
      type: Variable

    - name: group
      title: Grouping Variable
      type: Variable

    - name: alt
      title: Alternative hypothesis
      type: List
      options:
        - name: notEqual
          title: Not equal
        - name: oneGreater
          title: One greater
        - name: twoGreater
          title: Two greater
      default: notEqual

    - name: varEq
      title: Assume equal variances
      type: Bool
      default: true
```

文件顶部是有关分析的信息：

```yaml
---
name:  ttest # 用到的函数名称, 它必须以字母开头，并且只能由字母和数字组成
title: Independent Samples T-Test  # 分析的标题是分析在菜单、帮助文本和结果中的显示方式
jas:     "1.1"  # jamovi analysis spec
version: "1.0.0" # 你开发的模块的版本号
...
```

接下来是选项: data，dep，group，alt和varEq。 当用作 R 包时，这些选项对应于传递给R 函数的参数。在这种情况下，也就是:

```r
ttestIS(data, dep, group, alt='not equal', varEq=FALSE)
```

（如果你往里面看ttest.h.R，你会发现这个确切的函数已经生成了。）

在jamovi 中使用时，这些选项对应于分析的UI 选项。现在让我们来看看。安装我们刚刚创建的模块并打开jamovi（或者先打开jamovi，然后安装模块——顺序无关紧要）：

```
jmvtools::install()
```

（请注意，如果您的模块有其他依赖项，这些也将在此阶段安装。您可以在本教程末尾的附加说明中阅读有关附加依赖项的更多信息。）

该SuperAwesome菜单现在可以使用了，并且包含Independent Samples T-Test。

<img src='imgs/01.png'>

打开这个分析的界面, 就会看到它的配置选项:

<img src="imgs/02.png">

从`ttestis.a.yaml`文件中就可以找到这些配置选项的信息:

```yaml
    - name: dep
      title: Dependent Variable
      type: Variable

    - name: group
      title: Grouping Variable
      type: Variable
```

我们可以看出来, dep和group的类型都是Variable, 意味着他们指的是数据集中的一列变量。

接下来看`alt`选项, 它是指的是一些额外假设, `options`中列出了所有可选项:

```
    - name: alt
      title: Alternative hypothesis
      type: List
      options:
        - name: notEqual
          title: Not equal
        - name: oneGreater
          title: One greater
        - name: twoGreater
          title: Two greater
      default: notEqual
```

最后来看`varEq`: 它是一个布尔值, 只有"true"和"false"两个值, 它在界面上就是一个可选框:

```yaml
...
    - name: varEq
      title: Assume equal variances
      type: Bool
      default: true
```

还有许多不同的选项类型。API 中提供了对它们中的每一个的更全面的描述，以及它们的属性: https://dev.jamovi.org/api_analysis-definition.html

当然，我们的分析实际上还没有做任何事情——我们还没有编写任何 R 代码。

## 实现分析(R代码)

在本节中，我们将添加实现，即 R 代码，以执行我们的 t 检验分析。

在jamovi 分析中，这些R代码的实现存在于`.b.R`文件中，所以如果我们查看我们的ttest.b.R文件，我们会看到：

```R
# This file is a generated template, your changes will not be overwritten

#' @rdname jamovi
#' @export
ttestClass <- R6::R6Class(
    "ttestClass",
    inherit = ttestBase,
    private = list(
        .run = function() {

            # `self`$data` contains the data
            # `self$`

您还会注意到该.run()函数不接收任何参数。用户指定的参数实际上都编程了self的属性。同样，这可能看起来有点陌生，但它非常简单。

例如我们的四个参数可以通过这种方式获得:

```
- self`$options$`dep
- self`$options$`group
- self`$options$`alt
- self`$options$`

你看到的``$`负号实际上就是一个属性获取负号, `self$`options`$dep`翻译过来就是self的options中的dep, 分析用到的数据保存在`self$`data`中, 这样我们就可以编写我们的t检验了:

```
ttestClass <- R6::R6Class("ttestClass",
    inherit=ttestBase,
    private=list(
        .run=function() {

            formula <- paste(self`$options$`dep, '~', self`$options$`group)
            formula <- as.formula(formula)
        
            results <- t.test(formula, self`$data)
        
            print(results)
        })
)
```

这段代码做的事情很简单, self$`options`$dep和self$`options`$group这两者都是字符串并且它们组装成一个公式。然后我们可以调用t.test()传入这个公式的函数，以及self$`data数据框。最后，我们打印结果。
                              
在jamovi 中运行时，打印语句(print)的结果将出现在终端，而不是应用程序的结果区域（用户希望的地方）。为了解决这个问题，我们不是简单地打印结果，而是将结果分配给分析的结果对象。在 R 会话中运行时，仍会打印结果，但在 jamovi 中运行时，结果将显示在结果面板中。我们使用self`$results来保存结果。我们的新函数现在将变为：

```
ttestClass <- R6::R6Class("ttestClass",
    inherit=ttestBase,
    private=list(
        .run=function() {

            formula <- paste(self$`options`$dep, '~', self$`options`$group)
            formula <- as.formula(formula)
        
            results <- t.test(formula, self$`data, var.equal=self`$options$`varEq)
        
            self`$results$`

result的text属性可以存放我们的字符串, 并且使用setContent来写入结果:

所以现在我们的分析已经实现了，是时候安装并试用它了。使用通常的方式安装模块：

```
jmvtools::install()

```

下面再做一个分析就可以看到类似结果:

<img src="imgs/03.png">

同样，我们可以使用devtools包（不要与 混淆jmvtools）将此模块安装为 R 包，并在交互式 R 会话中运行相同的分析：

```
devtools::install()
library(SuperAwesome)
data(ToothGrowth)
ttest(data=ToothGrowth, dep='len', group='supp')
```

输出结果:

```
Independent Samples T-Test

    Two Sample t-test

data:  len by supp
t = 1.9153, df = 58, p-value = 0.06039
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -0.1670064  7.5670064
sample estimates:
mean in group OJ mean in group VC 
        20.66333         16.96333 
```

在我们继续之前，精明的读者会意识到组装我们的公式paste是有问题的。如果任一列名称有空格或特殊字符，粘贴将产生错误的公式。例如，如果用户指定了一个被称为的因变量the fish——结果公式将为the fish~group，而对 的调用as.formula()将失败：

```as.formula('the fish~group')```

```
## Error in parse(text = x, keep.source = FALSE) : 
##   <text>:1:5: unexpected symbol
## 1: the fish
##         ^
```

jmvcore提供了函数constructFormula()，它可以组合简单的公式来适当地转义列名：

```
constructFormula('the fish', c('group'))```


我们的代码做出相应的改变:

```
ttestISClass <- R6Class("ttestISClass",
    inherit=ttestISBase,
    private=list(
        .run=function() {

            formula <- constructFormula(self`$options$`dep, self`$options$`group)
            formula <- as.formula(formula)
        
            results <- t.test(formula, self`$data)
        
            self$`results`$text$`

该jmvcore软件包包含许多此类有用的功能。值得一试。

## 代码调试

做开发的免不了有bug, 所以jamovi提供了很好的调试工具。

我们特地把之前的代码改成错误的:

```
ttestISClass <- R6Class("ttestISClass",
    inherit=ttestISBase,
    private=list(
        .run=function() {

            t.test(c(Inf, 3))  # <-- produces an error!
        })
)
```

会看到这样的错误提示:

<img src="imgs/04.png">

在这个例子中，我们的代码只有一行代码，所以我们可以合理地确定问题出在哪里。然而，实际上软件可以是两行或三行甚至更多行代码。在更复杂的情况下，有一个“堆栈跟踪”会很方便，它告诉我们问题发生在哪里。jamovi 可以置于“开发模式”，它会在发生错误时显示堆栈跟踪。开发模式可以从应用程序菜单切换到 jamovi 窗口的右上角：

<img src="imgs/05.png">

然后错误信息就会更详细:

<img src="imgs/06.png">

## 创建丰富结果

在本节中，我们将为我们的分析添加丰富的结果；一个不错的 APA 格式表，如下所示：

<img src="imgs/07.png">

### 结果的定义

为了提供丰富的结果，我们需要在结果定义中添加一些条目。这是`ttest.r.yaml`文件的目的：

```yaml
---
name:  ttest
title: Independent Samples T-Test
jrs:   '1.1'

items:
    - name:  text
      title: Independent Samples T-Test
      type:  Preformatted
```


这与ttest.a.yaml文件非常相似；有一个名称、一个标题和一个 jamovi 结果规范 ( jrs) （注意，这jas与.a.yaml文件中的不同）。items描述了构成结果的所有项目。例如，结果可以由两个表和一个图组成。结果中的每一项都列在此处。

目前，结果包含一个Preformatted的文本名为"Independent Samples T-Test"。如果你回想上一节，我们访问了一个结果对象，如下所示：

```self`$results$`

### 添加表格

让我们为 t 检验结果添加一个表格。目前，我们将保留现有的“预格式化”结果项并在下方添加表格。这将让我们检查我们填充表格的结果是否正确。

修改ttest.r.yaml为：

```
---
name:  ttest
title: Independent Samples T-Test
jrs:   '1.1'

items:
    - name:  text
      title: Independent Samples T-Test
      type:  Preformatted

    - name:  ttest
      title: Independent Samples T-Test
      type: Table
      rows:  1
      columns:
        - name: var
          title: ''
          type: text
        - name: t
          type: number
        - name: df
          type: integer
        - name: p
          type: number
          format: zto,pvalue

```

通过这些修改，我们添加了一个名为ttest的新表, 名为`Independent Samples T-Test`。我们还指定它有 1 行，有 4 列；列名是var、t、df和p。请注意，我们为 var 的标题(title)指定了一个空字符串。如果未指定标题，则使用列名(name)。

你可以为每列的数据类型指定为text，number或integer。类型会影响列的格式化方式。text列是左对齐的，number和integer列右对齐。integer列被格式化为整数（没有小数位）。

该format字段是一串逗号分隔值。它提供了有关如何格式化列的附加信息。例如p列，它应用了两种格式，zto和pvalue. zto表示一个值在 0 和 1 之间；这会导致它被渲染到固定的小数位。相反，没有这种格式的值被格式化为固定数量的有效数字。没有zto值 0.006 将被呈现0.00600（3 个有效数字），而与zto它一样将被呈现0.006（3 个小数位）。对于诸如相关系数之类的值和范围在 0 和 1 之间的其他值，通常首选后者。

另一种格式是pvalue，表示该列中的值为 p-values。如果这些值中的任何一个低于阈值（默认为 .001），它们将被替换为< .001.

现在我们已经设置了我们的表，我们可以通过重新安装模块来查看它的样子：

```jmvtools::install()```

如果您现在返回到 jamovi，您会看到已安装的模块已更新，并且我们之前的分析已重新运行。我们添加的表现在在结果中可见。这非常方便：每当您重新安装模块时，它都会立即更新。您的结果现在应如下所示：

<img src="imgs/08.png">

### 填充表

现在我们已经创建了一个表，让我们用 t 检验中的值填充它。为此，我们需要从 Rt.test函数返回的 t-test 对象中提取实际值。相当尴尬的是，R 中的分析不会返回一致的结果对象；通常没有可预测的方式来了解如何访问基础值。有些 R 函数返回列表，有些返回 S3 对象，有些返回 S4。有些需要使用索引 读取值，有些需要使用插槽 (@)。通常需要一些反复试验才能弄清楚如何访问结果对象的基础值。一个有用的函数是mode()函数。例如，我们可以像这样对结果对象调用 mode ：

```
results <- t.test(1:5)
mode(results)
```


输出:`## [1] "list"`

这告诉我们 t.test 函数的结果对象是一个列表（尽管有些难懂）。然后我们可以使用我们通常在列表上使用的函数，例如：

```
results <- t.test(1:5)
names(results)
```

输出:
```
## [1] "statistic"   "parameter"   "p.value"     "conf.int"    "estimate"   
## [6] "null.value"  "alternative" "method"      "data.name"
```

稍加修改，我们可以找出results`$statistic包含t统计量、results$`parameter自由度和results`$p.valuep 值的值（最后一个可能不需要那么多修改）。

我们可以使用以下setRow()函数将这些值中的每一个分配给表中的行：

```
table <- self$`results`$ttest
table$`setRow(rowNo=1, values=list(
    var=self`$options$`dep,
    t=results`$statistic,
    df=results$`

删除文本结果:

```
ttestISClass <- R6Class("ttestISClass",
    inherit=ttestISBase,
    private=list(
        .run=function() {

            formula <- constructFormula(self`$options$`dep, self`$options$`group)
            formula <- as.formula(formula)
        
            results <- t.test(formula, self`$data)
        
            table <- self$`results`$ttest
            
            table$`setRow(rowNo=1, values=list(
                var=self`$options$`dep,
                t=results`$statistic,
                df=results$`

我们也来看看在 R 会话中运行这个分析。我们可以使用以下命令将软件包安装到 R 中：

`devtools::install()  # note here we're using devtools, not jmvtools`

并使用以下命令运行分析：

```
library(SuperAwesome)
data("ToothGrowth")
ttest(ToothGrowth, dep='len', group='supp')
```
输出:

```
 Independent Samples T-Test

 Independent Samples T-Test     
 ────────────────────────────── 
          t       df    p       
 ────────────────────────────── 
   len    1.92    55    0.061   
 ────────────────────────────── 
 ```
 
 可以看出，在 R 中也生成了一个格式良好的表。一切都保持不变，精确到小数位数。通过这种方式，jamovi 可以使 R 包——即使你不打算发布为 jamovi 模块——更有吸引力、更容易阅读、也更一致。

## 添加图

在本节中，我们将为我们在本系列中开发的 t 检验分析添加一个图。绘图是出现在结果中的另一项，因此我们将在ttest.r.yaml文件中添加另一个条目：

```yaml
---
name:  ttest
title: Independent Samples T-Test
jrs:   '1.1'

items:
    - name:  ttest
      title: Independent Samples T-Test
      type: Table
      rows:  1
      columns:
        - name: var
          title: ''
          type: text
        - name: t
          type: number
        - name: df
          type: integer
        - name: p
          type: number
          format: zto,pvalue
    
    - name: plot
      title: Descriptives Plot
      type: Image
      width:  400
      height: 300
      renderFun: .plot
```

和以前一样，我们定义了一个项目有name，title和type; 在这种情况下，
类型是Image. 此外，我们定义renderFun了负责渲染图像的函数的名称。
无论我们指定什么渲染函数，我们都必须将其作为私有成员函数添加到ttestClassin:

```
#' @export
ttestClass <- R6::R6Class(
    "ttestClass",
    inherit = ttestBase,
    private = list(
        .run = function() {
            formula <- paste(self`$options$`dep, '~', self`$options$`group)
            formula <- as.formula(formula)
            
            results <- t.test(formula, self`$data)
            
            table <- self$`results`$ttest
            table$`setRow(rowNo=1, values=list(
                var=self`$options$`dep,
                t=results`$statistic,
                df=results$`

我们将ggplot2用于绘图，因此请确保您已安装它。要在这个包/模块中使用 ggplot2，我们需要在描述和命名空间文件中添加一些条目。我们将 ggplot2 添加到说明文件(DESCRIPTION)中的导入行，因此它显示为：

```
Imports: jmvcore, R6, ggplot2
```
然后在代码中使用ggplots2需要引入:

```import(ggplot2)```

这些都是基本的R语言特性。



### 代码实现

在jamovi 模块中，绘图分两个阶段进行；首先准备绘图的数据，然后渲染绘图。
这两个阶段意味着如果图像被调整大小，或者用户请求不同的文件格式，只需要再次进行渲染——数据准备只需要发生一次。

对于 t 检验，我们将绘制每个组的平均值和标准误。在 中ggplot2，我们需要将这些“绘图点”组合成一个数据框，我们将按如下方式进行：

```
    means  <- aggregate(formula, self`$data, mean)[,2]
    ses    <- aggregate(formula, self$`data, function(x) sd(x)/sqrt(length(x)))[,2]
    sel    <- means - ses  # standard error lower bound
    seu    <- means + ses  # standard error upper bound
    levels <- base::levels(self`$data[[self$`

输出:

```
##   level     mean      sel      seu
## 1    OJ 20.66333 19.45733 21.86934
## 2    VC 16.96333 15.45417 18.47250
```

我们使用setState()函数给图像设置数据:

```
    image <- self`$results$`plot
    image`$setState(plotData)
```

接下来，我们将绘图代码添加到.plot()我们创建的函数中：

```
#' @export
ttestClass <- R6::R6Class(
    "ttestClass",
    inherit = ttestBase,
    private = list(
        .run = function() {
            formula <- paste(self$`options`$dep, '~', self$`options`$group)
            formula <- as.formula(formula)
            
            results <- t.test(formula, self$`data)
            
            table <- self`$results$`ttest
            table`$setRow(rowNo=1, values=list(
                var=self$`options`$dep,
                t=results$`statistic,
                df=results`$parameter,
                p=results$`p.value
            ))
            
            means  <- aggregate(formula, self`$data, mean)[,2]
            ses    <- aggregate(formula, self$`data, function(x) sd(x)/sqrt(length(x)))[,2]
            sel    <- means - ses  # standard error lower bound
            seu    <- means + ses  # standard error upper bound
            levels <- base::levels(self`$data[[self$`options`$group]])
            plotData <- data.frame(level=levels, mean=means, sel=sel, seu=seu)
            
            image <- self$`results`$plot
            image$`setState(plotData)
        },
        
        .plot=function(image, ...) {
            plotData <- image`$state
            plot <- ggplot(plotData, aes(x=level, y=mean)) +
                geom_errorbar(aes(ymin=sel, ymax=seu, width=.1)) +
                geom_point(aes(x=level, y=mean)) +
                labs(title=self$`

## 发布模块

调用以在当前工作目录中jmvtools::install()生成具有扩展名的文件.jmo。这个文件是你的模块，可以分发给其他人，以“加载”。这是在测试期间分发模块的好方法，您可能希望将其发送给少数人。人们可以从 jamovi 商店（可从 jamovi 右上角的菜单访问）内加载模块。

一旦您对您的模块准备好进行更广泛的分发感到满意，我们鼓励您将其提交到 jamovi 商店。这使得任何使用 jamovi 的人都可以浏览和发现您的模块。

如果您有想要提交给 jamovi 商店的模块，请与我们联系：contact@jamovi.org

## 补充

### 依赖关系

jmvtools::install()还会下载您的所有软件包依赖项（在DESCRIPTION文件中列出），并将它们捆绑到您的模块中。这确保了模块拥有它需要的一切，并且模块将始终使用可预测的依赖版本。这会导致更大的模块文件大小，但可以说是考虑到磁盘空间的便宜，为可重复性付出的代价很小。

### 命名空间

我们建议您尽量减少NAMESPACE文件中的导入语句。这些可能会导致加载包时出现大量延迟，因为无论是否需要，都会加载文件中列出的所有包。

相反，访问具有完整命名空间的函数，即：

```
stats::t.test(...)
```

使用这种方法，依赖项仅在需要时加载。这会缩短启动时间（用户选择您的分析之一与结果首次出现之间的延迟），并且可以显着减少您的模块使用的 RAM 量。

## 动态表

这是我们之前设置的结果:

```yaml
...
    - name:  ttest
      title: Independent Samples T-Test
      type: Table
      rows:  1
      columns:
        - name: var
          title: ''
          type: text
        - name: t
          type: number
        - name: df
          type: integer
        - name: p
          type: number
          format: zto,pvalue
```

结果包含一个名为ttest“独立样本 T 检验”的表格，有 4 列和 1 行。

然而，实际上，表中的行数通常不是固定的。它们可能会根据用户选择的选项或分析本身的结果而有所不同。在本教程中，我们将专注于前者。

在之前的教程系列中，我们创建了 t 检验分析。它允许用户指定单个因变量和单个分组变量。但是，我们可以通过允许人们指定多个因变量来使这种分析更加方便。例如，数据集可能包含“性别”、“身高”和“体重”列。通过允许多个因变量，用户可以指定“身高”和“体重”作为因变量，并指定“性别”作为分组变量。然后我们的分析可以执行多个 t 检验（每个因变量一个）。结果分析可能如下所示：

<img src="imgs/12.png">

我们需要做的第一件事就是改变因变量的.a.yaml文件，从Variable到Variables。

```
---
name:  ttest
title: Independent Samples T-Test
menuGroup: SuperAwesome
version: '1.0.0'
jas: '1.1'

options:
    - name: data
      type: Data

    - name: deps                  # <-- let's add an s
      title: Dependent Variables  # <-- and another s
      type: Variables             # <-- Variables with an s!
      
...
```

注意当前 jmvtools 中存在一个错误，其中 UI 未适当更新。在这种情况下，jmvtools应该更新 .u.yaml 文件以接受多个变量，但这不会发生。可以手动更新 .u.yaml 文件，但通常最简单的方法是简单地删除 .u.yaml 文件，然后让 jmvtools 从头开始创建一个。这是将在未来几周内解决的问题。

请注意，您必须关闭 jamovi，然后重新启动它才能查看分析 UI 的更改。

由于我们更改了dep变量的名称和类型，我们的 t 检验将不再起作用。目前应该注释掉或删除.run()t检验分析函数的内容，否则会产生一些错误。我们将在本教程的稍后部分返回。

执行这些修改后，您的 t-test UI 应如下所示：

<img src="imgs/13.png">


我们需要修改`.y.raml`, rows是需要更改的值, 现在表格不是1行了, 但是具体是几行完全取决于用户设置的因变量(deps)数量:

```yaml
...
- name:  ttest
      title: Independent Samples T-Test
      type: Table
      rows: 1
...
```

我们就直接更改为:

```yaml
...
- name:  ttest
      title: Independent Samples T-Test
      type: Table
      rows: (deps)
...
```

以这种方式绑定时，表中的行数始终与用户指定的变量数相匹配。让我们重新安装我们的模块，看看它的实际效果：

<img src="imgs/14.png">

可以看出，我们的表相应地增长和缩小。但我们可以做得更好。
第一列应该包含变量名，虽然我们可以使用 Table 的setRow()函数添加它，但有更好的方法来做到这一点。
我们可以使用content这个选项:

```yaml
items:
    - name:  ttest
      title: Independent Samples T-Test
      type:  Table
      rows:  (deps)
      columns:
        - name: var
          title: ''
          type: text
          content: (`$key)  # <- here!
```
你会发现`($`key)`这个特殊的字段, 它实际上是每一行的key, 这个key需要你在代码中设置, 所以你看到下面的R代码的时候才知道是什么

现在就是在`b.R`文件中设置我们的表格, 我们在调用`setRow`的时候, 使用了rowKey这个参数, 这样我们的表格每一行都有个key。

```
    .run=function() {
    
        table <- self`$results$`ttest
    
        for (dep in self`$options$`deps) {
    
            formula <- jmvcore::constructFormula(dep, self`$options$`group)
            formula <- as.formula(formula)
        
            results <- t.test(formula, self`$data)
        
            table$`setRow(rowKey=dep, values=list(  # set by rowKey!
                t=results`$statistic,
                df=results$`

## 数据处理

到目前为止，在这些教程中，我们还没有真正检查self`$data数据框实际包含的内容。
它包含来自电子表格视图中显示的数据集的数据，但这些值如何映射到 R 类型系统有点微妙。

在jamovi 中有四种变量类型：

- Nominal Text 名义文本
- Nominal 名义
- Ordinal 序数
- Continuous 连续

Nominal Text变量只有“文本”值，因此将self$`data作为因子出现在数据框中。Continuous变量只有数字值，所以在self`$data数据框中，它们是数字类型。但是，变量Nominal和Ordinal变量类型有点棘手。这些可以同时具有数字和文本值。

（注意jamovi 目前不支持将文本值（标签）分配给 Nominal 和 Ordinal 变量。这将在未来添加。）

此外，在某些情况下，您希望将 Nominal或Ordinal变量视为因子（即，当它用作 t 检验的分组变量时），但其他时候，您希望将其用作数字（即 里克特量表）。（有些人会争辩说这永远不应该发生——你永远不应该取分类变量的平均值，这可能是真的——但有些人仍然觉得它很有用）。

Nominal变量“双重性质”的另一个优点是，如果用户不想担心它，则可以忽略变量类型。在处理大型数据集时，检查和设置所有列、确保它们具有正确的变量类型等的过程可能既漫长又乏味。所以只使用变量类型作为指导可以让用户更容易。这也与包括 SPSS 在内的许多统计软件的工作方式一致。

因此，应将Nominal变量视为因子还是连续变量应由上下文来确定。例如，对于 ANCOVA，分配给“因子”的变量应视为因子，分配给“协变量”的变量应视为数字。避免根据变量的类型推断用户希望如何处理变量，即避免使用“独立变量”选项，如果用户分配名义变量，则将其视为因子，如果用户分配连续变量，则被视为协变量——这是隐含的行为，用户会犯错误。

在jamovi，默认情况下，Nominal和Ordinal变量都被当作因子。每列的数值作为属性附加到slef$`data列。您不需要直接与此属性交互，但在某些情况下，知道它在那里是件好事。

与这些属性有关的一个问题是包中的许多 R 函数不尊重属性。使用na.omit或subset有可能对self`$data进行修改，导致这些属性的丢弃。出于这个原因，最好在使用这些函数之前将这些列转换为您想要使用的类型（因此不再需要这些属性）。

将Nominal或者Ordinal变量（作为因子出现）转换为数字，jmvcore提供toNumeric()函数。要反向转换，从数字到因子，您可以使用R 内置的factor()或as.factor()函数。如果toNumeric()已经是数字的变量上调用它，则它不起作用。类似地，如果as.factor()在一个已经是因子的变量上调用它，它没有效果。所以你可以在每一列上调用它们，而无需检查它们是否已经是正确的类型。

回到我们的 ANCOVA 示例，该示例需要单个数字因变量、一个或多个因子作为因子，以及一个或多个协变量作为数字，我们可以.run()按如下方式开始函数：

```
    .run = function() {
        
        # read the option values into shorter variable names
        
        dep  <- self$`options`$dep
        facs <- self$`options`$factors
        covs <- self$`options`$covs
        
        # get the data
        
        data <- self$`

## 状态

到目前为止，教程系列中演示的分析完全无状态。这意味着每次运行分析时（例如，响应用户选中复选框）它都会从头到尾运行分析。在许多情况下，这不是很有效。用户可以运行 t 检验，然后选择请求描述的复选框。如果没有state，分析将在每次更改分析时重新计算 t 检验结果，即使更改的选项对 t 检验结果没有影响。

对于许多分析来说，这不是问题——事实上，t 检验运行得非常快，因此每次更改选项时重新计算并不会真正造成问题；用户仍然几乎立即收到结果。但是，某些分析可能需要相当长的时间才能运行，并且在每次更改时完整地重新运行这些分析会导致长时间的延迟和糟糕的用户体验。这个问题的解决方案是state。

在使用状态下，分析会保留先前运行时的信息。如果用户对现有分析进行更改，则该分析可以使用先前计算的结果。以 t 检验为例，如果用户选中请求附加描述表的复选框，则分析可以重新使用上次运行分析时的 t 检验结果。但是，如果用户更改了影响 t 检验结果的选项（例如 t 检验的类型），则分析不应重复使用较早的 t 检验结果。是否应使用较早的结果由clearWith属性决定。

### clearWith

在r.yaml中使用:

```
items:
    - name:  ttest
      title: Independent Samples T-Test
      type:  Table
      rows:  (deps)
      
      clearWith:  # <-- here
        - group
        - alt
        - varEq
        
      columns:
        - name: var
          title: ''
          type: text
          content: ($key)
```

这clearWith设置了以后, 如果任何选项(group，alt或varEq)被清除或改变, 表格将重新计算, 请注意，我们尚未将deps选项添加到此列表中。当用户添加额外的因变量时，我们不希望它清除现有的行。您可以通过运行此示例并一次添加多个因变量来查看会发生什么。

但是，应该注意的是，我们实际上并没有减少正在执行的计算量。尽管在更改某些选项时不再清除该表，但我们在.b.R文件中的分析实现仍会遍历所有因变量并对每个因变量执行 t 检验。然后用这个新计算的值覆盖表中已有的值；完全相同的值。这不是问题，因为 t-test 运行得非常快，但是我们可以修改我们的.b.R文件以不计算表中已经存在的值。isFilled()方法帮我们找出哪行数据需要进行计算


### isFilled()

有三种调用方法:

```
table`$isFilled() # 整个表格是否填满

table$`isFilled(rowNo=i) # i行是否填满

table`$isFilled(rowKey=key) # key行是否填满

```

现在我们来改写我们的R代码:

```
    .run=function() {
    
        table <- self$`results`$ttest
    
        for (dep in self$`options`$deps) {
        
            if ( ! table$`isFilled(rowKey=dep)) {  # <- this if statement!
    
                formula <- jmvcore::constructFormula(dep, self`$options$`group)
                formula <- as.formula(formula)
            
                results <- t.test(formula, self`$data)
            
                table$`setRow(rowKey=dep, values=list(  # set by rowKey!
                    t=results`$statistic,
                    df=results$`

### setState

但是，有时我们不想只存储最终结果；有时我们也想存储中间对象。例如，我们可能想要创建一个拟合对象，然后在下次运行分析时重复使用这个相同的拟合对象。

可以使用以下方法和属性从任何结果元素（即 Image或 table ）保存和恢复状态

```
table`$setState(object)
object <- table$`


> **注意**
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的, 不论什么模型都可以, 只限制于1个研究内. 
> 跟我学统计可以代做分析, 每单几百元不等. 
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](jamovi模块开发教程.ipynb)
> 可以在微博上@mlln-cn向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
