import array

symbols = "$"
codes= []
# 第一种方式
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

#第二种方式
sec_codes = [ord(symbol) for symbol in symbols ]
print(sec_codes)


x = "my precious"
dumy = [x for x in "ABC"]
print(x)

byond_sc = [ord(s) for s in symbols if ord(s) > 30]
print(byond_sc)

beyond_sc = list(filter(lambda c: c > 30 , map(ord,symbols)))
print(beyond_sc)

xsymbol = "apple"
sd = tuple(x for x in xsymbol)
print(sd)
sddd = array.array("I",(ord(x) for x in xsymbol))
print(sddd)

sizes = ["黑","红","梅","方"]
colors = ["黑色","红色"]

for zh in ("%s%s"%(c,s) for c in colors for s in sizes):
    print(zh)


city,year,pop,chg,area = ("tokyo",2003,32450,0.66,8014)
traveler_ids = [("USA","31195855"),("BRA","CE342567"),("ESP","XDA205856")]
for passport in sorted(traveler_ids):
    print("%s/%s"%passport)
for country , _ in traveler_ids:
    print(country)


print(divmod(20,8))  #（2，,4）

t = (20,8)
# （*运算符）把一个可迭代对象拆开作为函数的参数
print(divmod(*t))
