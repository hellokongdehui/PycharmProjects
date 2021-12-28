# Author:D.辉
# Place：哈工深
# Time：2021/08/19 19:33
# 11.1 测试函数

def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
