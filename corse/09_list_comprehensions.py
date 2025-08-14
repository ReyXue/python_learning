def list_comprehensions_demo() -> None:
	squares = [n * n for n in range(6)]
	evens = [n for n in range(10) if n % 2 == 0]
	pairs = [(x, y) for x in range(3) for y in range(2)]
	print("squares:", squares)
	print("evens:", evens)
	print("pairs:", pairs)


if __name__ == "__main__":
	list_comprehensions_demo()
