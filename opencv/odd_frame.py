import numpy as np
import cv2

cap = cv2.VideoCapture('sample.mp4')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

print(w, h, fps)
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), fps/10, (w, h))
# out = cv2.VideoWriter('outpy.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))


# In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
# In Windows: DIVX (More to be tested and added)
# In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv)

count = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = np.stack((gray, )*3, axis=-1)
    # # gray = frame.copy()
    # out.write(gray)
    # cv2.imshow('frame',gray)
    if count % 10 == 0:
        out.write(frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    count += 1

cap.release()
out.release()
out = None
cv2.destroyAllWindows()