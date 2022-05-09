#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = demo01.py
@author =  Hj
@datetime = 2022/5/4
"""
import requests
url="https://www.ip138.com/"
# url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip&oq=ip&rsv_pq=f324eeae0034d5b3&rsv_t=1614Ig0%2FSFdqQsQDSJArr7w7H2xMK5HfvMfKf%2B9lr2VQKJqf27ubkbGJ4j0&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t"
headers={
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}

ip = "218.1.200.211:57114"
proxies = {
    'http': 'http://{}'.format(ip),
    'https': 'https://{}'.format(ip),
}

respose=requests.get(url=url, headers=headers,proxies=proxies)
respose.encoding = respose.apparent_encoding
text2 = respose.text

with open('aa.html', 'w', encoding=respose.apparent_encoding) as fp:
   fp.write(text2)


