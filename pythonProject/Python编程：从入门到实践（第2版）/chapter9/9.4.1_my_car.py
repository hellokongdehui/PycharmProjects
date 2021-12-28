# Author：D.H
# Place：哈工深
# Time：2021/8/11 23:52
# 9.4.1 导入单个类

from car import Car

my_new_car = Car('audi', 'a4l', '2021')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
