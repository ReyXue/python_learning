def show_basic_types() -> None:
    integer_value = 42
    float_value = 3.14159
    string_value = "Python"
    boolean_value = True

    print("整数:", integer_value, type(integer_value))
    print("浮点数:", float_value, type(float_value))
    print("字符串:", string_value, type(string_value))
    print("布尔值:", boolean_value, type(boolean_value))


def dynamic_typing_demo() -> None:
    value = 10
    print("初始:", value, type(value))
    value = "现在是字符串"
    print("重新赋值后:", value, type(value))


if __name__ == "__main__":
    show_basic_types()
    dynamic_typing_demo()
