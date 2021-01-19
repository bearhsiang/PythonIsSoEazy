import cv2
import numpy as np

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

w, h = int(0.5*w), int(0.5*h)

canvas = np.zeros((h, w, 3), dtype=np.uint8)
start = False
head = 0

while True:

    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (w, h))
    frame = cv2.flip(frame, 1)
    
    canvas[head, :, :] = frame[head, :, :]
    display = np.copy(frame)
    display[:head] = canvas[:head]
    display = cv2.line(display, (0, head), (w, head), (255, 200, 200), 3) 

    cv2.imshow('cap', frame)
    cv2.imshow('canvas', canvas)
    cv2.imshow('display', display)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    if start:
        head += 1
    if k == ord('b'):
        start = True
    if k == ord('p'):
        start = not start
    if head >= h:
        start = False

cv2.imwrite('output.jpg', canvas)

cap.release()
cv2.destroyAllWindows()