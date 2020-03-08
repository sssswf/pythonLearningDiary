import jieba
import wordcloud
from scipy.misc import imread
mk = imread("five.jpg")#词云生成特定形状，此处为五角星
txt = open("s.txt","r",encoding="utf-8")#打开文本
ls = txt.read()#读取文本
txt.close()
lsList = jieba.lcut(ls)#对文本进行分词并返回一个列表
lstxt = " ".join(lsList)#将列表转换成元素之间空格间隔的文本
w = wordcloud.WordCloud(width=1000,height=700,background_color='white',max_words=40, font_path="msyh.ttc",mask=mk)
w.generate(lstxt)
w.to_file("file.jpg")
