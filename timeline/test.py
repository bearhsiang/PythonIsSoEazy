import cv2
import numpy as np

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

w, h = int(0.5*w), int(0.5*h)

canvas = np.zeros((h, w, 3), dtype=np.uint8)
head = 0
while True:

    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (w, h))
    
    canvas[head, :, :] = frame[head, :, :]
    frame = cv2.line(frame, (0, head), (w, head), (255, 200, 200), 3) 

    cv2.imshow('cap', frame)
    cv2.imshow('canvas', canvas)

    k = cv2.waitKey(1)
    head += 1
    if head >= h:
        break

cv2.imwrite('output.jpg', canvas)

cap.release()
cv2.destroyAllWindows()
