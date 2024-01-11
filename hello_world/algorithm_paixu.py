
# 简单选择排序
def select_sort(items, comp = lambda x, y : x <y):
    items = items[:]
    for i in range(len(items)-1):
        min_index= i
        for j in range(i+1, len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items[min_index],items[i]
    return items

items = [1,2,3,34,99,4,998,234,123,3,4,55,6677,888]

print(select_sort(items)) # [1, 2, 3, 3, 4, 4, 34, 55, 99, 123, 234, 888, 998, 6677]

print("====~~~~~~~~分割线~~~~~~~~")

# 冒泡排序
def bubble_sort(items,comp = lambda x,y : x>y):
    items = items[:]
    for i in range(len(items) -1):
        swapped = False
        for j in range(len(items) -1 - i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True
        if not swapped:
            break
    return items

print(bubble_sort(items))

print("~~~~~~~~~~~~分割线~~~~~~~~~~")

list_ui = [1,2,3,4,7]
