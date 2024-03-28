name = "small girl"
print(name.title())
print(name.upper())
print(name.lower())
print(name.islower())

sname = "i 'm a"

ssname = f"{sname} {name}"
print(ssname) # i 'm a small girl
print(f"Hello, {ssname.title()}") # Hello, I 'M A Small Girl

favorite_language = "english "
print(favorite_language)
print(favorite_language.rstrip()) # 删除空白字符

message = "One of Python's strengths is its diverse community."
print(message)

fb_name = "Jobs"
print(f"Hello {fb_name}, would you like to learn some Python today?")

albet = "Albert Einstein once said,“A person who never made a \nmistake never tried anything new.”"
print(albet)

famous_person = " Yu Guo "
print(famous_person.lstrip()) # 剔除前面的空白
print(famous_person.rstrip()) # 剔除尾部的空白
print(famous_person.strip()) # 剔除两端的空白
message = (f"{famous_person} once said,\"A person who nerver make a \n mistake never tried anything new.\"")
print(message)
famous_person = famous_person.strip()
print(famous_person)
message =  (f"{famous_person} once said,\"A person who nerver make a \n mistake never tried anything new.\"")
print(message)

universe_age = 14_000_000
print(universe_age)

# 要指出应将特定的变量视为常量，可将其字母全部大写。
MAX_CONNECTIONS = 500
print(MAX_CONNECTIONS)

bicycles = [1,2,2,3,"34","sss"]
print(bicycles)
print(bicycles[0])
bicycles.append("we")
bicycles.insert(0,"indexss")
print(bicycles)
del bicycles[1]
print(bicycles)
first_owned = bicycles.pop(0)
print(first_owned)
print(bicycles)
bicycles.remove(2)
print(bicycles)