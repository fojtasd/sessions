import cv2 as cv
import sys
import numpy as np
from dataclasses import dataclass


@dataclass
class Rgb:
    red: int
    green: int
    blue: int


def main():
    color_changer(Rgb(0, 0, 153), Rgb(255, 255, 255))

def color_changer(current_color: Rgb, demanded_color: Rgb):
    blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    blank_image[:] = (current_color.blue, current_color.green, current_color.red)
    while current_color != demanded_color:
        cv.imshow("Colors", blank_image)
        if current_color.blue != demanded_color.blue:
            current_color.blue = current_color.blue + 1
        if current_color.blue > 255:
            current_color.blue = 0
        if current_color.green != demanded_color.green:
            current_color.green = current_color.green + 1
        if current_color.green > 255:
            current_color.green = 0
        if current_color.red != demanded_color.red:
            current_color.red = current_color.red + 1
        if current_color.red > 255:
            current_color.red = 0
        blank_image[:] = (current_color.blue, current_color.green, current_color.red)
        cv.waitKey(1)
        cv.imshow("Colors", blank_image)
    cv.imshow("Colors", blank_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
