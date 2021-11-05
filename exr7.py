import cv2
import random


img=cv2.imread('add.jpg' , 0)
height ,width =img.shape

for i in range(height):
    for j in range(width):
        r = random.random()
        if r < 0.075:
            img[i][j] = 0
        elif r > 1:
            img[i][j] = 255
        else:
            img[i][j] = img[i][j]
   

cv2.imwrite('7AddNoice.jpg' , img)
cv2.imshow('Noise' , img)
cv2.waitKey()
