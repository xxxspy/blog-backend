
---

title: mongodb解决textsearch搜索中文的问题
date: 2019-06-26 12:44:03
tags: [requests, python, cookies, mongodb]

---

这篇文章我主要介绍一下cookies的保存和复用。

<!-- more -->

### 简介

python的requests库是非常著名的模拟网络访问的库, 通常我们使用requests发送一些网络请求, 以便获取数据或者上传数据。

对于数据requests的人来说, 下面的代码应该非常熟悉:


```python
import requests
sess = requests.session()
sess.cookies.update({'logined': '1'})
sess.get('http://baidu.com')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <Response [200]>

</div>
{% endraw %}



假如我们的cookies保留了登录信息, 那我们想要复用这个登录信息, 就可以免去重复登录的麻烦了。所以我想到的是将cookies保存到硬盘, 用到的时候再复用。

### 具体实现

在诸如`r = sess.get（）`之类的调用之后，`r.cookies`将返回一个`RequestsCookieJar`对象，你可以直接pickle它，即可以保存到硬盘了。


```python
import pickle
def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

#save cookies
r = sess.get('http://baidu.com/')
save_cookies(r.cookies, 'd:/test.cookies')

#load cookies and do a request
sess.get('http://baidu.com/', cookies=load_cookies('d:/test.cookies'))
```




{% raw %}
<div class="output">
输出(plain):<br/>

    <Response [200]>

</div>
{% endraw %}



### 高级实现

session可以和任何cookielib CookieJar一起使用。 LWPCookieJar（和MozillaCookieJar）可以在文件中保存和加载cookie。下面是一个完整的代码片段，它将为session保存和加载cookie。 ignore_discard参数用于与测试的httpbin一起使用，但您可能不希望将其包含在实际代码中。


```python
import os
from http.cookiejar import LWPCookieJar

import requests


s = requests.Session()
s.cookies = LWPCookieJar('cookiejar')
if not os.path.exists('cookiejar'):
    # Create a new cookies file and set our Session's cookies
    print('setting cookies')
    s.cookies.save()
    r = s.get('http://httpbin.org/cookies/set?k1=v1&k2=v2')
else:
    # Load saved cookies from the file and use them in a request
    print('loading saved cookies')
    s.cookies.load(ignore_discard=True)
    r = s.get('http://httpbin.org/cookies')
print(r.text)
# Save the session's cookies back to the file
s.cookies.save(ignore_discard=True)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
setting cookies
{
  "cookies": {
    "k1": "v1", 
    "k2": "v2"
  }
}


</div>
{% endraw %}

### 保存到json

很多时候我们希望使用json来保存json, 因为requests.Session可以当作一个字典数据, 保存字典最直观的方式就是使用json:


```python
# to save cookie
import json

with open('cookie.txt', 'w') as f:
    json.dump(requests.utils.dict_from_cookiejar(sess.cookies), f)
```


```python
# to load cookie
import json
with open('cookie.txt', 'r') as f:
    cookie = requests.utils.cookiejar_from_dict(json.load(f))
    print(cookie)
```

{% raw %}
<div class="output" contenteditable="true">
输出(stream):<br>
<RequestsCookieJar[<Cookie logined=1 for />]>

</div>
{% endraw %}

### 保存到mongodb

在生产环境我们更希望把所有数据都保存到数据库, 这时候使用mnongodb保存cookies也是不错的选择。
我们都知道mongodb是可以保存字典字段的, 所以使用`dict_from_cookiejar`将cookies对象转换成字典, 
然后将字典保存到数据库即可, 这里不多演示了。


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](requests(python)怎样持久化cookies以便复用.ipynb)
> 统计咨询请加QQ 2726725926, 微信 shujufenxidaizuo,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
