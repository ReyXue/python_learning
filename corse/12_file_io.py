from pathlib import Path


def write_and_read_text(file_path: Path) -> None:
	content = "Hello, file!\n这是第二行。\n"
	file_path.write_text(content, encoding="utf-8")
	read_back = file_path.read_text(encoding="utf-8")
	print("读取到的内容:\n" + read_back)


if __name__ == "__main__":
	tmp = Path("example.txt")
	write_and_read_text(tmp)
