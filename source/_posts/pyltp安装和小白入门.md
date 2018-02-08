---
title: pyltp安装和小白入门
date: 2018-02-03 07:28:47
tags: [文本挖掘, python]
---


之前一篇文章我介绍了一下如何在windows下安装pyltp, 但是自我感觉对小白还是不太友好, 因为我也是小白出身(潜在语义你懂), 所以我对小白有一种发自内心的感情纠结, 所以思前想后辗转反侧以后, 我决定再补充一篇入门教程.

我的开发环境:

- win10 64bit
- python3.5 64bit

我的意思是不要问我python怎么装上去的.

### 安装

参考{% post_link pyltp在windows下的编译安装 %}下载对应版本的wheel文件, 这是我自己打包的一个免编译安装文件, 为小白独家定制的, 拿走. 我下载的是`pyltp-0.2.1-cp35-cp35m-win_amd64.whl`.

我的习惯是, 为每个任务创建一个虚拟环境.

假如我打算在`D:\programs\learn-pyltp`目录下做开发, 后面简称工程根目录. 打开powershell, 不知道怎么打开的需要百度. cd 到这个目录.

```powershell
# 创建.env文件夹, 并以此作为虚拟环境的目录
> python -m venv .env 
# 激活虚拟环境
> .env/script/activate
```

把wheel文件放到工程根目录下, 运行命令:`pip install pyltp-0.2.1-cp35-cp35m-win_amd64.whl`.


