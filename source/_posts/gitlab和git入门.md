---
title: gitlab和git入门
date: 2017-09-07 11:31:47
tags: git
---

## 安装 git for windows

>> 下载链接：http://pan.baidu.com/s/1b1hNtG 密码：pe3y。

安装很简单，不详细介绍。

## 初始设置

```bash
git config --global user.name "gitlab网站的用户名"
git config --global user.email "注册的邮箱"
```

## 复制代码

从gitlab克隆一个项目：

http://gitlab.eachina.com:10080/ydsun/functional-test.git

```bash
git clone http://gitlab.eachina.com:10080/ydsun/functional-test.git
```

## 修改代码

可以新建、删除、修改文件。

## 保存修改

你修改的代码只是保存在工作区，并没有进入版本仓库中，
你需要使用如下命令保存修改。

```bash
git add .
git commit -m "增加登录测试"
```

## 推送修改

只有推动到gitlab网站，才能使得别人看到你做的修改。但是在推送之前，需要保证你已经拿到了最新的代码，所以按照以下步骤进行推送：

先更新代码，也就是从gitlab服务器中下载最新版本：

```bash
git pull origin master
```

然后再推送你的修改

```bash
git push origin master
```