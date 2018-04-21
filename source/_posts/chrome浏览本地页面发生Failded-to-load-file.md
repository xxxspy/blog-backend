---
title: chrome浏览本地页面发生Failded to load file
date: 2018-04-21 11:44:13
tags: [nodejs]
---

有时候从网上下载一堆静态页面, 在本地打开, 如果你用的是chrome(别的应该也不行), 会遇到错误:`Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, https.` 这种问题其实是chrome的安全机制, 不允许网页访问本地的文件. 有一种解决方案是禁用chrome的安全机制, 但是风险显而易见就是chrome不安全了. 其实, 本地查看静态页面, 最好的方式就是开启一个静态页面的服务器, 看似复杂, 其实就一条命令搞定.

<!--more-->

- 假设你已经安装了nodejs.

- 打开你最喜欢的终端模拟器

- 我们先安装`http-server`:

    npm install http-server -g

- 开启服务器: `http-server path/to/your/angular/root/directory -o`

