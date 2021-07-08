
---
title: html技术构建python桌面程序-利用eel
date: 2018-11-09 18:17:55
tags: [python, gui]
toc: true

---
<span></span>
<!-- more -->


### Eel简介

Eel是一个轻量的python桌面GUI开发第三方库, 它使用HTML/JS作为界面开发语言, 但是能够访问所有的python功能, 类似于electron, 但是比它轻量。

Eel实际上是启动了一个本地的web服务器, 它允许你将python的函数暴露给javascript, 所以网页端也能调用python函数。

有很多类似于electron的python实现, 比如cefpython, 但是Eel是轻量级的, 它只是启动了一个chrome app, 所以需要你提前安装好chrome浏览器才可以, 而electron和cefpython都是封装了网页渲染引擎的。

### 安装很简单:

使用pip就行:


```python
pip install eel
```

{% raw %}
<div class="output">
输出(stream):<br>
    Looking in indexes: https://mirrors.ustc.edu.cn/pypi/web/simple
    <br />Collecting eel
    <br />  Downloading https://mirrors.ustc.edu.cn/pypi/web/packages/68/32/4349918ac947d6b3042525df852f529f7ea92a053e1a1ec5dcd55aefbaf8/Eel-0.9.10.tar.gz
    <br />Collecting bottle (from eel)
    <br />  Downloading https://mirrors.ustc.edu.cn/pypi/web/packages/bd/99/04dc59ced52a8261ee0f965a8968717a255ea84a36013e527944dbf3468c/bottle-0.12.13.tar.gz (70kB)
    <br />Collecting bottle-websocket (from eel)
    <br />  Downloading https://mirrors.ustc.edu.cn/pypi/web/packages/17/8e/a22666b4bb0a6e31de579504077df2b1c2f1438136777c728e6cfabef295/bottle-websocket-0.2.9.tar.gz
    <br />Requirement already satisfied: future in d:\mysites\deeplearning.ai-master\.env\lib\site-packages (from eel) (0.16.0)
    <br />Collecting whichcraft (from eel)
    <br />  Downloading https://mirrors.ustc.edu.cn/pypi/web/packages/ab/c6/eb4d1dfbb68168bb01c4394420e5e71d5851e64b910838aa0f14ebd5c7a0/whichcraft-0.5.2-py2.py3-none-any.whl
    <br />Collecting gevent-websocket (from bottle-websocket->eel)
    <br />  Downloading https://mirrors.ustc.edu.cn/pypi/web/packages/7b/84/2dc373eb6493e00c884cc11e6c059ec97abae2678d42f06bf780570b0193/gevent_websocket-0.10.1-py3-none-any.whl
    <br />Collecting gevent (from gevent-websocket->bottle-websocket->eel)
    <br />  Downloading https://mirrors.ustc.edu.cn/pypi/web/packages/96/07/7175f1c519c92ea58d15c36f52421ba5456bf46a28b1c2080dfdd72a93e2/gevent-1.3.7-cp36-cp36m-win_amd64.whl (2.1MB)
    <br />Requirement already satisfied: cffi>=1.11.5; sys_platform == "win32" and platform_python_implementation == "CPython" in d:\mysites\deeplearning.ai-master\.env\lib\site-packages (from gevent->gevent-websocket->bottle-websocket->eel) (1.11.5)
    <br />Collecting greenlet>=0.4.14; platform_python_implementation == "CPython" (from gevent->gevent-websocket->bottle-websocket->eel)
    <br />  Downloading https://mirrors.ustc.edu.cn/pypi/web/packages/a9/a3/2a7a15c2dc23f764eaed46d41e081659aadf45570b4170156dde1c76d4f7/greenlet-0.4.15-cp36-cp36m-win_amd64.whl
    <br />Requirement already satisfied: pycparser in d:\mysites\deeplearning.ai-master\.env\lib\site-packages (from cffi>=1.11.5; sys_platform == "win32" and platform_python_implementation == "CPython"->gevent->gevent-websocket->bottle-websocket->eel) (2.19)
    <br />Building wheels for collected packages: eel, bottle, bottle-websocket
    <br />  Running setup.py bdist_wheel for eel: started
    <br />  Running setup.py bdist_wheel for eel: finished with status 'done'
    <br />  Stored in directory: C:\Users\syd\AppData\Local\pip\Cache\wheels\c6\f2\40\c6694f11d9a710776eef88ccf71ee0a31a98f153980ac796cf
    <br />  Running setup.py bdist_wheel for bottle: started
    <br />  Running setup.py bdist_wheel for bottle: finished with status 'done'
    <br />  Stored in directory: C:\Users\syd\AppData\Local\pip\Cache\wheels\83\83\b1\ca2cc2879a08fbc994b9e77788620b4ec0321be4a3c4ef4585
    <br />  Running setup.py bdist_wheel for bottle-websocket: started
    <br />  Running setup.py bdist_wheel for bottle-websocket: finished with status 'done'
    <br />  Stored in directory: C:\Users\syd\AppData\Local\pip\Cache\wheels\48\36\51\3be1cc3daf74671c54fef48d24c88943cb6b24894a4334fc2c
    <br />Successfully built eel bottle bottle-websocket
    <br />Installing collected packages: bottle, greenlet, gevent, gevent-websocket, bottle-websocket, whichcraft, eel
    <br />Successfully installed bottle-0.12.13 bottle-websocket-0.2.9 eel-0.9.10 gevent-1.3.7 gevent-websocket-0.10.1 greenlet-0.4.15 whichcraft-0.5.2
    <br />
</div>
{% endraw %}

{% raw %}
<div class="output">
输出(stream):<br>
    You are using pip version 18.0, however version 18.1 is available.
    <br />You should consider upgrading via the 'python -m pip install --upgrade pip' command.
    <br />
</div>
{% endraw %}

### 用法

#### 目录结构

Ele工程需要将前端页面和js代码都放在一个特定的文件夹, 其他python模块可以放到任意可以使用的地方。类似这样的目录结构:

```
my_python_script.py     <-- Python scripts
other_python_module.py
static_web_folder/      <-- Web folder
  main_page.html
  css/
    style.css
  img/
    logo.png
```

#### HelloWrold

你需要写一个简单的`main.html`页面, 然后放到存放网页的文件夹`web`, 这个文件夹内的文件都被前端访访问。然后写一个简单的`app.py`文件, 代码如下:

```
import eel
eel.init('web')
eel.start('main.html')
```

最后只要在命令行运行:`python app.py`即可看到你的页面。

#### 可选参数

在调用`eel.start`的时候, 可以传入一些参数, 比如设置窗口尺寸的size参数:`eel.start('main.html', size=(50, 50))`, 还可以使用options参数, 主要可以设置mode/port和启动chrome的时候一些命令行参数, 这些命令行参数可以从这里查看 :

```
web_app_options = {
	'mode': "chrome-app", #or "chrome"
	'port': 8080,
	'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

eel.start('main.html', options=web_app_options)
```

#### 暴露函数

为了实现高级的功能, 你必须要在前端页面中引入下面的js模块:

```html
<script type="text/javascript" src="/eel.js"></script>
```

然后你可以在写python模块的时候, 使用装饰器`eel.expose`来暴露你的python函数给JavaScript:

```python
@eel.expose
def my_python_function(a, b):
    print(a, b, a + b)
```

然后你在前端, 可以使用下面的js代码来调用你的python函数:

```js
console.log('Calling Python...');
eel.my_python_function(1, 2);   // This calls the Python function that was decorated
```


当然你也可可以将JavaScript代码暴露给python用:

```js
eel.expose(my_javascript_function);
function my_javascript_function(a, b, c, d) {
  if(a < b){
    console.log(c * d);
  }
}
```

然后你就可以在python中掉用JavaScript:

```python
print('Calling Javascript...')
eel.my_javascript_function(1, 2, 3, 4)  # This calls the Javascript function
```

### 完整案例

下面是我们的'main.html'文件的主要内容:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello, World!</title>
        
        <!-- Include eel.js - note this file doesn't exist in the 'web' directory -->
        <script type="text/javascript" src="/eel.js"></script>
        <script type="text/javascript">
        
        eel.expose(say_hello_js);               // Expose this function to Python
        function say_hello_js(x) {
            console.log("Hello from " + x);
        }
        
        say_hello_js("Javascript World!");
        eel.say_hello_py("Javascript World!");  // Call a Python function
        
        </script>
    </head>
    
    <body>
        Hello, World!
    </body>
</html>
```

然后python模块是:

```python
import eel

eel.init('web')                     # Give folder containing web files

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

say_hello_py('Python World!')
eel.say_hello_js('Python World!')   # Call a Javascript function

eel.start('hello.html')             # Start (this blocks and enters loop)
```

#### 回调函数

当你调用一个被暴露的函数的时候, 我们可以传入一个函数, 这样就能在函数执行完毕之后立即调用这个函数。例如:

在js里定义一个函数:

```js
eel.expose(js_random);
function js_random() {
  return Math.random();
}
```

然后, 在python里调用的时候:

```py
# 这是一个回调函数
def print_num(n):
    print('Got this from Javascript:', n)

# 在python里调用js的函数, 然后, 再传入一个回调函数  
# 回调函数将会在js函数执行完毕之后再执行
eel.js_random()(print_num)

```

#### 同步返回

在python端, 我们只要不使用回调函数就能同步返回:

```py
n = eel.js_random()()  # 这里有两个括号
print('Got this from Javascript:', n)
```

假如python里已经暴露了一个函数`py_random`, 在JavaScript端, 程序不允许阻塞, 所以只能使用await来避免使用回调函数:

```js
async function run() {
  // 只要函数前面带有async, 才能在函数内部使用await
  
  let n = await eel.py_random()();    // Must prefix call with 'await', otherwise it's the same syntax
  console.log('Got this from Python: ' + n);
}

run();
```

### 打包二进制文件

如果你想让用户下载你的软件使用, 而用户没有安装python, 你最好将你的程序打包成二进制可执行文件, 那么最好使用pyinstaller。

在你的app根目录下执行下面的命令:

```
python -m eel [your_main_script] [your_web_folder]
```

这将创建一文件夹`dist`, 如果你想要创建单文件程序, 你需要使用`--onefile`参数, 如果不想程序运行的时候有一个黑色命令窗口, 你可以使用`--noconsole`参数。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](html技术构建python桌面程序-利用eel.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
