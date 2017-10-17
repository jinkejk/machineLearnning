from __future__ import print_function

from PIL import Image, ImageFilter

im = Image.open('../data/timg.jpeg')
print(im.format, im.size, im.mode)
im2 = im.filter(ImageFilter.BLUR)
im.show()
im2.show()
