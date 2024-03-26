from openpyxl import load_workbook
import  requests

def seedfind_shopcenter():
        url = "https://restapi.amap.com/v5/place/text"
        params = {
            'key': '161e94976c239ae8e4b069ff76848aad',
            'output': 'json',
            'keywords': '购物中心',
            "page_size":50,
            "page_num":1


        }
        print(url)
        response = requests.get(url,params)
        if response.status_code == 200:
             data = response.json()
             print(data)
             print("-----")
             if data["status"] == "1":
                reslts = data["pois"]
                print(reslts)
                print("++++")
                for dic in reslts:
                    print(dic["address"],dic["name"],dic["location"])
                return reslts
             else:
                print(data["info"])
        else:
          print("请求失败")




# 打开Excel文件
workbook = load_workbook(filename='shoppingcenter.xlsx')
sheet1 = workbook['Sheet1']
reslts =seedfind_shopcenter()
for dic in reslts:
    locaton = dic["location"]
    arr = locaton.split(",")
    row = [dic["name"],dic["adcode"],dic["pname"],dic["cityname"],dic["adname"],dic["type"],dic["address"],arr[0],arr[1]]
    sheet1.append(row)
# 保存 Excel 文件
workbook.save(filename='shoppingcenter.xlsx')
# 关闭 Excel 文件
workbook.close()
