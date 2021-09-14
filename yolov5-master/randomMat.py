import random
import numpy as np
from PIL import Image as im
import cv2

def makeR():
    return random.randrange(0,256)
    
width = 480
height = 640
npArr = np.zeros((width,height,3))
for i in range(480):
    for j in range(640):
        for k in range(3):
            npArr[i][j][k] = makeR()   
                 
#print(npArr)
cv2.imwrite("noise.png", npArr)