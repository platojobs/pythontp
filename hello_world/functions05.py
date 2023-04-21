import math

#1. 求绝对值的函数abs
print(abs(-30))

# 而max函数max()可以接收任意多个参数，并返回最大的那个
sd_Maxscore = max(1,23,4,5,6,99)
print(sd_Maxscore)

# 数据类型转换
s_strue = bool(1)
print(s_strue)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
s_afunc = abs
print(s_afunc(-40))
colorsss = 100
print(hex(colorsss))

# 定义函数
def my_abs(x):
 if x>= 0:
  return x
 else:
  return -x

print(my_abs(-90))

# 空函数
def nop():
  pass

print(nop())

# 数据类型检查
def my_funcAbs(x):
  if not isinstance(x,(int,float)):
   raise TypeError('bad operand type')
  if x >= 0:
   return x
  else:
   return -x

print(my_funcAbs(12.3))

# 返回多个值

def move(x,y,step,angle=0):
  nx = x + step*math.cos(angle)
  ny = y - step*math.sin(angle)
  return nx, ny
r = move(100,100,60,math.pi/6)
x,y = move(100,100,60,math.pi/6)
print(r)
print(x,y)

'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。

'''


'''
练习

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 

 a*x**2 +b*x+c=0 的两个解。



'''

def quadratic(a, b, c):
   if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)) :
    raise TypeError('bad operand type error')
   else:
    print('start')
    s1 = b**2 - 4*a*c
    print(s1)
    x1 = (-b + math.sqrt(abs(s1)))/(2*a)
    x2 = (-b - math.sqrt(abs(s1)))/(2*a)
    return x1,x2

s = quadratic(2,3,4)

print(s)

# 函数的参数
def power(x,n):
   return x**n

print(power(5,3))

# 参数

def enroll(name,gender,age=6,city='BeiJing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
    return '--END--'
print(enroll('Sarach','F'))

def enroll_s(name: str):
    if not  isinstance(name,str):
        raise TypeError('type error')
    else:
        print(name)


my_foods = ['pizza','falafel','carrotcake']
friend_foods = my_foods[:]
friend_foods.append('cake')
print(friend_foods)
print(friend_foods[0:4:2])  #步长值取值


'''
定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
def add_end(L=None):
    if L is None:
        L =[]
        L.append("END")
        return L
print(add_end())
print(add_end())

# 可变参数
def calc(numbers):
    s_sum = 0
    for n in numbers:
        s_sum = s_sum + n**2
    return s_sum

# 组装的调用
ss_sum = calc([1,2,3])
print(ss_sum)

print(calc((1,3,5,7)))

'''
1,5,9
1,10,35,84
'''

def s_calc(*numbers):
    s_sum = 0
    for n in numbers:
        s_sum = s_sum + n**2
    return s_sum

# 不用组装的调用
print(s_calc(1,2,3))
print(s_calc(1,3,5,7))
'''
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，
参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，
可以传入任意个参数，包括0个参数
'''
print(s_calc())
print(s_calc(1,2))

'''
如果已经有一个list或者tuple，要调用一个可变参数怎么办？
'''
nums = [1,2,3]
print(s_calc(nums[0],nums[1],nums[2]))
#另外一种 *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
print(s_calc(*nums))

# 关键字参数
'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。
'''

def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

print(person('Michael',30))

print(person('Bob',35,city='BeiJing'))
print(person('Adam', 45, gender='M', job='Engineer'))
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
print(person('jobs',45,extra = extra))
print(person('KK',100,**extra)) # 效果同185
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
对kw的改动不会影响到函数外的extra
'''

#命名关键字参数
'''
对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，
就需要在函数内部通过kw检查。
'''
def s_person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

print(s_person('jack',24,city ='BeiJing',addr= 'Chaoyang',zipcode= 123))

#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下

def ss_person(name,age,*,city,job):
    print(name,age,city,job)

print(ss_person('HuangHua',45,city='BeiJing',job ='Teacher'))

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person_notApplyPerson(name,age,*args,city='深圳',job):
    print(name,age,args,city,job)

print(person_notApplyPerson('Mick',34,'Nike',city='GG',job='Worker'))

print(person_notApplyPerson('ZuSong',45,job='worker'))

#位置参数和命名关键字参数

#参数组合

'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用。但是请注意，
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''


def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

'''

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。


'''

# 递归函数
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(1))
print(fact(2))
print(fact(3))

'''
解决递归调用栈溢出的方法是通过尾递归优化，
事实上尾递归和循环的效果是一样的，
所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，
并且，return语句不能包含表达式。这样，
编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
都只占用一个栈帧，不会出现栈溢出的情况。
'''

#尾递归
def fact_iter(num,product):
    if num == 1:
       print(f'表达式===》{num}*{product}')
       return product
    print(f'表达式===》{num}*{product}')
    return fact_iter(num-1 , num*product)
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
'''
遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。哈哈笑死
'''
fact_iter(5,1)
print(fact_iter(5,1))

'''
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，
没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

'''

'''
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法，

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C


'''

def pro_hannuota(n,A,B,C):
    if n ==1:
        print(A,'--->',C)
    else:
        pro_hannuota(n-1,A,C,B)
        print(A,'--->',C)
        pro_hannuota(n-1,B,A,C)


pro_hannuota(3,'A','B','C')