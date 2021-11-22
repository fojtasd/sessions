"""
Máme prostor A, který má souřadný systém X v <0, 1>, Y <0, 1>

A: X <0, 1>; Y <0, 1>
B: X <0, 800>; Y <0, 800> (X <0, width>; Y <0, height>)

z prostoru A chci převést dvě hodnoty (x, y) -> do prostoru B (x', y')
"""

from dataclasses import dataclass
from typing import Tuple
import cv2 as cv
import numpy as np
import math
from typing import List


@dataclass
class Range:
    min: float
    max: float


@dataclass
class RangeConverter:
    input_range: Range
    output_range: Range

    def convert(self, input_value: float) -> float:
        k = (self.output_range.min - self.output_range.max) / (self.input_range.min - self.input_range.max)
        q = -k * self.input_range.max + self.output_range.max
        result = k * input_value + q
        return result


@dataclass
class SpaceConverter:
    x_converter: RangeConverter
    y_converter: RangeConverter

    def convert(self, input_point: Tuple[float, float]) -> Tuple[float, float]:
        result_x = self.x_converter.convert(input_point[0])
        result_y = self.y_converter.convert(input_point[1])

        return result_x, result_y


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


def main():
    a_x = Range(-2, 4)
    a_y = Range(-2, 4)
    width = 800
    b_x = Range(0, width)
    height = 800
    b_y = Range(0, height)

    x_converter = RangeConverter(a_x, b_x)
    y_converter = RangeConverter(a_y, b_y)

    space_converter = SpaceConverter(x_converter, y_converter)

    blank_image = np.zeros(shape=[height, width, 3], dtype=np.uint8)

    colors = [
        Rgb(255, 0, 0),
        Rgb(0, 255, 0),
        Rgb(0, 0, 255),
    ]

    center = (1, 1)
    radius = 1

    # fi = f(x,y)
    # r = g(x,y)
    # ** je umocňování

    for y in np.arange(-2.0, 4.0, 0.005):
        for x in np.arange(-2.0, 4.0, 0.005):
            r = math.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
            fi = math.atan(y / x)
            t = fi / (math.pi / 2)
            b_coord = space_converter.convert((x, y))

            if radius > r:
                print(t)
                color = color_ramp(colors, t)
                blank_image[int(b_coord[1]), int(b_coord[0])] = [color.blue, color.green, color.red]

    cv.imshow("Transformations", blank_image)

    k = cv.waitKey(0)
    cv.destroyAllWindows()
    # zobrazit opencv okno s tím že vykreslíš obrázek 800x600 který je celý černý


if __name__ == "__main__":
    main()
