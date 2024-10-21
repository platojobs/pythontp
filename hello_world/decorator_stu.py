import time


def cctv6(func):
    def punch():
        print(time.strftime("%Y-%m-%d",time.localtime(time.time())))
        func()
    return punch

@cctv6
def cctv77():
    print("电视剧: 《安宁》 部门：导演 下班了")


cctv77()
