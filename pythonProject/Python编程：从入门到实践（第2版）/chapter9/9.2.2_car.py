# Author：D.H
# Place：哈工深
# Time：2021/8/8 8:36
# 9.2.2 给属性指定默认值

class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化描述汽车的领域"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description_name(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4l', 2021)
print(my_new_car.get_description_name())
my_new_car.read_odometer()
