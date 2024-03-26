# 字典的方法
students = {
    1001:{"name":"john","age": 23,"place":"shanxi"},
    1002:{"name":"jobs","age": 70,"place":"guangdong"},
    1003:{"name":"lilei","age": 63,"place":"sichuan"}
}
# 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
print(students.get(1001)) # {'name': 'john', 'age': 23, 'place': 'shanxi'}
print(students.get(1001).get("name")) # john
print(students.get(1005)) # None

# 获取字典的所有的键
print(students.keys())
# 获取字典所有的值
print(students.values())
# 获取字典所有的键值对
print(students.items())
# 对字典中的键值对进行循环遍历
for key,value in students.items():
    print(key,"----->", value)
    for subkey,subvalue in value.items():
        print(subkey,"=", subvalue)

# 使用pop方法删除键值并返回该值
stue_01 = students.pop(1001) # 返回1001对应的值
print(stue_01) # {'name': 'john', 'age': 23, 'place': 'shanxi'}
print(len(students)) # 2
# 使用popitem方法删除字典中最后一组的键值对并返回对应的二元组
# 如果字典中没有元素，调用该方法会引发异常
key,value = students.popitem()
print(key,value) # 1003 {'name': 'lilei', 'age': 63, 'place': 'sichuan'}
print(len(students)) # 1
print(students)# {1002: {'name': 'jobs', 'age': 70, 'place': 'guangdong'}}
#如果update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键回添加到字典中
others = {
    1005:{"name": "qiaofeng","sex":True,"age":32},
    10010:{"name": "qiaofeng","sex":True,"age":32}

}
students.update(others)
print(students) #{1002: {'name': 'jobs', 'age': 70, 'place': 'guangdong'}, 1005: {'name': 'qiaofeng', 'sex': True, 'age': 32}, 10010: {'name': 'qiaofeng', 'sex': True, 'age': 32}}
person = {
    "name":"wangdalu","age":23,"sex":True
}
del  person["age"]  # 在删除元素的时候如果指定的键索引不到对应的值，一样会引发KeyError异常
print(person) # {'name': 'wangdalu', 'sex': True}

# 输入一段话，统计出每个英文字母出现的次数
sentence = input("请输出一段话：")
counter = {}
for ch in sentence:
    if "A"<= ch <= "Z" or "a" <= ch <= "z":
        counter[ch] = counter.get(ch,0) + 1
for key , value in counter.items():
    print(f"字母{key}出现了{value}次")
"""
请输出一段话：areyouokfineoklove
字母a出现了1次
字母r出现了1次
字母e出现了3次
字母y出现了1次
字母o出现了4次
字母u出现了1次
字母k出现了2次
字母f出现了1次
字母i出现了1次
字母n出现了1次
字母l出现了1次
字母v出现了1次

"""

# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
stocks = {
    "Apple":191.99,
    "GOOD": 1198.09,
    "IBM":149.88,
    "ORFL":177.09,
    "FB":38,
    "SYM":32,
    "DFG":101,
    "DFHG":65
}

stocks2 = {key:value for key,value in stocks.items() if value > 100}
print(stocks2)
# {'Apple': 191.99, 'GOOD': 1198.09, 'IBM': 149.88, 'ORFL': 177.09, 'DFG': 101}