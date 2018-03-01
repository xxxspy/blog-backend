---
title: 'python错误(ValueError: source code string cannot contain null bytes)'
date: 2018-03-01 13:55:56
tags: [python]
---

read more

<!--more-->

今天在开发的时候发现一只无法引用我自己的库``, 代码是这样的:

```python
from wikicorpus import wikicorpus
import unittest

class TestExtactCategory(unittest.TestCase):
    def test_(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

错误是:

```cmd
ValueError: source code string cannot contain null bytes
```

我们纳闷, 找不到问题在哪, 而且没有详细的错误提示. 经过Google以后, 我发现我的这个库有一个模块只有一个换行符`\n`. 这个文件就是`wikicorpus/__init__.py`. 所以每次import的时候就会运行这个空文件. 导致错误`ValueError: source code string cannot contain null bytes`. 只要删除空行就行了.
