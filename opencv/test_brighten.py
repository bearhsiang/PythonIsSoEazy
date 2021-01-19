import cv2
import numpy as np

img = cv2.imread('bird_small.jpg')

mask = img <= 205
img[mask] = img[mask] + 50
img[~mask] = 255
cv2.imshow('before', img)
# # k = 50
# # mask = img <= 255-k
# # print(mask.shape)
# # img[mask] += k
# # img[~mask] = 255
# img += 50

# cv2.imshow('after', img)
cv2.waitKey(0)
cv2.destroyAllWindows()