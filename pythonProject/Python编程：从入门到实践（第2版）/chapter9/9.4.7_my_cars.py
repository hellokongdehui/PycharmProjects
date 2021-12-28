# Author:D.辉
# Place：哈工深
# Time：2021/08/13 23:03
# 9.4.7 使用别名

from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2023)
print(my_tesla.get_descriptive_name())
