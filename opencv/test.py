import cv2

img = cv2.imread('bird.jpg')

h, w, c = img.shape
r = 0.2

new_h = int(h * r)
new_w = int(w * r)

new_img = cv2.resize(img, (new_w, new_h))

print(img.shape)
print(new_img.shape)

cv2.imshow('origin', img)
cv2.imshow('resize', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('bird_small.jpg', new_img)