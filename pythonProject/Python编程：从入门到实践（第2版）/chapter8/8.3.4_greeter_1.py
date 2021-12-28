# Author：D.H
# Place：哈工深
# Time：2021/7/31 8:25
# 8.3.4 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# 这是一个无限循环！
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':  # 设置随时停止的条件
        break

    l_name = input("Last name:")
    if f_name == 'q':  # 设置随时停止的条件
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")