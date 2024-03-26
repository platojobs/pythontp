
import random
from random import  randint

# 函数
def testfunction(arg):
    print("Id inside the function", id(arg))
    arg += 1
    print("new object after increment", arg, id(arg))


# 引用传递
var = 10
print("id brefore passsing", id(var))
testfunction(var)
print("value after function call", var)
# 上述的解释只是传递的是不可变的，在函数内部创建了一个新的变量，原始变量保持不变


def test_varfunction(arg):
    print("Id inside the function", arg)
    print("ID inside the function:", id(arg))
    arg = arg.append(100)

blist = [1,3,4,5]
print("ID before", blist) # ID before [1, 3, 4, 5]
test_varfunction(blist)
print("after _ blist",blist) # after _ blist [1, 3, 4, 5, 100]

# 参数的默认值
def roll_dicen(n=2):
    total = 0
    for _ in range(n):
        total += randint(1,6)
        return total
print(roll_dicen()) # 如果没有指定参数，那么默认的就是2
print(roll_dicen(3)) # 3颗色子

def add(a=0,b=0,c=0):
    return a + b + c
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))

# 可变参数
# 用星号表达式来表示arg的可以接受的0个或者任意个参数
def var_add(*arg):
    total = 0
    for var in arg:
        if type(var) in (int, float):
            total += var
    return total

print(var_add())
print(var_add(1))
print(var_add(1,2))
print(var_add(1,2,3))
print(var_add(1,2,3,4,0.9))

#用模块管理函数 ，一个文件就是一个模块，可以导入不同的模块，用不同的模块名来调用函数
# 也可以给函数取别名，也可以给模块取别名来避免同名函数的调用覆盖问题
# 标准库中的模块和函数
import  math
print(abs(-3)) # 3
print(bin(123)) #  0b1111011
print(bin(2)) # 0b10
print(chr(65)) # A
print(hex(16)) # 0x10
print(round(1.2345621,4)) # 保留四位小数


# 函数是对功能相对独立且会重复使用的代码的封装
import  string

all_chars = string.digits + string.ascii_letters + string.punctuation
print(string.ascii_letters) # 大小写字母
print(string.digits) # 数字
print(string.punctuation) # 英文标点符号
def generate_code(code_len = 4):
    return "".join(random.choices(all_chars,k=code_len))

print(generate_code(3))

for _ in range(5):
    print(generate_code())






