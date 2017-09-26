---
title: gitignore配置详解
date: 2015-07-17 18:01:11
tags: []
author: mlln.cn
---
如果你使用git来管理代码版本，你必须懂得如何使用.gitignore文件，该文件可以指定git忽略哪些文件，在git中的作用非常重要。在理解gitignore的配置之前，我们要先看看这些规则都可以来自哪里。通常git可以从多个地方获取忽略规则，优先级从上到下依次为：

- .gitignore文件适合写于项目有关的规则，并且这些规则需要与合作者分享。

- `$GIT_DIR/info/exclude`适用于与项目有关，但是你不想分享给其他作者，这些规则可能只适用于你自己。

- `core.excludesFile`适用于你在任何情况下都需要忽略的规则。这种情况不常用。

- 空行不匹配任何文件，所以空行通常是规则分组的分隔符，只是在视觉上将不同的规则分组。

{% asset_img 21e5582309f790527c5640f005f3d7ca7acbd570.jpg gitignore配置详解 %}

- 以`#`开始的行代表注释，所以也不匹配任何文件。

{% asset_img 73ca5910b912c8fcb345f103f5039245d788210e.jpg gitignore配置详解 %}

- 末尾的空格没有任何意义，如果你想匹配空格，你需要在空格前加转义字符``。

- 例如：`a `这种写法可以匹配`a `

{% asset_img d7c9ca3f8794a4c20583e0e507f41bd5ac6e3918.jpg gitignore配置详解 %}

- 感叹号`!`的作用是从已有的忽略规则里排除一部分文件。注意想要让感叹号起作用，必须在前规则中使用通配符`*`。例如：

- 前规则写成：`.env/*`

- 想要追踪`.env`文件夹下的`data.txt`，需要追加一个规则：`!.env/data.txt`

- 如果前规则写成`.env`，则`!.env/data.txt`不起作用。

- 如果规则以`/`结尾，则表示匹配文件夹, 类似的文件和链接都不会匹配。

{% asset_img 4bd1e803738da977974181e5b951f8198718e357.jpg gitignore配置详解 %}

- 如果规则中不包含`/`，则规则即可匹配文件夹也可以匹配文件和链接，类似于linux shell中的通配符，可以匹配任何可以与通配符匹配的路径。

{% asset_img ae8267310a55b31949fc85bb4aa98226cefc17b3.jpg gitignore配置详解 %}

- 通配符无法匹配符号`/`，所以类似这样的规则`foo/*.html`不能匹配`foo/bar/test.html`。

{% asset_img 61183b2dd42a2834ceef31c552b5c9ea14cebf70.jpg gitignore配置详解 %}

- 规则以`/`开头表示匹配`.gitignore`文件所在的目录。也就是说规则`/*.txt`只能匹配.gitignore所在目录下的所有txt文件，不能匹配其他目录下的txt文件。

{% asset_img dc854fda81cb39db37766098d9160924aa18300e.jpg gitignore配置详解 %}

- 以`**/`开头的规则表示匹配所有文件夹，规则`**/a/b`能匹配`foo/a/b`也能匹配`foo/bar/a/b`

- 以`/**`结尾的规则表示匹配目录下所有文件和文件夹，规则`a/b/**`能匹配`/a/b/c`也能匹配`a/b/c/d/e`

- 规则中间包含`/**/`表示匹配任意路径，比如规则`a/**/b`可以匹配`a/foo/bar/b`和`a/e/m/c/b`。

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
