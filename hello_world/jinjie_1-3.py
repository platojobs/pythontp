# 生成式或者推导式的用法
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

prices2 = { key: value for key,value in prices.items() if value > 100 }
print(prices2)

# 嵌套列表的坑

def qiantaoList():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    courses = ['语文', '数学', '英语']
    scores = [[None] * len(courses) for _ in range(len(names))]
    print(scores)
    for row ,name in enumerate(names):
        print(row)
        for col,course in enumerate(courses):
            print(col,course)
            scores[row][col] = float(input(f"请输入{name}的{course}成绩："))
            print(scores)

#qiantaoList()

import heapq
# 堆排序
def heap_list():
    list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
    list2 = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print(heapq.nlargest(3, list1))
    print(heapq.nsmallest(3, list1))
    print(heapq.nlargest(2, list2, key=lambda x: x['price']))
    print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
    print(heapq.nsmallest(2,list2,key = lambda x: x["price"]))
    print(heapq.nsmallest(2,list2,key = lambda x: x["shares"]))

# heap_list()


# itertools模块
import  itertools

def itertools_test():
    itertools.permutations("ABCD")
    itertools.combinations("ABCDE",3)
    itertools.product("ABCD","123")
    itertools.cycle(("A","B","C"))

#itertools_test()
from collections import Counter
def collections_test():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
        'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    counter = Counter(words)
    print(counter.most_common(3)) # 列出出现最多的元素

# collections_test()

def test(key,value):
    print(key)
    print(value)

dicts = {"name":"jobs","age":"12"}
test(*dicts)

def add(x,y):
    return x + y
lambda