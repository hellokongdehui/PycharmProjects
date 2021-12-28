# Author:D.辉
# Place：哈工深
# Time：2021/08/16 21:41
# 10.1.7 file_reader

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday, in the form mmddyy:')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
