import cv2
import numpy as np
import matplotlib.pyplot as plt

# plt.ion()

def show_plt(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	plt.imshow(img)
	# plt.draw()
	plt.show()
	# plt.pause(0.00001)

img = cv2.imread('/Users/caixiangsheng/Desktop/IMG_5203.JPG')
print(img.shape)
# h, w, c = img.shape

# B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]
# blank = np.zeros((h, w), np.uint8)

# B = np.stack([B, blank, blank], axis = -1)
# G = np.stack([blank, G, blank], axis = -1)
# R = np.stack([blank, blank, R], axis = -1)

# cv2.imwrite('B.jpg', B)
# cv2.imwrite('G.jpg', G)
# cv2.imwrite('R.jpg', R)

# show_plt(B)

# cv2.imshow('B', B)
# cv2.imshow('G', G)
# cv2.imshow('R', R)

# cv2.waitKey(0)
# cv2.destroyAllWindows()