# 05 条件分支

## 练习
1) 分数转等级函数 `grade(score)`：90+ 优秀，80-89 良好，60-79 及格，否则不及格。
2) 判断闰年：能被400整除或被4整除但不被100整除。
3) BMI 分类：<18.5 偏瘦，18.5-23.9 正常，24-27.9 偏重，≥28 肥胖。

## 参考答案
```python
def grade(score: int) -> str:
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def bmi_category(weight: float, height: float) -> str:
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "偏瘦"
    if bmi < 24:
        return "正常"
    if bmi < 28:
        return "偏重"
    return "肥胖"
```

## 思考与扩展
- 为 `bmi_category` 增加输入校验（非正数时抛出异常或返回提示）。
