---
title: selenium进阶教程
date: 2017-09-27 18:16:38
tags: [selenium, python]
---

本篇文章主要介绍一下python-selenium在进行自动化功能测试的时候经常用到的一些高级API，这些API的灵活运用可以提高测试脚本的质量和性能。

### 回顾初级教程

如果没有接触过python-selenium，恐怕你需要先浏览一下这篇文章：[selenium数据采集入门(for psychologist)](/2017/06/10/selenim%E6%95%B0%E6%8D%AE%E9%87%87%E9%9B%86%E5%85%A5%E9%97%A8-for-psychologist/)

<!--more--> 

### 等待加载

很多时候页面的加载时间较长，有些元素还没有加载就尝试去获取该元素会导致程序错误，为了避免网络延迟造成的影响，我们通常需要使用一些等待的API。

#### time.sleep

最简单的方法就是使用python自带的time库中的sleep方法。该方法强制程序暂停，等待页面加载。比如：

```python
import time
import selenium
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://mlln.cn/") #打开页面
time.sleep(1)# 暂停1秒，等待所有页面元素加载
```

#### 隐性等待

不要尝试顾名思义，因为我认为这不是一个好名字，但是别人一直这样用，所以我们也就这么叫。隐性等待就是让程序等待页面加载一定的时间t，如果在时间t内，页面没有加载完毕，那么ok，我不等你了，程序会接着运行，如果在时间t内页面加载完成，则程序不会等到t后再运行，而是在页面加载完的那一刻就运行，例如：

```python
import selenium
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(30) #最长等待30秒，过了30秒，即便页面没有加载完，程序依然运行
driver.get("http://mlln.cn/") #打开页面
```

#### 显性等待

显性等待用`WebDriverWait`, 比隐性等待更常用的是显性等待，显性等待也有一个最长等待时间t，但是如果在t时间内页面没有加载完，它会抛出异常，从而程序停止。而且，显性等待允许你明确到底在等什么，也就是等待条件。selenium提供了`until`和`until_not`方法来支持显性等待。

我们先来看一个例子：

```python
from selenium import webdriver  
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By  
driver = webdriver.Chrome()  
driver.implicitly_wait(10) # 隐性等待和显性等待可以同时用, 等待的最长时间取两者之中的大者  
driver.get('http://mlln.cn/')  
locator = (By.LINK_TEXT, 'DataScience')
## 等待20秒，每过0.5秒就检查一下等待条件是否满足(即程序是否可以接着运行)
## 等待条件是locator的出现，而locator是定义好的一个元组
WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))  
driver.find_element_by_link_text('DataScience')
driver.close()  
```

##### 等待条件

其实应该叫做期望条件，但是我们现在主要在讲等待。等待的条件有很多，都存放在`selenium.webdriver.support.expected_conditions`中，我们大概浏览一下有哪些可用的：

```python
title_is  
title_contains  
这两个人条件验证元素是否出现，传入的参数都是元组类型的locator，如(By.ID, 'kw')  
顾名思义，一个只要一个符合条件的元素加载出来就通过；另一个必须所有符合条件的元素都加载出来才行  


presence_of_element_located  
presence_of_all_elements_located  
这三个条件验证元素是否可见，前两个传入参数是元组类型的locator，第三个传入WebElement  
第一个和第三个其实质是一样的  


visibility_of_element_located  
invisibility_of_element_located  
visibility_of  
这两个人条件判断某段文本是否出现在某元素中，一个判断元素的text，一个判断元素的value  


text_to_be_present_in_element  
text_to_be_present_in_element_value  
这个条件判断frame是否可切入，可传入locator元组或者直接传入定位方式：id、name、index或WebElement  


frame_to_be_available_and_switch_to_it  
这个条件判断是否有alert出现  


alert_is_present  
这个条件判断元素是否可点击，传入locator 

element_to_be_clickable  
这四个条件判断元素是否被选中，第一个条件传入WebElement对象，第二个传入locator元组  
第三个传入WebElement对象以及状态，相等返回True，否则返回False  
第四个传入locator以及状态，相等返回True，否则返回False  

element_to_be_selected  
element_located_to_be_selected  
element_selection_state_to_be  
element_located_selection_state_to_be  
最后一个条件判断一个元素是否仍在DOM中，传入WebElement对象，可以判断页面是否刷新了  
staleness_of  
```

### iframe

selenium不能直接操作iframe内部的元素，因为iframe内部元素相当于另一个页面，这个页面有自己的head和body。 为了获取iframe内部元素，需要使用`switch_to_frame`方法，参数是iframe元素的id属性或者通过`find_element_by*`方法获取得到的iframe元素对象。想要跳出iframe可以用`switch_to_default_content`方法。

例如，利用你以前的知识，不使用`switch_to_frame`, 点击下面页面的`百度一下`按钮。你是无法实现的。

{% iframe https://www.baidu.com/s?wd=datascience%20mlln&rsv_spt=1&rsv_iqid=0x9b326cdd0001c746&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&inputT=16327&rsv_t=7f19HubaxP8B9AT0rP98mJIV3qBjmgqdZ55T5vhT1w7ivFI8rDBOldGNIe%2BsZIzIVP4G&oq=DataScience&rsv_pq=94c4d7540001b034&rsv_sug3=52&rsv_sug1=32&rsv_sug7=100&rsv_sug2=0&rsv_sug4=16327 100% 400px %}

下面使用`switch_to_frame`：

```python
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://mlln.cn/2017/09/27/selenium%E8%BF%9B%E9%98%B6%E6%95%99%E7%A8%8B/')
frame=driver.find_element_by_tag_name('iframe')
driver.switch_to_frame(frame)
driver.find_element_by_id('su').click()
driver.switch_to_default_content()
```

### 未完待续

后面遇到问题再补充到这里。