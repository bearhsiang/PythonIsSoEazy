import cv2

def detect(img, detector, resize=True, new_w=600):
    if resize:
        img = cv2.resize(img, (new_w, int(img.shape[0]*new_w/img.shape[1])))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objs = detector.detectMultiScale(gray)
    return img, objs

    
def draw(img, l):
    for (x,y,w,h) in l:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return img

def between(face, smile):
    if smile[0] > face[0] and smile[0] < face[0]+face[2]:
        if smile[1] > face[1] and smile[1] < face[1]+face[3]:
            return True
    return False

def filtering(faces, smiles):

    new_smiles = []
    for smile in smiles:
        for face in faces:
            if between(face, smile):
                new_smiles.append(smile)
                break
    return new_smiles
    

face_file = 'haarcascade_frontalface_default.xml'
smile_file = 'haarcascade_smile.xml'
face_cascade = cv2.CascadeClassifier(face_file)
smile_cascade = cv2.CascadeClassifier(smile_file)

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    img, faces = detect(img, face_cascade)
    img, smiles = detect(img, smile_cascade, resize=False)
    smiles = filtering(faces, smiles)
    img = draw(img, faces)
    img = draw(img, smiles)

    cv2.imshow('img',img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()