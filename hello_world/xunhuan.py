"""
sum = 0
# <11 的整数之和
for  x in range(11):
    sum += x
print(sum)

ou_sum = 0
# <11的偶数之和
for x in range(2,11,2):
    print(f"{x:}")
    ou_sum += x
print(ou_sum)


import random

answer = random.randint(1,100)
#print(answer)
counter = 0
while True:
    counter += 1
    number = int(input("请输入："))
    if number < answer:
        print("小了一点")
    elif number > answer:
        print("大了一点")
    else:
        print("恭喜你答对了！")
        break
print("你一共猜了%d次" % counter)
print(f"{counter:}")
if counter > 7:
    print("你的智商余额明显不足")
"""

# 不包括10 的一个序列
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i:}*{j:} = {(i*j):}")
    print()
print("========")

# 不含有5的序列
items = list(range(1,5))
items_1= list(range(5))
print(items)  # 1,2,3,4
print(items_1)  # 0,1,2,3,4

def sum_100():
    sum = 0
    for x in range(101):
        sum += x
    return sum
# 计算1-100的所有的数字的和
print(sum_100())

def sum_100_while():
    sum = 0
    n = 100
    while n > 0:
        sum += n
        n -= 1
    return sum

print(sum_100_while())

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operand type")
    if x >= 0:
       return x
    else:
        return -x

print(my_abs(1.23))

def power_test(x,n=2):
    return  x**n

print(power_test(5,4))
print(power_test(5,1))
print(power_test(5,2))
print(power_test(5,3))
print(power_test(4))


def list_append(L =[]):
    L.append("end")
    return L

print(list_append([1,2,3]))
print(list_append([1,2,3]))

print(list_append()) # ['end']
print(list_append()) # ['end', 'end']
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def list_appendDefault(L = None):
    if L is None:
        L= []
    L.append("end")
    return L
print(list_appendDefault()) # ['end']
print(list_appendDefault()) # ['end']

# 关键字参数
def person(name,age,**kw):
    print("name:",name,"age:",age,"toher:",kw)

person("jobs",89) # name: jobs age: 89 toher: {}
person("bob",34,city = "北京") #  name: bob age: 34 toher: {'city': '北京'}
person("jobs",45,gender = "男",city = "美国") #name: jobs age: 45 toher: {'gender': '男', 'city': '美国'}

