# 1.切片
pro_names  = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
pro_name_slice = pro_names[0:3] # [0:3]表示，从索引0开始取，直到索引3为止
pro_name_slice1= pro_names[:3]
print(pro_name_slice) # ['Michael', 'Sarah', 'Tracy']
print(pro_name_slice1) # ['Michael', 'Sarah', 'Tracy']


pro_name_slice2 = pro_names[:-2] # 不包括-2元素
print(pro_name_slice2) #['Michael', 'Sarah', 'Tracy']

pro_name_slice3 = pro_names[-2:]

print(pro_name_slice3) # ['Bob', 'Jack']


pro_numbers = list(range(21))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15,16,17,18,19,20]
print(pro_numbers)

print(pro_numbers[-10:]) # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(pro_numbers[10:20])# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(pro_numbers[:10:2]) # [0, 2, 4, 6, 8]
print(pro_numbers[::5]) #[0, 5, 10, 15, 20]

# tuple
pro_tuple = (1,2,3,4,5)

pro_tuple_slice = pro_tuple[:2]
print(pro_tuple_slice)

#字符串也可以用切片操作，只是操作结果仍是字符串
pro_strings = 'ADFCVFRRERRYUI'
pro_strings_slice = pro_strings[:6]
print(pro_strings_slice)


# 2.迭代
pro_dict =  {'a': 1, 'b': 2, 'c': 3}
# 默认迭代的是key
for key in pro_dict:
    print(key)
for value in pro_dict.values():
    print(value)

'''
任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，
只要符合迭代条件，就可以使用for循环。
'''

#3.列表生成式
'''
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
'''

pro_numberslist = [x * x for x in range(1, 11)]
print(pro_numberslist)#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

pro_twolistLaba = [m+n for m in 'abs' for n in 'xya']
print(pro_twolistLaba)#['ax', 'ay', 'aa', 'bx', 'by', 'ba', 'sx', 'sy', 'sa']

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
pro_xx = [x*x for x in range(1,11) if x % 2 == 0]
print(pro_xx)#[4, 16, 36, 64, 100]

#三层和三层以上的循环就很少用到了。

'''
运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，
可以通过一行代码实现
'''
import os

pro_filepath = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(pro_filepath)

pro_dict = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in pro_dict.items():
    print(k,'=',v)
'''
x = A
y = B
z = C

'''

pro_xx_dict = {
    'x':'A',
    'y':'B',
    'z':'C',
    'w':'D'
}
pro_xx_dictlist = [k + '=' + v for k,v in pro_xx_dict.items()]
print(pro_xx_dictlist) # ['x=A', 'y=B', 'z=C', 'w=D']

pro_charavters = ['hello','world','inm','jobs','apple']
pro_charavters_lowers = [x.lower() for x in pro_charavters]
print(pro_charavters_lowers) #['hello', 'world', 'inm', 'jobs', 'apple']
#最后把一个list中所有的字符串变成小写：

#if ... else在列表生成式中的应用
pro_if_elselist = [x if x % 2 ==0 else -x for x in range(1,12)]
print(pro_if_elselist) #[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10, -11]

x = 7
print(x if x % 2 == 0 else -x)
# x if x % 2 == 0  就是错误的

pro_LLLL = ['Hello', 'World', 18, 'Apple', None]
pro_LLLL_lower = [s.lower() for s in pro_LLLL if isinstance(s,str)]
print(pro_LLLL_lower)

if pro_LLLL_lower == ['hello', 'world', 'apple']:
    print('测试通过')
else:
    print('测试失败')
'''
运用列表生成式，可以快速生成list，
可以通过一个list推导出另一个list，而代码却十分简洁。
'''

#4.生成器

pro_shengchengqilist = [x * x for x in range(10)]
print(pro_shengchengqilist) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pro_generator = (x*x for x in range(10))
print(pro_generator)
for n in pro_generator:
    print(n)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n += 1
    return 'done'

print(fib(5))
'''
1 n=0
1 n=1
2 n=2
3 n=3
5 n=4
done n=5
'''
#改造上面的函数
def pro_fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

pro_oo = pro_fib(4)
print(next(pro_oo))
print(next(pro_oo))
print(next(pro_oo))
'''
1
1
2
'''


def pro_odd():
    print('step1')
    yield 1
    print('step2')
    yield(3)
    print('step3')
    yield(5)

o = pro_odd()
print(next(o))
print(next(o))
'''
step1
1
step2
3
'''

pro_gg = pro_fib(6)
while True:
    try:
        x = next(pro_gg)
        print('gg:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# 关于如何捕获错误，后面的错误处理还会详细讲解。

'''

杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1

'''

def yanghuisanjiao(max):
    n = 0
    row = [1]
    while(n < max):
        n+=1
        yield (row)
        row = [1] +[row[k] + row[k+1] for k in range(len(row)-1)] + [1]


results = yanghuisanjiao(6)
for x in results:
    print(x)

'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
'''

'''
请注意区分普通函数和generator函数，普通函数调用直接返回结果
generator函数的调用实际返回一个generator对象
'''

# 迭代器 可以使用isinstance()判断一个对象是否是Iterable对象
from  collections.abc import Iterable

print(isinstance([],Iterable)) # True
print(isinstance(100, Iterable)) #False


'''

'''