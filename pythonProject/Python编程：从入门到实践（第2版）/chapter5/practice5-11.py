# Author：D.H
# Place：哈工深
# Time：2021/7/27 16:32
# 练习5-11：序数
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for num in nums:
    if num == '1':
        print('1st')
    elif num == '2':
        print('2nd')
    elif num == '3':
        print('3rd')
    elif num == '4':
        print('4th')
    elif num == '5':
        print('6th')
    elif num == '7':
        print('7th')
    elif num == '8':
        print('8th')
    elif num == '9':
        print('9th')

print('-------------------')# 版本2
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')