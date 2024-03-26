
# 创建集合的字面量语法
set1 = {1,2,3,4,5,3,3,4,5,5,8} # 重复元素不会出现在集合中
print(set1) # {1, 2, 3, 4, 5, 8}
print(len(set1)) # 6

# 创建集合的构造器语法
set2 = set("hello")
print(set2) # {'o', 'e', 'l', 'h'}

#将列表换转成集合
set3 = set([1,2,3,3,2,1])
print(set3)  # {1,2,3}

# 创建集合的生成式语法
set4 = {num for num in range(1,20) if num % 3 == 0 or num % 5 == 0}
print(set4) # {3, 5, 6, 9, 10, 12, 15, 18}
print("~~~~~~start~~~~~")
def xuhuan():
    for num in set4:
        print(num)
xuhuan()
print("~~~~end~~~~~")

# 集合中的元素必须是hashable类型的，所谓hashable类型指的是能够计算出哈希码的数据类型
test_set1 = {11,12,1,3,14}
test_set2 = {11,12,10,30,414}
print(10 in test_set1) # False
print(16 not in test_set1) #True
# in 和 not in 检测是否为集合中的元素
print(test_set1 & test_set2) # {11, 12}
print(test_set1.intersection(test_set2)) #{11, 12}

# 并集
print(test_set1 | test_set2)  # {1, 3, 10, 11, 12, 14, 30, 414}
print(test_set1.union(test_set2)) # {1, 3, 10, 11, 12, 14, 30, 414}
# 差集
print(test_set1 - test_set2) #  {1, 3, 14}
print(test_set1.difference(test_set2)) # {1, 3, 14}

# 对称差
print(test_set1 ^ test_set2) # {1, 414, 3, 14, 10, 30}
print(test_set1.symmetric_difference(test_set2))  # {1, 414, 3, 14, 10, 30}
# 并集 - 共有元素 = 对称差集
print(test_set1 | test_set2 -(test_set1 & test_set2)) # {1, 3, 414, 30, 10, 11, 12, 14}

# test_set1 |= test_set2 # 并集赋值给set1
# print(test_set1)
# test_set1.update(test_set2)  # 效果同上
# print(test_set1)

# 比较运算
comparison_set1 = {1,3,5}
comparison_set2 =  {1,2,3,4,5}
comparison_set3 = comparison_set2
# < 表示真子集，<=运算表示子集
print(comparison_set1 < comparison_set2 , comparison_set1 <= comparison_set2 ) # True True
print(comparison_set2 < comparison_set3,comparison_set2 <= comparison_set3) # False True
# 通过issubset方法也能进行子集判断
print(comparison_set1.issubset(comparison_set2)) # True
# 通过方法做超集判断
print(comparison_set2.issuperset(comparison_set1)) # True
print(comparison_set2 > comparison_set1) # 超集判断 # true

# 集合的方法 ，集合是可变类型，可以通过集合类型的方法为集合添加和删除元素
funcset1 = set()
funcset1.add(1)
print(funcset1)
print("------1-") # {1}
funcset1.add("2")
print(funcset1)
print("------2-") #{1, '2'}
funcset1.update({34,0.01})
print(funcset1) # {1, 34, 0.01, '2'}
print("------3-")
funcset1.discard(1)
print(funcset1)
print("------4--")

# 移除元素
funcset1.discard(34)
print(funcset1)
# 增添元素
funcset1.add(123)
funcset1.add(23)
# 和另外一个集合合并进元素
funcset1.update({"q","w",2,3,4,5})
if 123 in funcset1:
    funcset1.remove(123)  #移除元素
print(funcset1)
# 随机删除一个元素并且返回该元素
print(funcset1.pop())  # 返回随机删除的元素
print(funcset1)

# 判断两个集合有没有相同的元素可以使用
same_set1 = {"java","Python","Go","Kotlin"}
same_set2 = {"Kotlin","swift","Java","OC","Dart"}
same_set3 = {"Html","CSS","JavaScript"}
# 判断两个元素是不是有交集
print(same_set1.isdisjoint(same_set2)) # False
print(same_set1.isdisjoint(same_set3)) # True

# 不可变集合 ，不能添加和删除元素
frozeset1 = frozenset({1,2,3})
frozeset2 = frozenset(range(1,6))
print(frozeset1 & frozeset2) # frozenset({1, 2, 3})
print(frozeset1 | frozeset2) # frozenset({1, 2, 3, 4, 5})
print(frozeset1 - frozeset2) # frozenset()
print(frozeset1 < frozeset2) # True

# python的集合底层使用了哈希存储的方式，元素必须是hashable类型，没有顺序，不能用索引运算、不能重复
