import cv2
import numpy as np
import math

from typing import Generator, List
from dataclasses import astuple, dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Range:
    min: float
    max: float

    def make_steps(self, steps: int) -> Generator[float, None, None]:
        step_jump = (self.max - self.min) / steps
        return np.arange(self.min, self.max, step_jump)

    def map_value(self, to_range: "Range", value: float) -> float:
        return to_range.min + (to_range.max - to_range.min) / (self.max - self.min) * (value - self.min)


@dataclass
class Color:
    blue: int
    green: int
    red: int


@dataclass
class ColorRamp:
    colors: List[Color]

    def ramp(self, t: float) -> Color:
        color_count = len(self.colors)

        if color_count == 0:
            raise RuntimeError("No colors in ramp")

        if color_count == 1:
            return self.colors[0]

        if t <= 0.0:
            return self.colors[0]

        if t >= 1.0:
            return self.colors[-1]

        frac, integer = math.modf(t * (color_count - 1))
        local_t = frac
        color_index = int(integer)

        c1 = self.colors[color_index]
        c2 = self.colors[color_index + 1]

        red = c1.red * (1 - local_t) + c2.red * local_t
        green = c1.green * (1 - local_t) + c2.green * local_t
        blue = c1.blue * (1 - local_t) + c2.blue * local_t

        return Color(blue, green, red)


class FractalDrawer:
    def __init__(self) -> None:
        cv2.namedWindow("image")
        cv2.startWindowThread()

        self.width = 900 * 2
        self.height = 600 * 2
        self.channels = 3  # BGR

        self.dimensions = (self.height, self.width, self.channels)
        self.image = np.zeros(self.dimensions, dtype=np.uint8)

        self.image_x_range = Range(0, self.width)
        self.image_y_range = Range(0, self.height)

        self.x_range = Range(-2.0, 1.0)
        self.y_range = Range(-1.0, 1.0)

    def fractal_point_to_image_point(self, fractal_point: Point) -> Point:
        x = self.x_range.map_value(
            self.image_x_range,
            fractal_point.x
        )

        y = self.y_range.map_value(
            self.image_y_range,
            fractal_point.y
        )

        return Point(int(x), int(y))

    def draw(self):
        thresh = 4.0
        iter_limit = 50
        default_z_0 = 0.0 + 0.0j

        color_ramp = ColorRamp([
            Color(255, 253, 158),
            Color(72, 13, 222),
            Color(255, 46, 161),
            Color(3, 186, 252),
            Color(3, 252, 198),
            Color(72, 13, 222),
        ])

        for y in self.y_range.make_steps(self.height):
            for x in self.x_range.make_steps(self.width):

                pixel = self.fractal_point_to_image_point(Point(x, y))
                c = complex(x, y)
                z = default_z_0

                for i in range(iter_limit):
                    z = z ** 2 + c
                    if (z.real ** 2 + z.imag ** 2) > thresh:
                        break

                point_is_not_in = i == iter_limit - 1

                if point_is_not_in:
                    self.image[pixel.y, pixel.x] = (0, 0, 0)
                else:
                    color = color_ramp.ramp(i / iter_limit)
                    self.image[pixel.y, pixel.x] = astuple(color)

            cv2.imshow("image", self.image)

            key_code = cv2.waitKey(1)
            if key_code == ord("q"):
                break

        print("Done!")
        cv2.waitKey()


def main() -> None:
    drawer = FractalDrawer()
    drawer.draw()


if __name__ == "__main__":
    main()
