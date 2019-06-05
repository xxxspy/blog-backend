---
title: jupyter notebook 扩展开发之内容API
date: 2018-03-31 20:19:18
tags: [jupyter, notebook]
---

这是jupyter notebook 插件开发的系列文档之一, 文章最末尾列出了这个系列的所有博客连接.

<!--more-->



什么是内容API
======

Jupyter Notebook Web应用程序提供了一个用于在虚拟文件系统中创建/打开/重命名和删除文件的图形界面。

ContentsManager类定义了一个抽象API，用于将这些交互转换为特定存储介质上的操作。默认的FileContentsManager使用服务器的本地文件系统进行存储，并直接将笔记本序列化为JSON。用户可以通过提供ContentsManager的自定义子类来覆盖这些行为。

本节介绍ContentsManager子类实现的接口。我们把这个接口称为Contents API。

数据模型
----------

#### 文件系统实体

ContentsManager将虚拟文件系统实体表示为字典，我们称之为**模型**。

模型可能包含以下条目：

<div class="wy-table-responsive"><table border="1" class="docutils">
<colgroup>
<col width="33%">
<col width="18%">
<col width="49%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Key</th>
<th class="head">Type</th>
<th class="head">Info</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><strong>name</strong></td>
<td>unicode</td>
<td>Basename of the entity.</td>
</tr>
<tr class="row-odd"><td><strong>path</strong></td>
<td>unicode</td>
<td>Full
(<a class="reference internal" href="#apipaths"><span class="std std-ref">API-style</span></a>)
path to the entity.</td>
</tr>
<tr class="row-even"><td><strong>type</strong></td>
<td>unicode</td>
<td>The entity type. One of
<code class="docutils literal notranslate"><span class="pre">"notebook"</span></code>, <code class="docutils literal notranslate"><span class="pre">"file"</span></code> or
<code class="docutils literal notranslate"><span class="pre">"directory"</span></code>.</td>
</tr>
<tr class="row-odd"><td><strong>created</strong></td>
<td>datetime</td>
<td>Creation date of the entity.</td>
</tr>
<tr class="row-even"><td><strong>last_modified</strong></td>
<td>datetime</td>
<td>Last modified date of the
entity.</td>
</tr>
<tr class="row-odd"><td><strong>content</strong></td>
<td>variable</td>
<td>The “content” of the entity.
(<a class="reference internal" href="#modelcontent"><span class="std std-ref">See
Below</span></a>)</td>
</tr>
<tr class="row-even"><td><strong>mimetype</strong></td>
<td>unicode or
<code class="docutils literal notranslate"><span class="pre">None</span></code></td>
<td>The mimetype of <code class="docutils literal notranslate"><span class="pre">content</span></code>,
if any.  (<a class="reference internal" href="#modelcontent"><span class="std std-ref">See
Below</span></a>)</td>
</tr>
<tr class="row-odd"><td><strong>format</strong></td>
<td>unicode or
<code class="docutils literal notranslate"><span class="pre">None</span></code></td>
<td>The format of <code class="docutils literal notranslate"><span class="pre">content</span></code>,
if any. (<a class="reference internal" href="#modelcontent"><span class="std std-ref">See
Below</span></a>)</td>
</tr>
</tbody>
</table></div>


根据模型的类型字段，某些模型字段在结构上会有所不同。有三种模型类型：笔记本，文件和目录。

      
- ``notebook`` models
     - ```format```字段总是``json``。
     - ``mimetype``字段总是``None``。
     - ``content``字段包含一个:class:`nbformat.notebooknode.NotebookNode` 代表.pynb文件的类. 请参阅 `NBFormat`文档描述。

- ``file`` models
     -  ``format``字段可以是 ``"text"`` or ``"base64"``.
     - 对于文本格式``mimetype``字段是``text/plain``, 
      base64格式是`application/octet-stream`。
     - ``content``”字段始终为``unicode``类型。对于文本格式
      文件模型，``content``只是解码后的文件字节
      作为UTF-8。非文本（``base64``）文件读取为字节，base64编码，
      然后解码为UTF-8。

- ``directory`` models
     - ``format`` 字段总是``json``。
     - ``mimetype``字段总是“None”。
     -  ``content``字段包含一个`content-free`模型列表, 
      表示目录中的实体的模型。
      
> 注意: 
在某些情况下，我们不需要实体的完整内容来完成内容API请求。在这种情况下，我们会忽略模型中的mimetype，content和format键。这在列出目录时最常出现，在这种情况下，我们将目录中的文件表示为无内容模型，以避免必须递归遍历并序列化整个文件系统。


#### 案例

```js
# Notebook Model with Content
{
    'content': {
        'metadata': {},
        'nbformat': 4,
        'nbformat_minor': 0,
        'cells': [
            {
                'cell_type': 'markdown',
                'metadata': {},
                'source': 'Some **Markdown**',
            },
        ],
    },
    'created': datetime(2015, 7, 25, 19, 50, 19, 19865),
    'format': 'json',
    'last_modified': datetime(2015, 7, 25, 19, 50, 19, 19865),
    'mimetype': None,
    'name': 'a.ipynb',
    'path': 'foo/a.ipynb',
    'type': 'notebook',
    'writable': True,
}

# Notebook Model without Content
{
    'content': None,
    'created': datetime.datetime(2015, 7, 25, 20, 17, 33, 271931),
    'format': None,
    'last_modified': datetime.datetime(2015, 7, 25, 20, 17, 33, 271931),
    'mimetype': None,
    'name': 'a.ipynb',
    'path': 'foo/a.ipynb',
    'type': 'notebook',
    'writable': True
}
```



### API path

ContentsManager将文件系统资源的位置表示为API样式的路径。这些路径被解释为相对于笔记本服务器的根目录。为了跨系统兼容，需要做出以下保证：

- 路径总是“unicode”，而不是“bytes”。
- 路径不是URL转义的。
- 路径始终是正斜杠（/）分隔，即使在Windows上也是如此。
- 前后斜杠被剥离。例如``/ foo / bar / buzz /``成为``foo / bar / buzz``。
- 空字符串（``""``）表示根目录。

### 编写一个自定义ContentsManager

默认的ContentsManager是为在个人计算机上运行笔记本作为应用程序的用户而设计的。它将笔记本作为.ipynb文件存储在本地文件系统中，并将Notebook UI中的文件和目录映射到磁盘上的文件和目录。通过实现ContentsManager的自定义子类，可以重写笔记本的存储方式。例如，如果您在不信任或无法访问笔记本服务器文件系统的环境中部署笔记本，则可以编写自己的ContentsManager，将笔记本和文件存储在数据库中。

#### Required Methods


自定义ContentsManager的最小完整实现必须实现以下方法：

<div class="wy-table-responsive"><table border="1" class="longtable docutils">
<colgroup>
<col width="10%">
<col width="90%">
</colgroup>
<tbody valign="top">
<tr class="row-odd"><td><code class="xref py py-obj docutils literal notranslate"><span class="pre">ContentsManager.get</span></code>(path[,&nbsp;content,&nbsp;type,&nbsp;…])</td>
<td>Get a file or directory model.</td>
</tr>
<tr class="row-even"><td><code class="xref py py-obj docutils literal notranslate"><span class="pre">ContentsManager.save</span></code>(model,&nbsp;path)</td>
<td>Save a file or directory model to path.</td>
</tr>
<tr class="row-odd"><td><code class="xref py py-obj docutils literal notranslate"><span class="pre">ContentsManager.delete_file</span></code>(path)</td>
<td>Delete the file or directory at path.</td>
</tr>
<tr class="row-even"><td><code class="xref py py-obj docutils literal notranslate"><span class="pre">ContentsManager.rename_file</span></code>(old_path,&nbsp;new_path)</td>
<td>Rename a file or directory.</td>
</tr>
<tr class="row-odd"><td><code class="xref py py-obj docutils literal notranslate"><span class="pre">ContentsManager.file_exists</span></code>([path])</td>
<td>Does a file exist at the given path?</td>
</tr>
<tr class="row-even"><td><code class="xref py py-obj docutils literal notranslate"><span class="pre">ContentsManager.dir_exists</span></code>(path)</td>
<td>Does a directory exist at the given path?</td>
</tr>
<tr class="row-odd"><td><code class="xref py py-obj docutils literal notranslate"><span class="pre">ContentsManager.is_hidden</span></code>(path)</td>
<td>Is path a hidden directory or file?</td>
</tr>
</tbody>
</table></div>



### jupyter notebook 扩展开发系列:

- {% post_link "jupyter notebook 扩展开发之自定义请求处理程序" %}
- {% post_link "jupyter notebook 扩展开发之内容API" %}
- {% post_link "jupyter notebook 扩展开发之 Custom bundler extensions" %}
- {% post_link "jupyter notebook 扩展开发之  文件保存钩子" %}
- {% post_link "jupyter notebook扩展开发之前端插件开发" %}
- {% post_link "jupyter notebook 扩展开发之 将Jupyter扩展作为Python包分发" %}


转载请注明出处:http://mlln.cn 或者 http://jupyter.cn