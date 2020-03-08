# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 10:30:53 2018

@author: Administrator
"""

#测试集

import os
import pickle
import face_recognition as fr


#1:load test set
test_dir = 'images_test'
# load knn model
model_path = 'trained_knn_model.clf'
for image_file in os.listdir(test_dir):
    full_file_path = os.path.join(test_dir,image_file)          #os.path.join(path1[,path2[,......]]),将多个路径组合后返回
    print('--->Looking for faces in {}'.format(image_file))
    #2:load knn model
    with open(model_path,'rb') as f:
        knn_clf = pickle.load(f)            #将knn训练模型序列化读出
    #3:load waited image
    test_image = fr.load_image_file(full_file_path)
    face_box = fr.face_locations(test_image)
    #4:econding face
    test_ecod = fr.face_encodings(test_image,face_box)
    #5:use khn
    print('------>There are{}'.format(knn_clf.predict(test_ecod)))