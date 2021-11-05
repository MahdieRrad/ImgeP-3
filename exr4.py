import cv2
import numpy as np


images = []
for i in range(1,20):
    img=cv2.imread(f'hightway/h{i}.jpg', 0)
    images.append(img)
    Rows,Cols=img.shape

Image=np.zeros((Rows,Cols) ,dtype ='uint8')

for image in images:
    Image+=image//20


cv2.imwrite('4Road.jpg', Image)
cv2.imshow('Road', Image)
cv2.waitKey()
