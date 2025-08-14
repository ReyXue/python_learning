from typing import List


def add(a: int, b: int = 0) -> int:
	return a + b


def greet(name: str, prefix: str = "你好") -> str:
	return f"{prefix}, {name}!"


def sum_list(numbers: List[int]) -> int:
	total = 0
	for n in numbers:
		total += n
	return total


if __name__ == "__main__":
	print(add(3, 4))
	print(greet("Python"))
	print(sum_list([1, 2, 3, 4]))
