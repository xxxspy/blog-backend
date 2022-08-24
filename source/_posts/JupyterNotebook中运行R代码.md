
---

title: Jupyter notebook中运行R代码
date: 2022-08-24 08:44:03
tags: [jupyter, R]
toc: true

---

本篇教程展示了如何在jupyter notebook中运行R代码， 并用一个案例介绍了这种方式编写R代码的好处。

<!-- more -->



## 安装R

如果你已经安装了R, 请忽略这一步骤。

你可以从[这里](https://cloud.r-project.org/index.html)下载R的安装文件, 我这里安装的是`4.2.1`, 你可以选择适合自己的版本, 如果不知道, 可以选择最新版本.

<img src="imgs/installr.png">

## 安装Python

你可以从[这里下载python的安装包](https://www.python.org/downloads/)， 安装非常简单， 我们不再演示。

我使用的版本是3.6， 建议你选择最新版本进行安装。

<img src="imgs/installpython.png">

## 安装Jupyter notebook

Jupyter notebook是python的包， 因此我们使用python安装包的命令pip进行安装：

安装之前最好先对pip进行升级：

`python -m pip install --upgrade pip  `

升级完成以后， 安装jupyter：

`python -m pip install jupyter`

<img src="imgs/installjupyter.png">

安装完成以后， 你可以在CMD中（或PowerShell）使用命令`jupyter notebook`启动notebook, 
你就可以打开浏览器， 打开网址“localhost:8888”， 就看到了下面类似的界面。

<img src="imgs/runjupyter.png">

## 安装 R kernel

R kernel用来与R代码解释器进行通讯， 实际上jupyter notebook是运行在python中， python想要执行R代码， 
必须通过R解释器， 也就是你上面第一步安装的。

你可以打开R解释器：

<img src="imgs/openr.png">

执行命令`install.packages('IRkernel')`

<img src="imgs/install.packages.png">

安装了以后， 你还需要执行命令`IRkernel::installspec(user=FALSE)`， 这个命令的作用是， 让jupyter找到你的R。

<img src="imgs/installspec.png">

## 最后一步 在notebook中创建R文件

使用`jupyter notebook`命令来启动你的notebook， 打开网址“localhost:8888”， 在菜单处可以新建一个R notebook：

<img src="imgs/newrfile.png">

## 初试R

在新建的R文件里面， 你可以先执行安装命令， 我们装一个数据可视化的库：

`install.packages("plotly")`

你会看到如下输出结果：

```
Installing package into 'C:/Users/syd/AppData/Local/R/win-library/4.2'
(as 'lib' is unspecified)

also installing the dependencies 'lazyeval', 'crosstalk'


Warning message in download.file(url, destfile, method, mode = "wb", ...):
"downloaded length 720896 != reported length 3174189"
Warning message in download.file(url, destfile, method, mode = "wb", ...):
"URL 'https://cran.r-project.org/bin/windows/contrib/4.2/plotly_4.10.0.zip': Timeout of 60 seconds was reached"
Error in download.file(url, destfile, method, mode = "wb", ...) : 
  download from 'https://cran.r-project.org/bin/windows/contrib/4.2/plotly_4.10.0.zip' failed
Warning message in download.packages(pkgs, destdir = tmpd, available = available, :
"download of package 'plotly' failed"
package 'lazyeval' successfully unpacked and MD5 sums checked
package 'crosstalk' successfully unpacked and MD5 sums checked

The downloaded binary packages are in
	C:\Users\syd\AppData\Local\Temp\RtmpIDqbO6\downloaded_packages
```

之后， 我们随便画一个图， 看看：

```r
library(ggplot2)
library(plotly)  

n <- 20

x1 <- rnorm(n); x2 <- rnorm(n)
y1 <- 2 * x1 + rnorm(n)
y2 <- 3 * x2 + (2 + rnorm(n))
A <- as.factor(rep(c(1, 2), each = n))
df <- data.frame(x = c(x1, x2), y = c(y1, y2), A = A)
fm <- lm(y ~ x + A, data = df)

p <- ggplot(data = cbind(df, pred = predict(fm)), aes(x = x, y = y, color = A))
p <- p + geom_point() + geom_line(aes(y = pred))

ggplotly(p)

```

<img src="imgs/scatter.png">



再画一个箱线图：

```r

p <- plot_ly(midwest, x = ~percollege, color = ~state, type = "box")

p
```


<img src="imgs/box.png">

## 视频教程

<iframe style="width:900px;height:600px" 
src="//player.bilibili.com/player.html?bvid=BV1LT411w7BJ&page=1" 
scrolling="no" border="0" 
frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>


> **注意**
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的, 不论什么模型都可以, 只限制于1个研究内. 
> 跟我学统计可以代做分析, 每单几百元不等. 
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](JupyterNotebook中运行R代码.ipynb)
> 可以在微博上@mlln-cn向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
