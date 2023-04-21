#Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言
#1.高阶函数
'''
变量可以指向函数
'''
import advanced06

f = abs # 函数本身也可以赋值给变量，即：变量可以指向函数。
print(f(10))

# 函数名也是变量
#传入函数

def f(x):
    if isinstance(x ,int):
        return x
    else:
        return 0

a = f
def add(x,y,f):
    return f(x) + f(y)

print(add(5,6,a))

b = abs

print(add(7,-8,b))
'''
编写高阶函数，就是让函数的参数能够接收别的函数
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
'''

# 2. map/reduce

def pro_f(x):
    return x**2

pro_r = map(pro_f,[1,2,3,4,5,6])
print(list(pro_r))

pro_numberslist = list(map(str,[1,2,3,4,55,7]))
print(pro_numberslist)

pro_strlist = list(map(int,['1','2','3','45','9','7']))
print(pro_strlist)

from functools import reduce
#reduce

def sumTT(x,y):
    return x + y

pro_reducesum = reduce(sumTT,[1,2,3,4])
pro_sum = sum([1,2,3,4])

print(pro_reducesum)
print(pro_sum)

# 如果要把序列[1, 3, 5, 7, 9]变换成整数13579 reduce就可以派上用场

def fn(x,y):
    return x*10 + y

pro_reducetool = reduce(fn,[1,3,5,7,9])
print(pro_reducetool) # 13579


def greet_user(username):
    print(f'hello,{username.title()}')

greet_user('jesse')


def describe_pet(animal_type, pet_name):
    print(f'\n I have a { animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}")

#关键字实参
describe_pet(animal_type='hamster',pet_name='harry')
#默认值

def describe_petts(pet_name,animal_type = 'dog'):
    print(f"\n I have a{animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_petts(pet_name='willie')

def get_fomatted_name(first_name,last_name):
    full_name = f'{first_name}-{last_name}'
    return full_name.title()

musician = get_fomatted_name('jimi','hendrix')
print(musician)

# 可选的
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
       full_name = f'{first_name}{middle_name}{last_name}'
    else:
       full_name = f'{first_name}{last_name}'
    return full_name.title()

pro_musician = get_formatted_name('jimi','hendrix')
print(pro_musician)
pro_musician = get_formatted_name('john','hooker','lee')
print(pro_musician)

unittest_names = ['23','345','45','56']
complete_names =[]

while unittest_names:
    current = unittest_names.pop()
    print(f'printeing model:{current}')
    complete_names.append(current)

print(complete_names)

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model:{current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_mmodels):
    print('\n The following models have been printed:')
    for completed_model in completed_mmodels:
        print(completed_model)

unittest_designs = ['phone code','robot pendant','dodecahedron']
complete_moels = []
s = unittest_designs[:]
print(f'origi:{s}')
print_models(unittest_designs[:],complete_moels)
show_completed_models(complete_moels)

#传递任意数量的实参
def make_pizzza(*toppings):
    print(toppings)
make_pizzza('pepperoni')
make_pizzza('mushrooms','green peppers','extra cheese')

#形参名*toppings中的星号让Python创建一个名为toppings的空元组

#结合使用位置实参和任意数量实参

def make_pizza(size,*toppings):
    print(f'\n Making a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'-{topping}')

make_pizza(16,'pettys')
make_pizza(12,'mushrooms','green pepers','extra cheese')

#使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princetion',field='physics')

print(user_profile)

# 导入模块的应用  pizza_test就是一个模块
import pizza_test

pizza_test.make_pizza_test(12,'laojiao')


# 导入某个模块的一个函数，用这种方式
# from advanced06 import pro_odd
#
# s = advanced06.pro_odd()
#
# print(next(s))
# print(next(s))

##使用as给函数指定别名

'''
使用as给函数指定别名
from module_name import funcname as funname2(别名)
'''
from advanced06 import pro_odd as odd

sss = odd()
print(next(sss))
print(next(sss))

# 导入模块中的所有函数
'''
导入模块中的所有函数语法：
from module_name import *
'''
from pizza_test import *

make_pizza(12,"KI")

#使用as给模块指定别名

'''
给模块指定别名的通用语法如下：
import module_name as name(别名)
'''

import pizza_test as p_fun

p_fun.make_pizza_test(26,"TTTY")



