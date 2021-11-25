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


def window():
    width = 900
    height = 600

    a_x = Range(0, width)
    a_y = Range(0, height)
    b_x = Range(-2, 1)
    b_y = Range(-1, 1)
    x_converter = RangeConverter(a_x, b_x)
    y_converter = RangeConverter(a_y, b_y)
    space_converter = SpaceConverter(x_converter, y_converter)

    blank_image = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    for x in range(0, width):
        for y in range(0, height):
            converted_coord = space_converter.convert((x, y))
            color = mandelbrot(converted_coord[0], converted_coord[1])
            blank_image[y, x] = (color.blue, color.green, color.red)

    cv.imshow("Window", blank_image)
    cv.waitKey(0)


def mandelbrot(x: float, y: float):
    z = complex(0, 0)
    c = complex(x, y)
    max_iters = 100
    thresh = 4
    iter_counter = 0

    while True:
        z = z ** 2 + c
        if z.real ** 2 + z.imag ** 2 > thresh:
            return Rgb(255, 0, 0)
            # vyletěl jsem do nekonečna -> je uvnitř množiny
        if iter_counter > max_iters:
            return Rgb(255, 255, 255)
            # jsem nevyletěl do nekonečna (během max_iters) -> není uvnitř množiny
        iter_counter = iter_counter + 1

    # ukončovací podmínka pro iterování funkce bude: if (z.real ** 2 + z.imag ** 2) > thresh: break


def main():
    mandelbrot(-1, 0.8)

    # X: <-2, 1>
    # Y: <-1, 1>

    window()


if __name__ == '__main__':
    main()
