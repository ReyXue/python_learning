def arithmetic_demo() -> None:
    a = 7
    b = 3
    print("加法:", a + b)
    print("减法:", a - b)
    print("乘法:", a * b)
    print("除法(浮点):", a / b)
    print("整除:", a // b)
    print("取余:", a % b)
    print("幂:", a ** b)


def comparison_and_logical_demo() -> None:
    x = 10
    y = 20
    print("x == y:", x == y)
    print("x != y:", x != y)
    print("x > y:", x > y)
    print("x < y:", x < y)
    print("x >= y:", x >= y)
    print("x <= y:", x <= y)

    is_adult = True
    has_ticket = False
    print("and:", is_adult and has_ticket)
    print("or:", is_adult or has_ticket)
    print("not:", not is_adult)


def membership_and_identity_demo() -> None:
    letters = ["a", "b", "c"]
    print("'a' in letters:", "a" in letters)
    print("'z' not in letters:", "z" not in letters)

    p = [1, 2, 3]
    q = p
    r = [1, 2, 3]
    print("p is q:", p is q)
    print("p is r:", p is r)


if __name__ == "__main__":
    arithmetic_demo()
    comparison_and_logical_demo()
    membership_and_identity_demo()
