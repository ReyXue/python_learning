# 07 函数

## 练习
1) 实现 `factorial(n)`（阶乘），用循环与递归两种方式。
2) 实现 `greet(name, prefix="你好")`，并写 docstring。
3) 实现 `summation(*numbers)`，可变参数求和。

## 参考答案
```python
def factorial_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n 必须非负")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("n 必须非负")
    if n in (0, 1):
        return 1
    return n * factorial_rec(n - 1)


def greet(name: str, prefix: str = "你好") -> str:
    """返回问候语，例如 greet("小明") -> "你好, 小明!"""
    return f"{prefix}, {name}!"


def summation(*numbers: int) -> int:
    total = 0
    for x in numbers:
        total += x
    return total
```

## 思考与扩展
- 对 `factorial_rec` 添加尾递归优化讨论（Python 不优化尾递归）。
