def grade_message(score: int) -> str:
	if score >= 90:
		return "优秀"
	elif score >= 80:
		return "良好"
	elif score >= 60:
		return "及格"
	else:
		return "不及格"


def main() -> None:
	scores = [95, 83, 61, 40]
	for s in scores:
		print(s, grade_message(s))


if __name__ == "__main__":
	main()
