from dataclasses import dataclass
import cv2 as cv
import numpy as np


@dataclass
class Rgb:
    red: int
    green: int
    blue: int


# černá barva je 0,0,0
# bílá barva je pak 255,255,255

def color_blend(c1: Rgb, c2: Rgb, t: float) -> Rgb:
    # y = a(1 - t) + bt
    y = Rgb(0, 0, 0)
    y.red = c1.red * (1 - t) + c2.red * t
    y.blue = c1.blue * (1 - t) + c2.blue * t
    y.green = c1.green * (1 - t) + c2.green * t
    return y


# // dvojite lomítko je integerovské dělení

def main():
    color1 = Rgb(255, 153, 255)  # homobarva žůžová
    color2 = Rgb(0, 0, 204)  # tmavě modrá
    blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
    fps = 60
    color_blending_time = 5
    t = 0
    dt = 1 / (fps * color_blending_time)
    while t <= 1:
        current_color = color_blend(color1, color2, t)
        t = t + dt
        blank_image[:] = (current_color.blue, current_color.green, current_color.red)
        cv.imshow("color blending", blank_image)
        k = cv.waitKey(1000 // fps)
        if k == ord("q"):
            break
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
