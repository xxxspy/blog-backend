---
title: jupyter notebook 扩展开发之 Custom bundler extensions
date: 2018-03-31 20:19:18
tags: [jupyter, notebook]
---

这是jupyter notebook 插件开发的系列文档之一, 文章最末尾列出了这个系列的所有博客连接.

<!--more-->

### Custom bundler extensions

笔记本服务器支持编写用于转换/打包/下载/部署笔记本文件的bundler扩展。作为开发人员，您只需编写一个Python函数来实现一个bundler。笔记本服务器会自动在笔记本前端生成一个 `File -> Download` 或`File -> Deploy`菜单项，以触发您的bundler程序。

以下是可以使用bundler扩展实现的一些示例：


- 将笔记本文件转换为HTML文档并将其发布为博客网站上的帖子
- 创建当前笔记本环境的快照，并将该定义和笔记本捆绑到一个zip下载中
- 将笔记本部署为独立的交互式仪表板


要实现bundler扩展，您必须执行以下所有操作：

- 在您的Python包中声明bundler扩展元数据
- 编写一个响应bundler请求的bundler函数
- 指导您的用户如何启用/禁用bundler

以下各节详细介绍这些步骤。

#### 声明bundler元数据

您必须通过实现`_jupyter_bundlerextensions_paths`函数提供有关bundler扩展的信息。只要可以在import package时能够引入你的bundler，此函数可以放在在软件包中的任何位置。 （请参阅[启用/禁用捆绑程序扩展](http://jupyter-notebook.readthedocs.io/en/stable/extending/bundler_extensions.html#enabling-bundlers)。）

```python
# in mypackage.hello_bundler

def _jupyter_bundlerextension_paths():
    """Example "hello world" bundler extension"""
    return [{
        'name': 'hello_bundler',                    # unique bundler name
        'label': 'Hello Bundler',                   # human-redable menu item label
        'module_name': 'mypackage.hello_bundler',   # module containing bundle()
        'group': 'deploy'                           # group under 'deploy' or 'download' menu
    }]
```

请注意，返回值是一个列表。通过返回列表中的多个字典，您允许用户一次启用/禁用所有bundler。

#### Writing the bundle function

在运行时，具有给定标签的菜单项出现在`File -> Download` 或`File -> Deploy`菜单中，具体取决于元数据中的值。当用户单击菜单项时，会打开一个新的浏览器选项卡，并且笔记本服务器将调用元数据中指定的`module_name`中的包函数。

您必须实现类似以下代码的bundler：

```python
# in mypackage.hello_bundler

def bundle(handler, model):
    """Transform, convert, bundle, etc. the notebook referenced by the given
    model.

    Then issue a Tornado web response using the `handler` to redirect
    the user's browser, download a file, show a HTML page, etc. This function
    must finish the handler response before returning either explicitly or by
    raising an exception.

    Parameters
    ----------
    handler : tornado.web.RequestHandler
        Handler that serviced the bundle request
    model : dict
        Notebook model from the configured ContentManager
    """
    handler.finish('I bundled {}!'.format(model['path']))
```

您的bundler函数可以随意执行任何需求并以任何方式进行响应。例如，它可以从请求中读取附加的查询参数，发出重定向到另一个站点，运行本地进程（例如nbconvert），向另一个服务发出HTTP请求等。

bundler函数的调用者是@ tornado.gen.coroutine，并用torando.gen.maybe_future封装其调用。这种行为意味着你可以像上面的例子那样同步处理web请求，或者像下面的例子那样异步使用@ tornado.gen.coroutine和yield。

如果bundler长时间运行，您应该更喜欢采用第二种异步方法，否则会在同步处理时阻塞笔记本服务器主循环。

有关从菜单项点击到捆bundler函数调用的数据流的更多细节，请参阅[bundler程序调用详细信息](http://jupyter-notebook.readthedocs.io/en/stable/extending/bundler_extensions.html#bundler-details)。


笔记本服务器有用于启用和禁用bundler程序扩展的命令行接口（CLI）。

您应该写文档说明启用和禁用bundler的基本命令。例如, 启用hello_bundler示例的一个可能命令如下：

```
jupyter bundlerextension enable --py mypackage.hello_bundler --sys-prefix
```

以上内容将使用mypackage.hellow_bundler._jupyter_bundlerextension_paths函数返回的元数据更新当前conda / virtualenv环境（-sys-prefix）中的笔记本配置文件。

禁用bundler函数的相应命令如下：

```
jupyter bundlerextension disable --py mypackage.hello_bundler --sys-prefix
```

有关使用bundlerextension子命令的更多帮助，请运行以下命令。

```
jupyter bundlerextension --help
```

#### Example: IPython Notebook bundle (.zip)

本文档中的hello_bundler示例简洁明了。有关更多有意义的示例，请参阅`notebook / bundler / zip_bundler.py`和`notebook / bundler / tarball_bundler.py`。你可以像这样尝试它们：

```
jupyter bundlerextension enable --py notebook.bundler.zip_bundler --sys-prefix
jupyter bundlerextension enable --py notebook.bundler.tarball_bundler --sys-prefix
```

#### Bundler invocation details

- 对bundler扩展的支持来自`notebook / bundler`中的Python模块和`notebook / static / notebook / js / menubar.js`中的JavaScript。各部分之间的数据流大致如下：

- 用户打开笔记本文档
- 笔记本前端JavaScript加载笔记本配置
- Bundler前端JS为配置中的所有bundler扩展创建菜单项
- 用户单击捆绑器菜单项
- JS点击处理程序打开一个新的浏览器窗口/标签到`<notebook base_url> / bundle / <path / to / notebook>？bundler = <name>`（即HTTP GET请求）
- bundler处理器验证笔记本路径和捆绑器名称
- Bundle处理程序将请求委托给捆绑程序的module_name中的捆绑功能
- 捆绑功能完成HTTP请求



### jupyter notebook 扩展开发系列:

- {% post_link "jupyter notebook 扩展开发之自定义请求处理程序" %}
- {% post_link "jupyter notebook 扩展开发之内容API" %}
- {% post_link "jupyter notebook 扩展开发之 Custom bundler extensions" %}
- {% post_link "jupyter notebook 扩展开发之  文件保存钩子" %}
- {% post_link "jupyter notebook扩展开发之前端插件开发" %}
- {% post_link "jupyter notebook 扩展开发之 将Jupyter扩展作为Python包分发" %}


转载请注明出处:http://mlln.cn 或者 http://jupyter.cn