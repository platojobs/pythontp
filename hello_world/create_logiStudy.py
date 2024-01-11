"""
水仙花数也被称为超完全数字不变数、自恋数、自幂数、
阿姆斯特朗数，它是一个3位数，
该数字每个位上数字的立方之和正好等于它本身，
例如：$1^3 + 5^3+ 3^3=153$。

"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low**3 + mid**3 + high**3:
        print("水仙花数==%d", num)


"""
正整数反转

pinum = int(input("pinum = "))
reversed_num = 0
while pinum >0:
    print(pinum)
    reversed_num = reversed_num*10 + pinum % 10
    print(reversed_num)
    pinum //= 10
    print(pinum)
print(reversed_num)

"""

"""
公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？


            
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100 and x > 0 and y > 0 and z > 0:
           # print("公鸡：%d 只， 母鸡= %d 只， 小鸡 = %d 只", x, y, z)
            print("公鸡：%d 只， 母鸡= %d 只， 小鸡 = %d 只" %(x, y, z))
