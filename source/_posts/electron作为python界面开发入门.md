---
title: electron作为python界面开发入门
date: 2018-01-08 05:41:49
tags: [electron, python]
---



<-- more -->


### 安装全局依赖

- 安装nodejs
- 安装python3.5(作为开发环境)
- 安装node-gyp(`npm install -g node-gyp`)
- 安装windows下的编译环境(`npm install --global --production windows-build-tools`)

你会发现安装`windows-build-tools`同时会把python2安装到你的`%USERPROFILE%\.windows-build-tools\python27`下, 想知道'USERPROFILE'指向哪里, 只需要在powershell中输入`$env:USERPROFILE`即可. 现在就需要让node-gyp知道你的python在哪里, 设置`node-gyp --python /path/to/python2.7`, 或者你用npm的方式调用, 需要设置`npm config set python /path/to/executable/python2.7`.


### 初始化项目

- 创建一个项目文件夹
- 初始化项目`npm init`
- 创建文件夹`py`
- 在文件夹`py`内部创建虚拟环境`python -m venv .env`
- 在虚拟环境中安装依赖`zerorpc`和`pyinstaller`(python 方面比较简单, 不详细介绍)

### 安装node依赖

#### 编辑`package.json`文件, 可以参考我的:

```json
{
  "name": "python-electron",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "author": "",
  "license": "ISC",
  "scripts": {
    "start": ".\\node_modules\\.bin\\electron .",
    "rebuild": ".\\node_modules\\.bin\\electron-rebuild.cmd"
  },
  "devDependencies": {
    "electron": "^1.7.10",
    "electron-rebuild": "^1.6.0"
  },
  "dependencies": {
    "zerorpc": "^0.9.7"
  }
}
```
#### 配置npm

- 在项目根目录下创建`.npmrc`, 然后输入如下内容:

```
npm_config_target="1.7.10" # electron version
npm_config_runtime="electron" # 为elelctron编译
npm_config_disturl="https://atom.io/download/electron" # 资源下载地址
npm_config_build_from_source="true" # 从源码编译
```


#### 源码编译安装依赖

`npm install`

这个过程会安装所有列在package.json中的库.

### 开发测试程序

#### python部分

这是一个简单的API, 主要功能是把前端发来的字符串经过python的`eval`处理. 测试程序是否能跑起来, 只需要激活你的python虚拟环境, 然后`python ./py/api.py`即可.

```python
# 下面的代码放到`./py/api.py`
from __future__ import print_function
import sys
import zerorpc


class CalcApi(object):
    def eval(self, text):
        """based on the input text, return the int result"""
        try:
            return eval(text)
        except Exception as e:
            return 0.0

    def echo(self, text):
        """echo any text"""
        return text


def parse_port():
    return 4242


def main():
    addr = 'tcp://127.0.0.1:{}'.format(parse_port())
    s = zerorpc.Server(CalcApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()


if __name__ == '__main__':
    main()

```

#### electron部分

主线程程序, 主要是创建窗口并启动python.

```javascript
const electron = require('electron')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require('path')

let mainWindow = null
const createWindow = () => {
  mainWindow = new BrowserWindow({width: 800, height: 600})
  mainWindow.loadURL(require('url').format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))
  mainWindow.webContents.openDevTools()
  mainWindow.on('closed', () => {
    mainWindow = null
  })
}
app.on('ready', createWindow)
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})
app.on('activate', () => {
  if (mainWindow === null) {
    createWindow()
  }
})

// 以下是创建python的进程

let pyProc = null
let pyPort = null

const selectPort = () => {
  pyPort = 4242
  return pyPort
}

const createPyProc = () => {
  console.log('creating python server...')
  let port = '' + selectPort()
  let script = path.join(__dirname, 'py', 'api.py')
  let pypath = path.join(__dirname, 'py','.env','scripts','python.exe')
  pyProc = require('child_process').spawn(pypath, [script, port])
  if (pyProc != null) {
    console.log('child process success')
  }
}

const exitPyProc = () => {
  pyProc.kill()
  pyProc = null
  pyPort = null
}

app.on('ready', createPyProc)
app.on('will-quit', exitPyProc)
 

```

主页`index.html`, 就是实现了一个简单的输入框.

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Hello Calculator!</title>
  </head>
  <body>
    <h1>Hello Calculator!</h1>
    <p>Input something like <code>1 + 1</code>.</p>
    <p>This calculator supports <code>+-*/^()</code>,
    whitespaces, and integers and floating numbers.</p>
    <input id="formula" value="1 + 2.0 * 3.1 / (4 ^ 5.6)"></input>
    <div id="result"></div>
  </body>
  <script>
    require('./render.js')
  </script>
</html>

```

功能模块`render.js`, 这部分是响应用户操作并与python通讯的.

```JavaScript
const zerorpc = require("zerorpc")
let client = new zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")

let formula = document.querySelector('#formula')
let result = document.querySelector('#result')
formula.addEventListener('input', () => {
  client.invoke("eval", formula.value, (error, res) => {
    if(error) {
      console.error(error)
    } else {
      result.textContent = res
    }
  })
})
formula.dispatchEvent(new Event('input'))
```

### 启动程序

如果你看我写的package.json文件, 我已经写好了一个启动命令.

```
npm run start
```


### 打包文件

#### 打包api.py

前面我们已经安装了python的打包工具`pyinstaller`, 所以现在我们在package.json文件中加一条命令即可:

```
"build-python":"pyinstaller ./py/api.py --clean --distpath ./pydist"
```

现在只要使用命令`npm run build-python`即可.

于是在项目根目录下生成了一个`pydist`文件夹, `pydist/api/`目录结构如下, 虽然文件多, 但是我们只要知道, api.exe是程序入口即可. 下面可以打包到electron程序里.

```
(.env) PS E:\programs\python-electron> ls .\pydist\api
    目录: E:\programs\python-electron\pydist\api
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        2018/1/10     16:45                Include
d-----        2018/1/10     16:45                tcl
d-----        2018/1/10     16:45                tk
d-----        2018/1/10     16:45                zmq
-a----        2018/1/10     16:45          11616 api-ms-win-core-file-l1-2-0.dll
-a----        2018/1/10     16:45          11616 api-ms-win-core-file-l2-1-0.dll
-a----        2018/1/10     16:45          14176 api-ms-win-core-localization-l1-2-0.dll
-a----        2018/1/10     16:45          12128 api-ms-win-core-processthreads-l1-1-1.dll
-a----        2018/1/10     16:45          12128 api-ms-win-core-synch-l1-2-0.dll
-a----        2018/1/10     16:45          11616 api-ms-win-core-timezone-l1-1-0.dll
-a----        2018/1/10     16:45          12640 api-ms-win-crt-conio-l1-1-0.dll
-a----        2018/1/10     16:45          15712 api-ms-win-crt-convert-l1-1-0.dll
-a----        2018/1/10     16:45          12128 api-ms-win-crt-environment-l1-1-0.dll
-a----        2018/1/10     16:45          13664 api-ms-win-crt-filesystem-l1-1-0.dll
-a----        2018/1/10     16:45          12640 api-ms-win-crt-heap-l1-1-0.dll
-a----        2018/1/10     16:45          12128 api-ms-win-crt-locale-l1-1-0.dll
-a----        2018/1/10     16:45          20832 api-ms-win-crt-math-l1-1-0.dll
-a----        2018/1/10     16:45          19808 api-ms-win-crt-multibyte-l1-1-0.dll
-a----        2018/1/10     16:45          12640 api-ms-win-crt-process-l1-1-0.dll
-a----        2018/1/10     16:45          16224 api-ms-win-crt-runtime-l1-1-0.dll
-a----        2018/1/10     16:45          17760 api-ms-win-crt-stdio-l1-1-0.dll
-a----        2018/1/10     16:45          17760 api-ms-win-crt-string-l1-1-0.dll
-a----        2018/1/10     16:45          14176 api-ms-win-crt-time-l1-1-0.dll
-a----        2018/1/10     16:45          12128 api-ms-win-crt-utility-l1-1-0.dll
-a----        2018/1/10     16:44        2481852 api.exe
-a----        2018/1/10     16:45           1028 api.exe.manifest
-a----        2018/1/10     16:44         765325 base_library.zip
-a----        2018/1/10     16:45         285696 gevent.libev.corecext.pyd
-a----        2018/1/10     16:45          80896 gevent._semaphore.pyd
-a----        2018/1/10     16:45          29184 greenlet.pyd
-a----        2018/1/10     16:45          59904 msgpack._packer.pyd
-a----        2018/1/10     16:45          75776 msgpack._unpacker.pyd
-a----        2018/1/10     16:45         633152 MSVCP140.dll
-a----        2018/1/10     16:45         829264 MSVCR100.dll
-a----        2018/1/10     16:45         189952 pyexpat.pyd
-a----        2018/1/10     16:45        3935744 python35.dll
-a----        2018/1/10     16:45         138752 pywintypes35.dll
-a----        2018/1/10     16:45          19968 select.pyd
-a----        2018/1/10     16:45        1640960 tcl86t.dll
-a----        2018/1/10     16:45        1954304 tk86t.dll
-a----        2018/1/10     16:45        1004136 ucrtbase.dll
-a----        2018/1/10     16:45         865792 unicodedata.pyd
-a----        2018/1/10     16:45          87888 VCRUNTIME140.dll
-a----        2018/1/10     16:45         124416 win32api.pyd
-a----        2018/1/10     16:45          62464 win32evtlog.pyd
-a----        2018/1/10     16:45          29696 win32wnet.pyd
-a----        2018/1/10     16:45          55296 zmq.backend.cython.constants.pyd
-a----        2018/1/10     16:45          60928 zmq.backend.cython.context.pyd
-a----        2018/1/10     16:45          30720 zmq.backend.cython.error.pyd
-a----        2018/1/10     16:45          77312 zmq.backend.cython.message.pyd
-a----        2018/1/10     16:45         119808 zmq.backend.cython.socket.pyd
-a----        2018/1/10     16:45          34816 zmq.backend.cython.utils.pyd
-a----        2018/1/10     16:45          46592 zmq.backend.cython._device.pyd
-a----        2018/1/10     16:45          53248 zmq.backend.cython._poll.pyd
-a----        2018/1/10     16:45          26624 zmq.backend.cython._version.pyd
-a----        2018/1/10     16:45          87552 _bz2.pyd
-a----        2018/1/10     16:45         122368 _ctypes.pyd
-a----        2018/1/10     16:45         314880 _decimal.pyd
-a----        2018/1/10     16:45        1443840 _hashlib.pyd
-a----        2018/1/10     16:45         146432 _lzma.pyd
-a----        2018/1/10     16:45          22528 _multiprocessing.pyd
-a----        2018/1/10     16:45          66048 _socket.pyd
-a----        2018/1/10     16:45        2045440 _ssl.pyd
-a----        2018/1/10     16:45          80896 _testcapi.pyd
-a----        2018/1/10     16:45          58368 _tkinter.pyd
```
#### 打包electron部分

这里有一些代码需要修改. 因为之前启动python程序是直接用虚拟环境中的python调用api.py文件, 现在得调用`pydist/api/api.exe`.

之前的代码是:

```JavaScript
const createPyProc = () => {
  console.log('creating python server...')
  let port = '' + selectPort()
  let script = path.join(__dirname, 'py', 'api.py')
  let pypath = path.join(__dirname, 'py','.env','scripts','python.exe')
  pyProc = require('child_process').spawn(pypath, [script, port])
  if (pyProc != null) {
    console.log('child process success')
  }
}
```

改为:

```javascript
// 设置一个全局变量来决定是否为开发环境
const NODE_ENV = 'production'
// const NODE_ENV = 'development'
// 根据不同的环境来选择不同的启动方式
const createPyProc = () => {
  console.log('creating python server...')
  let port = '' + selectPort()
  if (NODE_ENV ==='development'){
    let script = path.join(__dirname, 'py', 'api.py')
    let pypath = path.join(__dirname, 'py', '.env', 'scripts', 'python.exe')
    pyProc = require('child_process').spawn(pypath, [script, port])
  }else{
    let exePath = path.join(__dirname, 'pydist', 'api','api.exe')
    pyProc=require('child_process').execFile(exePath, [port])
  }
  if (pyProc != null) {
    console.log('child process success')
  }
}
```
然后, 你需要关闭dev tools, 为了方便调试, 我们在程序中调用了`mainWindow.webContents.openDevTools`, 同样是加一个判断即可.

```JavaScript
if(NODE_ENV==='development'){
	mainWindow.webContents.openDevTools()
}
```

然后, 你启动一下看是否有问题, 按道理是没有问题的.

最后就是打包electron, 用到了`electron-packager`, 我还是把打包命令写在了package.json中:

```
    "pack-app": "./node_modules/.bin/electron-packager . --overwrite --ignore=py$ --ignore=\\.env --ignore=\\.vscode --ignore=old-post-backup"

```

### 安装过程可能出现的问题

#### 安装electron出现网络超时

```
/Users/chenlei/node_modules/electron/install.js:47
  throw err
  ^

Error: connect ETIMEDOUT 54.231.34.41:443
```

你需要设置淘宝镜像, 在powershell中运行:

$env:ELECTRON_MIRROR="http://npm.taobao.org/mirrors/electron/"

#### 总是编译失败

- 可能是网络原因, 你需要翻墙或者找个网络好的地方
- 可能是配置有问题, 我在这里列出我的环境

```
PS E:\programs\python-electron> npm config ls
; cli configs
metrics-registry = "https://registry.npm.taobao.org/"
scope = ""
user-agent = "npm/5.5.1 node/v8.9.3 win32 x64"

; project config E:\programs\python-electron\.npmrc
npm_config_build_from_source = true
npm_config_disturl = "https://atom.io/download/electron"
npm_config_runtime = "electron"
npm_config_target = "1.7.10"

; userconfig C:\Users\wangluobu\.npmrc
msvs_version = "2015"
python = "C:\\Users\\wangluobu\\.windows-build-tools\\python27"
registry = "https://registry.npm.taobao.org/"

; node bin location = C:\Program Files\nodejs\v8\node.exe
; cwd = E:\programs\python-electron
; HOME = C:\Users\wangluobu
; "npm config ls -l" to show all defaults.
```

### 结束语

有什么问题请在下方留言. 你可以下载我打包好的程序试一试, 只不过比较大, 我放在[网盘](http://mlln.cn)里了.