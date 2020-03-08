# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 08:48:31 2018

@author: Administrator
"""

#训练集

import os
import face_recognition as fr
from face_recognition.face_recognition_cli import image_files_in_folder
from sklearn import neighbors
import pickle

train_dir = 'images_practise'#'examples/train'
model_save_path =  'trained_knn_model.clf'
train_set = []
train_label = []
print("--->Traing ...")


#加载数据集，转换为openface的特征编码形式
#os.chdir(train_dir)
for class_id in os.listdir(train_dir):
    #whether a path is a directory
    if not os.path.isdir(os.path.join(train_dir,class_id)):
        continue
    #os.path.isdir(path),如果path是一个存在的目录，则返回True。否则返回False。
    # if the path is not a directory,then End the current loop and move on to the next
    # print(os.path.join(train_dir,class_id))
    for img_path in image_files_in_folder(os.path.join(train_dir,class_id)):
        image = fr.load_image_file(img_path)
        face_box = fr.face_locations(image)
        face_code = fr.face_encodings(image,known_face_locations = face_box)[0]
        #存储图片openface特征编码
        train_set.append(face_code)
        #给当前编码打上一个标签
        train_label.append(class_id)

#如果报错list index out of range，是因为有未识别到人脸的图片

#把特征编码和标签加入对应的列表中
knn_classify = neighbors.KNeighborsClassifier(n_neighbors=3)
knn_classify.fit(train_set,train_label)


#训练KNN
if model_save_path is not None:
    with open(model_save_path,'wb') as f:
        pickle.dump(knn_classify,f)
        
print('--->Training complerion')

#保存KNN模型文件

