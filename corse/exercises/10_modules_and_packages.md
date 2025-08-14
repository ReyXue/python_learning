# 10 模块与包

## 练习
1) 分别使用 `math`、`datetime`、`sys` 输出常用信息。
2) 编写自定义模块 `utils.py`，实现 `add(a,b)` 并在主脚本中导入使用。
3) 了解包结构：创建 `pkg/__init__.py` 与 `pkg/helper.py`，在主脚本中导入。

## 参考答案
```python
import math
from datetime import datetime
import sys
print(math.pi, math.isqrt(16))
print(datetime.now())
print(sys.version)

# utils.py
# def add(a, b):
#     return a + b

# main.py
# from utils import add
# print(add(3, 4))
```

## 思考与扩展
- 尝试相对导入与绝对导入的区别。
