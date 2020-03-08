import cv2
def detect():
    face_cascade = cv2.CascadeClassifier('F:/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face_cascade.load('F:/anaconda/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    eye_cascade	= cv2.CascadeClassifier('F:/anaconda/Lib/site-packages/cv2/data/haarcascade_eye.xml')
    eye_cascade.load('F:/anaconda/Lib/site-packages/cv2/data/haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    while (True):
        frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h,x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 3, 0, (20, 20))
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
        camera.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
	detect()
