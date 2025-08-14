# 08 容器：列表/元组/字典/集合

## 练习
1) 列表增删改查：添加两个元素、删除一个元素、切片获取前两个。
2) 元组拆包赋值：交换 `a` 与 `b` 的值。
3) 字典计数：统计一句话中各单词出现次数。
4) 集合去重：从列表生成不重复元素集合。

## 参考答案
```python
# 1)
nums = [1, 2, 3]
nums.append(4)
nums.append(5)
del nums[1]
print(nums[:2])

# 2)
a, b = 10, 20
a, b = b, a
print(a, b)

# 3)
from collections import Counter
text = "to be or not to be"
words = text.split()
count = dict(Counter(words))
print(count)

# 4)
arr = [1,2,2,3,3,3]
unique = set(arr)
print(unique)
```

## 思考与扩展
- 使用 `defaultdict(int)` 手写词频统计。
