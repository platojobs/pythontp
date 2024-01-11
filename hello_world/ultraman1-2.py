
from abc import ABCMeta , abstractmethod
from random import  randint,randrange

class Fighter(object,metaclass=ABCMeta):
    __slots__ = ("_name","_hp")

    def __init__(self,name,hp):
        self._name = name
        self._hp = hp
    @property
    def name(self):
        return self._name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp = hp if hp >=0 else 0
    @property
    def alive(self):
        return self._hp >0
    @abstractmethod
    def attack(self,other):
        print("抽象类")

class Ultraman(Fighter):
    __slots__ = ("_name","_hp","_mp")
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp
    def attack(self,other):
        other._hp -= randint(15,25)
    def hug_attack(self,other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other._hp *3 // 4
            injury = injury if injury >= 50 else 50
            other._hp -= injury
            return True
    def magic_attack(self,others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp._hp -= randint(10,15)
            return True
        else:
            return False
    def resume(self):
        incr_point = randint(1,10)
        self._mp += incr_point
        return incr_point

class Monster(Fighter):
    __slots__ = ("_name","_hp")

    def attack(self,other):
        other._hp -= randint(10,20)
    def __str__(self):
        return "~~~~%s小怪兽~~~\n" % self.name + "生命值:%d\n" % self._hp
def is_any_alive(monsters):
        for monster in monsters:
            if monster.alive:
                return True
            else:
                return False
def select_alive_one(monsters):
        monsters_len = len(monsters)
        while True:
            index = randrange(monsters_len)
            monster = monsters[index]
            if monster.alive:
                return monster
def display_info(ultraman, monsters):
        print("display ==%s " % ultraman)
        for monster in monsters:
            print(monster,end = " ")



u = Ultraman("赛博",1000,120)
m1 = Monster("狄仁杰",250)
m2 = Monster("李元芳",500)
m3 = Monster("王大雷",750)
ms = [m1,m2,m3]
fight_round = 1
while u.alive and is_any_alive(ms):
    print("=====第%02d回合" % fight_round)
    m = select_alive_one(ms)
    skill = randint(1,10)
    if skill <= 6:
        print("%s使用的普通攻击打了%s" % (u.name,m.name))
    elif skill <=9:
        if u.magic_attack(ms):
            print("%s使用了魔法攻击" % u.name)
        else:
            print("%s使用魔法攻击失败" % u.name)
    else:
        if u.hug_attack(m):
            print("%s放大招攻击" % u.name)
        else:
            print("%s使用了普通攻击打了%s" % (u.name , m.name))
            print("%s的魔法恢复了%d点" % (u.name , u.resume()))
    if m.alive:
        print("%s回击了%s" % (m.name , u.name))
        m.attack(u)
    display_info(u,ms)
    fight_round += 1
print("\n===== 战斗结束!=====\n")
if u.alive :
    print("%s奥特曼胜利" % u.name)
else:
    print("小怪兽胜利")

