def safe_divide(a: float, b: float) -> float:
	try:
		return a / b
	except ZeroDivisionError:
		print("错误: 不能除以 0。")
		return float("inf")
	finally:
		pass


if __name__ == "__main__":
	print(safe_divide(10, 2))
	print(safe_divide(10, 0))
