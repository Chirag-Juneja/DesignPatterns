# A construct which adapts an existing interface X to
# conform to the required interface Y

import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


class Rectangle:
    def __init__(self, x, y, w, h) -> None:
        self.xywh = [x, y, w, h]


class RectangleAdapter:
    @staticmethod
    def xywh2xxyy(rect):
        x, y, w, h = rect.xywh
        return [x, y, x+w, y+h]


img = np.zeros((100, 100, 3))

rects = [
    Rectangle(1, 1, 10, 10),
    Rectangle(50, 50, 25, 25),
    Rectangle(25, 25, 20, 20),
]


def draw(rect):
    x, y, x2, y2 = RectangleAdapter.xywh2xxyy(rect)
    cv.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 1)


for rect in rects:
    draw(rect)

plt.imshow(img)
plt.show()
