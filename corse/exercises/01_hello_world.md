# 01 入门：Hello World

## 练习
1) 打印 `Hello, World!`。
2) 打印两行欢迎语。
3) 编写函数 `greet(name)` 返回 `你好, <name>!`。

## 参考答案
```python
def greet(name: str) -> str:
    return f"你好, {name}!"

print("Hello, World!")
print("欢迎学习 Python")
print("一起开始吧！")
print(greet("同学"))
```

## 思考与扩展
- 使用 `input()` 获取用户名，并调用 `greet` 打印问候。
