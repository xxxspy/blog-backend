---
title: 测试d3.js在hexo博客中的效果
date: 2017-06-11 08:12:09
tags: [hexo, d3js]
d3js: true
---

d3.js可以在hexo博客中使用，如下图所示。但是有一些坑需要你提前知道如何填。

#### json数据

d3经常需要用到json格式的数据文件，如果放在代码里不太好，加载js的时候比较慢，
所以通常我们都是用`d3.json`方法，它需要你准备一个可被调用的json文件。
那么，我的做法是，在文章（post）的同名资源文件夹中加入json文件，但是我遇到一个问题，
就是json文件会被hexo当做一篇post给渲染，导致你的网站中会出现一篇无名的文章，
内容就是json文件的内容。你可能想到在`_config.yml`中配置`skip_render`，但是，
这个选项还有一些bug，我也懒得去改，这么做并不能防止生成一篇莫名文章。
我想到没有后缀名的文件是不会被渲染的，所以我就把json文件的后缀名给去掉，这样就可以了。

#### 代码

hexo中想要嵌入到文章中的代码通常写在`{ raw }your html code{ endraw }`中(标签中百分号没写)，
我也是这么做的。但是你一定要注意，文章不仅会出现在文章页面，还可能会出现在index(home)页，
这就麻烦了，因为你的JavaScript很可能影响到首页。如果你加载太多JavaScript库，还会导致首页加载速度过慢，
如果你在意用户体验或者SEO，你就需要注意这点。

我的方法是在文章开始输入一个配置变量，这是我这篇文章的配置：

```
---
title: 测试d3.js在hexo博客中的效果
date: 2017-06-11 08:12:09
tags: [hexo, d3js]
d3js: true
---
```

你可以看到d3js这个变量。但是它还不能发挥作用，因为我们还得修改网站的模板。让模板侦测该变量，
如果为true就加载d3.js这个库。所以我们先增加一个partial文件，在主题文件夹下`layout/_partial/d3js.ejs`：

```
<script src="https://d3js.org/d3.v4.min.js"></script>
```

然后再修改`head.ejs`, 增加如下代码：

```javascript
    <% if(page.d3js){ %>
        <!-- d3js -->
        <%- partial('d3js') %>
    <% } %>
```

到此，我们已经成功了一半了（怎么还有一半？）

#### 探测d3是否加载

在写post的时候，你如果直接用d3这个变量，会引发错误，因为在index页面我们不允许加载d3，但是文章出现在首页的时候，
错误就发生了，告诉你d3是undefined。所以在使用d3前，你需要判断d3是否为undefined。你可以用in操作符即可：

```javascript
if("d3" in window){
    // code to run
} 
```


#### 代码

OK, 是时候让你看到我文章中写的全部代码了，而代码的运行效果就是下图。

```html

<div id="d3js-example-content">
    这里是文章自定义内容，你需要进入该文章才能看到。
</div>  
<style>

# input-button {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  position: relative;
  left: 10px;
  top: 10px;
}

</style>

<script>

if ('d3' in window){
    var html=''
    var contentDiv=document.getElementById("d3js-example-content");
    contentDiv.innerHTML='<canvas width="960" height="600"></canvas>' +
                            '<label id="input-button"><input style="width:240px;" type="range" min="0" max="1" step="any" value="0.5">'+
                            ' Link Strength</label>';

    var canvas = document.querySelector("canvas"),
        context = canvas.getContext("2d"),
        width = canvas.width,
        height = canvas.height;

    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) { return d.id; }).strength(0.5))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2))
        // .alphaDecay(0);

    d3.select("input[type=range]")
        .on("input", inputted);

    d3.json("miserables", function(error, graph) {
      if (error) throw error;

      simulation
          .nodes(graph.nodes)
          .on("tick", ticked);

      simulation.force("link")
          .links(graph.links);

      function ticked() {
        context.clearRect(0, 0, width, height);

        context.beginPath();
        graph.links.forEach(drawLink);
        context.strokeStyle = "#aaa";
        context.stroke();

        context.beginPath();
        graph.nodes.forEach(drawNode);
        context.fill();
        context.strokeStyle = "#fff";
        context.stroke();
      }
    });

    function inputted() {
      simulation.force("link").strength(+this.value);
      simulation.alpha(1).restart();
    }

    function drawLink(d) {
      context.moveTo(d.source.x, d.source.y);
      context.lineTo(d.target.x, d.target.y);
    }

    function drawNode(d) {
      context.moveTo(d.x + 3, d.y);
      context.arc(d.x, d.y, 3, 0, 2 * Math.PI);
    }




}


</script>
```



{% raw %}

<div id="d3js-example-content">
    这是特殊内容，你需要进入该文章才能看到。
</div>  

<style>

# input-button {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  position: relative;
  left: 10px;
  top: 10px;
}

</style>

<script>

if ('d3' in window){
    var html=''
    var contentDiv=document.getElementById("d3js-example-content");
    contentDiv.innerHTML='<canvas width="960" height="600"></canvas>' +
                            '<label id="input-button"><input style="width:240px;" type="range" min="0" max="1" step="any" value="0.5">'+
                            ' Link Strength</label>';

    var canvas = document.querySelector("canvas"),
        context = canvas.getContext("2d"),
        width = canvas.width,
        height = canvas.height;

    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) { return d.id; }).strength(0.5))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2))
        // .alphaDecay(0);

    d3.select("input[type=range]")
        .on("input", inputted);

    d3.json("miserables", function(error, graph) {
      if (error) throw error;

      simulation
          .nodes(graph.nodes)
          .on("tick", ticked);

      simulation.force("link")
          .links(graph.links);

      function ticked() {
        context.clearRect(0, 0, width, height);

        context.beginPath();
        graph.links.forEach(drawLink);
        context.strokeStyle = "#aaa";
        context.stroke();

        context.beginPath();
        graph.nodes.forEach(drawNode);
        context.fill();
        context.strokeStyle = "#fff";
        context.stroke();
      }
    });

    function inputted() {
      simulation.force("link").strength(+this.value);
      simulation.alpha(1).restart();
    }

    function drawLink(d) {
      context.moveTo(d.source.x, d.source.y);
      context.lineTo(d.target.x, d.target.y);
    }

    function drawNode(d) {
      context.moveTo(d.x + 3, d.y);
      context.arc(d.x, d.y, 3, 0, 2 * Math.PI);
    }




}


</script>
{% endraw %}

