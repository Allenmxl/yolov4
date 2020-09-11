import numpy as np
import cv2

img = np.zeros((512,512,3))
img[:, :, 0] = np.zeros([512,512]) + 255
# img[:, :, 1] = np.ones([400, 400]) + 254
# img[:, :, 2] = np.ones([400, 400]) * 255
cv2.imshow("img",img)
cv2.waitKey()