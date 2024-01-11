#字符串和编码
abc_length = len('ABC')
print(abc_length)

# 格式化 - 占位符
'''
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数

'''


print('Age: %s. Gender:%s'%(24,True)) # %s  它会把任何数据类型转换为字符串
print('growth rate: %d %%'%7)  # %

'''
打印结果：
3
Age: 24. Gender:True
growth rate: 7 %

'''

# format() 函数
print('hello , {0} ,score is {1:.2f}%'.format('Jos',23.13235))
#打印结果： hello , Jos ,score is 23.13%

# f-string
r = 2.34
s = 3.14 * r**2
print(f'The area of a circle with radius {r} is {s:.4f}')

# The area of a circle with radius 2.34 is 17.1934
'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：

'''
# 解法1
s1 = 72
s2 = 85
score_r = (s2 -s1)*100/s1
print(f'小明成绩提高了{score_r:.1f}%')
# 解法2
print('小明成绩提高了%.1f%%'%score_r)

'''
Python 3的字符串使用Unicode，直接支持多语言 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8
'''

print('中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文

