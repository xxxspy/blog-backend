---
title: 2022年conda常用命令常见问题手册
date: 2022-10-26 10:17:23
tags: [conda]
---

这篇文章列出conda的常用方法和常见问题， 欢迎大家提问和补充。

<!-- more -->


### conda proxy设置问题

在国内做数据科学， 很多时候你必须用proxy代理， 否则很多资料找不到，
那怎样让conda使用本地的vpn呢？
你只需要在这个设置文件中添加代理， win10下设置文件在这里  `C:\Users\{username}\.condarc` ，
username是你自己的电脑的用户名。

添加如下的设置：

```yaml
proxy_servers:
  http: http://127.0.0.1:7890
  https: https://127.0.0.1:7890
```

但是你会发现conda出现这样的问题：

```
ProxyError: Conda cannot proceed due to an error in your proxy configuration.
Check for typos and other configuration errors in any '.netrc' file in your home directory,
any environment variables ending in '_PROXY', and any other system-wide proxy
configuration settings.
```

这个问题可能的原因有很多， 我的解决方法之一是将https去掉s， 设置改为：

```yaml
proxy_servers:
  http: http://127.0.0.1:7890
  https: http://127.0.0.1:7890
```

因为你本地的vpn可能不支持https的加密通讯。


### conda 不支持powershell

在windows系统下， cmd已经逐渐被边缘， 现在更多人使用powershell，
那么， 很多人在powershell中使用conda 的时候发现激活不了某个环境，
运行`conda activate ...` 的时候没有任何反应，
这时候你需要这样设置，

在菜单栏打开`Anaconda Powershell Prompt` , 
运行命令`conda init powershell`， conda会做一些更改， 然后你就可以正常使用你的 powershell+conda 了。