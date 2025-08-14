# 11 异常处理

## 练习
1) 实现安全除法 `safe_div(a,b)`，当 b=0 时返回 `None` 并打印友好提示。
2) 使用 `try/except/else/finally` 完整结构读文件，不存在时创建默认内容。
3) 自定义异常 `InvalidScoreError`，当分数不在 0..100 时抛出。

## 参考答案
```python
class InvalidScoreError(ValueError):
    pass


def safe_div(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("不能除以 0")
        return None


def read_or_create(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        with open(path, "w", encoding="utf-8") as f:
            f.write("default")
        return "default"
    finally:
        pass


def set_score(score: int) -> None:
    if not (0 <= score <= 100):
        raise InvalidScoreError("分数范围应为 0..100")
```

## 思考与扩展
- 日志记录：将异常写入日志文件。
