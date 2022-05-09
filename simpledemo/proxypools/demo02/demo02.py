#!/usr/bin/python3
# encoding: utf-8

"""
@project = simpledemo
@file_name = demo01.py
@author =  Hj
@datetime = 2022/5/4
"""
import requests
url="https://www.baidu.com"
# url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&fenlei=256&rsv_pq=ed0391db00041b66&rsv_t=3434I1Q%2FRSn7RzmhcFrZpgpjy28tpL23S4GyRTPWuBqqDngiRAuibP24A62Q&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=3&rsv_sug1=3&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=ip&rsp=5&inputT=1221&rsv_sug4=2021"
headers={
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}

text2 = requests.get(url=url, headers=headers).text
print(text2)
with open('aa.html', 'w', encoding='GB2312') as fp:
   fp.write(text2)


