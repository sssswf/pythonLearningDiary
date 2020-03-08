def getText():
    txt = open("hamlet.txt",'r').read()
    txt = txt.lower()#将文本全部转换为小写形式
    for ch in '!@#$%^&*()_+-,./<>=?[\\]"{|}~':
        txt = txt.replace(ch,'')#将所有的符号全部替换成为空格
    return txt
hamletTxt = getText()
words = hamletTxt.split()
counts = {}#利用字典数据类型对结果进行存储
for word in words:
    counts[word] = counts.get(word,0) +1 #遍历，统计每个单词出现的次数
items = list(counts.items())#取出所有键值对并存入列表中
items.sort(key=lambda x:x[1],reverse=True)#按照词频由大到小的顺序排列
for i in range(10):
    word,count = items[i]
    print("{:<10}{:>5}".format(word,count))
