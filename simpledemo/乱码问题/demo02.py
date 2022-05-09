#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = demo02.py
@author =  Hj
@datetime = 2022/5/4
"""

import requests

url = "https://www.ip138.com/"
# url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip&oq=ip&rsv_pq=f324eeae0034d5b3&rsv_t=1614Ig0%2FSFdqQsQDSJArr7w7H2xMK5HfvMfKf%2B9lr2VQKJqf27ubkbGJ4j0&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}
respose = requests.get(url, headers=headers)
print(respose)
print(respose.status_code)
print(requests.codes.ok)
if respose.status_code != requests.codes.ok:
    pass

print("respose.encoding:", respose.encoding)
print("respose.apparent_encoding:", respose.apparent_encoding)
print("requests.utils.get_encodings_from_content:", requests.utils.get_encodings_from_content(respose.text))

print("content to text 1:", respose.content.decode(respose.encoding) == respose.text)
print("content to text 2:", str(respose.content, encoding=respose.encoding) == respose.text)

print("text to content 1:", respose.text.encode(respose.encoding) == respose.content)
print("text to content 2:", bytes(respose.text, encoding=respose.encoding) == respose.content)

# # 方法1,根据编码进行转换
resp1 = respose.content.decode(respose.apparent_encoding)
# print(respose.text)
#
# # 方法2,设置页面的编码
respose.encoding = respose.apparent_encoding
resp2 = respose.text
#
print("resp1 and resp2:", resp1 == resp2)
print("++++++++++++++++++++++++++++++++++")
# print("resp:", resp1)

