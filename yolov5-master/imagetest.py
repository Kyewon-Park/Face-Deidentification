

# 이미지 불러오기 400 400

# 노이즈 이미지 만들기

# 위치 [100 100 100 100]

import cv2
import random
import numpy as np

img1 = cv2.imread('dog.jpg')
noise = cv2.imread('noise.png')
img2 = noise[0:177,0:284]
cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

added = cv2.addWeighted(img1, 0.2, img2, 0.8, 0.0)
added2 = cv2.addWeighted(img1, 0.1, img2, 0.9, 0.0)
cv2.imshow("added2",added2)


cv2.waitKey(0)


