import math
import sys
from datetime import datetime


def show_stdlib_usage() -> None:
	print("math.pi:", math.pi)
	print("sqrt(16):", math.isqrt(16))
	print("当前时间:", datetime.now())
	print("Python 版本:", sys.version)


if __name__ == "__main__":
	show_stdlib_usage()
