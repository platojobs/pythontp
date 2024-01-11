
from abc import ABCMeta , abstractmethod

class Pet(object,metaclass=ABCMeta):
    def __init__(self,nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        print("发出声音")


class Dog(Pet):
    def make_voice(self):
        print("%s: 汪汪汪" % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print("%s: 喵喵喵" % self._nickname)

pets = [Dog("旺财"),Cat("黑猫警长"),Dog("大黄")];
for pet in pets:
    pet.make_voice()

# Pet是一个抽象的类，所谓抽象的类就是不能够创建对象的类，这种类的存在本身就是为了让其他类去继承它




