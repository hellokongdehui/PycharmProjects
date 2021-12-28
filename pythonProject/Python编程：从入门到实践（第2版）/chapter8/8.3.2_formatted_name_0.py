# Author：D.H
# Place：哈工深
# Time：2021/7/31 7:47
# 8.3.2 让实参变成可选
def get_formatted_name(first_name, last_name, middle_name=' '):
    """返回整洁的姓名"""
    if middle_name:  # 表示 if middle_name 将为True， 非空字符串为True，
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
