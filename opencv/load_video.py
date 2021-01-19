import numpy as np
import cv2

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

print(w, h, fps)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    
    # key = cv2.waitKey(1)
    # if key == ord('q'):
    #     break
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()