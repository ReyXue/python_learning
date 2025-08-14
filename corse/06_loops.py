def for_loop_demo() -> None:
	for i in range(5):
		if i == 2:
			continue
		print("for:", i)


def while_loop_demo() -> None:
	count = 0
	while count < 5:
		if count == 3:
			break
		print("while:", count)
		count += 1


if __name__ == "__main__":
	for_loop_demo()
	while_loop_demo()
