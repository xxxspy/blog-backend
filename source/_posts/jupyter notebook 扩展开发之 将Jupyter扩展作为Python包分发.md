---
title: jupyter notebook 扩展开发之 将Jupyter扩展作为Python包分发
date: 2018-03-31 20:19:18
tags: [jupyter, notebook]
---

这是jupyter notebook 插件开发的系列文档之一, 文章最末尾列出了这个系列的所有博客连接.

<!--more-->


### 怎样扩展notebook功能

Jupyter Notebook客户端和服务器应用程序都可以进行深度定制。他们的行为可以通过分别创建以下功能来扩展：

- nbextension：笔记本扩展
    - 一个单独的JS文件或JavaScript目录或Cascading StyleSheets等，它们至少包含一个AMD模块，该模块导出一个函数`load_ipython_extension`
- 服务器扩展：一个可导入的Python模块
    - 实现load_jupyter_server_extension
- bundler扩展：一个可导入的Python模块，利用`File  - > Download as / Deploy`作为菜单项触发器
    - 实现`bundler`方法
    
### 为什么要为Jupyter扩展创建一个Python包？


由于很少有服务器扩展没有任何前端组件（nExxtension），为了方便和一致，所有这些客户端和服务器扩展及其资产都可以作为Python包打包和版本化，并带有一些简单的命令。这使得用户可以更容易地安装扩展包并且不易出错。

### 安装Jupyter扩展

#### 安装一个包含Jupyter扩展的Python包

有几种方法可以获得包含Jupyter Extensions的Python包。通常，您会使用软件包管理器：

```py
pip install helpful_package
# or
conda install helpful_package
# or
apt-get install helpful_package

# where 'helpful_package' is a Python package containing one or more Jupyter Extensions
```

#### 启用服务器扩展

最简单的情况是启用没有前端组件的服务器扩展。

希望将其配置存储在其主目录中的pip用户将键入以下命令：

```cmd
jupyter serverextension enable --py helpful_package
```

或者，virtualenv或conda用户可以传递--sys-prefix，以保持其环境的独立性和可重复性。例如：

```cmd
# Make sure that your virtualenv or conda environment is activated
[source] activate my-environment

jupyter serverextension enable --py helpful_package --sys-prefix
```

#### 安装nbextension assets


如果某个软件包还具nbextension前端资源（但默认情况下未启用），请使用以下命令安装这些资源：

```py
jupyter nbextension install --py helpful_package # or --sys-prefix if using virtualenv or conda
```

#### 启用nbextension资源

如果每次在浏览器中加载Jupyter应用程序（例如实验室，笔记本，仪表板，终端）时，你的应用程序需要加载资源，则可使用以下命令启用nbextension：

```cmd
jupyter nbextension enable --py helpful_package # or --sys-prefix if using virtualenv or conda
```

#### 它生效了吗？通过列出Jupyter扩展来检查


在运行一个或多个扩展安装步骤之后，您可以列出目前已知的有关nbextensions，服务器扩展或捆绑包扩展的内容。以下命令将列出哪些扩展可用，是否已启用以及其他扩展详细信息：

```cmd
jupyter nbextension list
jupyter serverextension list
jupyter bundlerextension list
```

### 示例 - 服务器扩展

#### 使用服务器扩展创建一个Python包

下面是一个python模块的例子，它包含一个服务器扩展。它有这个目录结构：

```
- setup.py
- MANIFEST.in
- my_module/
  - __init__.py
```

#### 定义服务器扩展

此示例显示服务器扩展及其`load_jupyter_server_extension`函数是在`__init__.py`文件中定义的。

`my_module/__init__.py`:

```py
def _jupyter_server_extension_paths():
    return [{
        "module": "my_module"
    }]


def load_jupyter_server_extension(nbapp):
    nbapp.log.info("my module enabled!")
    
```

### 示例 - 服务器扩展和nbextension

#### 使用服务器扩展创建一个Python包


这是另一个带有前端模块的服务器扩展。它应当有这样的目录结构:

```py
- setup.py
- MANIFEST.in
- my_fancy_module/
  - __init__.py
  - static/
    index.js
    ```
    
#### 定义服务器扩展和nbextension

这个例子再次表明服务器扩展及其`load_jupyter_server_extension`函数是在`__init__.py`文件中定义的。这一次，`nbextension`还有一个函数`_jupyter_nbextension_path`。


```py

def _jupyter_server_extension_paths():
    return [{
        "module": "my_fancy_module"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        # 相对于 `my_fancy_module`的相对路径
        src="static",
        # directory in the `nbextension/` namespace
        dest="my_fancy_module",
        # _also_ in the `nbextension/` namespace
        require="my_fancy_module/index")]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("my module enabled!")
    
```

#### 安装并启用服务器扩展和nbextension

```cmd
jupyter nbextension install --py my_fancy_module [--sys-prefix|--user]
jupyter nbextension enable --py my_fancy_module [--sys-prefix|--system]
jupyter serverextension enable --py my_fancy_module [--sys-prefix|--system]
```

### 案例- Bundler extension


#### 目录结构

```cmd
- setup.py
- MANIFEST.in
- my_tarball_bundler/
  - __init__.py
```

#### 在`__init__.py`中定义

```py
import tarfile
import io
import os
import nbformat

def _jupyter_bundlerextension_paths():
    """Declare bundler extensions provided by this package."""
    return [{
        # unique bundler name
        "name": "tarball_bundler",
        # module containing bundle function
        "module_name": "my_tarball_bundler",
        # human-redable menu item label
        "label" : "Notebook Tarball (tar.gz)",
        # group under 'deploy' or 'download' menu
        "group" : "download",
    }]


def bundle(handler, model):
    """Create a compressed tarball containing the notebook document.

    Parameters
    ----------
    handler : tornado.web.RequestHandler
        Handler that serviced the bundle request
    model : dict
        Notebook model from the configured ContentManager
    """
    notebook_filename = model['name']
    notebook_content = nbformat.writes(model['content']).encode('utf-8')
    notebook_name = os.path.splitext(notebook_filename)[0]
    tar_filename = '{}.tar.gz'.format(notebook_name)

    info = tarfile.TarInfo(notebook_filename)
    info.size = len(notebook_content)

    with io.BytesIO() as tar_buffer:
        with tarfile.open(tar_filename, "w:gz", fileobj=tar_buffer) as tar:
            tar.addfile(info, io.BytesIO(notebook_content))

        # Set headers to trigger browser download
        handler.set_header('Content-Disposition',
                           'attachment; filename="{}"'.format(tar_filename))
        handler.set_header('Content-Type', 'application/gzip')

        # Return the buffer value as the response
        handler.finish(tar_buffer.getvalue())
```


### jupyter notebook 扩展开发系列:

- {% post_link "jupyter notebook 扩展开发之自定义请求处理程序" %}
- {% post_link "jupyter notebook 扩展开发之内容API" %}
- {% post_link "jupyter notebook 扩展开发之 Custom bundler extensions" %}
- {% post_link "jupyter notebook 扩展开发之  文件保存钩子" %}
- {% post_link "jupyter notebook扩展开发之前端插件开发" %}
- {% post_link "jupyter notebook 扩展开发之 将Jupyter扩展作为Python包分发" %}


转载请注明出处:http://mlln.cn 或者 http://jupyter.cn