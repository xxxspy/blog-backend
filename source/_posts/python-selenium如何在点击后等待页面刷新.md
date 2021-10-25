
---
title: python selenium如何在点击后等待页面刷新
date: 2018-05-22 18:17:55
tags: [python, selenium]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---

<span></span>
<!-- more -->

> 声明: 本文由[DataScience](http://mlln.cn)原创发表, 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.

本文代码运行环境:

- windows10
- python3.6
- selenium
- jupyter notebook

### 问题提出

你的Selenium测试中可能会被一种奇怪的行为所困扰。你告诉它点击一个链接，然后你查询一些关于新页面的内容，它会从旧页面返回一些内容, 比如运行如下代码, 你可能会发现问题:


```python
from selenium import webdriver
browser = webdriver.Firefox()
```


```python
browser.get('http://mlln.cn/')
btn1 = browser.find_element_by_class_name('logo')
btn1.click()
# 页面刷新后, 
btn1.text
```




    'DataScience'



如果你是个selenium老手, 你可能会看出问题的端倪, 因为点击按钮后, 页面应当会刷新, 旧页面会过期, 那么当你再次使用btn1(来自于旧页面), 应当会报错, 但是现在没有报错. 因为页面还没有完成刷新. 如果你不信, 你可以运行下面的代码看错误.


```python
browser.get('http://baidu.com/')
btn1 = browser.find_element_by_id('su')
btn1.click()
# 页面刷新后, 
btn1.text
```


    ---------------------------------------------------------------------------

    StaleElementReferenceException            Traceback (most recent call last)

    <ipython-input-8-003f9d4fe710> in <module>()
          3 btn1.click()
          4 # 页面刷新后,
    ----> 5 btn1.text
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\selenium\webdriver\remote\webelement.py in text(self)
         74     def text(self):
         75         """The text of the element."""
    ---> 76         return self._execute(Command.GET_ELEMENT_TEXT)['value']
         77 
         78     def click(self):
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\selenium\webdriver\remote\webelement.py in _execute(self, command, params)
        626             params = {}
        627         params['id'] = self._id
    --> 628         return self._parent.execute(command, params)
        629 
        630     def find_element(self, by=By.ID, value=None):
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\selenium\webdriver\remote\webdriver.py in execute(self, driver_command, params)
        312         response = self.command_executor.execute(driver_command, params)
        313         if response:
    --> 314             self.error_handler.check_response(response)
        315             response['value'] = self._unwrap_value(
        316                 response.get('value', None))
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\selenium\webdriver\remote\errorhandler.py in check_response(self, response)
        240                 alert_text = value['alert'].get('text')
        241             raise exception_class(message, screen, stacktrace, alert_text)
    --> 242         raise exception_class(message, screen, stacktrace)
        243 
        244     def _value_or_default(self, obj, key, default):
    

    StaleElementReferenceException: Message: The element reference of <input id="su" class="bg s_btn btnhover" type="submit"> is stale; either the element is no longer attached to the DOM, it is not in the current frame context, or the document has been refreshed
    


这就是selenium经常给我们带来困扰的地方, 同样的代码, 有时候能返回预期的结果, 有时候却会报错(其实这取决于你的网速). 但是做测试怎么能允许这种不确定性. 所以我们的需求就出现了, 如何让selenium点击一个链接, 然后等待页面刷新后再执行新的操作?

### 捕捉错误StaleElementReferenceException

因为页面刷新后, 旧元素会失效, 引发`StaleElementReferenceException`错误, 利用这个特性, 我们可以这么做:


```python
from selenium.common.exceptions import StaleElementReferenceException
browser.get('http://mlln.cn/')
btn1 = browser.find_element_by_class_name('read-more')
btn1.click()
# 页面刷新后, 
while True:
    try: 
        print('Text of btn:')
        print(btn1.text)
    except StaleElementReferenceException:
        print('Error Happened!')
        break
        
btn2 = browser.find_element_by_class_name('logo')
btn2.text
```

    Text of btn:
    Error Happened!
    




    ''



### with语句

上面的方法已经足够好用的话, 下面你旧可以忽略了. 但是我现在的想法是, 我们需要提供一个可以复用的功能, 便于我以后开发用. 所以我想实现一个`with`语句, 这样看起来更优雅.

下面我们尝试一种新的监测页面发生变化的方法. 我们知道selenium给每个页面DOM元素分配一个id, 如果页面刷新, id会发生变化, 所以我们就通过比较页面元素id变量来判断页面是否发生变化.


```python
import time

class wait_page_load:
    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.timeout = timeout
        
    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')
        print(f'Old page id is {self.old_page.id}')
    
    def __exit__(self, *_):
        start = time.time()
        while time.time() - start < self.timeout:
            new_page = self.browser.find_element_by_tag_name('html')
            print(f'New page id is {new_page.id}')
            if new_page.id != self.old_page.id:
                return True
            else:
                time.sleep(0.1)
        raise Exception(f'Timeout after {self.timeout} secends')            
```

下面我们使用with语句来优雅的等待页面加载.


```python
browser.get('http://mlln.cn/')
with wait_page_load(browser):
    print('Button will click!')
    browser.find_element_by_class_name('read-more').click()
    print('Button clicked!')
    
print('Page is ready')
```

    Old page id is 40178fe8-c3b1-49d9-8271-cead0d01e724
    Button will click!
    Button clicked!
    New page id is 2c7d508b-181d-41c6-ac6f-3ef962b494b6
    Page is ready
    

### staleness_of内置方法

其实, 绕了一大圈, 我发现selenium已经有一个内置方法来等待元素过期, 就是`staleness_of`. 利用这个方法, 我们的代码还可以更简洁:


```python
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.expected_conditions import staleness_of


class wait_page_load:
    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.timeout = timeout
        
    def __enter__(self):
        self.old_page = self.browser.find_element_by_tag_name('html')
    
    def __exit__(self, *_):
        WebDriverWait(self.browser, self.timeout).until(staleness_of(self.old_page))
```

测试新的方法:


```python
browser.get('http://mlln.cn/')
with wait_page_load(browser):
    print('Button will click!')
    browser.find_element_by_class_name('read-more').click()
    print('Button clicked!')
    
print('Page is ready')
```

    Button will click!
    Button clicked!
    Page is ready
    

> 声明: 本文由[DataScience](http://mlln.cn)原创发表, 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](python-selenium如何在点击后等待页面刷新.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
