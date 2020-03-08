# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:34:55 2018

@author: Administrator
"""

import os
import os.path
import pickle
from PIL import Image,ImageDraw
import face_recognition as fr
  

li_names1=[]        #存储识别出的居民
li_names2=[]        #存储陌生人


#定义预测函数
def predict(X_img_path,knn_clf=None,model_path=None,distance_threshold=0.4):
    '''
    利用KNN分离器识别给定照片中的人脸
    ：return:[(人名1，边界盒子1),...]
    distance_threshold：设定阈值
    '''
    
    #保证KNN模型前提
    if knn_clf is None and model_path is None:
        raise Exception("必须提供分类器：可选方式为 knn_clf 或 model_path")
    if knn_clf is None:
        with open(model_path,'rb') as f:
            knn_clf = pickle.load(f)
            
    #加载图片
    X_img = fr.load_image_file(X_img_path)
    #得到人脸位置
    X_face_locations = fr.face_locations(X_img)
    #得到特征编码
    encodings = fr.face_encodings(X_img,known_face_locations=X_face_locations)
    #利用KNN model 找出与测试人脸最匹配的人脸
    #encoding :128个人脸特征构成的向量
    closest_distances = knn_clf.kneighbors(encodings,n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold
                   for i in range(len(X_face_locations))]
    #预言类别，返回语言结果和人脸位置
    return [(pred,loc) if rec else ("unknown people",loc)
            for pred,loc,rec in zip(knn_clf.predict(encodings),X_face_locations,are_matches)]


#定义人物识别结果信息显示函数
def show_names_on_image(img_path,predictions):
    '''
    人脸识别可视化
    ：param img_path:待识别图片的位置
    ：param predictions:预测的结果
    '''
    
    pil_image = Image.open(img_path).convert("RGB")
    draw = ImageDraw.Draw(pil_image)        #新建ImageDraw模块对象
    for name,(top,right,bottom,left) in predictions:
        #用Pillow模块画出人脸边界盒子
        draw.rectangle(((left,top),(right,bottom)),outline=(0,0,255))
        #pillow里可能生成非UTF-8格式，所以这里做如下转换
        
        #red,green,控制输出信息背景色,用来将不同的识别结果输出信息进行区别
        red=0
        green=0
        #根据识别结果显示不同的信息，用info存储输出信息
        if name =="unknown people":
            info=name+" ,No !"
            red=255       #陌生人信息红底显示
            li_names2.append(name)      #追加名字
        else:
            info = "resident " + name + ",Please Entry!"
            green=255       #居民信息绿底显示
            li_names1.append(name)      #追加名字
        info = info.encode("UTF-8")
        #info = info.encode("ascii")
        #在人脸上写下名字作为标签
        text_width,text_height = draw.textsize(info)
        #输出信息显示区
        #背景
        draw.rectangle(((left,top-text_height-5),(left+text_width,top)),fill=(red,green,0))
        #信息
        draw.text([left,top-text_height-5],info,fill=(255,255,255))
    #从内存删除draw
    del draw
    #显示结果图
    pil_image.show()
    

#定义门禁识别信息输出函数
def output():
    print("\n")
    j=1
    for i in li_names1:
        print("识别出居民{}:{}".format(j,i))
        j+=1
    print("已允许居民进入小区")
    print("识别出{}个陌生人，已禁止其进入小区".format(len(li_names2)))


if __name__ == "__main__":
    #利用训练好的数据，对新照片进行预测
    for image_file in os.listdir("images_door"):
        full_file_path = os.path.join("images_door",image_file)
        print("在{}中寻找人脸...".format(image_file))
        #利用分类器，找出所有人脸
        predictions = predict(full_file_path,model_path="trained_knn_model.clf")
        #打印预测结果
        for name,(top,right,bottom,left) in predictions:
            who=name
            if name =="unknown people":
                who="陌生人"
            print("发现{}".format(who))
        #在图片上显示预测结果
        show_names_on_image(os.path.join("images_door",image_file),predictions)
        
    output()
    
