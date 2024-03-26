import csv
import requests


# 定义列表转字符串函数
def list_to_str(i):
    if i == []:
        # 如果为空数组，则将其设为 None 或者某个默认值
        return None
    else:
        # 如果不为空，则继续使用原来的值
        separator = "，"
        result = separator.join(i)
        return result


def keyword_search(
    input_file=None, keywords=None, city=None, types=None, output_file="poi.csv"
):
    url = "https://restapi.amap.com/v3/place/text"
    pois = []
    if input_file is not None:
        # 读取包含地名的csv文件
        with open(input_file, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 构造请求参数
                page = 1
                while True:
                    params = {
                        "key": "161e94976c239ae8e4b069ff76848aad",
                        "keywords": row["名称"],
                        "city": row["城市"],
                        "citylimit": True,
                        "output": "JSON",
                        "offset": 20,  # 每页输出的POI数量，默认为20
                        "page": page,
                        "extensions": "all",
                    }
                    # 发送请求
                    response = requests.get(url, params=params)
                    data = response.json()  # data是一个字典
                    print(data)
                    print(response.text)  # 打印出服务器的响应文本
                    if data["status"] == "1":
                        if not data["pois"]:  # data["pois"]是一个列表
                            break
                        pois.extend(data["pois"])
                    else:
                        print(f"Error: {data['info']}")
                        break
                    page += 1

        # 将结果保存到csv文件中
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "id",
                    "名称",
                    "类型",
                    "类型编码",
                    "地址",
                    "经度",
                    "纬度",
                    "电话",
                    "邮编",
                    "网站",
                    "邮箱",
                    "省份编码",
                    "省份名称",
                    "城市编码",
                    "城市名称",
                    "区域编码",
                    "区域名称",
                    "图片地址",
                ]
            )  # writer.writerow只能写入传递格式为列表或者元组的参数
            for poi in pois:
                location = poi["location"].split(",")
                photo = list(poi["photos"])
                str = ""
                if len(photo) == 0:
                    str = ""
                else:
                    str = photo[0]["url"]
                writer.writerow(
                    [
                        poi["id"],
                        poi["name"],
                        poi["type"],
                        poi["typecode"],
                        poi["address"],
                        location[0],
                        location[1],
                        poi["tel"],
                        list_to_str(poi["postcode"]),
                        list_to_str(poi["website"]),
                        list_to_str(poi["email"]),
                        poi["pcode"],
                        poi["pname"],
                        poi["citycode"],
                        poi["cityname"],
                        poi["adcode"],
                        poi["adname"],
                        str
                    ]
                )  # poi['postcode'],poi['website'],poi['email']均是列表

    elif city is not None or types is not None:
        # 构造请求参数
        page = 1
        while True:
            params = {
                "key": "161e94976c239ae8e4b069ff76848aad",
                "city": city,
                "types": types,
                "citylimit": True,
                "output": "JSON",
                "offset": "10",  # 每页输出的POI数量，默认为20
                "page": page,
                "extensions": "all",
            }
            # 发送请求
            response = requests.get(url, params=params)
            data = response.json()
            print(data)
            if data["status"] == "1":
                if not data["pois"]:
                    break
                pois.extend(data["pois"])
            else:
                print(f"Error: {data['info']}")
                break
            page += 1

        # 将结果保存到csv文件中
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "id",
                    "名称",
                    "类型",
                    "类型编码",
                    "地址",
                    "经度",
                    "纬度",
                    "电话",
                    "邮编",
                    "网站",
                    "邮箱",
                    "省份编码",
                    "省份名称",
                    "城市编码",
                    "城市名称",
                    "区域编码",
                    "区域名称",
                    "图片",
                ]
            )  # writer.writerow只能写入传递格式为列表或者元组的参数
            for poi in pois:
                location = poi["location"].split(",")
                photo = list(poi["photos"])
                str = ""
                if len(photo) == 0:
                    str = ""
                else:
                    str = photo[0]["url"]
                writer.writerow(
                    [
                        poi["id"],
                        poi["name"],
                        poi["type"],
                        poi["typecode"],
                        poi["address"],
                        location[0],
                        location[1],
                        poi["tel"],
                        list_to_str(poi["postcode"]),
                        list_to_str(poi["website"]),
                        list_to_str(poi["email"]),
                        poi["pcode"],
                        poi["pname"],
                        poi["citycode"],
                        poi["cityname"],
                        poi["adcode"],
                        poi["adname"],
                        str
                    ]
                )


# keyword_search(input_file='./city.csv', output_file='地名_POI.csv')
keyword_search(city="330000", types="060101", output_file="zhejiangsheng_shopping.csv")
# 河北、山西、黑龙江、吉林、辽宁、江苏、浙江、安徽、福建、江西、山东、河南、湖北、湖南、广东、海南、四川、贵州、云南、陕西、甘肃、青海、台湾。