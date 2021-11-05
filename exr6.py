import cv2

img = cv2.imread('Mona_Lisa.jpg',0)
img = cv2.resize(img,(400,400))

inverted=255-img
pic=cv2.GaussianBlur(inverted,(21,21),0)
pic_B=255-pic

paint=img/pic_B
paint=paint*255

cv2.imwrite('Paint.jpg',paint)
cv2.imshow('Paint',paint)
cv2.waitKey()
