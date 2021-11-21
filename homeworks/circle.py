# matematický prostor, kde X je omezeno v intervalu <-2, 2>,
# Y je omezeno v intervalu <-1, 1>, v tomto prostoru nakresli kružnici se středem uprostřed
# a tento celý prostor pak vykresli na plátno o velikost 1024x768
# jedná se hlavně o to mít funkci, do které zadám souřadnici X,Y z matematického
# prostoru (X leží v <-2, 2>, Y leží v <-1, 1>) a tato funkce bude kreslit do matice (obrázku) 1024x768
import cv2 as cv
import numpy as np
from dataclasses import dataclass


@dataclass
class Space:
    x: float
    y: float

    def __init__(self):
        x = 0
        y = 0


def draw_circle():
    width = 512
    height = 512
    blank_image = np.zeros(shape=[width, height, 3], dtype=np.uint8)
    blank_image[:] = (255, 255, 255)
    color = (0, 0, 0)
    center_coordinates = (int(width / 2), int(height / 2))
    radius = 30
    thickness = -1
    image = cv.circle(blank_image, center_coordinates, radius, color, thickness)
    cv.imshow("window", image)
    cv.waitKey(0)


def create_space():
    width = 512
    height = 512
    blank_image = np.zeros(shape=[width, height, 3], dtype=np.uint8)


def main():
    draw_circle()


if __name__ == '__main__':
    main()
