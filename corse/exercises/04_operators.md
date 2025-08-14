# 04 运算符

## 练习
1) 计算两个整数的加减乘除、整除、取余与幂。
2) 编写表达式判断某数是否在闭区间 [10, 20]。
3) 使用 `in`/`not in` 与 `is`/`is not` 进行演示。

## 参考答案
```python
a, b = 7, 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

x = 15
print(10 <= x <= 20)

letters = ["a", "b"]
print("a" in letters, "z" not in letters)
p = [1,2,3]
q = p
r = [1,2,3]
print(p is q, p is r)
```

## 思考与扩展
- 比较 `==` 与 `is` 的区别。
