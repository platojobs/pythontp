
import requests
import json

def func_requset(sstr:dict):
 # jsonstr = json.dumps(sstr)
  resp = requests.get("https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=alamap&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E8%B4%AD%E7%89%A9%E4%B8%AD%E5%BF%83&c=289&src=0&wd2=&pn=0&sug=0&l=12&b=(13469224.026196316,3608474.036809816;13560387.88779141,3663552.203190184)&from=webmap&biz_forward={%22scaler%22:2,%22styles%22:%22pl%22}&sug_forward=&auth=uxNVEBLHVEVtEBODKUQWOKyDUxb8XLQ8ehefG0N6JSWa925252SUc15jDECET%40KHRKKK%40BvxRYuVtvkGcuVtvvhguVtvyheuVtvCMGuVtvCQMuVtvIPcuxtw8wkv7uvZgMuVtv%40vcuVtvc3CuVtcvY1SGpuxEtHpZZ2eGveGvuEHtAimNz8yvh3CuVtvhgMuzVVtvrMhuxVtNllgl1GDf0wd0vyO7FCMFFF7&seckey=e%2BTmSTAtX1D82hWE0kneROzEYUGmyMGlUy2sQduQqbA%3D%2Ck35g4SP5f6H40GfCg4-qOUilmuTCQSKaOBS4XBHb501mRdB-EhsqQWfhdNVTTejEGb2TlTDnemUbeT4hPnGNZTC-T25914vqlr9NoeO6vynqOY1cUIkbGdJeDUVZF697JVfbYbDVqhiv6xibAe4q0T1KVeezsZpqMkuthBmlCJAE5kSUU4rSLe4558e5yCE1&device_ratio=2&tn=B_NORMAL_MAP&nn=0&u_loc=12682859,2557255&ie=utf-8&t=1704365184800&newfrom=zhuzhan_webmap")
  data_model = json.loads(resp.text)
  print(data_model)
  for news in data_model["result"]["list"]:
      print(news["title"] + "==00")


dicts = {
  "code": 200,
  "msg": "success",
  "result": {
    "curpage": 1,
    "allnum": 500,
    "list": [
      {
        "id": "0f6c3e7827c44b107b8064dd36ea2e08",
        "ctime": "2022-04-22 16:35",
        "title": "爸爸说敢养宠物就搬出去，女孩冒险带回一只猫，结果自己没地位了",
        "description": "有的没有养宠物的人会特别讨厌这些小动物，然后要是自己的家人想要养宠物的，他们就会变得很生气，可是如果...",
        "source": "新浪宠物",
        "picUrl": "https://n.sinaimg.cn/sinakd20220422ac/40/w480h360/20220422/ecb6-68e76539cbbf40a81d4bcdeec168e3c2.jpg",
        "url": "https://k.sina.com.cn/article_6381647155_17c60353300101d5md.html"
      },
      {
        "id": "afd8371d851233036581c5f7fda50d7f",
        "ctime": "2022-04-22 16:35",
        "title": "男子带回蜥蜴当宠物，众人看后不敢靠近，男子一句话众人无语了",
        "description": "现在很多人家里都比较喜欢养一些宠物，其中比较多的可能就是猫狗了吧，可是有些人并不喜欢这种比较平常的动...",
        "source": "新浪宠物",
        "picUrl": "https://n.sinaimg.cn/sinakd20220422ac/40/w480h360/20220422/d303-2b40f71637f16ddd5643698ada95234a.jpg",
        "url": "https://k.sina.com.cn/article_6348919861_17a6cd435001019dts.html"
      },
      {
        "id": "9b53b4b45982393fd7849bdf7f55cad9",
        "ctime": "2021-04-22 16:35",
        "title": "源飞宠物境外收入占9成，与中宠股份关联交易，披露数据差异大",
        "description": "伴随着独自生活的人群增多，“吸猫”“撸狗”的新生活方式正逐渐盛行。为宠“氪金”催生了宠物经济的火...",
        "source": "新浪宠物",
        "picUrl": "https://n.sinaimg.cn/spider20220422/294/w640h454/20220422/6ba3-3b4ab1485a56d29433484e301d85b9b9.png",
        "url": "https://finance.sina.com.cn/stock/newstock/zrzdt/2022-04-22/doc-imcwipii5836208.shtml"
      }
    ]
     }
   }

func_requset(dicts)