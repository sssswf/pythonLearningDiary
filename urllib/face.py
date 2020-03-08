# -*- coding:utf-8 -*-
# OpenCV版本的视频检测
import cv2


# 图片识别方法封装
def discern(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cap = cv2.CascadeClassifier("F:/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier('F:/anaconda/Lib/site-packages/cv2/data/haarcascade_lefteye_2splits.xml')
    mouth_cascade = cv2.CascadeClassifier('F:/anaconda/Lib/site-packages/cv2/data/haarcascade_smile.xml')
    faceRects = cap.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=3, minSize=(50, 50))
    eyeRects = eye_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=2, minSize=(10, 10))
    mouthRects = mouth_cascade.detectMultiScale(
        gray, scaleFactor=1.16, minNeighbors=35, minSize=(20, 20))
    if len(faceRects):
        for faceRect in faceRects:
            x, y, w, h = faceRect
            cv2.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 2)  # 框出人脸
    if len(eyeRects):
        for eyeRect in eyeRects:
            x1, y1, w1, h2 = eyeRect
            cv2.rectangle(img, (int(x1), int(y1)), (int(x1) + int(w1), int(y1) + int(h2)), (0, 255, 0), 2, 0)
            # 画出眼睛区域
    if len(mouthRects):
        for mouthRect in mouthRects:
            xm1, ym1, wm1, hm2 = mouthRect
            cv2.rectangle(img, (int(xm1), int(ym1)), (int(xm1) + int(wm1), int(ym1) + int(hm2)),
                          (0, 0, 255), 2, 0)
            # 画出嘴巴区域
    cv2.imshow("Image", img)


# 获取摄像头0表示第一个摄像头
cap = cv2.VideoCapture(0)
while (1):  # 逐帧显示
    ret, img = cap.read()
    # cv2.imshow("Image", img)
    discern(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 释放摄像头
cv2.destroyAllWindows()  # 释放窗口资源
