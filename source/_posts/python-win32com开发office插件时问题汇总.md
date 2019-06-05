---
title: python win32com开发office插件时问题汇总
date: 2018-04-12 20:19:31
tags: [python]
---


#### 

事先我用如下代码开发并注册了一个COM:

```py
import pythoncom
class PythonUtilities:
    _public_methods_ = [ 'add_watermark' ]
    _reg_progid_ = "PythonDemo.Utilities"
    # NEVER copy the following ID
    # Use "print pythoncom.CreateGuid()" to make a new one.
    _reg_clsid_ = "{B7E3EE50-5E2A-4044-8241-4F76B1DAB885}"

if __name__=='__main__':
    print( "Registering COM server...")
    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonUtilities)
```

在python种使用`win32com.client.Dipatch`可以调用该COM, 但是在VBA种却报错:`specific module coundn't be found`:

```VB
Sub Test()
    ' Create the Python COM objects.
    Set stringmod = CreateObject("PythonDemo.Utilities")
    ' Call string.split
End Sub
```

> 解决方法就是, 没有找到`pythoncom35.dll`和`pywintypes35.dll`这两个DLL导致的. 

这两个文件位于`Lib/site-packages/pywin32_system32`下, 把他们复制到`pythondir/Scripts`这个文件夹下就行了. 因为通常这个文件夹是添加到环境变量Path种的.


有啥问题可以直接在下面留言奥.
