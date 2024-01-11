width = 20
int_nofloat = 20 // 3
print(int_nofloat)
name = "jhon"
text = name + "Palto"
print(name)
print(text)

"""
f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
print("%.1f华氏温度 = %.1f摄氏温度" % (f ,c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
print(f"{f:.1f}华氏度 = {c:.1f}摄氏度")

"""

"""
radius = float(input("请输入半径："))
perimeter = 2*3.1415926*radius
area = 3.1415926*(radius**2)
print("周长：%.2f" % perimeter)
print("面积： %.2f" % area)
print(f"周长 = {perimeter:.2f}， ，面积 = {area:.2f}")
"""

"""
year = int(input("请输入月份："))
is_leap = year % 4 ==0 and year % 100 != 0 or year % 400 ==0
print(is_leap)
print(year % 100)

"""

"""
username = input("请输入姓名：")
password = input("亲输入密码：")
if username == "admin" and password == "123456" :
    print("身份验证成功")
else:
    print("身份验证失败")
"""

"""
x = float(input("x="))
if x>1:
    y = 3*x - 5
elif x>=-1:
    y = x + 2
else:
    y = 5*x + 3
print("x = %.2f , y = %.2f" % (x , y))

"""

"""

value = 12.0
unit = "cm"
if unit == "in" or unit == "英寸":
    print("%.2f英寸 = %.2f厘米" % (value,value*2.54))
elif unit == "cm" or unit == "厘米":
    print("%.2f厘米 = %.2f英寸" % (value , value/2.54))
else:
    print("输入错误")

score = float(input("请输入成绩:"))
if score >= 90:
    grade = "A"
elif score >=80:
    grade = "B"
elif score >=70:
    grade = "C"
elif score >=60:
    grade = "D"
else:
    grade = "E"
print("对应的等级:", grade)

"""

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if a + b > c and a + c > b and b + c >a:
    print("周长:%.f" % (a +b + c))
    p = (a+b+c) / 2
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    print("area = %.2f" % area)
else:
    print("not is 三角形")







