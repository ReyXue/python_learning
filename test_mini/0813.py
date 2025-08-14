'''
Author: xuesl xuesl@yeesun.com
Date: 2025-08-13 10:39:20
LastEditors: xuesl xuesl@yeesun.com
LastEditTime: 2025-08-13 16:59:40
FilePath: /Python/test1/0813.py
Description: Python数据类型
'''
# 字符串
# print("hello world")
# print("hello \'world\''")
# print("hello \"world\"")
# print(r"hello 'world'")
# print(r'''hello,
# world1
# world2''')

# 数字，浮点数
# print(100)
# print(100.1)

#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
num = (85-72) / 72;
format_num = "%.1f%%" % (num * 100)
# print(format_num)

# list 类似JS的数组类型
# list = [1,2,3,4,5]
# list.append(6)
# list.insert(0,0) # 在0的位置插入0
# list.pop() # 删除最后一个元素
# list.pop(0) # 删除第一个元素
# list.remove(3) # 删除指定元素
# list.sort() # 排序
# list.reverse() # 反转
# list.clear() # 清空
# print(list)
# print(list[1])

#tuple 元组，不可变列表，一旦初始化就不能修改
tuple = (1,2,3,4,5)
tuple2 = (1,) # 元组中只有一个元素时，需要加逗号
print(tuple)
print(tuple[1])













