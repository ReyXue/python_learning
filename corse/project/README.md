# 综合项目：CLI 待办清单

目标：实现一个命令行待办清单（To-Do）工具，支持添加、列出、完成、删除任务，并持久化到本地 `JSON` 文件。

## 功能清单
- 添加任务：标题、可选优先级（low/medium/high）
- 列出任务：按创建时间或优先级排序，支持过滤状态（未完成/已完成）
- 完成任务：按 ID 标记完成
- 删除任务：按 ID 删除
- 持久化：`data/todos.json`

## 快速开始
```powershell
cd E:\Python\corse\project
python todo.py add "学习 Python" --priority high
python todo.py list --status pending
python todo.py done 1
python todo.py remove 1
```

## 进阶要求
- 异常与错误处理（无效 ID、重复标题等）
- 文件读写的健壮性（文件不存在时自动创建）
- 代码结构化（模块/函数划分明确，类型注解）
- 单元测试（可选）
