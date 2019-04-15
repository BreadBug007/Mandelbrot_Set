from PIL import Image, ImageDraw
import numpy as np


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))


width, height = 1000, 700
im = Image.new('HSV', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(im)

max_iter = 1000

for x in range(width):
    for y in range(height):
        c = complex(-2 + (x / width) * 3, -1 + (y / height) * 2)
        m = mandelbrot(c)
        hue = int(255 * m / max_iter)
        saturation = 255
        value = 255 if m < max_iter else 0
        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('Mandelbrot Set.png', 'PNG')

