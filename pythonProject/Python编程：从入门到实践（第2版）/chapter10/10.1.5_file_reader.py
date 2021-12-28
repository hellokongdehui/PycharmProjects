# Author:D.辉
# Place：哈工深
# Time：2021/08/16 21:15
# 10.1.5 使用文件的内容

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
