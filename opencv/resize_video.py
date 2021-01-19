import numpy as np
import cv2


cap = cv2.VideoCapture('sample.mp4')

fps = int(cap.get(cv2.CAP_PROP_FPS))

code = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('outpy.avi', code, fps, (500, 500))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    resized = cv2.resize(frame, (500, 500))

    cv2.imshow('resized', resized)
    out.write(resized)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()