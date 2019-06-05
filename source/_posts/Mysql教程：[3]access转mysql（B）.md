---
title: Mysql教程：[3]access转mysql（B）
date: 2016-03-05 18:11:05
tags: [mysql]
author: mlln.cn
---
软件access2mysql下载： http://jingyan.baidu.com/article/4d58d541c993ab9dd5e9c010.html

- 首先，我们需要在mysql中创建一个数据库来保存我们即将要导入的access中的数据和表。从开始菜单进入mysql

{% asset_img 6c63514a20a446230a4a88289a22720e0df3d7bc.jpg Mysql教程：[3]access转mysql（B） %}

- 输入命令如图所示，创建一个表：liangbiao

{% asset_img 32bb9c8ba61ea8d38756594e950a304e241f58c0.jpg Mysql教程：[3]access转mysql（B） %}

- 接着我们打开access2mysql软件，然后点击source按钮

{% asset_img 38403f3fb80e7bec12f12fab2d2eb9389b506b15.jpg Mysql教程：[3]access转mysql（B） %}

- 设置数据源为access，如图所示

{% asset_img 7787b9efce1b9d16a8ecb62bf1deb48f8c546415.jpg Mysql教程：[3]access转mysql（B） %}

- 输入该数据库的密码，如果没有，可以空着

{% asset_img 1e71f724b899a901a808777c1f950a7b0208f578.jpg Mysql教程：[3]access转mysql（B） %}

- 通过浏览按钮，找到你要转的access文件

{% asset_img 8cf0d51349540923b5424f349058d109b3de4915.jpg Mysql教程：[3]access转mysql（B） %}

- 点击next按钮

{% asset_img 948bcfc8a786c917fd287e73cb3d70cf3bc75715.jpg Mysql教程：[3]access转mysql（B） %}

- 设置数据库为mysql，填写密码

{% asset_img b25d9901a18b87d6fa848655050828381e30fd73.jpg Mysql教程：[3]access转mysql（B） %}

- 点击test connection测试链接是否成功

{% asset_img 95afee1f3a292df5bf88815fbe315c6035a873f5.jpg Mysql教程：[3]access转mysql（B） %}

{% asset_img 7e7f7909c93d70cfbc8e8747fadcd100bba12bc0.jpg Mysql教程：[3]access转mysql（B） %}

- 输入我们刚才在mysql中建立的那个数据库名称liangbiao。点击next

{% asset_img d7c9ca3f8794a4c2e457ca610cf41bd5ac6e39c0.jpg Mysql教程：[3]access转mysql（B） %}

- 这个界面显示了access中所有的表，你可以选择自己需要的表，不需要的可以不转，这样可以提高速度

{% asset_img 966aca0735fae6cdd0c0862b0db30f2443a70fc0.jpg Mysql教程：[3]access转mysql（B） %}

- 点击提交按钮，开始转换

{% asset_img c87c6ecf3bc79f3d71aac97ab8a1cd11738b29f5.jpg Mysql教程：[3]access转mysql（B） %}

- 来到mysql，在这里，我们先切换到liangbiao这个数据库，使用use命令

{% asset_img 9304c888d43f87943cb46564d01b0ef41ad53af5.jpg Mysql教程：[3]access转mysql（B） %}

- 使用show命令，看一下表是不是都已经存在了。说明都转成功了。

{% asset_img a583631ed21b0ef487a3b514dfc451da80cb3ef5.jpg Mysql教程：[3]access转mysql（B） %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
