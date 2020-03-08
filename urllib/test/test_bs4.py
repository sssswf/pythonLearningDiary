# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 08:54:11 2018

@author: ASUS
"""
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc,"html.parser")
links = soup.find_all("a")
print("获取所有a链接")
for link in links:
    print(link.name,link["href"],link.get_text())

link1 = soup.find("a",href="http://example.com/elsie")
print("打印第一个链接")
print(link1.name,link1["href"],link1.get_text())

print("打印p节点")
p_node = soup.find("p",class_="title")
print(p_node.name,p_node.get_text())