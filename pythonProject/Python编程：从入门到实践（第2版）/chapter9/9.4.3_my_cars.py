# Author:D.辉
# Place：哈工深
# Time：2021/08/13 20:44
# 9.4.3 从一个模块中导入多个类

from car import Car,ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2021)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2021)
print(my_tesla.get_descriptive_name())
