import numpy as np
import cv2


cap = cv2.VideoCapture(0)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
# code = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('outpy.mp4', code, fps, (w, h))
code = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('outpy.avi', code, fps, (w, h))

while True:
   ret, frame = cap.read()
  
   if not ret:
       break

   out.write(frame)

   cv2.imshow('webcam', frame)
   k = cv2.waitKey(1)
   if k == ord('q'):
       break

cap.release()
out.release()
cv2.destroyAllWindows()


