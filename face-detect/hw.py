import cv2

def detect(img, detector, resize=True, new_w=600):
    if resize:
        img = cv2.resize(img, (new_w, int(img.shape[0]*new_w/img.shape[1])))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray)
    return img, faces

    
def draw(img, l):
    for (x,y,w,h) in l:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return img

file = 'haarcascade_frontalface_default.xml'
# file = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(file)

cap = cv2.VideoCapture('video.mp4')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))


out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))


while True:
    ret, img = cap.read()
    if not ret:
        break
    img, faces = detect(img, face_cascade, resize = False)
    img = draw(img, faces)

    cv2.imshow('img',img)
    out.write(img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    
out.release()
cap.release()
cv2.destroyAllWindows()