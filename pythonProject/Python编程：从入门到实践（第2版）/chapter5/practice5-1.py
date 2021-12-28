# Author：D.H
# Place：哈工深
# Time：2021/7/26 21:29
#练习5-1：条件测试
car = 'subaru'
if car == 'subaru':
    print('you are right! that car is subaru.')
else:
    print('sorry! you are wrong!')

print('==========p63============')
# 5.1 一个简单的的示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())