# 06 循环

## 练习
1) 计算 1..n 的和，要求分别用 `for` 与 `while`。
2) 打印 9x9 乘法表（左上三角）。
3) 找出区间 [2, 50] 内的所有质数。

## 参考答案
```python
def sum_to_n_for(n: int) -> int:
    s = 0
    for i in range(1, n + 1):
        s += i
    return s


def sum_to_n_while(n: int) -> int:
    s, i = 0, 1
    while i <= n:
        s += i
        i += 1
    return s


def print_multiplication_table() -> None:
    for i in range(1, 10):
        row = []
        for j in range(1, i + 1):
            row.append(f"{j}x{i}={i*j}")
        print("\t".join(row))


def primes_between(a: int, b: int) -> list[int]:
    result = []
    for x in range(max(2, a), b + 1):
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0:
                break
        else:
            result.append(x)
    return result
```

## 思考与扩展
- 将质数生成改为生成器函数，惰性产生质数。
