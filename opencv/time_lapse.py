import numpy as np
import cv2

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

count = 0
N = 10

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    if count % N == N - 1:
        out.write(frame)
    
    count += 1

cap.release()
out.release()
cv2.destroyAllWindows()