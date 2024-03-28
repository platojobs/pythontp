cars = ["bmw","audi","toyota","subaru"]
# cars.sort()
print(sorted(cars))  # sorted ,不会影响列表原来的顺序
print(cars)
numbers = list(range(6))

# 使用range()创建数字列表

print(numbers) #  [0, 1, 2, 3, 4, 5]

print(min(numbers)) # 0
print(max(numbers)) # 5
print(sum(numbers)) # 15
# 列表解析

squres = [value*2 for value in range(1,11) ]
print(squres) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(squres[:3]) # [2, 4, 6]
print(squres[:4]) # [2, 4, 6, 8]
print(squres[-3:]) # [16, 18, 20] 最后三个元素
print(squres[-4:-1:2]) # [14, 18] 第三个值代表间隔或者步长多久取一个值
