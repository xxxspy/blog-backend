---
title: win32com.gen_py错误has no attribute CLSIDToClassMap
date: 2018-04-23 16:09:31
tags: [win32com]
---

office自动化的开发很麻烦, 很多东西不是很懂, 发生错误也不知道怎么回事. 今天遇到一个错误, 运行下面这个语句的时候发生的:

```python
gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 7, bForDemand=True)
```

<!--more-->


错误的详细信息如下:

```python
Traceback (most recent call last):
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\server\policy.py", line 136, in CreateInstance
    return retObj._CreateInstance_(clsid, reqIID)
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\server\dispatcher.py", line 37, in _CreateInstance_
    return self._HandleException_()
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\server\dispatcher.py", line 34, in _CreateInstance_
    self.policy._CreateInstance_(clsid, reqIID)
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\server\policy.py", line 194, in _CreateInstance_
    myob = call_func(classSpec)
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\server\policy.py", line 728, in call_func
    return resolve_func(spec)(*args)
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\server\policy.py", line 717, in resolve_func
    module = _import_module(mname)
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\server\policy.py", line 736, in _import_module
    __import__(mname)
  File "D:\mysites\jupyterReport\wdclient\word_addin.py", line 38, in <module>
    gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 7, bForDemand=True) # Wrod 16
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\client\gencache.py", line 391, in EnsureModule
    module = GetModuleForTypelib(typelibCLSID, lcid, major, minor)
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\client\gencache.py", line 266, in GetModuleForTypelib
    AddModuleToCache(typelibCLSID, lcid, major, minor)
  File "C:\Users\syd\AppData\Local\Programs\Python\Python35\lib\site-packages\win32com\client\gencache.py", line 552, in AddModuleToCache
    dict = mod.CLSIDToClassMap
AttributeError: module 'win32com.gen_py.00020905-0000-0000-C000-000000000046x0x8x7' has no attribute 'CLSIDToClassMap'
pythoncom error: CPyFactory::CreateInstance failed to create instance. (80004005)
```

发生这个错误的原因并不是很清楚, 大概是升级了一下系统, 但是我并不清楚内部原因.

解决的方法就是, 因为这个缓存的文件有问题, 所以就应该删掉缓存. 所以我先找到这个缓存文件:

```python
from win32com.client.gencache import EnsureDispatch
import sys
xl = EnsureDispatch("Word.Application")
print(sys.modules[xl.__module__].__file__)
```

运行这段代码, 就会找到它的位置. 然后删除`gen_py`文件夹下的所有包含这一堆数字的文件夹`0020905-0000-0000-C000-000000000046x0`.

然后你的程序又能顺利运行了.