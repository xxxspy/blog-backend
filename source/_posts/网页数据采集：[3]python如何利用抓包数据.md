---
title: 网页数据采集：[3]python如何利用抓包数据
date: 2016-06-19 18:23:19
tags: [python]
author: mlln.cn
---
上次我们教大家如何使用httpwatch来进行抓包，其实这不重要，重要的是如何使用获得的数据包，你能读懂数据包吗？好吧，我们今天就是用python来示范一下如何使用数据包。

- 先来设置两个url地址，第一个用于第一次访问，这样可以获得网站服务器发来的cookie，第二个网址是用于登陆的地址

{% asset_img fcbbb151f3deb48fd18981f0f21f3a292cf578f8.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 引入两个模块，cookielib和urllib2

{% asset_img 8d158aeef01f3a294c28f5e09b25bc315d607cf8.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 接着，我们安装一个cookie处理器，代码如下，这个代码很多人不太能读懂，其实你会用就可以了，他们就是这个固定的形式，顶多改改变量的名字。你复制下来以后自己用就可以了，用多了，你再去看代码的意义，你就都懂了。

{% asset_img 58c3acb7d0a20cf40d6edef174094b36adaf99e6.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 然后我们先访问一下网站，获得一个cookie，你不用管这个cookie该怎么弄，前面设置的cookie处理器会自动处理。

{% asset_img 9864a2315c6034a8390298afc9134954082376f8.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 接着，我们写一下postdata，也就是你要post的数据，因为我们打算登陆网站，所以postdata里肯定有用户名和密码，那么怎么知道该怎么写postdata呢？看你抓包得到的post数据。下面第一幅图是httpwatch抓包截图，点击postdata，看到post的数据，然后我们看第二幅图，就是python的写法。你自己感受一下。

{% asset_img d041a4a1cd11728bd7faaf0ccafcc3cec2fd2c8d.jpg 网页数据采集：[3]python如何利用抓包数据 %}

{% asset_img 35e940df8db1cb1323891c3ddf54564e93584bf8.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 写完postdata以后，我们 要将postdata转码一下，让服务器可以解读postdata数据

{% asset_img 2f9cbdcc7cd98d10442a2c1f233fb80e7aec90e6.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 接着设置headers信息，headers也是抓包得到的。同样的方式，你去写header内的信息

{% asset_img 0b907cd9f2d3572ce14cbef28813632762d0c337.jpg 网页数据采集：[3]python如何利用抓包数据 %}

{% asset_img 7d98931001e9390166fcad1079ec54e737d196e6.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 然后我们通过request方法来登陆网站，并返回数据，返回的数据存储在request中

{% asset_img 00a82701213fb80e322f41f934d12f2eb83894e6.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 通过rulopen方法和read方法来读取数据，并打印出来。

{% asset_img 32bb9c8ba61ea8d380c2542a950a304e241f58f8.jpg 网页数据采集：[3]python如何利用抓包数据 %}

- 我们看到输出的结果，这说明我们虽然正确的模拟了登陆网站需要的post信息，但是没有考虑到登陆网站是需要验证码的，后期我们会看到如何处理验证码，如果你拿这个教程去处理没有验证码的登陆问题，那么你现在已经成功了。

{% asset_img 4e83cb628535e5ddb4d285f174c6a7efcf1b62e6.jpg 网页数据采集：[3]python如何利用抓包数据 %}

> 转载请注明来自[DataScience](http://mlln.cn).

> 邮箱: 675495787@qq.com 
