---
title: jupyter notebook扩展开发之前端插件开发
date: 2018-03-31 20:19:18
tags: [jupyter, notebook]
---

这是jupyter notebook 插件开发的系列文档之一, 文章最末尾列出了这个系列的所有博客连接.

<!--more-->


这里描述了为Jupyter笔记本前端编写JavaScript插件的基本步骤。这允许您自定义各种页面的行为，如仪表板，笔记本或文本编辑器。

### 前端插件的结构

>  注意: 笔记本前端和Javascript API不稳定，并且会受到很多变化。为当前笔记本电脑写的任何扩展程序几乎都无法保证在下一个版本兼容。

前端扩展是一个JavaScript文件，它定义了一个AMD模块，该模块至少公开了一个名为load_ipython_extension的函数，该函数不带任何参数。我们不会深入讨论每个术语的细节，但这里是工作扩展所需的最少代码：

```js
// file my_extension/main.js

define(function(){

    function load_ipython_extension(){
        console.info('this is my first extension');
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
```

如果您熟悉JavaScript，则可以使用此模板来调用任何Jupyter模块并修改其配置，或者在客户端JavaScript中执行其他任何操作。您的扩展程序将在笔记本页面初始化期间的正确加载，以便为页面可触发的各种事件设置侦听程序。

您可能需要访问页面上各种Jupyter笔记本组件的对象，而不是模块中定义的类。当前实例由名为`base / js / namespace`的模块所暴露。如果您打算访问页面上的实例，则应该要求使用此模块，而不是访问将来将被删除的全局变量Jupyter。以下示例演示如何访问当前笔记本实例：

```js
// file my_extension/main.js

define([
    'base/js/namespace'
], function(
    Jupyter
) {
    function load_ipython_extension() {
        console.log(
            'This is the current notebook application instance:',
            Jupyter.notebook
        );
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
```

### 修改快捷键


插件的功能之一是修改热键绑定，但是这又是一个不能保证稳定的API。但是，自定义热键经常被用到，并且有助于增加用户友好度，因此在下面我们将演示如何设置他们。

下面是一个扩展的例子，它将在命令模式下取消绑定快捷键0,0，这通常会重新启动内核，并在其位置绑定0,0,0：

```js
// file my_extension/main.js

define([
    'base/js/namespace'
], function(
    Jupyter
) {

    function load_ipython_extension() {
        // 删除热键
        Jupyter.keyboard_manager.command_shortcuts.remove_shortcut('0,0');
        // 添加热键
        Jupyter.keyboard_manager.command_shortcuts.add_shortcut('0,0,0', 'jupyter-notebook:restart-kernel');
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
```

> 标准键盘绑定可能无法在非美式键盘上正常工作。不幸的是，这是浏览器实现的局限性，以及一般网络上键盘事件处理的状态。


你可以看到我使用了action(动作/操作)名称`jupyter-notebook：restart-kernel`来绑定新的快捷方式。目前还没有API可以访问所有可用action的列表，尽管在笔记本页面的浏览器的JavaScript控制台中的以下内容应该让您了解可用的action:

```js
Object.keys(require('base/js/namespace').actions._actions);
```

### 定义和注册您自己的action(动作/操作)

作为前端扩展的一部分，您可能希望定义可附加到工具栏按钮的动作，或从命令选项板调用动作。下面是一个扩展示例，它定义了一个（不是非常有用的）动作来显示警告信息，并使用完整的动作名称添加了toolabr按钮：

```js
// file my_extension/main.js

define([
    'base/js/namespace'
], function(
    Jupyter
) {
    function load_ipython_extension() {

        var handler = function () {
            alert('this is an alert from my_extension!');
        };

        var action = {
            icon: 'fa-comment-o', // a font-awesome class used on buttons, etc
            help    : 'Show an alert',
            help_index : 'zz',
            handler : handler
        };
        var prefix = 'my_extension';
        var action_name = 'show-alert';

        var full_action_name = Jupyter.actions.register(action, action_name, prefix); // returns 'my_extension:show-alert'
        Jupyter.toolbar.add_buttons_group([full_action_name]);
    }

    return {
        load_ipython_extension: load_ipython_extension
    };
});
```

每个动作都需要一个名字，当与其前缀连接起来形成完整的动作名称时，该名称应该是唯一的。内置的操作，如jupyter-notebook：在先前的Modifying Key绑定示例中绑定的重新启动内核，使用前缀jupyter-notebook。对于扩展中定义的操作，使用扩展名称作为前缀是有意义的。对于动作名称，应考虑以下准则：


- 首先为动作选择一个名词和动词。例如，如果操作是“重新启动内核”，则动词是“restart”，名词是“kernel”。
- 默认情况下省略“selected”和“active”等术语，因此“delete-cell”而不是“delete-selected-cell”。如果它不是默认的“selected”或“active”范围，则只提供一个范围如“-all-”。
- 如果某个操作具有第二部操作，请将第二步操作与`-and-`分开，这样`restart-kernel-and-clear-output`。
- 使用` above/below`或`previous/next`来指示空间和顺序关系。
- 不要使用`before/after `，因为它们具有在空间环境中使用时容易混淆的时间内涵。
- 对于对话框，请使用指示对话框将完成的动作，如“confirm-restart-kernel”。

### 安装和启用扩展

您可以使用以下命令来安装nbextension：

```sh
jupyter nbextension install path/to/my_extension/ [--user|--sys-prefix]
```



默认安装是系统范围的。您可以使用--user来执行每个用户的安装，或者使用--sys-prefix来安装到Python的前缀（例如，在虚拟或conda环境中）。 my_extension是包含Javascript文件的目录。这会将其复制到Jupyter数据目录（确切位置取决于操作系统/平台 - 请参阅[Data Files](https://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html#jupyter-path)）。

如果插件正在开发中, 还没发布，您可以使用`--symlink`标志来链接您的扩展，而不是复制它，这样不需要在更改后重新安装。

要使用你的扩展，你还需要启用它，它告诉笔记本接口加载它。你可以用另一个命令来做到这一点：

`jupyter nbextension enable my_extension/main [--sys-prefix]`

该参数引用包含您的load_ipython_extension函数的Javascript模块，在本例中为`my_extension / main.js`。有一个相应的禁用命令来停止使用扩展程序而不卸载它。

在版本4.2中进行了更改：添加了`--sys-prefix`参数

### 内核特定的扩展


### jupyter notebook 扩展开发系列:

- {% post_link "jupyter notebook 扩展开发之自定义请求处理程序" %}
- {% post_link "jupyter notebook 扩展开发之内容API" %}
- {% post_link "jupyter notebook 扩展开发之 Custom bundler extensions" %}
- {% post_link "jupyter notebook 扩展开发之  文件保存钩子" %}
- {% post_link "jupyter notebook扩展开发之前端插件开发" %}
- {% post_link "jupyter notebook 扩展开发之 将Jupyter扩展作为Python包分发" %}


转载请注明出处:http://mlln.cn 或者 http://jupyter.cn