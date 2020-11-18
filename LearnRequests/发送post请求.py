"""
发送post请求
1,使用data传表单格式的参数
2，使用json传json格式的参数
3，带请求头使用headers
"""
import requests
# 发送post请求，带参数时，可以使用data或json来传参，具体使用哪个要看系统怎么实现
# 上一步注册成功的手机号，验证登录，登录使用post

ur1 = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"18178961234","pwd":"123455"}
r = requests.post(ur1,data=canshu)
print(r.text)

r = requests.post(ur1,json=canshu)# json,金融系统不支持json方式传参
print(r.text)

# 发送请求到httpbin，观察区别
r = requests.post("http://www.httpbin.org/post", data=canshu)#"Content-Type": "application/x-www-form-urlencoded",
print(r.text)
r = requests.post("http://www.httpbin.org/post", json=canshu)#"Content-Type": "application/json",
print(r.text)