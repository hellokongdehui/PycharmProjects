# Author：D.H
# Place：哈工深
# Time：2021/8/10 13:16
# 9.3.2 给子类定义属性和方法

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

    def update_odometer(self, mileage):  # 通过方法修改属性的值
        """将里程表读书设置为指定的数。禁止将里程表读书往回调。"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # 通过方法对属性的值进行递增
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kwh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_description_name())
my_tesla.describe_battery()
