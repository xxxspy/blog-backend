
---
title: pyscript用python写JavaScript
date: 2018-07-13 20:17:55
tags: [javascript, python]
toc: true
xiongzhang: true


---
<span></span>
<!-- more -->

> 声明: 本文由[DataScience](http://mlln.cn)发表,未经允许不得转载。 转载请注明[本文链接](http://mlln.cn)mlln.cn, 并在文后留言`转载`.

本文代码运行环境:

- windows10
- jupyter notebook
- python3.6

### pyscript简介

pyscript模块提供了将Python代码转换为JavaScript的功能。这是使用PyScript的简要介绍。有关详细信息，请参阅以下部分。

PyScript是一种使用Python语言编写JavaScript的工具。支持所有相关的内置功能，以及list，dict和str的方法。不支持set，带step参数的切片操作，yield和import。除此之外，大多数Python代码应该按预期工作...根据经验，代码在正确时应该按预期运行，但错误报告可能不是非常Pythonic。

您需要了解的最重要的函数是`py2js`和`evalpy`。原则上，您不需要JavaScript的知识来编写PyScript代码，尽管它在极端情况下确实有帮助。

### 目标

使用web技术实现可视化和用户交互的Python项目有所增加。 PyScript允许用户在Python中编写JavaScript回调，实现交互的灵活/快速。

这导致了以下两个主要目标：

通过让人们使用Python语法和内置函数来编写javascript，并修复一些JavaScripts怪癖，使编写JavaScript变得更容易，更不令人沮丧。允许在Python程序中定义JavaScript代码段。PyScript生成的代码可以独立工作。任何（PyScript兼容的）Python片段都可以转换为JS;你不需要另一个JS库来运行它。

PyScript还可用于开发独立的JavaScript（AMD）模块。

### 注意

PyScript修复了JS的一些怪癖，但它仍然只是JavaScript。这是一个值得关注的事项列表。此列表可能不完整。如果您打算大量使用PyScript，我们建议您熟悉JavaScript。

- JavasScript有一个null（即None）的概念，以及undefined。有时您可能想要使用`if x is None or x is undefined`
- 访问不存在的属性不会引发AttributeError但会产生undefined, 这是JavaScript的特性
- 类上的魔术函数（例如，用于运算符重载）不起作用。
- 调用以大写字母开头的对象被假定为类实例化（使用new）：PyScript类必须以大写字母开头，而任何其他callables都不能。
- 如果函数具有** kwargs参数或* args之后的命名参数，则函数可以接受它。将关键字传递给不处理关键字参数的函数可能会导致混淆错误。

### 案例

为了在notebook中实时显示python转JavaScript的过程, 我们注册一个魔法函数, 功能很简单, 就是把python代码转成JavaScript, 并显示在输出区域。


```python
from IPython.core.magic import register_cell_magic
from IPython.display import Markdown


@register_cell_magic
def py2js(line, cell):
    from pscript import py2js
    js= py2js(cell)
    return Markdown(f'```javascript\n{js}\n```')
```


```python
%%py2js

a = 1
```




```javascript
var a;
a = 1;
```



#### 基本操作


```python
%%py2js

# Simple operations
3 + 4 -1
3 * 7 / 9
5**2
pow(5, 2)
7 // 2
```




```javascript
var _pyfunc_pow = Math.pow;
(3 + 4) - 1;
(3 * 7) / 9;
Math.pow(5, 2);
_pyfunc_pow(5, 2);
Math.floor(7/2);
```



#### 数据类型



```python
%%py2js

[True, False, None]

foo = [1, 2, 3]
bar = {'a': 1, 'b': 2}
```




```javascript
var bar, foo;
[true, false, null];
foo = [1, 2, 3];
bar = ({a: 1, b: 2});
```




```python
%%py2js

a = [2,3,4]
a.sort()
```




```javascript
var _pymeth_sort = function (key, reverse) { // nargs: 0 1 2
    if (!Array.isArray(this)) return this.sort.apply(this, arguments);
    var comp = function (a, b) {a = key(a); b = key(b);
        if (a<b) {return -1;} if (a>b) {return 1;} return 0;};
    comp = Boolean(key) ? comp : undefined; 
    this.sort(comp);
    if (reverse) this.reverse();
};
var a;
a = [2, 3, 4];
_pymeth_sort.call(a, undefined, false);
```



#### 切片操作和取值


```python
%%py2js

foo = [1, 2, 3, 4, 5]
foo[2:]
foo[2:-2]
```




```javascript
var foo;
foo = [1, 2, 3, 4, 5];
foo.slice(2);
foo.slice(2,-2);
```




```python
%%py2js
bar = 'abcdefghij'
bar[2:]
bar[2:-2]
```




```javascript
var bar;
bar = "abcdefghij";
bar.slice(2);
bar.slice(2,-2);
```




```python
%%py2js
# Subscripting
foo = {'bar': 3}
foo['bar']
foo.bar  # Works in JS, but not in Python
```




```javascript
var foo;
foo = ({bar: 3});
foo["bar"];
foo.bar;
```



#### 格式化字符串


```python
%%py2js
"value: %f" % val

# 卧槽, 生成的代码太长了
```




```javascript
var _pyfunc_format = function (v, fmt) {  // nargs: 2
    fmt = fmt.toLowerCase();
    var s = String(v);
    if (fmt.indexOf('!r') >= 0) {
        try { s = JSON.stringify(v); } catch (e) { s = undefined; }
        if (typeof s === 'undefined') { s = v._IS_COMPONENT ? v.id : String(v); }
    }
    var i0 = fmt.indexOf(':');
    if (i0 < 0) {
    } else if (fmt.indexOf('i', i0) > i0) { // integer formatting
        s = Number.parseInt(v).toFixed(0);
    } else if (fmt.indexOf('f', i0) > i0) {  // float formatting
        v = Number.parseFloat(v);
        var spec = fmt.slice(i0+1, fmt.indexOf('f', i0));
        var decimals = 6;
        if (spec.indexOf('.') >= 0) {
            var decimals = Number(spec.slice(spec.indexOf('.')+1));
        }
        s = v.toFixed(decimals);
    } else if (fmt.indexOf('e', i0) > i0) {  // exp formatting
        v = Number.parseFloat(v);
        var precision = 6;
        var spec = fmt.slice(i0+1, fmt.indexOf('e', i0));
        if (spec.indexOf('.') >= 0) {
            precision = Number(spec.slice(spec.indexOf('.')+1)) || 1;
        }
        s = v.toExponential(precision);
    } else if (fmt.indexOf('g', i0) > i0) {  // "general" formatting
        v = Number.parseFloat(v);
        var precision = 6;
        var spec = fmt.slice(i0+1, fmt.indexOf('g', i0));
        if (spec.indexOf('.') >= 0) {
            precision = Number(spec.slice(spec.indexOf('.')+1)) || 1;
        }
        // Exp or decimal?
        s = v.toExponential(precision-1);
        var s1 = s.slice(0, s.indexOf('e')), s2 = s.slice(s.indexOf('e'));
        if (s2.length == 3) { s2 = 'e' + s2[1] + '0' + s2[2]; }
        var exp = Number(s2.slice(1));
        if (exp >= -4 && exp < precision) { s1=v.toPrecision(precision); s2=''; }
        // Skip trailing zeros and dot
        var j = s1.length-1;
        while (j>0 && s1[j] == '0') { j-=1; }
        s1 = s1.slice(0, j+1);
        if (s1.endsWith('.')) { s1 = s1.slice(0, s1.length-1); }
        s = s1 + s2;
    }
    if (i0 >= 0 && v > 0) {
        if (fmt[i0+1] == '+') { s = '+' + s; }
        if (fmt[i0+1] == ' ') { s = ' ' + s; }
    }
    return s;
};
var _pymeth_format = function () {
    if (this.constructor !== String) return this.format.apply(this, arguments);
    var parts = [], i = 0, i1, i2;
    var itemnr = -1;
    while (i < this.length) {
        // find opening
        i1 = this.indexOf('{', i);
        if (i1 < 0 || i1 == this.length-1) { break; }
        if (this[i1+1] == '{') {parts.push(this.slice(i, i1+1)); i = i1 + 2; continue;}
        // find closing
        i2 = this.indexOf('}', i1);
        if (i2 < 0) { break; }
        // parse
        itemnr += 1;
        var fmt = this.slice(i1+1, i2);
        var index = fmt.split(':')[0].split('!')[0];
        index = index? Number(index) : itemnr
        var s = _pyfunc_format(arguments[index], fmt);
        parts.push(this.slice(i, i1), s);
        i = i2 + 1;
    }
    parts.push(this.slice(i));
    return parts.join('');
};
_pymeth_format.call("value: {:f}", val);
```




```python
%%py2js

'{a}'.format(a)
```




```javascript
var _pyfunc_format = function (v, fmt) {  // nargs: 2
    fmt = fmt.toLowerCase();
    var s = String(v);
    if (fmt.indexOf('!r') >= 0) {
        try { s = JSON.stringify(v); } catch (e) { s = undefined; }
        if (typeof s === 'undefined') { s = v._IS_COMPONENT ? v.id : String(v); }
    }
    var i0 = fmt.indexOf(':');
    if (i0 < 0) {
    } else if (fmt.indexOf('i', i0) > i0) { // integer formatting
        s = Number.parseInt(v).toFixed(0);
    } else if (fmt.indexOf('f', i0) > i0) {  // float formatting
        v = Number.parseFloat(v);
        var spec = fmt.slice(i0+1, fmt.indexOf('f', i0));
        var decimals = 6;
        if (spec.indexOf('.') >= 0) {
            var decimals = Number(spec.slice(spec.indexOf('.')+1));
        }
        s = v.toFixed(decimals);
    } else if (fmt.indexOf('e', i0) > i0) {  // exp formatting
        v = Number.parseFloat(v);
        var precision = 6;
        var spec = fmt.slice(i0+1, fmt.indexOf('e', i0));
        if (spec.indexOf('.') >= 0) {
            precision = Number(spec.slice(spec.indexOf('.')+1)) || 1;
        }
        s = v.toExponential(precision);
    } else if (fmt.indexOf('g', i0) > i0) {  // "general" formatting
        v = Number.parseFloat(v);
        var precision = 6;
        var spec = fmt.slice(i0+1, fmt.indexOf('g', i0));
        if (spec.indexOf('.') >= 0) {
            precision = Number(spec.slice(spec.indexOf('.')+1)) || 1;
        }
        // Exp or decimal?
        s = v.toExponential(precision-1);
        var s1 = s.slice(0, s.indexOf('e')), s2 = s.slice(s.indexOf('e'));
        if (s2.length == 3) { s2 = 'e' + s2[1] + '0' + s2[2]; }
        var exp = Number(s2.slice(1));
        if (exp >= -4 && exp < precision) { s1=v.toPrecision(precision); s2=''; }
        // Skip trailing zeros and dot
        var j = s1.length-1;
        while (j>0 && s1[j] == '0') { j-=1; }
        s1 = s1.slice(0, j+1);
        if (s1.endsWith('.')) { s1 = s1.slice(0, s1.length-1); }
        s = s1 + s2;
    }
    if (i0 >= 0 && v > 0) {
        if (fmt[i0+1] == '+') { s = '+' + s; }
        if (fmt[i0+1] == ' ') { s = ' ' + s; }
    }
    return s;
};
var _pymeth_format = function () {
    if (this.constructor !== String) return this.format.apply(this, arguments);
    var parts = [], i = 0, i1, i2;
    var itemnr = -1;
    while (i < this.length) {
        // find opening
        i1 = this.indexOf('{', i);
        if (i1 < 0 || i1 == this.length-1) { break; }
        if (this[i1+1] == '{') {parts.push(this.slice(i, i1+1)); i = i1 + 2; continue;}
        // find closing
        i2 = this.indexOf('}', i1);
        if (i2 < 0) { break; }
        // parse
        itemnr += 1;
        var fmt = this.slice(i1+1, i2);
        var index = fmt.split(':')[0].split('!')[0];
        index = index? Number(index) : itemnr
        var s = _pyfunc_format(arguments[index], fmt);
        parts.push(this.slice(i, i1), s);
        i = i2 + 1;
    }
    parts.push(this.slice(i));
    return parts.join('');
};
_pymeth_format.call("{a}", a);
```



#### 赋值操作


```python
%%py2js

bar.foo = 3
```




```javascript
bar.foo = 3;
```




```python
%%py2js
a = 1, 2, 3
```




```javascript
var a;
a = [1, 2, 3];
```




```python
%%py2js
a1, a2, a3 = a
```




```javascript
var a1, a2, a3, stub1_;
stub1_ = a;
a1 = stub1_[0];a2 = stub1_[1];a3 = stub1_[2];
```




```python
%%py2js

del bar.foo
```




```javascript
delete bar.foo;
```




```python
%%py2js
# 大写字母开头, 实例化这个类
foo = Foo()
```




```javascript
var foo;
foo = new Foo();
```



#### 比较


```python
%%py2js

foo is bar
```




```javascript
foo === bar;
```




```python
%%py2js

foo == bar
```




```javascript
var _pyfunc_op_equals = function op_equals (a, b) { // nargs: 2
    if (a == null || b == null) {
    } else if (Array.isArray(a) && Array.isArray(b)) {
        var i = 0, iseq = a.length == b.length;
        while (iseq && i < a.length) {iseq = op_equals(a[i], b[i]); i+=1;}
        return iseq;
    } else if (a.constructor === Object && b.constructor === Object) {
        var akeys = Object.keys(a), bkeys = Object.keys(b);
        akeys.sort(); bkeys.sort();
        var i=0, k, iseq = op_equals(akeys, bkeys);
        while (iseq && i < akeys.length)
            {k=akeys[i]; iseq = op_equals(a[k], b[k]); i+=1;}
        return iseq;
    } return a == b;
};
_pyfunc_op_equals(foo, bar);
```




```python
%%py2js
# 深度比较, 和js不同
(2, 3, 4) == (2, 3, 4)
(2, 3) in [(1,2), (2,3), (3,4)]
```




```javascript
var _pyfunc_op_contains = function op_contains (a, b) { // nargs: 2
    if (b == null) {
    } else if (Array.isArray(b)) {
        for (var i=0; i<b.length; i++) {if (_pyfunc_op_equals(a, b[i]))
                                           return true;}
        return false;
    } else if (b.constructor === Object) {
        for (var k in b) {if (a == k) return true;}
        return false;
    } else if (b.constructor == String) {
        return b.indexOf(a) >= 0;
    } var e = Error('Not a container: ' + b); e.name='TypeError'; throw e;
};
var _pyfunc_op_equals = function op_equals (a, b) { // nargs: 2
    if (a == null || b == null) {
    } else if (Array.isArray(a) && Array.isArray(b)) {
        var i = 0, iseq = a.length == b.length;
        while (iseq && i < a.length) {iseq = op_equals(a[i], b[i]); i+=1;}
        return iseq;
    } else if (a.constructor === Object && b.constructor === Object) {
        var akeys = Object.keys(a), bkeys = Object.keys(b);
        akeys.sort(); bkeys.sort();
        var i=0, k, iseq = op_equals(akeys, bkeys);
        while (iseq && i < akeys.length)
            {k=akeys[i]; iseq = op_equals(a[k], b[k]); i+=1;}
        return iseq;
    } return a == b;
};
_pyfunc_op_equals([2, 3, 4], [2, 3, 4]);
_pyfunc_op_contains([2, 3], ([[1, 2], [2, 3], [3, 4]]));
```




```python
%%py2js

foo is undefined
```




```javascript
foo === undefined;
```




```python
%%py2js

"foo" in "this has foo in it"
```




```javascript
var _pyfunc_op_contains = function op_contains (a, b) { // nargs: 2
    if (b == null) {
    } else if (Array.isArray(b)) {
        for (var i=0; i<b.length; i++) {if (_pyfunc_op_equals(a, b[i]))
                                           return true;}
        return false;
    } else if (b.constructor === Object) {
        for (var k in b) {if (a == k) return true;}
        return false;
    } else if (b.constructor == String) {
        return b.indexOf(a) >= 0;
    } var e = Error('Not a container: ' + b); e.name='TypeError'; throw e;
};
var _pyfunc_op_equals = function op_equals (a, b) { // nargs: 2
    if (a == null || b == null) {
    } else if (Array.isArray(a) && Array.isArray(b)) {
        var i = 0, iseq = a.length == b.length;
        while (iseq && i < a.length) {iseq = op_equals(a[i], b[i]); i+=1;}
        return iseq;
    } else if (a.constructor === Object && b.constructor === Object) {
        var akeys = Object.keys(a), bkeys = Object.keys(b);
        akeys.sort(); bkeys.sort();
        var i=0, k, iseq = op_equals(akeys, bkeys);
        while (iseq && i < akeys.length)
            {k=akeys[i]; iseq = op_equals(a[k], b[k]); i+=1;}
        return iseq;
    } return a == b;
};
_pyfunc_op_contains("foo", "this has foo in it");
```




```python
%%py2js

3 in [0, 1, 2, 3, 4]
```




```javascript
var _pyfunc_op_contains = function op_contains (a, b) { // nargs: 2
    if (b == null) {
    } else if (Array.isArray(b)) {
        for (var i=0; i<b.length; i++) {if (_pyfunc_op_equals(a, b[i]))
                                           return true;}
        return false;
    } else if (b.constructor === Object) {
        for (var k in b) {if (a == k) return true;}
        return false;
    } else if (b.constructor == String) {
        return b.indexOf(a) >= 0;
    } var e = Error('Not a container: ' + b); e.name='TypeError'; throw e;
};
var _pyfunc_op_equals = function op_equals (a, b) { // nargs: 2
    if (a == null || b == null) {
    } else if (Array.isArray(a) && Array.isArray(b)) {
        var i = 0, iseq = a.length == b.length;
        while (iseq && i < a.length) {iseq = op_equals(a[i], b[i]); i+=1;}
        return iseq;
    } else if (a.constructor === Object && b.constructor === Object) {
        var akeys = Object.keys(a), bkeys = Object.keys(b);
        akeys.sort(); bkeys.sort();
        var i=0, k, iseq = op_equals(akeys, bkeys);
        while (iseq && i < akeys.length)
            {k=akeys[i]; iseq = op_equals(a[k], b[k]); i+=1;}
        return iseq;
    } return a == b;
};
_pyfunc_op_contains(3, [0, 1, 2, 3, 4]);
```



#### Truthy和Falsy


```python
%%py2js

# 这些值都被判定为false

# These evaluate to False:
0
NaN
""  # empty string
None  # JS null
undefined
[]
{}
```




```javascript
0;
NaN;
"";
null;
undefined;
[];
({});
```




```python
%%py2js

# 支持这样的操作
a = []
a = a or [1]  # a is now [1]
```




```javascript
var _pyfunc_truthy = function (v) {
    if (v === null || typeof v !== "object") {return v;}
    else if (v.length !== undefined) {return v.length ? v : false;}
    else if (v.byteLength !== undefined) {return v.byteLength ? v : false;}
    else if (v.constructor !== Object) {return true;}
    else {return Object.getOwnPropertyNames(v).length ? v : false;}
};
var a;
a = [];
a = _pyfunc_truthy(a) || [1];
```



#### 函数操作


```python
%%py2js

# Business as usual
foo(a, b)
```




```javascript
foo(a, b);
```




```python
%%py2js

# 支持 args (不支持 **kwargs)
foo(*a)
```




```javascript
foo.apply(null, a);
```



#### if语句


```python
%%py2js


if val > 7:
    result = 42
elif val > 1:
    result = 1
else:
    result = 0
```




```javascript
var result;
if ((val > 7)) {
    result = 42;
} else if ((val > 1)) {
    result = 1;
} else {
    result = 0;
}
```



#### 循环


```python
%%py2js

val = 0
while val < 10:
    val += 1
```




```javascript
var _pyfunc_op_add = function (a, b) { // nargs: 2
    if (Array.isArray(a) && Array.isArray(b)) {
        return a.concat(b);
    } return a + b;
};
var val;
val = 0;
while (val < 10) {
    val = _pyfunc_op_add(val, 1);
}
```




```python
%%py2js

# Using range() yields true for-loops
for i in range(10):
    print(i)
```




```javascript
var i;
for (i = 0; i < 10; i += 1) {
    console.log(i);
}
```




```python
%%py2js

for i in range(100, 10, -2):
    print(i)
```




```javascript
var i;
for (i = 100; i > 10; i += -2) {
    console.log(i);
}
```




```python
%%py2js

# One way to iterate over an array
for i in range(len(arr)):
    print(arr[i])
```




```javascript
var i;
for (i = 0; i < arr.length; i += 1) {
    console.log(arr[i]);
}
```




```python
%%py2js
# But this is equally valid (and fast)
for element in arr:
    print(element)
```




```javascript
var element, stub1_seq, stub2_itr;
stub1_seq = arr;
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    element = stub1_seq[stub2_itr];
    console.log(element);
}
```




```python
%%py2js

# 遍历字符串
for char in "foo bar":
    print(c)
```




```javascript
var char, stub1_seq, stub2_itr;
stub1_seq = "foo bar";
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    char = stub1_seq[stub2_itr];
    console.log(c);
}
```




```python
%%py2js

# 更复杂的遍历
for i, j in [[1, 2], [3, 4]]:
    print(i+j)
```




```javascript
var _pyfunc_op_add = function (a, b) { // nargs: 2
    if (Array.isArray(a) && Array.isArray(b)) {
        return a.concat(b);
    } return a + b;
};
var i, j, stub1_seq, stub2_itr, stub3_tgt;
stub1_seq = [[1, 2], [3, 4]];
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    stub3_tgt = stub1_seq[stub2_itr];
    i = stub3_tgt[0]; j = stub3_tgt[1];
    console.log(_pyfunc_op_add(i, j));
}
```



支持用于迭代的Buildin函数：enumerate, zip, reversed, sorted, filter, map


```python
%%py2js

for i, x in enumerate(foo):
    print(i, x)
```




```javascript
var _pyfunc_enumerate = function (iter) { // nargs: 1
    var i, res=[];
    if ((typeof iter==="object") && (!Array.isArray(iter))) {iter = Object.keys(iter);}
    for (i=0; i<iter.length; i++) {res.push([i, iter[i]]);}
    return res;
};
var i, stub1_seq, stub2_itr, stub3_tgt, x;
stub1_seq = _pyfunc_enumerate(foo);
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    stub3_tgt = stub1_seq[stub2_itr];
    i = stub3_tgt[0]; x = stub3_tgt[1];
    console.log(i + " " + x);
}
```




```python
%%py2js

for a, b in zip(foo, bar):
    pass
```




```javascript
var _pyfunc_zip = function () { // nargs: 2 3 4 5 6 7 8 9
    var i, j, tup, arg, args = [], res = [], len = 1e20;
    for (i=0; i<arguments.length; i++) {
        arg = arguments[i];
        if ((typeof arg==="object") && (!Array.isArray(arg))) {arg = Object.keys(arg);}
        args.push(arg);
        len = Math.min(len, arg.length);
    }
    for (j=0; j<len; j++) {
        tup = []
        for (i=0; i<args.length; i++) {tup.push(args[i][j]);}
        res.push(tup);
    }
    return res;
};
var a, b, stub1_seq, stub2_itr, stub3_tgt;
stub1_seq = _pyfunc_zip(foo, bar);
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    stub3_tgt = stub1_seq[stub2_itr];
    a = stub3_tgt[0]; b = stub3_tgt[1];
}
```




```python
%%py2js

for x in reversed(sorted(foo)):
    pass
```




```javascript
var _pyfunc_reversed = function (iter) { // nargs: 1
    if ((typeof iter==="object") && (!Array.isArray(iter))) {iter = Object.keys(iter);}
    return iter.slice().reverse();
};
var _pyfunc_sorted = function (iter, key, reverse) { // nargs: 1 2 3
    if ((typeof iter==="object") && (!Array.isArray(iter))) {iter = Object.keys(iter);}
    var comp = function (a, b) {a = key(a); b = key(b);
        if (a<b) {return -1;} if (a>b) {return 1;} return 0;};
    comp = Boolean(key) ? comp : undefined; 
    iter = iter.slice().sort(comp);
    if (reverse) iter.reverse();
    return iter;
};
var stub1_seq, stub2_itr, x;
stub1_seq = _pyfunc_reversed(_pyfunc_sorted(foo, undefined, false));
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    x = stub1_seq[stub2_itr];
}
```




```python
%%py2js

for x in map(lambda x: x+1, foo):
    pass
```




```javascript
var _pyfunc_map = function (func, iter) { // nargs: 2
    if (typeof func === "undefined" || func === null) {func = function(x) {return x;}}
    if ((typeof iter==="object") && (!Array.isArray(iter))) {iter = Object.keys(iter);}
    return iter.map(func);
};
var stub1_seq, stub2_itr, x;
stub1_seq = _pyfunc_map((function (x) {return x + 1;}), foo);
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    x = stub1_seq[stub2_itr];
}
```




```python
%%py2js

for x in filter(lambda x: x>0, foo):
    pass
```




```javascript
var _pyfunc_filter = function (func, iter) { // nargs: 2
    if (typeof func === "undefined" || func === null) {func = function(x) {return x;}}
    if ((typeof iter==="object") && (!Array.isArray(iter))) {iter = Object.keys(iter);}
    return iter.filter(func);
};
var stub1_seq, stub2_itr, x;
stub1_seq = _pyfunc_filter((function (x) {return x > 0;}), foo);
if ((typeof stub1_seq === "object") && (!Array.isArray(stub1_seq))) { stub1_seq = Object.keys(stub1_seq);}
for (stub2_itr = 0; stub2_itr < stub1_seq.length; stub2_itr += 1) {
    x = stub1_seq[stub2_itr];
}
```



#### list 推导


```python
%%py2js

# List comprehensions just work
x = [i*2 for i in some_array if i>0]
y = [i*j for i in a for j in b]
```




```javascript
var _pyfunc_op_mult = function (a, b) { // nargs: 2
    if ((typeof a === 'number') + (typeof b === 'number') === 1) {
        if (a.constructor === String) return _pymeth_repeat.call(a, b);
        if (b.constructor === String) return _pymeth_repeat.call(b, a);
        if (Array.isArray(b)) {var t=a; a=b; b=t;}
        if (Array.isArray(a)) {
            var res = []; for (var i=0; i<b; i++) res = res.concat(a);
            return res;
        }
    } return a * b;
};
var _pymeth_repeat = function(count) { // nargs: 0
    if (this.repeat) return this.repeat(count);
    if (count < 1) return '';
    var result = '', pattern = this.valueOf();
    while (count > 1) {
        if (count & 1) result += pattern;
        count >>= 1, pattern += pattern;
    }
    return result + pattern;
};
var stub1_, stub1_i, stub1_i0, stub1_iter0, stub2_, stub2_i, stub2_i0, stub2_i1, stub2_iter0, stub2_iter1, stub2_j, x, y;
stub1_ = [];stub1_iter0 = some_array;if ((typeof stub1_iter0 === "object") && (!Array.isArray(stub1_iter0))) {stub1_iter0 = Object.keys(stub1_iter0);}for (stub1_i0=0; stub1_i0<stub1_iter0.length; stub1_i0++) {stub1_i = stub1_iter0[stub1_i0];if (!((stub1_i > 0))) {continue;}{stub1_.push(_pyfunc_op_mult(stub1_i, 2));}}
x = stub1_;
stub2_ = [];stub2_iter0 = a;if ((typeof stub2_iter0 === "object") && (!Array.isArray(stub2_iter0))) {stub2_iter0 = Object.keys(stub2_iter0);}for (stub2_i0=0; stub2_i0<stub2_iter0.length; stub2_i0++) {stub2_i = stub2_iter0[stub2_i0];stub2_iter1 = b;if ((typeof stub2_iter1 === "object") && (!Array.isArray(stub2_iter1))) {stub2_iter1 = Object.keys(stub2_iter1);}for (stub2_i1=0; stub2_i1<stub2_iter1.length; stub2_i1++) {stub2_j = stub2_iter1[stub2_i1];{stub2_.push(_pyfunc_op_mult(stub2_i, stub2_j));}}}
y = stub2_;
```



#### 定义函数


```python
%%py2js

def display(val):
    print(val)
```




```javascript
var display;
display = function flx_display (val) {
    console.log(val);
    return null;
};

```




```python
%%py2js

# 支持 *args
def foo(x, *values):
    bar(x+1, *values)
```




```javascript
var foo;
foo = function flx_foo (x) {
    var values;
    values = Array.prototype.slice.call(arguments, 1);
    bar.apply(null, [].concat([x + 1], values));
    return null;
};

```




```python
%%py2js

# 想要混编JavaScript, 也可以使用RawJS
def bar(a, b):
    RawJS('''
    var c = 4;
    return a + b + c;
    ''')
```




```javascript
var bar;
bar = function flx_bar (a, b) {
    var c = 4;
    return a + b + c;;
    return null;
};

```




```python
%%py2js

# Lambda 表达式
foo = lambda x: x**2
```




```javascript
var foo;
foo = function (x) {return Math.pow(x, 2);};
```



#### 定义类

类被转换为JavaScript原型类paragigm，这意味着它们应该可以很好地与其他JS库一起使用。支持继承，但不支持多重继承。此外，super（）的工作方式与Python 3相同。


```python
%%py2js
class Foo:
    a_class_attribute = 4
    def __init__(self):
        self.x = 3
```




```javascript
var _pyfunc_op_instantiate = function (ob, args) { // nargs: 2
    if ((typeof ob === "undefined") ||
            (typeof window !== "undefined" && window === ob) ||
            (typeof global !== "undefined" && global === ob))
            {throw "Class constructor is called as a function.";}
    for (var name in ob) {
        if (Object[name] === undefined &&
            typeof ob[name] === 'function' && !ob[name].nobind) {
            ob[name] = ob[name].bind(ob);
            ob[name].__name__ = name;
        }
    }
    if (ob.__init__) {
        ob.__init__.apply(ob, args);
    }
};
var Foo;
Foo = function () {
    _pyfunc_op_instantiate(this, arguments);
}
Foo.prototype._base_class = Object;
Foo.prototype.__name__ = "Foo";

Foo.prototype.a_class_attribute = 4;
Foo.prototype.__init__ = function () {
    this.x = 3;
    return null;
};


```




```python
%%py2js

class Bar(Foo):
    def __init__(self):
        super.__init__()
        self.x += 1
    def add1(self):
        self.x += 1
```




```javascript
var _pyfunc_op_add = function (a, b) { // nargs: 2
    if (Array.isArray(a) && Array.isArray(b)) {
        return a.concat(b);
    } return a + b;
};
var _pyfunc_op_instantiate = function (ob, args) { // nargs: 2
    if ((typeof ob === "undefined") ||
            (typeof window !== "undefined" && window === ob) ||
            (typeof global !== "undefined" && global === ob))
            {throw "Class constructor is called as a function.";}
    for (var name in ob) {
        if (Object[name] === undefined &&
            typeof ob[name] === 'function' && !ob[name].nobind) {
            ob[name] = ob[name].bind(ob);
            ob[name].__name__ = name;
        }
    }
    if (ob.__init__) {
        ob.__init__.apply(ob, args);
    }
};
var Bar;
Bar = function () {
    _pyfunc_op_instantiate(this, arguments);
}
Bar.prototype = Object.create(Foo.prototype);
Bar.prototype._base_class = Foo.prototype;
Bar.prototype.__name__ = "Bar";

Bar.prototype.__init__ = function () {
    super.__init__();
    this.x = _pyfunc_op_add(this.x, 1);
    return null;
};

Bar.prototype.add1 = function () {
    this.x = _pyfunc_op_add(this.x, 1);
    return null;
};


```




```python
%%py2js

# 实例化和调用方法
b = Bar()
setTimeout(b.add1, 1000)
```




```javascript
var b;
b = new Bar();
setTimeout(b.add1, 1000);
```




```python
%%py2js
# Functions defined in methods (and that do not start with self or this)
# have ``this`` bound the the same object.
class Spam(Bar):
    def add_later(self):
        setTimeout(lambda ev: self.add1(), 1000)
```




```javascript
var _pyfunc_op_instantiate = function (ob, args) { // nargs: 2
    if ((typeof ob === "undefined") ||
            (typeof window !== "undefined" && window === ob) ||
            (typeof global !== "undefined" && global === ob))
            {throw "Class constructor is called as a function.";}
    for (var name in ob) {
        if (Object[name] === undefined &&
            typeof ob[name] === 'function' && !ob[name].nobind) {
            ob[name] = ob[name].bind(ob);
            ob[name].__name__ = name;
        }
    }
    if (ob.__init__) {
        ob.__init__.apply(ob, args);
    }
};
var Spam;
Spam = function () {
    _pyfunc_op_instantiate(this, arguments);
}
Spam.prototype = Object.create(Bar.prototype);
Spam.prototype._base_class = Bar.prototype;
Spam.prototype.__name__ = "Spam";

Spam.prototype.add_later = function () {
    setTimeout((function (ev) {return this.add1();}).bind(this), 1000);
    return null;
};


```



#### 异常

引发的异常将转换为JavaScript Error对象，其name属性设置为引发的异常类型。捕获异常时，将检查name属性（如果它是一个Error对象)。您可以`raise`字符串或任何其他类型的对象，但您只能捕获Error对象。


```python
%%py2js

# 抛出异常
raise SomeError('asd')
raise AnotherError()
raise "In JS you can throw anything"
raise 4
```




```javascript
var _pyfunc_op_error = function (etype, msg) { // nargs: 2
    var e = new Error(etype + ': ' + msg);
    e.name = etype
    return e;
};
var err_0;
throw _pyfunc_op_error('SomeError', "asd");
throw _pyfunc_op_error('AnotherError', "");
throw "In JS you can throw anything";
throw 4;
```




```python
%%py2js
# Assertions 能正常工作
assert foo == 3
assert bar == 4, "bar should be 4"
```




```javascript
var _pyfunc_op_equals = function op_equals (a, b) { // nargs: 2
    if (a == null || b == null) {
    } else if (Array.isArray(a) && Array.isArray(b)) {
        var i = 0, iseq = a.length == b.length;
        while (iseq && i < a.length) {iseq = op_equals(a[i], b[i]); i+=1;}
        return iseq;
    } else if (a.constructor === Object && b.constructor === Object) {
        var akeys = Object.keys(a), bkeys = Object.keys(b);
        akeys.sort(); bkeys.sort();
        var i=0, k, iseq = op_equals(akeys, bkeys);
        while (iseq && i < akeys.length)
            {k=akeys[i]; iseq = op_equals(a[k], b[k]); i+=1;}
        return iseq;
    } return a == b;
};
var _pyfunc_op_error = function (etype, msg) { // nargs: 2
    var e = new Error(etype + ': ' + msg);
    e.name = etype
    return e;
};
if (!(_pyfunc_op_equals(foo, 3))) { throw _pyfunc_op_error('AssertionError', "_pyfunc_op_equals(foo, 3)");}
if (!(_pyfunc_op_equals(bar, 4))) { throw _pyfunc_op_error('AssertionError', "\"bar should be 4\"");}
```




```python
%%py2js

# 捕捉异常
try:
    raise IndexError('blabla')
except IndexError as err:
    print(err)
except Exception:
   print('something went wrong')
```




```javascript
var _pyfunc_op_error = function (etype, msg) { // nargs: 2
    var e = new Error(etype + ': ' + msg);
    e.name = etype
    return e;
};
var err, err_1;
try {
    throw _pyfunc_op_error('IndexError', "blabla");
} catch(err_1) {
    if (err_1 instanceof Error && err_1.name === "IndexError") {
        err = err_1;
        console.log(err);
    } else {
        console.log("something went wrong");
    }
}
```



#### python内置函数

大多数buildin函数（在JS中有意义的）会自动转换为JavaScript的内建函数：isinstance，issubclass，callable，hasattr，getattr，setattr，delattr，print，len，max，min，chr，ord，dict，list，tuple，range， pow，sum，round，int，float，str，bool，abs，divmod，all，any，enumerate，zip，reversed，sorted，filtered，map。

此外，还实现了list，dict和str的所有方法（str方法除外：encode，decode，format，format_map，isdecimal，isdigit，isprintable，maketrans）。


```python
%%py2js
# Printing 能正常工作
print('some test')
print(a, b, c, sep='-')
```




```javascript
console.log("some test");
console.log(a + "-" + b + "-" + c);
```




```python
%%py2js
# 获取字符串长度
len(foo)
```




```javascript
foo.length;
```




```python
%%py2js
# 保留小数和绝对值
round(foo)  # round to nearest integer
int(foo)  # round towards 0 as in Python
abs(foo)
```




```javascript
var _pyfunc_abs = Math.abs;
var _pyfunc_int = function (x) { // nargs: 1
    return x<0 ? Math.ceil(x): Math.floor(x);
};
var _pyfunc_round = Math.round;
_pyfunc_round(foo);
_pyfunc_int(foo);
_pyfunc_abs(foo);
```




```python
%%py2js
# 最大值和最小值
min(foo)
min(a, b, c)
max(foo)
max(a, b, c)
```




```javascript
Math.min.apply(null, foo);
Math.min(a, b, c);
Math.max.apply(null, foo);
Math.max(a, b, c);
```




```python
%%py2js
# 求余数
a, b = divmod(100, 7)  # -> 14, 2
```




```javascript
var _pyfunc_divmod = function (x, y) { // nargs: 2
    var m = x % y; return [(x-m)/y, m];
};
var a, b, stub1_;
stub1_ = _pyfunc_divmod(100, 7);
a = stub1_[0];b = stub1_[1];
```




```python
%%py2js
# 聚合
sum(foo)
all(foo)
any(foo)
```




```javascript
var _pyfunc_all = function (x) { // nargs: 1
    for (var i=0; i<x.length; i++) {
        if (!_pyfunc_truthy(x[i])){return false;}
    } return true;
};
var _pyfunc_any = function (x) { // nargs: 1
    for (var i=0; i<x.length; i++) {
        if (_pyfunc_truthy(x[i])){return true;}
    } return false;
};
var _pyfunc_sum = function (x) {  // nargs: 1
    return x.reduce(function(a, b) {return a + b;});
};
var _pyfunc_truthy = function (v) {
    if (v === null || typeof v !== "object") {return v;}
    else if (v.length !== undefined) {return v.length ? v : false;}
    else if (v.byteLength !== undefined) {return v.byteLength ? v : false;}
    else if (v.constructor !== Object) {return true;}
    else {return Object.getOwnPropertyNames(v).length ? v : false;}
};
_pyfunc_sum(foo);
_pyfunc_all(foo);
_pyfunc_any(foo);
```




```python
%%py2js
# 数据转换: numbers, bools and strings
str(s)
float(x)
bool(y)
int(z)  # this rounds towards zero like in Python
chr(65)  # -> 'A'
ord('A')  # -> 65
```




```javascript
var _pyfunc_bool = function (x) { // nargs: 1
    return Boolean(_pyfunc_truthy(x));
};
var _pyfunc_float = Number;
var _pyfunc_int = function (x) { // nargs: 1
    return x<0 ? Math.ceil(x): Math.floor(x);
};
var _pyfunc_str = String;
var _pyfunc_truthy = function (v) {
    if (v === null || typeof v !== "object") {return v;}
    else if (v.length !== undefined) {return v.length ? v : false;}
    else if (v.byteLength !== undefined) {return v.byteLength ? v : false;}
    else if (v.constructor !== Object) {return true;}
    else {return Object.getOwnPropertyNames(v).length ? v : false;}
};
_pyfunc_str(s);
_pyfunc_float(x);
_pyfunc_bool(y);
_pyfunc_int(z);
String.fromCharCode(65);
"A".charCodeAt(0);
```




```python
%%py2js
# 数据转换成 lists and dicts
dict([['foo', 1], ['bar', 2]])  # -> {'foo': 1, 'bar': 2}
list('abc')  # -> ['a', 'b', 'c']
dict(other_dict)  # make a copy
list(other_list)  # make copy
```




```javascript
var _pyfunc_dict = function (x) {
    var t, i, keys, r={};
    if (Array.isArray(x)) {
        for (i=0; i<x.length; i++) {
            t=x[i]; r[t[0]] = t[1];
        }
    } else {
        keys = Object.keys(x);
        for (i=0; i<keys.length; i++) {
            t=keys[i]; r[t] = x[t];
        }
    }
    return r;
};
var _pyfunc_list = function (x) {
    var r=[];
    if (typeof x==="object" && !Array.isArray(x)) {x = Object.keys(x)}
    for (var i=0; i<x.length; i++) {
        r.push(x[i]);
    }
    return r;
};
_pyfunc_dict(([["foo", 1], ["bar", 2]]));
_pyfunc_list("abc");
_pyfunc_dict(other_dict);
_pyfunc_list(other_list);
```



#### isinstance相关功能


```python
%%py2js
# 基本类型
isinstance(3, float)  # in JS there are no ints
isinstance('', str)
isinstance([], list)
isinstance({}, dict)
isinstance(foo, types.FunctionType)
```




```javascript
Object.prototype.toString.call(3).slice(8,-1).toLowerCase() === 'number';
Object.prototype.toString.call("").slice(8,-1).toLowerCase() === 'string';
Array.isArray([]);
Object.prototype.toString.call(({})).slice(8,-1).toLowerCase() === 'object';
Object.prototype.toString.call(foo).slice(8,-1).toLowerCase() === 'function';
```




```python
%%py2js
# 也可以用JS的字符串
isinstance(3, 'number')
isinstance('', 'string')
isinstance([], 'array')
isinstance({}, 'object')
isinstance(foo, 'function')
```




```javascript
Object.prototype.toString.call(3).slice(8,-1).toLowerCase() === 'number';
Object.prototype.toString.call("").slice(8,-1).toLowerCase() === 'string';
Array.isArray([]);
Object.prototype.toString.call(({})).slice(8,-1).toLowerCase() === 'object';
Object.prototype.toString.call(foo).slice(8,-1).toLowerCase() === 'function';
```




```python
%%py2js
# 可以用于自定义类型.
isinstance(x, MyClass)
isinstance(x, 'MyClass')  # equivalent
isinstance(x, 'Object')  # also yields true (subclass of Object)
```




```javascript
x instanceof MyClass;
x instanceof MyClass;
Object.prototype.toString.call(x).slice(8,-1).toLowerCase() === 'object';
```




```python
%%py2js
# issubclass 也能正常工作
issubclass(Foo, Bar)
```




```javascript
(Foo.prototype instanceof Bar);
```




```python
%%py2js
# callable也能正常工作
callable(foo)
```




```javascript
(typeof foo === "function");
```



#### hasattr, getattr, setattr and delattr


```python
%%py2js

a = {'foo': 1, 'bar': 2}
hasattr(a, 'foo')  # -> True
hasattr(a, 'fooo')  # -> False
hasattr(null, 'foo')  # -> False
getattr(a, 'foo')  # -> 1
getattr(a, 'fooo')  # -> raise AttributeError
getattr(a, 'fooo', 3)  # -> 3
getattr(null, 'foo', 3)  # -> 3
```




```javascript
var _pyfunc_getattr = function (ob, name, deflt) { // nargs: 2 3
    var has_attr = ob !== undefined && ob !== null && ob[name] !== undefined;
    if (has_attr) {return ob[name];}
    else if (arguments.length == 3) {return deflt;}
    else {var e = Error(name); e.name='AttributeError'; throw e;}
};
var _pyfunc_hasattr = function (ob, name) { // nargs: 2
    return (ob !== undefined) && (ob !== null) && (ob[name] !== undefined);
};
var a;
a = ({foo: 1, bar: 2});
_pyfunc_hasattr(a, "foo");
_pyfunc_hasattr(a, "fooo");
_pyfunc_hasattr(null, "foo");
_pyfunc_getattr(a, "foo");
_pyfunc_getattr(a, "fooo");
_pyfunc_getattr(a, "fooo", 3);
_pyfunc_getattr(null, "foo", 3);
```




```python
%%py2js

setattr(a, 'foo', 2)
```




```javascript
var _pyfunc_setattr = function (ob, name, value) {  // nargs: 3
    ob[name] = value;
};
_pyfunc_setattr(a, "foo", 2);
```




```python
%%py2js

delattr(a, 'foo')
```




```javascript
var _pyfunc_delattr = function (ob, name) {  // nargs: 2
    delete ob[name];
};
_pyfunc_delattr(a, "foo");
```



#### 使用JS专属功能

在Python模块中编写PyScript时，我们建议在使用特定JavaScript功能的地方，引用以window为前缀。其中window表示全局JS命名空间。所有全局JavaScript对象/函数和变量都自动成为window对象的成员。这有助于明确该功能是JS特有的，还有助于像flake8这样的静态代码分析工具。

除了window, flexx.pyscript 也提供 undefined, Inifinity, 和 NaN.


```python
%%py2js

def foo(a):
    return window.Math.cos(a)
```




```javascript
var foo;
foo = function flx_foo (a) {
    return window.Math.cos(a);
};

```




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pyscript用python写JavaScript.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
