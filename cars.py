cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
print(sorted(cars))
print(cars)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.odometer_reading = 0
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回格式规范的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条消息指出汽车里程"""
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'A4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

