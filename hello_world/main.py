# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#from functions05 import my_abs


print('hello.world')
#这是第一个程序

print(r'''hello,\n
world''')

print(3>2)
print('ABC'.encode('ascii'))   #以Unicode表示的str通过encode()方法可以编码为指定的bytes

message =  b'\xe4\xb8\xad\xff'
print(message.decode('utf-8',errors='ignore'))

print(len('abc'))

classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('adam')
print(classmates)
classmates.insert(1,'jack')
print(classmates)
classmates.pop()
print(classmates)