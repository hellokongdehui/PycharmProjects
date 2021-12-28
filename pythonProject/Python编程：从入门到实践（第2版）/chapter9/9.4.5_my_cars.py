# Author:D.辉
# Place：哈工深
# Time：2021/08/13 20:56
# 9.4.5 导入模块中的所有类

from car import *

my_beetle = Car('volkswagen', 'beetle', 2023)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2023)
print(my_tesla.get_descriptive_name())
