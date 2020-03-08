import jieba
txt = open("三国演义.txt",'r',encoding='utf-8').read()
excludes = {"将军","却说","荆州","二人","不可",
            "不能","如此","商议","如何","主公",
            "军士","左右","军马","引兵","次日",
            "大喜","天下","东吴"}#通过结果，去掉排在前面但又不是人名的词
words = jieba.lcut(txt)#将文本进行分词并返回一个列表
counts = {}#利用字典数据类型对结果进行存储
for word in words:
    if len(word) ==1:
        continue
    elif word =="诸葛亮" or word == "孔明曰":#将jieba识别出来的“别名”进行统一
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) +1 #遍历，统计每个单词出现的次数
for word in excludes:
    del counts[word]
items = list(counts.items())#取出所有键值对并存入列表中
items.sort(key=lambda x:x[1],reverse=True)#按照词频由大到小的顺序排列
for i in range(8):
    word,count = items[i]
    print("{:<10}{:>5}".format(word,count))
