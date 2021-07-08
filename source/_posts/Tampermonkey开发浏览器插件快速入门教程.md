
---

title: Tampermonkey开发浏览器插件快速入门教程
date: 2019-05-29 08:44:03
tags: [tamplermonkey, ]

---



### 简介

Tampermonkey是一个开发JavaScript脚本的浏览器插件, 它帮助我们使用js来控制浏览器中的页面, 提供页面上的额外功能(比如下载视频), 扩展浏览器的功能(比如vpn代理)等。我们都知道不管是谷歌浏览器还是火狐浏览器, 他们都支持浏览器插件的开发, 但是他们对开发者并不友好, 也许你只想向页面添加一个临时用的小按钮, 用Tampermonkey只需要新建一个脚本写简单代码, 但是如果你从头开始写插件, 那就很麻烦了, 这就是Tampermonkey存在的意义。

<!-- more -->

### 安装Tempermonkey

安装它的方法很简单, 比如chrome浏览器只需要在chrome web store中搜索并点击安装就行, 这里不再赘述。

安装好了以后可以在浏览器里看到这个插件:

<img src="images/tempermonkey-logo.png">

点击这个按钮, 就可以看到所有的可操作菜单:

<img src="images/tm-menu.png" >

### 新建脚本

为了开发自己的小工具, 我们需要新建一个脚本, 可以在上图所示的菜单中选择"添加新脚本"。

接着你会看到一个脚本编辑器就打开了。

<img src="images/tampermonkey-editor.png" >

### 脚本的基本设置

在下面的代码部分, 我们有一些需要填写的关键字段, 我们在备注中有解释每个字段的意义:

```
// ==UserScript==
// @name         脚本的名称
// @namespace    mlln.cn(脚本的命名空间)
// @version      0.1(版本号)
// @description  try to take over the world!(描述)
// @author       You(作者名称)
// @match        *study.163.com/*(脚本运行在哪些网址, 支持正则表达式)
// @require       https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js(脚本依赖)
// ==/UserScript==
```

正如你所见, 我的插件指定运行在"study.163.com"这个网址上, 其他网页不会启动。

并且, 值得注意的是, 我习惯使用jquery, 所以我在require字段指定了可以调用的jquery库, 这样在我写的插件脚本中可以使用$符号进行元素查询和操作了, 是不是很方便!


### 脚本主函数

你创建了新的脚本以后就可以看到这个空的主函数, 它是插件加载时候第一个运行的函数, 你的插件的所有功能都可以从这个主函数开始构建。

```js
(function() {
    'use strict';

    // Your code here...
})();
```

### HelloWorld

为了降低入门门槛, 我们先来开发一个简单的功能, 就是在你打开"study.163.com"这个网页的时候, 插件弹出一个"helloworld"问候, 表示我们的插件可以运行了。

具体的代码很简单:

```js

(function() {
    'use strict';

    alert("Hello World!");
})();
```

效果见下图:

<img src="images/tm-helloworld.png">


### 抓取页面所有链接

现在我们想要抓取这个网页上的所有链接, 我们可以使用jquery帮助我们实现这个功能:

```js
(function() {
    'use strict';
    let hrefs = new Array();
    let aa = `$('a');
    aa.each(function(i, ele){
        hrefs.push($`(ele).attr('href'))
})();
    console.log(hrefs);
```

注意, `$符号需要先声明才可以使用; 我们可以使用console.log来输出我们想看到的结果。

但是不幸的是, 我们的脚本并没有输出我们想要的结果, 只给我输出了一个链接, 这显然是不对的, 脚本的问题在于, 页面需要加载时间较长, 但是脚本运行较快, 导致页面还没完全加载就已经执行完了脚本, 所以我们可以通过延时执行脚本来解决这个问题:



```js
(function() {
    'use strict';
    let $` = window.`$;
    //console.log($`);
    setTimeout(function(){
    let hrefs = new Array();
    let aa = `$('a');
    aa.each(function(i, ele){
        hrefs.push($`

### 结束语

Templermonkey还有很多功能需要探索, 并且它可以整合chrome和firefox的一些插件的接口, 这些我们都会在以后的教程中接着跟大家分享, 这篇文章仅仅是一个快速入门的介绍性质的教程。

另外想要做一个好的插件, 其实主要的技能是js的功底!


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](Tampermonkey开发浏览器插件快速入门教程.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
