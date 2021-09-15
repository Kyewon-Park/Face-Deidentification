

# 이미지 불러오기 400 400

# 노이즈 이미지 만들기

# 위치 [100 100 100 100]

import cv2
import numpy as np

img1 = cv2.imread('D:\\Face-Deidentification\\yolov5-master\\dog.jpg')
noise = cv2.imread('D:\\Face-Deidentification\\yolov5-master\\noise.png')
noise_cut = noise[0:177,0:284]
cv2.imshow("img1",img1)
added = cv2.addWeighted(img1, 0.3, noise_cut, 0.7, 0.0)

noise_part = added[50:127,60:140] #합성 이미지 받아서 노이즈 잘라냄=noise_part
img1[50:127,60:140]=noise_part
cv2.imshow("after",img1)

cv2.waitKey(0)


