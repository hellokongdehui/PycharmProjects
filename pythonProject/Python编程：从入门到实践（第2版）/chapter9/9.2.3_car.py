# Author：D.H
# Place：哈工深
# Time：2021/8/8 9:09
# 9.2.3 修改属性的值
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

    def update_odometer(self, mileage):  # 通过方法修改属性的值
        """将里程表读书设置为指定的数。禁止将里程表读书往回调。"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):  # 通过方法对属性的值进行递增
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4l', 2021)
print(my_new_car.get_description_name())
my_new_car.odometer_reading = 23  # 直接修改属性的值
my_new_car.read_odometer()

my_new_car.update_odometer(25)
my_new_car.read_odometer()

my_new_car.update_odometer(20)  # 小了

my_used_car = Car('subaru', 'outback', 2015)  # 通过方法对属性的值进行递增
print('\n'+my_used_car.get_description_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
