
---

title: 如何在jupyter notebook中运行javascript和HTML代码
date: 2020-03-26 12:44:03
tags: [javascript, notebook]

---

作为一个博客主, 很多时候我们会用到jupyter notebook作为自己的博客撰写编辑器, 我们可能会遇到一个问题, 如何在notebook中运行JavaScript代码呢?

其实很简单, 用到了notebook中内置的魔法。

<!--more-->

<!--toc-->

### 列出魔法

如果你想要查看所有魔法你可以使用下面的命令:


```python
%lsmagic
```




{% raw %}
<div class="output">
输出(plain):<br/>

    Available line magics:
    <br />%alias  %alias_magic  %autoawait  %autocall  %automagic  %autosave  %bookmark  %cd  %clear  %cls  %colors  %config  %connect_info  %copy  %ddir  %debug  %dhist  %dirs  %doctest_mode  %echo  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %macro  %magic  %matplotlib  %mkdir  %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %popd  %pprint  %precision  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %ren  %rep  %rerun  %reset  %reset_selective  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
    <br />
    <br />Available cell magics:
    <br />%%!  %%HTML  %%SVG  %%bash  %%capture  %%cmd  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
    <br />
    <br />Automagic is ON, % prefix IS NOT needed for line magics.

</div>
{% endraw %}



上面的命令在notebook中运行就会列出所有的魔法, 如果你仔细查找会找到HTML和JavaScript魔法, 他们就是我们想要的。

### HTML代码

下面我们来写一个简单的HTML代码:(运行以后就会直接将html代码渲染成一个文件选择组件)


```python
%%HTML

<input id="file" type="file">
```


{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>

<input id="file" type="file">

</div>
{% endraw %}


### JavaScript代码

下面我们使用魔法"%%javascript"来运行js代码:


```javascript
%%javascript

$('#file').change(function(e){
       element.text(e.target.files[0].name)
})
```


{% raw %}
<div class="output">
输出(plain):<br/>

    <IPython.core.display.Javascript object>

</div>
{% endraw %}


运行了上面的代码以后, 我们点击上面的选择文件按钮就可以实时输出文件名称。

### 引入JavaScript第三方库

有时候我们需要用到其他js库, 引入js库到notebook的方法也很简单, 只需要用到HTML魔法, 比如:


```python
%%HTML

<script src="https://cdn.bootcss.com/xlsx/0.15.6/xlsx.full.min.js"></script>
```


{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>

<script src="https://cdn.bootcss.com/xlsx/0.15.6/xlsx.full.min.js"></script>

</div>
{% endraw %}


上面的库用于读取和写入excel数据的工具, 引入以上工具以后, 我们可以就可以得到一个新的对象"XLSX", 下面测试一下:如果下面的代码没有提示错误, 并成功弹出警示框, 说明你的XLSX已经引入成功了!!


```javascript
%%javascript

alert(XLSX)
```


{% raw %}
<div class="output">
输出(plain):<br/>

    <IPython.core.display.Javascript object>

</div>
{% endraw %}



> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](如何在jupyter-notebook中运行javascript和HTML代码.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
