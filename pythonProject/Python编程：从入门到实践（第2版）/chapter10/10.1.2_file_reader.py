# Author:D.辉
# Place：哈工深
# Time：2021/08/14 23:44
# 10.1.2 文件路径

with open('text_files/pi_digits2.txt') as file_object:  # 相对路径打开
    contents = file_object.read()
print(contents.rstrip())

# 绝对路径可以先赋予变量，记得加上文件名。
file_path = 'D:/PycharmProjects/pythonProject/Python编程：从入门到实践（第2版）/chapter10/text_files/pi_digits2.txt'
with open(file_path) as file_object:  # 绝对路径打开
    contents = file_object.read()
print(contents.rstrip())
