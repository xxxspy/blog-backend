
---

title: nginx配置两个静态网站
date: 2019-06-04 08:44:03
tags: [nginx, ]

---

略

<!-- more -->

### 任务介绍

本来我有一个网站已经使用nginx配置好了, 现在我要增加一个网站, 直接使用nginx配置多个网站即可, 但是我有几个问题:

- 我忘记nginx安装在哪里了
- 我忘记配置文件放在哪里了

所以我先解决这俩问题, 然后再配置多个网站。

### nginx安装位置

首先我想到的方法是使用命令`rpm -ql nginx `, 这个命令按道理可以列出所有nginx安装的目录, 但是前提是你是使用"yum"包管理的方式安装的nginx , 可惜的是, 我不是这种方式。

我知道我的nginx一直再运行状态, 所以我先看了看nginx的进程:

```
netstat -tnlp|grep nginx
```

得到了下面的信息:

```
tcp 0 0 0.0.0.0:80 0.0.0.0:* LISTEN 21196/nginx: master
```

使用上面得到的最后一组数字, 那就是进程号, 然后运行下面的命令:

```
ps -aux |grep 21196
```

得到的输出信息里就包含nginx的路径:

```
root 21196 0.0 0.0 48044 924 ? Ss 23:40 0:00 nginx: master process /usr/sbin/nginx -c /etc/nginx/nginx.conf
```

### nginx配置文件

我们下面开始找nginx配置文件的路径, 因为nginx一直在运行, 所以我使用下面的命令就行:

```
nginx -t
```

你可以看到输出信息, 指明了配置文件的路径。

这个配置文件中写明了一句:

```
include /etc/nginx/sites-avalable/*;
```

这说明sites-enabled目录下的配置文件也被纳入到配置中。

###  复制配置文件

因为我已经有一个网站在运行中, 所以在`/etc/nginx/sites-avalable/`目录下已经有了一个配置文件, 我直接复制已有的配置文件, 然后修改以下配置信息, 主要是配置"server_name", 它一般指你的网站域名, (注意两个网站都监听80端口是可以的, 只要server_name不同即可)。 

### 具体配置内容

具体配置内容很简单, 只要填写以下内容就可以了。

```
server {
    listen 80;
    server_name file.52itstyle.com; # 域名
    charset utf-8;
    root /data/share; # html页面所在路径
  }
```


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](nginx配置两个静态网站.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
