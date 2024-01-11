
# 模式匹配
score = "B"
match score:
    case "A":
        print("score is A")
    case "B":
        print("score is B")
    case "C":
        print("score is C")
    case _:
        print("socre is ????")


# 复杂的匹配
age = 14
match age:
    case x if x < 10:
        print("小于10岁：%d岁嘞" % x)
        print(f"小于10岁：真实的年龄是{x}岁")
    case 10:
        print("10岁嘞")
    case 11 | 12 | 13 | 14 | 15 :
        print("11-15岁嘞")
    case 16:
        print("还是未成年呀")
    case _:
        print("not match")


# 匹配列表
items = ["gcc","hello.c","world.c","te.text"]

match items:
    case ["gcc"]:
        print("gcc: missing source file(s)")
    case ["gcc",file1,*files]:
        print("gcc compile:" + file1 + "," + ",".join(files))
    case ["clean"]:
        print("clean")
    case _:
        print("invalid command")


