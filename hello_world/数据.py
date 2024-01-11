
class Account:
     def __init__(self, accout_holder):
         self.balance = 0
         self.holder = accout_holder
     def dsposit(self,amount):
         self.balance = self.balance + amount
     def withdraw(self,amount):
         if amount > self.balance:
             return "余额不足"
         self.balance = self.balance - amount
         return  self.balance



a = Account("Jack")

print(a.holder,a.balance)

a.balance = 128

print(a.balance)

b = Account("KKKK")
b.balance = 200

c = [v.balance for v in (a,b)]

print(c)
b.dsposit(120) # 存款120
print(b.balance)
b.withdraw(400)
print(b.withdraw(400))


ss = {"ss":"kk" }
print(ss["ss"])

set = {1,2,3,4,5}
print(set)

print(type(set))
print(abs(-3))