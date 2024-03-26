
# 字典
person1 = {"key1":"value1","key2":"value2"}

# 生成式语法
# dict函数构造器中的每一组参数就是字典的一组键值对
person = dict(name="A",age=33,weight = 120,home= "东大街34号")
print(person) # {'name': 'A', 'age': 33, 'weight': 120, 'home': '东大街34号'}
#也可以通过python的内置函数zip压缩两个序列并创建字典
itesms1 = dict(zip("abcdef","123456"))
print(itesms1) # {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6'}

iterms2 = dict(zip("abcdef",range(1,10)))
print(iterms2) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

#用字典生成式语法创建字典
iterms3 = { x :x**3  for x in range(1,6)}
print(iterms3) # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# for循环只是对字典的键做了遍历
for key in iterms3:
    print(key)
"""
key 结果
1
2
3
4
5
"""

# 字典的运算
students = {"name":"john","age":34,"height":1.88}
print("name" in students, "tel" in students) # True False
# 通过索引向字典中输入新的键值对
students["tel"] = 13109871234
students["signature"] = "4112223e3222yt3y3"
print("name"in students, "tel" in students) #  True True
print(students) # {'name': 'john', 'age': 34, 'height': 1.88, 'tel': 13109871234, 'signature': '4112223e3222yt3y3'}
print(len(students)) # 5

