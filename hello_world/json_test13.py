import  json

numbers = [2,3,4,5,22,13]
filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)

from name_function import  get_formatted_name

a = get_formatted_name("Janis","Joplin","Jobs")

print(a)