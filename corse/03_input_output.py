def format_output(name: str, age: int) -> None:
    print("你好, %s! 你今年 %d 岁。" % (name, age))
    print("你好, {}! 你今年 {} 岁。".format(name, age))
    print(f"你好, {name}! 你今年 {age} 岁。")


def main() -> None:
    # 注意: 运行到这里会等待用户输入
    name = input("请输入你的名字: ")
    age_text = input("请输入你的年龄: ")
    try:
        age = int(age_text)
    except ValueError:
        print("年龄应为整数，已将其设为 0。")
        age = 0

    format_output(name, age)


if __name__ == "__main__":
    main()
