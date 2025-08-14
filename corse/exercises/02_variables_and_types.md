# 02 变量与类型

## 练习
1) 创建整数、浮点数、字符串、布尔变量并打印其 `type()`。
2) 展示动态类型：让同一变量先保存整数，再保存字符串。
3) 将字符串形式的数字转换为整数参与加法。

## 参考答案
```python
x = 42
pi = 3.14
lang = "Python"
flag = True
print(type(x), type(pi), type(lang), type(flag))

v = 10
print(v, type(v))
v = "now string"
print(v, type(v))

text = "123"
num = int(text)
print(num + 7)
```

## 思考与扩展
- 尝试 `float("3.14")`、`str(100)` 等相互转换。
