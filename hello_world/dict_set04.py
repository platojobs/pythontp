# dict

names_Score = { 'Michael':95 , 'BOb': 75, 'Tracy': 88 }

print(names_Score['BOb'])

# 把数据放入字典
names_Score['Adam'] = 99
print(names_Score)

names_Score["BOb"] = 102
# key 存在 取出值
print(names_Score.get('BOb'))
# 检测 key 不存在 赋值为0
print(names_Score.get('XQ',0))

alien_0 = { 'color':'green','points':5 }
print(alien_0['color'])
print(alien_0['points'])

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = '78999'
print(alien_1)

del alien_1['color']
print(alien_1)





'''
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

需要注意的是：dict的key必须是不可变对象

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，
因此，可以放心地作为key。而list是可变的，就不能作为key

'''

# set

number_set = set([1,2,3])
print(number_set)
# 追加元素
number_set.add(4)
print(number_set)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作

number_s1 = set([1,2,3])
number_s2= set([2,3,4])
print(number_s1 & number_s2) # {2,3}

number_set.add((1,2,3))
print(number_set)
number_set.add((1,[2,3])) # 不起作用
print(number_set)

