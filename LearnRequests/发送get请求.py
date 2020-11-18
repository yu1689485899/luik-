"""
发送get1请求
"""

import requests

# 接口地址:"http://www.baidu.com"
# 发送一个get请求，r是接收到的响应
from urllib3.util import url

r = requests.get("http://www.baidu.com")
# 文本格式的响应内容
# print(r.text)
# # 响应码
# print(r.status_code)
# assert r.status_code == 200
# # OK
# print(r.reason)
# assert r.reason == 'OK'

# http://jy001:8081/futureloan/mvc/api/member/list
r = requests.get("http://jy001:8081/futureloan/mvc/api/loan/generateRepayments")
# r = requests.get(url)
# assert r.status_code == 200
# assert r.reason == 'OK'
# print(r.text)
#
# assert r.json()['status'] == 1
# print(333)
# assert r.json()['code'] == '20403'

# get请求带参数
# 方法1：拼接到URL后面(金融项目注册接口)
# r = requests.get("http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=18178961234&pwd=123455")
# print(r.text)
# assert r.json()['status'] == 1
# assert r.json()['code'] == '10001'
# 方法2：使用params传参
# ur1 = "http://jy001:8081/futureloan/mvc/api/member/register"
# canshu = {"mobilephone":"","pwd":"123456","regname":""}
# r = requests.get(ur1,params=canshu)
# print(r.text)

# get请求带请求头，设置User-Agent伪装成浏览器发送的请求，避免服务器屏蔽自动化发的请求
ur1 = "http://www.httpbin.org/get?mobilephone=&pwd=123456&regname=helloword" # 一个测试网站，get是接口名字，发送的请求，原封的返回来。
# r = requests.get(ur1)
# print(r.text)
#User-Agent 包含浏览器的版本号、操作系统的版本号信息。
tou ={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
r = requests.get(ur1,headers=tou)
print(r.text)

ur1 = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(ur1,headers=tou)
print(r.text)
print("蜂群算法源代码" in r.text)