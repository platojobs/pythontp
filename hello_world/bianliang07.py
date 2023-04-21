import random

a = 100
b = 12.345
c = 'hello, world'
d = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'str'>
print(type(d))    # <class 'bool'>

e = False
print(type(e))

print(321 // 123)  # 整除运算 是2

print(3 ** 3)  # 幂运算 27
print(3 ** 2) # 9

'''
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c)) # 等价的
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

'''

'''
radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
'''

'''
x = float(input("x= "))
if x>1:
    y = 3*x -5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5*x + 3
print(f'f({x}) = { y }')
'''

'''
answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input("请输入："))
    if number < answer:
        print("biger")
    elif number > answer:
        print("smaller")
    else:
        print("==")
print(f'total{couter}次')
'''

'''
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j} = {i * j}', end='\t')
    print()

print(2 ** 0.5)
'''
'''
x = int(input('x = '))
y = int(input('y = '))
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break
'''

'''
items = [1,2,3,4,5,6,7,8]
items2 = ['python', 'java','go','kotin']
items3 = list(range(1,10))
items22 = list('hello')
print(items22)

items4 = ['hello'] * 3
print(items4)
'''

'''
items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]

# 列表的拼接
items3 = items1 + items2
print(items3)    # [35, 12, 99, 68, 55, 87, 45, 8, 29]

# 列表的重复
items4 = ['hello'] * 3
print(items4)    # ['hello', 'hello', 'hello']

# 列表的成员运算
print(100 in items3)        # False
print('hello' in items4)    # True

# 获取列表的长度(元素个数)
size = len(items3)
print(size)                 # 9

# 列表的索引
print(items3[0], items3[-size])        # 35 35

items3[-1] = 100
print(size)
print(items3)
print(items3[size - 1], items3[-1])

print(items3[:5])

print(items3[:5])          # [35, 12, 99, 68, 55]
print(items3[4:])          # [55, 87, 45, 8, 100]
print(items3[-5:-7:-1])    # [55, 68]
print(items3[::-2])        # [100, 45, 55, 99, 35]

items5 = [1,2,3,4]
items6 = list(range(1,5))
print(items6)
print(items5 == items6) # True
items7 = [3,2,1]
print(items5 <= items7)  # True


itemsdd = ['python','swift','kotlin']
print(int(len(itemsdd))) # 3
# 便历数组
# 方法一
for index in range(len(itemsdd)):
    print(itemsdd[index])   #
#方法二
for item in itemsdd:
    print(item)

itemsdd.append("go") # ['python', 'swift', 'kotlin', 'go']
print(itemsdd)
itemsdd.insert(2,'SQL') #['python', 'swift', 'SQL', 'kotlin', 'go']
print(itemsdd)

itemsdd.remove('go') # 在使用remove方法删除元素时，如果要删除的元素并不在列表中，会引发ValueError异常
print(itemsdd) #  ['python', 'swift', 'SQL', 'kotlin']
itemsdd.pop(0) # 不要索引越界 ，会引发错误 IndexError 异常
print(itemsdd.pop(0)) # 返回删除的元素
print(itemsdd) #  ['swift', 'SQL', 'kotlin']
itemsdd.pop(len(itemsdd)-1)
print(itemsdd) #['swift', 'SQL']

itemsdd.clear() # 清空列表中的元素
print(itemsdd) #[]

'''

itemsddn = ['python','swift','java','kotlin','java','go','python','java']

print(itemsddn.index('python')) # 0
print(itemsddn.index('python',2)) # 5
# 注意 虽然列表中有java，但是从索引3
print(itemsddn.index('java',3))

print(itemsddn.count('python'))
print(itemsddn.count('java'))
print(itemsddn.count('swift'))

itemsddn.sort()
print(itemsddn)
itemsddn.reverse()
print(itemsddn)

itemsddn1 = []
itemsddn1 = [x for x in range(1,10)]
print(itemsddn1)
itemsddn1 = [x for x in 'hello' if x not in 'aeiou']
print(itemsddn1)
itemsddn1 = [x + y for x in 'ABC' for y in '12']
print(itemsddn1)