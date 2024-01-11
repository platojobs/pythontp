from math import  sqrt

class Point(object):
    def __init__(self,x =0,y=0):
        self.x = x
        self.y = y

    def move_to(self,x,y):
        self.x = x
        self.y = y
    def move_by(self,dx,dy):
        self.x += dx
        self.y += dy

    def distance(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return "(%s,%s)" % (str(self.x),str(self.y))



p1 = Point(3,5)
p2 = Point()
print(p1)
print(p2)
s = p1.__str__()
print(type(s))
print(s)

p2.move_by(-1,2)
print(p2)
print(p1.distance(p2))


# @property装饰器

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age
    # 包装属性的访问权限
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age
    def play(self):
        if self._age <= 16:
            print("%s在玩飞行棋" % self._name)
        else:
            print("%s在玩农药" % self._name)



students = Person("jobs",34)
students.play()
students.age = 12
students.play()
print(students.name)


class PPerson(object):
    __slots__ = ("_name","_age","_gender")
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self,gender):
        self._gender = gender

    def play(self):
        if self._age <=16:
            print("%s在玩dota" % self._name)
        else:
            print("%s在玩斗地主" % self._name)

person = PPerson("zhangsan", 23)
person.gender = "男"
person.play()
person.age = 12
person.play()

# 静态方法
class Triangle(object):
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
    @staticmethod   # 静态方法
    def is_valid(a,b,c):
        return a + b > c and b + c > a and a + c > b
    def perimeter(self):
        return self._a + self._b + self._c
    def area(self):
        half = self.perimeter()/2
        return sqrt(half*(half-self._a)*(half - self._b)*(half-self._c))

a,b,c = 3,4,5
if Triangle.is_valid(a,b,c):
    t = Triangle(a,b,c)
    print(t.perimeter())  #周长
    print(t.area())   #面积
    print(Triangle.perimeter(t)) #静态方法
else:
    print("无法构成三角形")

# python还可以定义类方法

from time import  time,localtime,sleep

class Clock(object):
    def __init__(self,hour = 0 , minute = 0 , second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)
    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        return "%02d:%02d:%02d" %(self._hour,self._minute,self._second)



clock = Clock.now()
a = 10
while a > 5:
    print(clock.show())
   # sleep(1)
    a -= 1
    #clock.run()
    #print(clock.show())

# 类之间的关系 is-a ,has-a 和 use-a关系
# is-a 继承和泛华的关系
# has-a 关系通常称之为关联 ，整体和部分的关系称为聚合关系，如果整体进一步负责了部分的生命周期，呢就是最强的关联关系，也叫做合成关系
# use-a 称之为依赖

