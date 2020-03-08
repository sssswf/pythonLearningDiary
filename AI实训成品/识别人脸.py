# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 14:44:14 2018

@author: Administrator
"""


#识别人脸


import os
from skimage import io
import dlib

#用image遍历所有图片
path="images_recognition"
imagelist=os.listdir(path)
print(imagelist)

#image = io.imread(image_file)

for j in imagelist:
    image = io.imread(os.path.join(path,j))
    detector = dlib.get_frontal_face_detector()
    
    detected_face = detector(image,1)
    print('--->Find{}faces on the{}'.format(len(detected_face),os.path.join(path,j)))

    model = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(model)

    win = dlib.image_window()
    win.set_image(image)
    win.set_title('FaceDetect')

    for i,box in enumerate(detected_face):
        win.add_overlay(box)
        print('第{}张人脸的位置:{},右边位置:{}.'.format(i,box.left(),box.right()))
        landmarks = predictor(image,box)
        win.add_overlay(landmarks)
        dlib.hit_enter_to_continue()
        



