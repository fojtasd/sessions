import cv2 as cv
import sys
import numpy as np

# img = cv.imread(cv.samples.findFile("draven.jpg"))
# img = cv.resize(img, (200, 200), None, None, None)

# black blank image

# white blank image
#blank_image2 = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
blank_image2 = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
blank_image2[0:100, 0:200] = (0, 0, 224)

cv.imshow("Displey window", blank_image2)
x = 0
y = 0
while True:
    blank_image2 = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    blank_image2[y: y + 20, x: x + 20] = (0, 0, 224)
    x = x + 1
    y = y + 1
    cv.imshow("Displey window", blank_image2)
    c = cv.waitKey(30) & 0xff
    if y > blank_image2.shape[0] or x > blank_image2.shape[1]:
        break
    if chr(c) == 'q':
        break

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("draven.jpg", blank_image2)
cv.destroyAllWindows()
