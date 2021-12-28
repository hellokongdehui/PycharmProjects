# Author:D.辉
# Place：哈工深
# Time：2021/08/16 21:34
# 10.1.6 包含一百万位的大型文件

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")  # [:52] 取小数点后52位
print(len(pi_string))
