# 条件判断
age = 20
# 粗略的判断
if age >= 18:
    print('your age is',age)
    print('adult')
else:
    print('teenager')
# 精细的判断

s_age = 12

if s_age >= 18:
    print('adult')
elif s_age >= 6:
    print('teenager')
else:
    print('kid')

# 只要s_age是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if s_age:
    print(True)

# input
birth = input('birth: ')
s_birth = int(birth)
if s_birth < 2000:
    print('00前')
else:
    print('00后')

#检查特定值是否不包含在列表中

banner_users = ['andrew','carolina','david']
user = 'marie'
if user not in banner_users:
    print(f'{user.title()},you can post a response if you wish.')



'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖

'''

xiaoming_height = 1.75
xiaoming_weight = 80.5
xiaoming_BMI = xiaoming_weight/xiaoming_height**2

if xiaoming_BMI <= 18.5:
    print('过轻')
elif 18.5 < xiaoming_BMI <= 25:
    print('正常')
elif 25 < xiaoming_BMI <= 28:
    print('过重')
elif 28 < xiaoming_BMI <= 32:
    print('肥胖')
else:
    print('严重肥胖')


'''
条件判断可以让计算机自己做选择，Python的if...elif...else很灵活。
条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。
'''

'''
循环
'''
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

s_numbers = [1,2,3,4,5,6,7,8,9,10]
s_sum = 0
for x in  s_numbers:
    s_sum += x

print(s_sum)

# range()函数  可以生成一个整数序列，再通过list()函数可以转换为list

s_range = range(5)
print(list(s_range)) # [0, 1, 2, 3, 4]

magicians = ['alice','david','carolina']

for magician in magicians:
    print(f'this is {magician}')


n = 1

while n<= 100:
    if n > 10:
        break
    print(n)
    n += 1
print('END')


sn = 0
while sn < 10:
    sn = sn + 1
    if sn % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(sn)