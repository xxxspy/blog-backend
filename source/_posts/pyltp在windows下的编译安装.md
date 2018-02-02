---
title: 哈工大自然语言处理ltp在windows10下的安装使用
date: 2018-01-31 08:32:30
tags: [python, 文本挖掘]
---

ltp是哈工大出品的自然语言处理工具箱, pyltp是python下对ltp(c++)的封装. 在linux下我们很容易的安装pyltp, 因为各种编译工具比较方便. 但是在windows下需要安装vs并且还得做一些配置, 因为我服务的人都是在windows下办公, 需要让他们能够在windows下使用ltp, 所以才有了这篇笔记. 我的方案有两个:

- 在win10 的bash下安装ltp, 然后启动ltp的server, 通过http协议来实现在windows下python调用ltp的方法.
- 安装编译好的wheel(目前只有python3.6/3.5 amd64)(我推荐这种方案)
- 我在文章最下面还引用了一种方法, 就是使用官方已经编译好的可执行exe文件, 直接在命令行(如cmd)下调用.

<!-- more -->
## 第一种方案: bash下安装
---

### 基本环境

- windows 10
- bash for windows
- python 3.6

### 安装bash on ubuntu on windows

这个大家自行百度, 安装很简单.

### 安装编译环境

```bash
sudo apt install cmake
sudo apt install g++
```
安装过程大概十几分钟.

### 下载ltp源码

下载源码, 这是[github地址](https://github.com/HIT-SCIR/ltp/releases).
解压到你能记住的位置

### 编译

cd到源码目录, 比如我的目录:

		cd /mnt/d/bash-sites/ltp-3.4.0

运行编译命令:

```bash
./configure
make
```
编译过程大概花费十几分钟. 现在我的目录里多了一个bin文件夹:
```
drwxrwxrwx 0 root root   512 Jan 31 15:42 ./
drwxrwxrwx 0 root root   512 Jan 31 15:30 ../
-rwxrwxrwx 1 root root   800 Jan 31 15:30 appveyor.yml*
-rwxrwxrwx 1 root root     0 Jan 31 15:30 AUTHORS*
drwxrwxrwx 0 root root   512 Jan 31 15:53 bin/
drwxrwxrwx 0 root root   512 Jan 31 15:42 build/
-rwxrwxrwx 1 root root 29301 Jan 31 15:30 ChangeLog.md*
drwxrwxrwx 0 root root   512 Jan 31 15:30 cmake/
-rwxrwxrwx 1 root root  1439 Jan 31 15:30 CMakeLists.txt*
drwxrwxrwx 0 root root   512 Jan 31 15:30 conf/
-rwxrwxrwx 1 root root   131 Jan 31 15:30 configure*
-rwxrwxrwx 1 root root   902 Jan 31 15:30 COPYING*
drwxrwxrwx 0 root root   512 Jan 31 15:30 doc/
-rwxrwxrwx 1 root root 79976 Jan 31 15:30 Doxyfile*
drwxrwxrwx 0 root root   512 Jan 31 15:30 examples/
-rwxrwxrwx 1 root root  1028 Jan 31 15:30 .gitignore*
drwxrwxrwx 0 root root   512 Jan 31 15:42 include/
-rwxrwxrwx 1 root root    85 Jan 31 15:30 INSTALL*
drwxrwxrwx 0 root root   512 Jan 31 15:53 lib/
-rwxrwxrwx 1 root root   965 Jan 31 15:30 Makefile*
-rwxrwxrwx 1 root root  6639 Jan 31 15:30 NEWS.md*
-rwxrwxrwx 1 root root  4750 Jan 31 15:30 README.md*
drwxrwxrwx 0 root root   512 Jan 31 15:30 src/
-rwxrwxrwx 1 root root  3048 Jan 31 15:30 subproject.d.json*
drwxrwxrwx 0 root root   512 Jan 31 15:31 thirdparty/
drwxrwxrwx 0 root root   512 Jan 31 15:31 tools/
-rwxrwxrwx 1 root root  1372 Jan 31 15:30 .travis.yml*
```

### 配置server

一开始我启动server遇到了这个错误.
```
[INFO] 2018-01-31 15:54:39 Loading segmentor model from "ltp_data/cws.model" ...
[ERROR] 2018-01-31 15:54:39 /mnt/d/bash-sites/ltp-3.4.0/src/ltp/LTPResource.cpp: line 50: LoadSegmentorResource(): Failed to load segmentor model
[ERROR] 2018-01-31 15:54:39 /mnt/d/bash-sites/ltp-3.4.0/src/ltp/Ltp.cpp: line 78: load(): in LTP::wordseg, failed to load segmentor resource
[ERROR] 2018-01-31 15:54:39 /mnt/d/bash-sites/ltp-3.4.0/src/server/ltp_server.cpp: line 172: main(): Failed to setup LTP engine.
```

因为缺少了模型文件, 在[这里](https://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569#list/path=%2F&parentPath=%2F)下载最新的模型文件.

解压到/mnt/d/bash-sites/ltp-3.4.0/ltp_data/下, 这是ltp默认的数据模型存放位置.

然后就能顺利启动服务器啦.

```bash
syd@DESKTOP-J02R2VJ:/mnt/d/bash-sites/ltp-3.4.0$ ./bin/ltp_server --port 9090
[INFO] 2018-01-31 15:56:36 Loading segmentor model from "ltp_data/cws.model" ...
[INFO] 2018-01-31 15:56:36 segmentor model is loaded.
[INFO] 2018-01-31 15:56:36 Loading postagger model from "ltp_data/pos.model" ...
[INFO] 2018-01-31 15:56:36 postagger model is loaded
[INFO] 2018-01-31 15:56:36 Loading NER resource from "ltp_data/ner.model"
[INFO] 2018-01-31 15:56:36 NER resource is loaded.
[INFO] 2018-01-31 15:56:36 Loading parser resource from "ltp_data/parser.model"
[INFO] 2018-01-31 15:56:37 parser is loaded.
[INFO] 2018-01-31 15:56:37 Loading srl resource from "ltp_data/pisrl.model"
[dynet] random seed: 493907432
[dynet] allocating memory: 2000MB
[dynet] memory allocation done.
[INFO] 2018-01-31 15:56:39 srl resource is loaded.
[INFO] 2018-01-31 15:56:39 Resources loading finished.
[INFO] 2018-01-31 15:56:39 Start listening on port [9090]...
```

### 测试

随便写个请求, 看看效果:

```python
import requests
import json
uri_base = "http://127.0.0.1:9090/ltp"
data = {'s': '我认为他叫汤姆去拿外衣和鞋子。', 'x': 'n', 't': 'srl'}
response = requests.get(uri_base, data=data)
rdata = response.json()
print(json.dumps(rdata, indent=4, ensure_ascii=False))
```

```json
[
    [
        [
            {
                "arg": [],
                "cont": "我",
                "id": 0,
                "ne": "O",
                "parent": 1,
                "pos": "r",
                "relate": "SBV"
            },
            {
                "arg": [
                    {
                        "beg": 0,
                        "end": 0,
                        "id": 0,
                        "type": "A0"
                    },
                    {
                        "beg": 2,
                        "end": 9,
                        "id": 1,
                        "type": "A1"
                    }
                ],
                "cont": "认为",
                "id": 1,
                "ne": "O",
                "parent": -1,
                "pos": "v",
                "relate": "HED"
            },
            {
                "arg": [],
                "cont": "他",
                "id": 2,
                "ne": "O",
                "parent": 3,
                "pos": "r",
                "relate": "SBV"
            },
            {
                "arg": [
                    {
                        "beg": 2,
                        "end": 2,
                        "id": 0,
                        "type": "A0"
                    },
                    {
                        "beg": 4,
                        "end": 4,
                        "id": 1,
                        "type": "A1"
                    },
                    {
                        "beg": 5,
                        "end": 9,
                        "id": 2,
                        "type": "A2"
                    }
                ],
                "cont": "叫",
                "id": 3,
                "ne": "O",
                "parent": 1,
                "pos": "v",
                "relate": "VOB"
            },
            {
                "arg": [],
                "cont": "汤姆",
                "id": 4,
                "ne": "S-Nh",
                "parent": 3,
                "pos": "nh",
                "relate": "DBL"
            },
            {
                "arg": [],
                "cont": "去",
                "id": 5,
                "ne": "O",
                "parent": 6,
                "pos": "v",
                "relate": "ADV"
            },
            {
                "arg": [
                    {
                        "beg": 7,
                        "end": 9,
                        "id": 0,
                        "type": "A1"
                    }
                ],
                "cont": "拿",
                "id": 6,
                "ne": "O",
                "parent": 3,
                "pos": "v",
                "relate": "VOB"
            },
            {
                "arg": [],
                "cont": "外衣",
                "id": 7,
                "ne": "O",
                "parent": 6,
                "pos": "n",
                "relate": "VOB"
            },
            {
                "arg": [],
                "cont": "和",
                "id": 8,
                "ne": "O",
                "parent": 9,
                "pos": "c",
                "relate": "LAD"
            },
            {
                "arg": [],
                "cont": "鞋子",
                "id": 9,
                "ne": "O",
                "parent": 7,
                "pos": "n",
                "relate": "COO"
            },
            {
                "arg": [],
                "cont": "。",
                "id": 10,
                "ne": "O",
                "parent": 1,
                "pos": "wp",
                "relate": "WP"
            }
        ]
    ]
]
```

## 第二种方案: 安装wheel
---

### 下载wheels

下面两个文件针对不同的python版本下载一个即可， 这是我在自己的电脑（win10）上编译的，不知道你的系统是否能用，64bit的windows应该都可以，有问题在下面留言。

- {% asset_link pyltp-0.2.1-cp35-cp35m-win_amd64.whl %}
- {% asset_link pyltp-0.2.1-cp36-cp36m-win_amd64.whl %}

> 注意: 这两个文件的区别是python版本号

### 安装文件

下载好了以后, 在命令行下, cd到wheel文件所在的目录, 然后使用命令`pip install wheel文件名`安装.

### 测试

安装好了以后, 打开python shell, 试用一下.

```python
from pyltp import SentenceSplitter
sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
print('\n'.join(sents))
```

### 下载models数据

- 下载models链接：https://pan.baidu.com/s/1o9vytmU 密码：5ntf
- 放到任意方便调用的地方即可， 因为程序里需要你自己主动调用的

## 第三种方案: 直接调用编译好的ltp的可执行文件
---

可以参考这篇[文章](http://blog.csdn.net/churximi/article/details/51174182), 但是我在3.4版本中测试不成功, 加载srl资源失败. 但是在3.3.1版本上测试是成功的.