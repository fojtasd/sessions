import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('coins.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY, )
ret, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("threshold", thresh)
cv.imshow("gray", gray)
cv.waitKey(0)
