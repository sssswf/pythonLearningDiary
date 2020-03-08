# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:00:06 2018

@author: ASUS
"""

from urllib import request,error

if __name__=='__main__':    
    url = "http://www.baidu.com"

    try:
        req = request.Request(url)
        req.add_header=(
            "User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
            )
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(len(html))
    except error.URLError as e:
        print(e)
    except error.URLError as e:
        print(e)
    