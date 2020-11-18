"""
上传文件 一般都是post接口，用files参数上传文件
"""
from cgitb import text

import requests

ur1 = "http://www.httpbin.org/post"

'''
files参数，字典的格式，'name': file-tuple
file-tuple可以是2-tuple('filename',fileobj)、3-tuple、4-tuple
'''
# with open("d:/test.txt",encoding='utf-8') as f:
#     # ，“text/plain” 如果上传的是一个文本文件，可以去掉content_type，默认文件类型是文本文件
#     file = {"file1":("test.txt",f,"text/plain")}
#     r = requests.post(ur1,files=file)
#     print(r.text)

# 上传一个图片文件，10k以内
# with open("d:\\p.jpg",mode='rb') as f:
#     file = {"file1":("p.jpg",f,"image/jpg")}
#     r = requests.post(ur1,files=file)
#     print(r.text)

# 可以一次上传多个文件
with open("d:\\test.txt", encoding='utf-8') as f:
    with open("d:\\test1.txt", encoding='utf-8') as f1:
        file = {"file1":("test.txt", f),"file2":("test1.txt", f1)}
        r = requests.post(ur1, files=file)
        print(r.text)

