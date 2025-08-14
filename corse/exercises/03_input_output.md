# 03 输入与输出

## 练习
1) 使用 `input()` 读取姓名与年龄，打印三种格式化输出（`%`、`str.format`、`f-string`）。
2) 当年龄不是整数时给出提示并置为 0。

## 参考答案
```python
def show(name: str, age: int) -> None:
    print("你好, %s! 你今年 %d 岁。" % (name, age))
    print("你好, {}! 你今年 {} 岁。".format(name, age))
    print(f"你好, {name}! 你今年 {age} 岁。")

name = input("姓名: ")
age_text = input("年龄: ")
try:
    age = int(age_text)
except ValueError:
    print("年龄应为整数，已设为 0")
    age = 0
show(name, age)
```

## 思考与扩展
- 使用 `strip()` 移除输入首尾空白。
