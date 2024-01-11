
# 字符串的切片
custom_str = "abc123456"
print(len(custom_str))
print(custom_str[2:5])  #c12
print(custom_str[-7:-4]) #c12

print(custom_str[2:]) #c123456
print(custom_str[2::2]) #c246

print(custom_str[::2]) #ac246
print(custom_str[1:-1:2]) #b135


print(custom_str[7:1:-1]) #54321c
print(custom_str[-2:-8:-1]) #54321c
print(custom_str[7::-1]) #54321cba
print(custom_str[::-2]) #642ca

print("~~~~~分割线0~~~~~~~~")

# 循环遍历每个字符1 下标遍历
custom_strXh = "plato jobs"
for index in range(len(custom_strXh)):
    print(custom_strXh[index])

print("~~~~~~分割线一~~~~~~~")
# 循环遍历字符串2 直接遍历
for ch in custom_strXh:
    print(ch)

print("~~~~~~~~分割线二~~~~~~~~")

# 字符串的相关操作
# 首字母大写后的字符串
print(custom_strXh.capitalize()) #Plato jobs
# 获取字符串每个单词的首字母大写的字符串
print(custom_strXh.title()) #Plato Jobs
# 获得所有字母大写的后的字符串
print(custom_strXh.upper()) # PLATO JOBS


sss2 = "HELLO"
# 所有小写字母
print(sss2.lower()) # hello

# 找到了目标字符串中给定字符串的首字符的索引
print(sss2.find("LO")) # 3

# 找不到的会返回-1
print(sss2.find("shit")) # -1

print("~~~~~~~~分割线三~~~~~~~~~~~")

sttt = "hello good world"

#从前向后查找字符o出现的位置(相当于第一次出现)
print(sttt.find("o")) # 4
#从索引为5的位置开始查找字符o出现的位置
print(sttt.find("o",5)) # 7
#从后向前查找字符o出现的位置(相当于最后一次出现)
print(sttt.rfind("o")) # 12

# 从性质判断
stsrTT = "hello world!"
# startwith方法检查字符串是否以指定的字符串开头返回布尔值
print(stsrTT.startswith("He"))
print(stsrTT.startswith("hel"))
#endswith方法检查字符串是否以指定的字符串结尾返回布尔值
print(stsrTT.endswith("!"))

startS3 = "abc123456"

#isdigit方法检查字符串是否由数字构成返回布尔值
print(startS3.isdigit())
#isalpha方法检查字符串是否以字母构成返回布尔值
print(startS3.isalpha())
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(startS3.isalnum())

# 格式化字符串
stonStr = "hello,world"
print(stonStr.center(20,"*")) #****hello,world*****
print(stonStr.rjust(20,"~")) #~~~~~~~~~hello,world
print(stonStr.ljust(20,"~")) #hello,world~~~~~~~~~
# 左侧补齐5位
print("33".zfill(5))
print("-33".zfill(5))
#字符串的格式化
a = 321
b = 123
print("%d *%d = %d" %(a,b,a*b))
print(f"{a} *{b} = {a * b}") # python3.6以后得简化模式

c = -1
print(f"{c:+.2f}")  # 带符号保留位

d = 3.1415926
print(f"{d:.0f}")
print("%.0f" % d)

digitbum = 12345678
print(f"{digitbum:x<10d}") # 12345678xx
print(f"{digitbum:,}") #12,345,678
flo_dightnum = 0.123
print(f"{flo_dightnum:.2%}")  #12.30%

ext_num = 1234566778
print(f"{ext_num:.2e}") # 1.23e+09 科学计数法
print("---====")
ss = '  jackfrued@126.com  \t\r\n'
print(ss)
print("--------")
print(ss.strip())

# 替换操作
