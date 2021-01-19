import cv2

img = cv2.imread('bird_small.jpg')

img1 = cv2.blur(img, (50, 50))
img2 = cv2.blur(img, (20, 20))
img3 = cv2.blur(img, (5, 5))

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()