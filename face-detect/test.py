import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	w = 400
	img = cv2.resize(img, (w, int(img.shape[0]*w/img.shape[1])))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imshow('img', gray)
	faces = face_cascade.detectMultiScale(gray)
	print(faces)

	for (x,y,w,h) in faces:
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		# roi_gray = gray[y:y+h, x:x+w]
		# roi_color = img[y:y+h, x:x+w]
		# eyes = eye_cascade.detectMultiScale(roi_gray)
		# for (ex,ey,ew,eh) in eyes:
		# 	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)
	k = cv2.waitKey(1)
	if k == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()