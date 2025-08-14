from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Literal

DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "todos.json"


Priority = Literal["low", "medium", "high"]
Status = Literal["pending", "done"]


@dataclass
class Todo:
	id: int
	title: str
	priority: Priority = "medium"
	status: Status = "pending"


def ensure_storage() -> None:
	DATA_DIR.mkdir(parents=True, exist_ok=True)
	if not DATA_FILE.exists():
		DATA_FILE.write_text("[]", encoding="utf-8")


def load_todos() -> List[Todo]:
	ensure_storage()
	raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
	return [Todo(**item) for item in raw]


def save_todos(todos: List[Todo]) -> None:
	DATA_FILE.write_text(json.dumps([asdict(t) for t in todos], ensure_ascii=False, indent=2), encoding="utf-8")


def cmd_add(args: argparse.Namespace) -> None:
	todos = load_todos()
	new_id = (max((t.id for t in todos), default=0) + 1)
	if any(t.title == args.title for t in todos):
		raise ValueError("标题已存在，请更换或先完成/删除旧任务")
	todo = Todo(id=new_id, title=args.title, priority=args.priority)
	todos.append(todo)
	save_todos(todos)
	print(f"已添加: [{todo.id}] {todo.title} ({todo.priority})")


def cmd_list(args: argparse.Namespace) -> None:
	todos = load_todos()
	if args.status:
		todos = [t for t in todos if t.status == args.status]
	if args.sort == "priority":
		order = {"high": 0, "medium": 1, "low": 2}
		todos.sort(key=lambda t: order[t.priority])
	else:
		todos.sort(key=lambda t: t.id)
	for t in todos:
		mark = "✓" if t.status == "done" else " "
		print(f"[{t.id}] [{mark}] {t.title} ({t.priority})")


def cmd_done(args: argparse.Namespace) -> None:
	todos = load_todos()
	for t in todos:
		if t.id == args.id:
			t.status = "done"
			save_todos(todos)
			print(f"已完成: [{t.id}] {t.title}")
			return
	raise ValueError("未找到对应 ID 的任务")


def cmd_remove(args: argparse.Namespace) -> None:
	todos = load_todos()
	new_list = [t for t in todos if t.id != args.id]
	if len(new_list) == len(todos):
		raise ValueError("未找到对应 ID 的任务")
	save_todos(new_list)
	print(f"已删除: ID {args.id}")


def build_parser() -> argparse.ArgumentParser:
	p = argparse.ArgumentParser(prog="todo", description="命令行待办清单")
	sub = p.add_subparsers(dest="command", required=True)

	p_add = sub.add_parser("add", help="添加任务")
	p_add.add_argument("title", type=str)
	p_add.add_argument("--priority", choices=["low", "medium", "high"], default="medium")
	p_add.set_defaults(func=cmd_add)

	p_list = sub.add_parser("list", help="列出任务")
	p_list.add_argument("--status", choices=["pending", "done"], default=None)
	p_list.add_argument("--sort", choices=["id", "priority"], default="id")
	p_list.set_defaults(func=cmd_list)

	p_done = sub.add_parser("done", help="完成任务")
	p_done.add_argument("id", type=int)
	p_done.set_defaults(func=cmd_done)

	p_rm = sub.add_parser("remove", help="删除任务")
	p_rm.add_argument("id", type=int)
	p_rm.set_defaults(func=cmd_remove)

	return p


def main() -> None:
	parser = build_parser()
	args = parser.parse_args()
	try:
		args.func(args)
	except Exception as exc:
		print("错误:", exc)


if __name__ == "__main__":
	main()
