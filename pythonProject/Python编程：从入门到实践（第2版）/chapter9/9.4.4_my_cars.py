# Author:D.辉
# Place：哈工深
# Time：2021/08/13 20:51
# 9.4.4 导入整个模块

import car

my_beetle = car.Car('volkswagen', 'beetle', 2022)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2022)
print(my_tesla.get_descriptive_name())
