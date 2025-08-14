# 12 文件读写

## 练习
1) 写入多行文本到 `example.txt`，再读取并打印。
2) 统计文件行数、单词数、字符数（简化版 wc）。
3) 使用 `pathlib.Path` 判断文件是否存在、大小、修改时间。

## 参考答案
```python
from pathlib import Path
p = Path("example.txt")
p.write_text("Hello\nPython\n", encoding="utf-8")
print(p.read_text(encoding="utf-8"))

text = p.read_text(encoding="utf-8")
lines = text.splitlines()
words = text.split()
print("lines=", len(lines), "words=", len(words), "chars=", len(text))

print(p.exists(), p.stat().st_size)
```

## 思考与扩展
- 使用 `with open()` 进行大文件逐行读取。
