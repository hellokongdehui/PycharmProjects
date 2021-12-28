# Author:D.辉
# Place：哈工深
# Time：2021/08/13 22:12
# 9.4.6 在一个模块中导入另一个模块

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2024)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2024)
print(my_tesla.get_descriptive_name())
