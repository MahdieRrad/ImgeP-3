import cv2

img1 = cv2.imread('board - origin.bmp',0)
img2 = cv2.imread('board - test.bmp',0)
img2 = cv2.flip(img2,1)

img = cv2.subtract(img2,img1)


cv2.imwrite('Board',img)
cv2.imshow('Board',img)
cv2.waitKey()
