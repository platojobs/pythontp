# study_day01

print('hello world')
# Note that print is a function

print()

# 三重引号
mstr = '''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
print(mstr)

# 单引号字符串和双引号字符串是相同的——它们没有任何区别
# Python中没有单独char的数据类型

age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name,age))
print('why is {0} playing with that python?'.format(name))
print('-----1-----')
# 也可以这样
print('{nam} was {age} years old when he wrote this book '.format(nam=name,age=age))

print('why is {name} playing with that python?'.format(name=name))
print('-----2-----')
# python3.6 引入 称为“f-strings”
print(f'{name} was {age}years old when he wrote this book')
print(f'why is {name} playing with that python?')
print('----3------')

# string
a = name + ' is ' + str(age) + ' years old'
print(a)
print('-----4-----')

# Python 在该format方法中所做的是将每个参数值替换为规范的位置。可以有更详细的规范
print('{0:.3f}'.format(1.0/3)) # 0.333
print('{0:_^11}'.format('hello')) # ___hello___
print('{name} wrote {book}'.format(name="jobs专辑",book = ' A byte of pyhton3.9')) # jobs专辑 wrote  A byte of pyhton3.9

# 换行
print(10)
print(11)
'''
10
11

'''

# 不换行
print('10',end='')
print('11',end='')
#*
1011
#
print('----------')
# 使用空格
print('a', end=' ')
print('b', end=' ')
print('c')
#*  a b c  #

# 转移序列 \n 换行

line = 'This is the first line\nThis is the second line'
print(line)

line_01 = "This is the first sentence. \
This is the second sentence."
print(line_01)

raw_line = r"Newlines are indicated by \n" # 原始字符串 如果您需要指定一些没有特殊处理（例如转义序列）的字符串，那么您需要通过前缀或字符串来指定原始字符串。一个例子是：rR
print(raw_line)

i = 5
# Error below! Notice a single space at the start of the line
 #print('Value is', i) # IndentationError: unexpected indent
print('I repeat, the value is', i)

print(ord('A')) # 65

# Python对bytes类型的数据用带b前缀的单引号或双引号表示
# s_a byte类型的数据
s_a = b'\xe4\xb8\xad\xe6\x96\x87'  #  要把bytes变为str
print(s_a.decode('utf-8'))


for username, score in [('piglei',200),('raymond',60)]:
    print(username,score)
