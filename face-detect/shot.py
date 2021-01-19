import cv2

cap = cv2.VideoCapture('sample.mp4')

while True:
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.resize(img, (500, 500))
    cv2.imshow('img',img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('s'):
        cv2.imwrite('shot.jpg', img)
        cv2.imshow('shot', img)

cap.release()
cv2.destroyAllWindows()