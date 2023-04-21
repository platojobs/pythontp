import requests
import json

baseUrl = 'http://apiold.17duu.com/'

# get请求
s = '深圳'.encode(encoding='UTF-8')
s_url = f'{baseUrl}/services'
pramas_data = {
    'page':1,
    'limit':10,
    'field': 1
}

#server_r = requests.get(s_url,params=pramas_data)

#print(server_r.url)
#print(server_r.text)
#print(server_r.json())
#print(server_r.headers)

headers = {'Server': 'nginx',
           'Content-Type': 'application/json',
           'Transfer-Encoding': 'chunked',
           'Connection': 'keep-alive',
           'X-Powered-By': 'PHP/7.2.15',
           'Cache-Control': 'private, must-revalidate',
           'Date': 'Fri, 19 Aug 2022 07:36:30 GMT',
           'ETag': '"9b0cd4ec6b5a3e87b78821f140ef0eb06d6632ec"',
           'Access-Control-Allow-Headers': 'Origin, Content-Type, Cookie, Accept, Source, Authorization,Duu-Client',
           'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, OPTIONS, DELETE',
           'Access-Control-Allow-Credentials': 'true',
           'Set-Cookie': '17duu_session=eyJpdiI6InprbFllMDhidUIrMWZ2TU12cXdaVUE9PSIsInZhbHVlIjoiYjJXcENPR1JSZFBFdTJleDg3UCtITjltXC9qMG1MY1FLV3NjQmZQamx0aE1INUkxRUZFWWJVc2I2YXo3STFOQlg4aUswdFFVUEpkbFA3dDZjbDlyMG9RPT0iLCJtYWMiOiI2MzhiYjc0NGUxMmFjOWQ4ZGNkMDY5N2EzZDY0MjU3OGU4NGEzZDE2ZTUxNTE2OTM1ZjEwOWRlZTYxYTI5ZTIzIn0%3D; expires=Fri, 19-Aug-2022 09:36:30 GMT; Max-Age=7200; path=/; HttpOnly'
           }

#post
pramas_data = {
    'content':'一个大傻叉，屌丝，大傻逼测试测试， 你大爷，赌博测试测'
}
server_r = requests.post('https://apiold.17duu.com/green/filter-text',params=pramas_data)

print(server_r.json())
print(server_r.headers)

s_header ={'Server': 'nginx',
           'Content-Type': 'application/json',
           'Transfer-Encoding': 'chunked',
           'Connection': 'keep-alive',
           'X-Powered-By': 'PHP/7.2.15',
           'Cache-Control': 'private, must-revalidate',
           'Date': 'Fri, 19 Aug 2022 07:44:35 GMT',
           'ETag': '"44563a5db9510f19eab3d2d54a022ed96e8c7de4"',
           'Access-Control-Allow-Headers': 'Origin, Content-Type, Cookie, Accept, Source, Authorization,Duu-Client', 'Access-Control-Allow-Methods': 'GET, POST, PATCH, PUT, OPTIONS, DELETE',
           'Access-Control-Allow-Credentials': 'true',
           'Set-Cookie': '17duu_session=eyJpdiI6Ik1BdllnRXptZTYxTUw0OUNEaHpvSUE9PSIsInZhbHVlIjoiVWgyamIxNVFMb2RhREhQdll0Mm1IY3FqRlVSV2pjQzU3Y0o1VTd1Mkt5VGJkNHFvWUg5YWs1NE12SWtCeFZPUFlINEE0Q0tNVXlZU2RuU094RFdLc3c9PSIsIm1hYyI6ImU3MTBkZmQxNTA3MjdhOTE0YWRmNThlMmM4ZmJiZjNhMDA5Mzc4MTUzYzNiYzgxMTBiY2Y0MTJlMTMzOTcyZGMifQ%3D%3D; expires=Fri, 19-Aug-2022 09:44:35 GMT; Max-Age=7200; path=/; HttpOnly'
           }



