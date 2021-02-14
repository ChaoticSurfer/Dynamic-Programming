"""
A set of utilities that are helpful for working with images. These are utilities
needed to actually apply the seam carving algorithm to images, but because they
aren't core the algorithm, they are implemented for you.

There is no need to change any code in this module.
"""


from PIL import Image


class Color:
    """
    A simple class representing an RGB value.
    """

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f'Color({self.r}, {self.g}, {self.b})'

    def __str__(self):
        return repr(self)


def read_image_into_array(filename):
    """
    Read the given image into a 2D array of pixels. The result is an array,
    where each element represents a row. Each row is an array, where each
    element is a color.

    See: Color
    """

    img = Image.open(filename, 'r')
    w, h = img.size

    pixels = list(Color(*pixel) for pixel in img.getdata())
    return [pixels[n:(n + w)] for n in range(0, w * h, w)]


def write_array_into_image(pixels, filename):
    """
    Write the given 2D array of pixels into an image with the given filename.
    The input pixels are represented as an array, where each element is a row.
    Each row is an array, where each element is a color.

    See: Color
    """

    h = len(pixels)
    w = len(pixels[0])

    img = Image.new('RGB', (w, h))

    output_pixels = img.load()
    for y, row in enumerate(pixels):
        for x, color in enumerate(row):
            output_pixels[x, y] = (color.r, color.g, color.b)

    img.save(filename)
