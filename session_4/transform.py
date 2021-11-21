"""
Máme prostor A, který má souřadný systém X v <-1, 1>, Y <-2, 4>
a tenhle prostor A chceme jeho obraz převést do prostoru B, který bude reprezentovat matici zobrazovanou na
display, tudíž bude např. 800x600 pixelů.

Do prostoru A budeme kreslit kružnici pomocí matematiky!

A: X <-1, 1>; Y <-2, 4>
B: X <0, 800>; Y <0, 600> (X <0, width>; Y <0, height>)

z prostoru A chci převést dvě hodnoty (x, y) -> do prostoru B (x', y')
"""

from dataclasses import dataclass
from typing import Tuple
import cv2 as cv
import numpy as np
import math


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

    # print(result)  # 800, 600
    blank_image = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    # blank_image[height//2, width//2] = [255, 255, 255]  # y, x
    # celočíslené dělení v pythonu //

    # teď chci abys vzal střed z prostoru A, vypočítal si souřadnice v prostoru B a do toho místa
    # nakreslil bílou tečku
    a_coord = (1, 1)
    b_coord = space_converter.convert(a_coord)

    # tady je třeba použít b_coord...

    blank_image[int(b_coord[1]), int(b_coord[0])] = [255, 255, 255]

    center = (1, 1)
    r = 1

    for fi in np.arange(0, 2 * math.pi, math.pi / 1500):
        x = center[0] + r * math.cos(fi)
        y = center[1] + r * math.sin(fi)
        b_coord = space_converter.convert((x, y))
        blank_image[int(b_coord[1]), int(b_coord[0])] = [255, 255, 255]

    cv.imshow("Transformations", blank_image)

    k = cv.waitKey(0)
    cv.destroyAllWindows()
    # zobrazit opencv okno s tím že vykreslíš obrázek 800x600 který je celý černý


if __name__ == "__main__":
    main()
