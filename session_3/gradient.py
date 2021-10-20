import math
from dataclasses import dataclass
import cv2 as cv
import numpy as np
from typing import List


@dataclass
class Rgb:
    red: int
    green: int
    blue: int


# černá barva je 0,0,0
# bílá barva je pak 255,255,255

def color_ramp(colors: List[Rgb], t: float) -> Rgb:
    color_count = len(colors)

    if color_count == 0:
        raise RuntimeError("No colors in ramp")

    if color_count == 1:
        return colors[0]

    if t <= 0.0:
        return colors[0]

    if t >= 1.0:
        return colors[-1]

    frac, integer = math.modf(t * (color_count - 1))
    local_t = frac
    color_index = int(integer)
    c1 = colors[color_index]
    c2 = colors[color_index + 1]
    result_color = Rgb(0, 0, 0)
    result_color.red = c1.red * (1 - local_t) + c2.red * local_t
    result_color.blue = c1.blue * (1 - local_t) + c2.blue * local_t
    result_color.green = c1.green * (1 - local_t) + c2.green * local_t
    return result_color


# // dvojite lomítko je integerovské dělení

def main():
    colors = [
        Rgb(255, 0, 0),
        Rgb(0, 255, 0),
        Rgb(0, 0, 255),
        Rgb(0, 0, 0),
        Rgb(255, 255, 255),
        Rgb(255, 255, 1)
    ]
    width = 1600
    height = 200
    blank_image = np.zeros(shape=[height, width, 3], dtype=np.uint8)

    for x in range(0, width):
        t = x / width
        current_color = color_ramp(colors, t)
        blank_image[0:height, x] = (current_color.blue, current_color.green, current_color.red)

    cv.imshow("color blending", blank_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
