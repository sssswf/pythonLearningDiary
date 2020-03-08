izhi# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 08:11:54 2018

@author: ASUS
"""

from urllib import request,error
if __name__=="__main__":
    url = "http://www.baidu.com"
    #设置代理地址
    proxy = {"http": "121.43.170.207:3128"}
    #创建proxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    #创建opener
    opener = request.build_opener(proxy_handler)
    #安装opener
    request.install_opener(opener)
    
    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(len(html))
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)