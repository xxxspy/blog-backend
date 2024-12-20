
---

title: 前端如何检测Chrome-Headless不被爬虫虐
date: 2019-07-05 12:44:03
tags: [javascript, chrome, 爬虫, 逆向工程]

---

前几天看到一篇文章讲chrome headless怎么用于爬虫, 后来发现一些加密网站会侦测chrome headless, 进而进行反爬虫, 于是乎我又去看了写资料关于如何检测chrome headless的, 下面是我看到的资料的翻译!

这篇文章问世之后, 立刻有人针对这些策略做了新的伪装方法, 防止检测chrome headless, 不过那是之后的一篇文章会讲的, 下面这篇文章就只讲简单的一些策略, 这些策略并不是百分之百有效的。

<!-- more -->

### 什么是Headless浏览器(无头浏览器)

无头浏览器是一种可以在没有图形界面的情况下使用的浏览器。它可以通过编程方式进行控制，以自动执行任务，例如进行测试或截取网页截图。

### 为什么要检测无头浏览器

除了先前给出的两个无害用例之外，无头浏览器还可用于自动执行恶意任务。最常见的情况是网页抓取，增加广告展示次数或查找网站上的漏洞。

到目前为止，最受欢迎的无头浏览器之一是PhantomJS。由于它是基于Qt框架构建的，因此与大多数流行的浏览器相比，它表现出许多差异。如本文所述，可以使用一些浏览器指纹识别技术来检测它。

自版本59以来，谷歌发布了其Chrome浏览器的无头版本。与PhantomJS不同，它基于一个普通的Chrome，而不是外部框架，使其存在更难以检测。

在下一部分中，我们将介绍几种可用于区分Chrome浏览器和以无头模式运行的Chrome的技术。

### UserAgent

我们从用户代理开始，该用户代理是常用于检测操作系统的属性以及用户的浏览器。在具有Chrome版本59的Linux计算机上，它具有以下值：“Mozilla / 5.0（X11; Linux x86_64）AppleWebKit / 537.36（KHTML，如Gecko）HeadlessChrome / 59.0.3071.115 Safari / 537.36”

因此，我们可以检查Chrome无头的存在：

```js
if (/HeadlessChrome/.test(window.navigator.userAgent)) {
    console.log("Chrome headless detected");
}
```

用户代理也可以从在后端在HTTP头中获取。但是，如果在两种agent下都是伪造的话，这就失效了。

### Plugins

navigator.plugins返回浏览器中存在的插件数组。通常，在Chrome上我们会找到默认插件，例如Chrome PDF查看器或Google Native Client。相反，在无头模式下，返回的数组不包含任何插件。

```js
if(navigator.plugins.length == 0) {
    console.log("It may be Chrome headless");
}
```

### Languages

在Chrome中，两个Javascript属性可以获取用户使用的语言：navigator.language和navigator.languages。第一个是浏览器UI的语言，而第二个是表示用户首选语言的字符串数组。但是，在无头模式下，navigator.languages返回一个空字符串。

```js
if(navigator.languages == "") {
    console.log("Chrome headless detected");
}
```

### WebGL

WebGL是一种在HTML画布中执行3D渲染的API。使用此API，可以查询图形驱动程序的供应商以及图形驱动程序的渲染器。

使用vanilla Chrome和Linux，我获得了渲染器和供应商的以下值：“Google SwiftShader”和“Google Inc.”。在无头模式下，我获得了“Mesa OffScreen”，这是用于渲染而不使用任何类型的窗口系统的技术和“Brian Paul”，这是启动开源Mesa图形库的程序。

```js
var canvas = document.createElement('canvas');
var gl = canvas.getContext('webgl');

var debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
var vendor = gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
var renderer = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);

if(vendor == "Brian Paul" && renderer == "Mesa OffScreen") {
    console.log("Chrome headless detected");
}
```

并非所有Chrome headless都具有相同的供应商和渲染器值。其他人保留的值也可以在非无头版本上找到。然而，“Mesa Offscreen”和“Brian Paul”表示无头版本的存在。

### Browser features

Modernizr库可以测试浏览器中是否存在各种HTML和CSS功能。我们在Chrome和无头Chrome之间找到的唯一区别是，后者没有hairline功能，可检测出对hidpi / retina hairlines的支持。

```js
if(!Modernizr["hairline"]) {
    console.log("It may be Chrome headless");
}
```

### Missing image

最后，我们最后的发现，也似乎是最稳健的方法，当Chrome无法加载某个图像的售后, 它会使用一个通用的错误图片。

如果使用vanilla Chrome，图像的宽度和高度取决于浏览器的缩放比例，但不等于零。在无头Chrome中，图像的宽度和高度等于零。

```js
var body = document.getElementsByTagName("body")[0];
var image = document.createElement("img");
image.src = "http://iloveponeydotcom32188.jg";
image.setAttribute("id", "fakeimage");
body.appendChild(image);
image.onerror = function(){
    if(image.width == 0 && image.height == 0) {
        console.log("Chrome headless detected");
    }
}
```

### 引用

> 文章原文: https://antoinevastel.com/bot%20detection/2017/08/05/detect-chrome-headless.html


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](前端如何检测Chrome-Headless不被爬虫虐.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
