import cv2 as cv
import sys
import numpy as np

img = cv.imread(cv.samples.findFile("draven.jpg"))
img = cv.resize(img, (200, 200), None, None, None)


if img is None:
    sys.exit("Obrázek nebyl nalezen.")
cv.imshow("Displey window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("draven.jpg", img)