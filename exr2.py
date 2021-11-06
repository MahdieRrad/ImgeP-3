import cv2
import numpy as np

images = []

for i in range(1,10):
    Imge = np.zeros((500, 500), dtype='uint8')
    for j in range(1,5):
        image = cv.imread(f'black hole/{i}/{j}.jpg', 0)
        Imge += image//10
    images.append(Imge)

PicN = np.zeros((1000, 1000), dtype='uint8')
PicN[0:500, 0:500] = images[0]
PicN[0:500, 500:1000] = images[1]
PicN[500:1000, 0:500] = images[2]
PicN[500:1000, 500:1000] = images[3]

cv2.imwrite('2BlackHole.jpg', PicN)
cv2.imshow('BlackHole',PicN)
cv2.waitKey()
