
num_int = 10
print("num_int",num_int)
num_float = float(num_int)
print("num_float:",num_float)

pairs = [1,2,3,4,5,8,6,5,4,4,5,6,]

def count(s, value):
    total = 0
    for elem in s:
        if elem == value:
            total += 1
    return total


s = count(pairs,4)
print(s)

op_pairs = [x+1 for x in pairs]
print(op_pairs)

print(type(op_pairs))
ss_float = 3/2
ss_int = 3//2
print(type(3/2))
print(ss_float)
print(type(3//2))
print(ss_int)