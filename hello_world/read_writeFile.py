
"""
f = None
try:
    f = open("致橡树.txt","r",encoding = "utf-8")
    print(f.read())
except FileNotFoundError:
    print("无法打开指定的文件")
except LookupError:
    print("指定了未知的编码")
except UnicodeDecodeError:
    print("解码失败")
finally:
    if f :
        f.close()

"""
import time

"""
# 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源 不用通过finally 语句去释放外部资源
try:
    with open("致橡树.txt","r",encoding = "utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("无法打开指定的文件")
except LookupError:
    print("指定了未知的编码！")
except UnicodeDecodeError:
    print("读取文件时解码失败")

"""

"""
除了使用文件对象的read方法读取文件之外，
还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
"""

def read_txt():
    with open("致橡树.txt","r",encoding="utf-8") as f:
        print(f.read())
    with open("致橡树.txt",mode="r") as f:
        for line in f:
            print(line,end = "")
            time.sleep(0.1)
    print("\n==分割符号==\n")
    with open("致橡树.txt") as f:
        lines = f.readlines()
    print(lines)

# read_txt()  # 逐行读取文件内容

filenames = ('a.txt', 'b.txt', 'c.txt')
fs_list = []
for filename in filenames:
    fs_list.append(filename)
print(fs_list)