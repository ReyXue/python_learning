def list_demo() -> None:
	fruits = ["apple", "banana", "cherry"]
	fruits.append("date")
	print("list:", fruits, "len=", len(fruits))


def tuple_demo() -> None:
	point = (10, 20)
	x, y = point
	print("tuple:", point, "x=", x, "y=", y)


def dict_demo() -> None:
	person = {"name": "Alice", "age": 30}
	person["city"] = "Shanghai"
	print("dict:", person)


def set_demo() -> None:
	unique_numbers = {1, 2, 2, 3}
	unique_numbers.add(4)
	print("set:", unique_numbers)


if __name__ == "__main__":
	list_demo()
	tuple_demo()
	dict_demo()
	set_demo()
