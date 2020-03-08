# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 09:29:30 2018

@author: ASUS
"""
 #请求 URL: http://fanyi.baidu.com/sug
from urllib import request,parse
import json
baseurl = "http://fanyi.baidu.com/sug"
kw = input("please input words:")
data = {
         "kw" : kw
         }
data = parse.urlencode(data).encode("utf-8")

headers = {
         "Content-Length":len(data)
         }
req = request.Request(url=baseurl,data=data,headers=headers)
rsp = request.urlopen(req)
json_data = rsp.read().decode("utf-8")
print(type(json_data))
json_data = json.loads(json_data)
for item in json_data["data"]:
    print(item["k"],"--",item["v"])