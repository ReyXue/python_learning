# 09 推导式

## 练习
1) 生成 0..9 的平方列表。
2) 从 0..20 中筛选偶数，生成集合。
3) 二维坐标对列表：`(x, y)`，`x=0..2, y=0..1`。
4) 字典推导式：将单词映射为长度，如 `{word: len(word)}`。

## 参考答案
```python
squares = [n * n for n in range(10)]
evens = {n for n in range(21) if n % 2 == 0}
pairs = [(x, y) for x in range(3) for y in range(2)]
words = ["python", "is", "fun"]
length_map = {w: len(w) for w in words}
print(squares, evens, pairs, length_map)
```

## 思考与扩展
- 试用嵌套推导式扁平化二维列表。
