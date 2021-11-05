import cv2
img1 = cv2.imread('a.tif')
img2 = cv2.imread('b.tif' )

imge = img2 - img1 

cv2.imwrite('Scrt.jpg' , imge)
cv2.imshow('Scrt',imge)
cv2.waitKey()
