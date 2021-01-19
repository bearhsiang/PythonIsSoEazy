import cv2

def detect(img, detector, resize=True, new_w=600):
	if resize:
		img = cv2.resize(img, (new_w, int(img.shape[0]*new_w/img.shape[1])))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray, minSize=(50, 50), maxSize=(100, 100))
	return img, faces

	
def draw(img, l):
	for (x,y,w,h) in l:
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	return img

# file = 'haarcascade_frontalface_default.xml'
file = 'haarcascade_smile.xml'
face_cascade = cv2.CascadeClassifier(file)

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()

	img, faces = detect(img, face_cascade)
	img = draw(img, faces)

	cv2.imshow('img',img)

	k = cv2.waitKey(1)
	if k == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()