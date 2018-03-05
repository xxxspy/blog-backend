---
title: wikipedia维基百科xml数据解压/解析/清理
date: 2018-02-27 16:13:00
tags: [自然语言处理]
---

维基百科是搞自然语言处理的人经常想用到的语料库, 但是因为其文本是带有xml标签的raw数据, 所以很多人望而生畏. 这篇post主要讲一下如何获取/解析/清理维基百科的数据.

<!-- more -->

### 下载

下载数据有两种方式, 一种是直接从维基百科的官网下载, 地址是: [Database backup dumps](https://dumps.wikimedia.org/backup-index.html), [中文dumps](https://dumps.wikimedia.org/zhwiki/20180220/).

但是我尝试了几次都下载失败, 因为下载时间过长, 总有各种原因导致失败. 

后来用了百度的离线下载, 先保存到网盘, 然后再用客户端慢慢下, 下了半天终于搞定, 这是我们的网盘资源链接：https://pan.baidu.com/s/1jJhuCom 密码：3ztw.

### 解压

今天我们用到的是`zhwiki-latest-pages-articles.xml.bz2`, 这是一个压缩文件. windows下解压比较麻烦, 我用windows下内置bash解压的:

```
bunzip2 -k zhwiki-latest-pages-articles.xml.bz2
```

> 注意使用k参数, 否则会删除源文件.

解压后得到文件`bunzip2 -k zhwiki-latest-pages-articles.xml`.

### 解析

我尝试了各种方式, 比如gensim内置的wikicorpus/[wiki-parser-py](https://github.com/KiranNiranjan/wiki-parser-py), 但是都不是很理想, 比如你没法拿到你最感兴趣的内容. 所以就决定自己解析.

数据是这样的xml(这是我从网上找的, 这个文件实在是太大):

```xml
<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="en">
  <siteinfo>
    <sitename>Wikipedia</sitename>
    <dbname>enwiki</dbname>
    <base>https://en.wikipedia.org/wiki/Main_Page</base>
    <generator>MediaWiki 1.29.0-wmf.12</generator>
    <case>first-letter</case>
    <namespaces>
      ...
    </namespaces>
  </siteinfo>
  <page>
    <title>AccessibleComputing</title>
    <ns>0</ns>
    <id>10</id>
    <redirect title="Computer accessibility" />
    <revision>
      <id>631144794</id>
      <parentid>381202555</parentid>
      <timestamp>2014-10-26T04:50:23Z</timestamp>
      <contributor>
        <username>Paine Ellsworth</username>
        <id>9092818</id>
      </contributor>
      <comment>add [[WP:RCAT|rcat]]s</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
      <text xml:space="preserve">#REDIRECT [[Computer accessibility]]
\{\{Redr|move|from CamelCase|up\}\}</text>
      <sha1>4ro7vvppa5kmm0o1egfjztzcwd0vabw</sha1>
    </revision>
  </page>
  <page>
    <title>Anarchism</title>
    <ns>0</ns>
    <id>12</id>
    <revision>
      <id>766348469</id>
      <parentid>766047928</parentid>
      <timestamp>2017-02-19T18:08:07Z</timestamp>
      <contributor>
        <username>GreenC bot</username>
        <id>27823944</id>
      </contributor>
      <minor />
      <comment>Reformat 1 archive link. [[User:Green Cardamom/WaybackMedic_2.1|Wayback Medic 2.1]]</comment>
      <model>wikitext</model>
      <format>text/x-wiki</format>
<text xml:space="preserve">
...
</text>
</mediawiki>
```

### 清理

未完待续


### 总结

类别数: 276645
总Page数: 3092774