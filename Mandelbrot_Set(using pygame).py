import pygame as py
import numpy as np


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_n:
        z = z*z + c
        n += 1
    if n == max_n:
        return max_n
    return n + 1 - np.log(np.log2(abs(z)))


py.init()

width, height = 1000, 700
screen = py.display.set_mode((width, height))

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 240)

screen.fill(white)

max_n = 200

for i in range(width):
    for j in range(height):
        c = complex(-2 + (i / width) * 3, -1 + (j / height) * 2)
        m = mandelbrot(c)
        value = 255 - (m*255/max_n)
        py.draw.circle(screen, (value, value, value), (i, j), 1)


py.display.update()
py.image.save(screen, "Mandelbrot Set.jpg")


