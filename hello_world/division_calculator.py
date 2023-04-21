import word_count
print("Give me two numbers, and T'll divide them.")
print("Enter 'q' to quit. ")
'''
while True:
    first_number = input("\n First number:")
    if first_number == 'q':
       break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = 0
    try:
       answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
       print("YouError")
    else:
       print(answer)
'''

# 调用方法

word_count.count_words("alice.txt")
