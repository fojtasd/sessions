import math
from dataclasses import dataclass
import cv2 as cv
import numpy as np
from typing import List
from typing import Tuple


@dataclass
class Rgb:
    red: int
    green: int
    blue: int


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


def window():
    width = 4500
    height = 3000
    #ratio 3:2
    a_x = Range(0, width)
    a_y = Range(0, height)
    b_x = Range(-2, 1)
    b_y = Range(-1, 1)
    x_converter = RangeConverter(a_x, b_x)
    y_converter = RangeConverter(a_y, b_y)
    space_converter = SpaceConverter(x_converter, y_converter)

    img = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    for x in range(0, width):
        for y in range(0, height):
            converted_coord = space_converter.convert((x, y))
            color = mandelbrot(converted_coord[0], converted_coord[1])
            img[y, x] = (color.blue, color.green, color.red)

    cv.imwrite("mandelbrot.png", img)
    cv.imshow("Window", img)
    cv.waitKey(0)


def mandelbrot(x: float, y: float):
    z = complex(0, 0)
    c = complex(x, y)
    max_iters = 100
    thresh = 4
    iter_counter = 0

    colors = [
        Rgb(255, 0, 0),
        Rgb(0, 255, 0),
        Rgb(0, 0, 255),
        Rgb(255, 0, 0),
        Rgb(0, 255, 0),
        Rgb(0, 0, 255),
        Rgb(255, 0, 0),
        Rgb(0, 255, 0),
        Rgb(0, 0, 255),
        Rgb(255, 0, 0),
        Rgb(0, 255, 0),
        Rgb(0, 0, 255),
    ]

    while True:
        z = z ** 2 + c
        if z.real ** 2 + z.imag ** 2 > thresh:
            t = iter_counter / max_iters
            return color_ramp(colors, t)
            # vyletěl jsem do nekonečna -> je uvnitř množiny
        if iter_counter > max_iters:
            return Rgb(0, 0, 0)
            # jsem nevyletěl do nekonečna (během max_iters) -> není uvnitř množiny
        iter_counter = iter_counter + 1

    # ukončovací podmínka pro iterování funkce bude: if (z.real ** 2 + z.imag ** 2) > thresh: break


def main():
    # X: <-2, 1>
    # Y: <-1, 1>

    window()


if __name__ == '__main__':
    main()
