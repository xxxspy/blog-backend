
---

title: python解析JavaScript生成语法树并修改之
date: 2019-06-29 12:44:03
tags: [javascript, python, js2py, ast]

---

本篇文章介绍了使用python解析JavaScript形成语法树(AST), 并且修改AST, 然后生成新js代码的过程。

<!-- more -->

### 前提

最近要做一个项目, 需要逆向破解前端的js代码, 但是js代码往往经过混淆而完全丧失可读性, 所以我想到一个办法就是通过解析js代码生成AST(抽象语法树), 然后通过简化AST来重新生成简化后的代码, 这样就在很大程度上降低了我们破解的难度, 但是并不是完全没有难度, 因为很多代码还是无法优化的。

### 内容简介

Esprima是一个Javascript解析器，即它生成一个嵌套对象AST，以比以人为中心的代码更容易处理的方式表示代码结构。
Escodegen是一个代码生成器，可以获取Esprima生成的对象并将其转换回Javascript代码。

这两个模块都是nodejs模块, 也就是你需要在node中使用他们。但是有人开发了js2py的python模块, 可以帮助我们在python中调用nodejs模块。所以, 我今天这篇文章就介绍一下python中使用Esprima生成js的语法树, 并通过修改语法树来修改js代码, 最后通过Escodegen生成js代码。

### 安装js2py模块


```python
!pip install js2py
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
Collecting js2py
  Using cached https://files.pythonhosted.org/packages/25/2f/b184437870d15cdcc1cc52b73f1f7d6bb9ab2062d93c6a0b205ce8f323d3/Js2Py-0.66.tar.gz
Collecting tzlocal>=1.2 (from js2py)
  Using cached https://files.pythonhosted.org/packages/cb/89/e3687d3ed99bc882793f82634e9824e62499fdfdc4b1ae39e211c5b05017/tzlocal-1.5.1.tar.gz
Requirement already satisfied: six>=1.10 in d:\venv\.common\lib\site-packages (from js2py) (1.12.0)
Collecting pyjsparser>=2.5.1 (from js2py)
  Using cached https://files.pythonhosted.org/packages/48/ef/c72abcfa2c6accd03e7c89c400790fc3d908c5804d50a7c4e9ceabd74d23/pyjsparser-2.7.1.tar.gz
Requirement already satisfied: pytz in d:\venv\.common\lib\site-packages (from tzlocal>=1.2->js2py) (2018.9)
Building wheels for collected packages: js2py, tzlocal, pyjsparser
  Building wheel for js2py (setup.py): started
  Building wheel for js2py (setup.py): finished with status 'done'
  Stored in directory: C:\Users\syd\AppData\Local\pip\Cache\wheels\d8\8d\3f\f8a103f421ae0ffe199aee63f2659bf62d23df22d9c620582b
  Building wheel for tzlocal (setup.py): started
  Building wheel for tzlocal (setup.py): finished with status 'done'
  Stored in directory: C:\Users\syd\AppData\Local\pip\Cache\wheels\15\ae\df\a67bf1ed84e9bf230187d36d8dcfd30072bea0236cb059ed91
  Building wheel for pyjsparser (setup.py): started
  Building wheel for pyjsparser (setup.py): finished with status 'done'
  Stored in directory: C:\Users\syd\AppData\Local\pip\Cache\wheels\a2\73\e6\3e433f3fd78257c3f971baf8cc9001cc0c4797268c61751e89
Successfully built js2py tzlocal pyjsparser
Installing collected packages: tzlocal, pyjsparser, js2py
Successfully installed js2py-0.66 pyjsparser-2.7.1 tzlocal-1.5.1

</div>
{% endraw %}

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
You are using pip version 19.0.3, however version 19.1.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

</div>
{% endraw %}

### 快速入门

js2py可以使用'require'方法加载所需的nodejs模块, 调用模块的时候, 就跟python模块的调用一样简单:


```python
import js2py

esprima = js2py.require('esprima')
escodegen = js2py.require('escodegen')

print(esprima)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
{'Syntax': {'ArrayExpression': 'ArrayExpression', 'ArrayPattern': 'ArrayPattern', 'ArrowFunctionExpression': 'ArrowFunctionExpression', 'AssignmentExpression': 'AssignmentExpression', 'AssignmentPattern': 'AssignmentPattern', 'AwaitExpression': 'AwaitExpression', 'BinaryExpression': 'BinaryExpression', 'BlockStatement': 'BlockStatement', 'BreakStatement': 'BreakStatement', 'CallExpression': 'CallExpression', 'CatchClause': 'CatchClause', 'ClassBody': 'ClassBody', 'ClassDeclaration': 'ClassDeclaration', 'ClassExpression': 'ClassExpression', 'ConditionalExpression': 'ConditionalExpression', 'ContinueStatement': 'ContinueStatement', 'DebuggerStatement': 'DebuggerStatement', 'DoWhileStatement': 'DoWhileStatement', 'EmptyStatement': 'EmptyStatement', 'ExportAllDeclaration': 'ExportAllDeclaration', 'ExportDefaultDeclaration': 'ExportDefaultDeclaration', 'ExportNamedDeclaration': 'ExportNamedDeclaration', 'ExportSpecifier': 'ExportSpecifier', 'ExpressionStatement': 'ExpressionStatement', 'ForInStatement': 'ForInStatement', 'ForOfStatement': 'ForOfStatement', 'ForStatement': 'ForStatement', 'FunctionDeclaration': 'FunctionDeclaration', 'FunctionExpression': 'FunctionExpression', 'Identifier': 'Identifier', 'IfStatement': 'IfStatement', 'ImportDeclaration': 'ImportDeclaration', 'ImportDefaultSpecifier': 'ImportDefaultSpecifier', 'ImportNamespaceSpecifier': 'ImportNamespaceSpecifier', 'ImportSpecifier': 'ImportSpecifier', 'LabeledStatement': 'LabeledStatement', 'Literal': 'Literal', 'LogicalExpression': 'LogicalExpression', 'MemberExpression': 'MemberExpression', 'MetaProperty': 'MetaProperty', 'MethodDefinition': 'MethodDefinition', 'NewExpression': 'NewExpression', 'ObjectExpression': 'ObjectExpression', 'ObjectPattern': 'ObjectPattern', 'Program': 'Program', 'Property': 'Property', 'RestElement': 'RestElement', 'ReturnStatement': 'ReturnStatement', 'SequenceExpression': 'SequenceExpression', 'SpreadElement': 'SpreadElement', 'Super': 'Super', 'SwitchCase': 'SwitchCase', 'SwitchStatement': 'SwitchStatement', 'TaggedTemplateExpression': 'TaggedTemplateExpression', 'TemplateElement': 'TemplateElement', 'TemplateLiteral': 'TemplateLiteral', 'ThisExpression': 'ThisExpression', 'ThrowStatement': 'ThrowStatement', 'TryStatement': 'TryStatement', 'UnaryExpression': 'UnaryExpression', 'UpdateExpression': 'UpdateExpression', 'VariableDeclaration': 'VariableDeclaration', 'VariableDeclarator': 'VariableDeclarator', 'WhileStatement': 'WhileStatement', 'WithStatement': 'WithStatement', 'YieldExpression': 'YieldExpression'}, 'parse': 'function parse(code, options, delegate) { [python code] }', 'parseModule': 'function parseModule(code, options, delegate) { [python code] }', 'parseScript': 'function parseScript(code, options, delegate) { [python code] }', 'tokenize': 'function tokenize(code, options, delegate) { [python code] }', 'version': '4.0.1'}

</div>
{% endraw %}

先来看下一个简单的js代码是如何被解析成AST的:


```python
esprima.parse('console.log("helloworld")')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    {'body': [{'expression': {'arguments': [{'raw': '"helloworld"', 'type': 'Literal', 'value': 'helloworld'}], 'callee': {'computed': False, 'object': {'name': 'console', 'type': 'Identifier'}, 'property': {'name': 'log', 'type': 'Identifier'}, 'type': 'MemberExpression'}, 'type': 'CallExpression'}, 'type': 'ExpressionStatement'}], 'sourceType': 'script', 'type': 'Program'}

</div>
{% endraw %}



它非常冗长，但我们现在可以更轻松地迭代指令。

上面的输出结果有些混乱, 我们最好使用json模块格式化一下:


```python
import json


tree = esprima.parse('console.log("helloworld")')

print(json.dumps(tree.to_dict(), indent=4))
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
{
    "body": [
        {
            "expression": {
                "arguments": [
                    {
                        "raw": "\"helloworld\"",
                        "type": "Literal",
                        "value": "helloworld"
                    }
                ],
                "callee": {
                    "computed": false,
                    "object": {
                        "name": "console",
                        "type": "Identifier"
                    },
                    "property": {
                        "name": "log",
                        "type": "Identifier"
                    },
                    "type": "MemberExpression"
                },
                "type": "CallExpression"
            },
            "type": "ExpressionStatement"
        }
    ],
    "sourceType": "script",
    "type": "Program"
}

</div>
{% endraw %}

关于如何读懂AST, 你需要参考esprima的官方文档, 我这里就不多废话了, 直接上链接: https://esprima.readthedocs.io/en/3.1/index.html

### 使用 Escodegen生成代码

得到了AST, 可以根据AST生成js代码:


```python
escodegen.generate(tree)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    "console.log('helloworld');"

</div>
{% endraw %}



### 注入代码

要注入代码，我们在将AST传递给Escodegen之前修改它。

我们可以避免必须直接处理解析树，方法是将我们想要注入的代码传递给esprima.parse, 生成一个tree的片段，然后再将其添加到解析树中：


```python
parsed = esprima.parse('console.log("Hello world!")')
parsed.body.unshift(esprima.parse('console.log("begin")'))
parsed.body.push(esprima.parse('console.log("end")'))
newcode = escodegen.generate(parsed)
print(newcode)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
console.log('begin');
console.log('Hello world!');
console.log('end');

</div>
{% endraw %}

### JavaScript转换成Python代码

当然作为js2py的功能之一, 它还可以将js代码转换成python代码, 但是生成的python代码可读性较差, 我感觉没有太大用处:


```python
print(js2py.translate_js(newcode))
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
var.get('console').callprop('log', Js('begin'))
var.get('console').callprop('log', Js('Hello world!'))
var.get('console').callprop('log', Js('end'))
pass


</div>
{% endraw %}

### 在python中js代码

既然能将js转换成python, 就能在python中运行js, 而使用js2py就很简单:


```python
js2py.eval_js(newcode)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
'begin'
'Hello world!'
'end'

</div>
{% endraw %}

### 总结

这篇文章比较简单, 就是介绍了js2py的一些简单功能, 后面的文章我会使用js2py进行JavaScript代码的精简, 也就是JavaScript的逆向开发, 以便读懂前端混淆的代码。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python解析JavaScript生成语法树并修改之.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
