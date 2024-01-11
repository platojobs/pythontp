print('list_study02')
'''
list
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
'''
变量classmates就是一个list。用len()函数可以获得list元素的个数：
'''

#获取元素 -适用索引和下标
print(len(classmates))
print(classmates[0])
classmates[1] = 'XQ'
print(classmates)
print(classmates[len(classmates)-1]) # last  最后一个元素
print(classmates[-1]) # last 最后一个元素  Tracy
print(classmates[-2]) # XQ
print(classmates[-3]) # Michael
# append 添加元素
classmates.append('HuangHua')
print(classmates)

# 添加元素到指定位置
classmates.insert(0,"ZuSong")
print(classmates)
# 删除元素
classmates.remove('XQ')
print(classmates)
# 删除末尾的元素
last_element = classmates.pop() # 删除末尾的元素返回末尾元素
print(last_element) # HuangHua
element_01 = classmates.pop(1)
print(element_01)
print(classmates)

classmates.remove('ZuSong')
print(classmates)
classmates.append('shell')
print(classmates)
print(classmates.index('shell')) # shell 的index == 1

# 修改元素
classmates[1] = 'IU'
classmates[0] = ['json','html']
list_2 = ['java','python','oc','kotlin']
classmates.append(list_2)
print(classmates)
print(classmates[2][0]) # java
classmates = []
print(classmates)
print('------list end----------')
'''
tuple

另一种有序列表叫元组：tuple。tuple和list非常类似，元组看起来很像列表，但使用圆括号而非中括号来标识。
定义元组后，就可使用索引来访问其元素，就像访问列表元素一样。
但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

'''
classmates_tuple = ('Michael', 'Bob', 'Tracy')
print(classmates_tuple[0])

# 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
tuple_01 = (1,2)
print(tuple_01)

# 空tuple
empty_tuple = ()
print(len(empty_tuple))
# 要定义一个只有1个元素的tuple
'''
注意　严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：

'''

one_tuple = (1,)
print(len(one_tuple))

# 含有list的tuple
list_tuple = ('1','2',['3','4',789])
list_tuple[2][0] = '987'
print(list_tuple)

'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(?)
# 打印Python:
print(?)
# 打印Lisa:
print(?)

'''
oper_L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(oper_L[0][0])
print(oper_L[1][1])
print(oper_L[2][2])

# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# 可变的tuple
t = ("a","b",["A","B"])
t[2][0] = "xd"
t[2][1] = "fg"
print(t)