class Dog:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting.')
    def roll_over(self):
        print(f'{self.name} rolled over！ ')


my_dog = Dog('David',32)
my_dog.sit()
my_dog.roll_over()

print(f'狗名: {my_dog.name} ')

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f'{self.restaurant_name} is restaurant_name')
        print(f'{self.cuisine_type} is cuisine_type ')
    def open_restaurant(self):
        print(f'{self.restaurant_name} is do {self.cuisine_type} is opening')

restaurant = Restaurant('泰国菜馆','泰国菜')
print(f'{restaurant.restaurant_name}')
print(f'{restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('餐馆1','川菜')
restaurant2 = Restaurant('餐馆2','粤菜')
restaurant3 = Restaurant('餐馆3','湘菜')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    def describe_user(self):
        print(f'name is {self.last_name}{self.first_name}')
    def greet_user(self):
        print(f'Hello,{ self.last_name}{self.first_name}! Thanks!')


user = User('Jobs' ,'Plato')
user.describe_user()
user.greet_user()

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.tank = 1
    def get_descriptive_name(self):
        long_name = f'{self.year}年{self.make}车是{self.model}款'
        return  long_name.title()
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self,mile):
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("你不能乱调表")
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print(f'only {self.tank}')

my_new_car = Car('audi','a4',2023)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 112
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def describe_size(self):
        print(f'This car is {self.battery_size} wh battery')


class ElectricalCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.crmile = 0
        self.battery = Battery(100)
    def fill_gas_tank(self):
        print('no tank')

my_elCar = ElectricalCar('tesla','model3',2019)
print(my_elCar.get_descriptive_name())
my_elCar.fill_gas_tank()
my_elCar.battery.describe_size()

# 定义一个函数 可编写一个try-except代码块来处理可能引发的异常
def try_zeroEror(make = 0):
    try:
       print(make/0)
    except ZeroDivisionError:
        print("you error")

try_zeroEror()