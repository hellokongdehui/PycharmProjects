# Author：D.H
# Place：哈工深
# Time：2021/7/31 7:29
# 8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)