---
title: jupyter notebook 扩展开发之自定义请求处理程序
date: 2018-03-31 20:19:18
tags: [jupyter, notebook]
---

这是jupyter notebook 插件开发的系列文档之一, 文章最末尾列出了这个系列的所有博客连接.

<!--more-->

## 自定义request(请求)处理程序

笔记本Web服务器可以使用定义良好的RESTful API进行交互。除了笔记本提供的接口之外，您还可以定义自定义请求处理程序。如下所述，要自定义处理程序，您需要先创建一个笔记本服务器扩展。然后，在扩展中，您可以注册自定义处理程序。


### 编写笔记本服务器扩展

笔记本网络服务器是用Python编写的，因此您的服务器扩展应该也是用Python编写的。服务器扩展，如IPython扩展，是定义了一个特殊的加载函数`load_jupyter_server_extension`的Python模块。该功能在扩展程序加载时调用。

```py
def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    pass
```

要让笔记本服务器加载自定义扩展，您需要将其添加到要加载的扩展列表中。你可以使用配置系统来做到这一点。` NotebookApp.nbserver_extensions`是一个配置变量，它是一个字符串字典(每个字符串代表需要导入的Python模块)，映射为True表示启用或False来禁用每个扩展。因为这个变量是笔记本配置，所以你可以用两种不同的方式设置它，使用配置文件或者通过命令行。


例如，要通过命令行加载您的扩展，请在变量名前添加一个双破折号，并将Python字典放在双引号中。如果你的包是“mypackage”，而模块是“mymodule”，这看起来像`jupyter notebook --NotebookApp.nbserver_extensions="{'mypackage.mymodule':True}"`. 这个字符串应该是Python可导入的。


或者，您可以通过在Jupyter配置文件中设置变量来加载您的扩展，而不考虑命令行参数。 Jupyter配置文件的默认位置是`~/.jupyter/jupyter_notebook_config.py`. (see [Configuration Overview](http://jupyter-notebook.readthedocs.io/en/stable/config_overview.html) ).在配置文件里面，你可以使用Python来设置变量。例如，以下配置与前面的命令行示例相同:

```py
c = get_config()
c.NotebookApp.nbserver_extensions = {
    'mypackage.mymodule': True,
}
```


在继续之前，确认您的扩展程序已经加载是一个好主意。使用打印语句打印独特的东西。启动笔记本服务器，您应该看到您的语句打印到控制台。

### 注册自定义处理程序


一旦定义了服务器扩展，您可以注册自定义请求处理程序，因为您拥有Notebook服务器应用程序实例（上面的nb_server_app）的句柄。但是，您首先需要定义您的自定义处理程序。要声明请求处理程序，请从`notebook.base.handlers.IPythonHandler`继承。下面的例子是一个Hello World处理程序：

```py
from notebook.base.handlers import IPythonHandler

class HelloWorldHandler(IPythonHandler):
    def get(self):
        self.finish('Hello, world!')
```

Jupyter Notebook服务器使用Tornado作为其Web框架。有关如何实现请求处理程序的更多信息，请参阅关于此问题的Tornado文档。

定义处理程序后，您需要在Notebook服务器上注册处理程序。看下面的例子:


将它与以上代码放在一起，该示例如下所示：

```python
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler

class HelloWorldHandler(IPythonHandler):
    def get(self):
        self.finish('Hello, world!')

def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/hello')
    web_app.add_handlers(host_pattern, [(route_pattern, HelloWorldHandler)])
```

### jupyter notebook 扩展开发系列:

- {% post_link "jupyter notebook 扩展开发之自定义请求处理程序" %}
- {% post_link "jupyter notebook 扩展开发之内容API" %}
- {% post_link "jupyter notebook 扩展开发之 Custom bundler extensions" %}
- {% post_link "jupyter notebook 扩展开发之  文件保存钩子" %}
- {% post_link "jupyter notebook扩展开发之前端插件开发" %}
- {% post_link "jupyter notebook 扩展开发之 将Jupyter扩展作为Python包分发" %}




转载请注明出处:http://mlln.cn 或者 http://jupyter.cn