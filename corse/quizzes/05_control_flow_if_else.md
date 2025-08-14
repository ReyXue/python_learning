# 05 条件分支：小测

1) `if-elif-else` 结构中，满足一个条件后会继续判断剩余条件吗？
- A. 会
- B. 不会

答案：B。

2) 判断闰年的表达式 `year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)` 是否正确？
- A. 正确
- B. 错误

答案：A。

3) `if x:` 中 x 的真假性，以下哪个会被判定为 False？
- A. 1
- B. "0"
- C. []
- D. [0]

答案：C。空容器为 False。

4) `if a and b:`，当 `a` 为 False 时 `b` 会被求值吗？
- A. 会
- B. 不会

答案：B。短路求值。

5) `if not x:` 等价于？
- A. `if x == False:`
- B. `if bool(x) is False:`
- C. 语义上等价，风格上 A 更 Pythonic

答案：C。
