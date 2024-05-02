from  PIL import Image
# import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = [12, 8]

im = Image.open("Tim.jpg")
# im.show()
width = im.width
height = im.height

OFFSET = 2

# out = Image.new("RGB", (width - OFFSET, height - OFFSET))
# for x in range(width - OFFSET):
#   for y in range(height - OFFSET):
#     p1 = im.getpixel(((width - OFFSET -1) - x, y))
#     p2 = im.getpixel((x + OFFSET, y))
#     p3 = im.getpixel((x, y + OFFSET))
#     out.putpixel((x, y), (p1[0], p2[1], p3[2]))

# out = Image.new("RGB", (width, height))
# for x in range(width):
#   for y in range(height):
#     c = x // 100
#     p1 = im.getpixel((((100 * c) + (100 - (x % 100)) ) % width, y))
#     p2 = im.getpixel((x, y))
#     p3 = im.getpixel((x, y))
#     out.putpixel((x, y), (p1[0], p2[1], p3[2]))


# out = Image.new("RGB", (width, height))
# for x in range(width):
#   for y in range(height):
#     c = x // 50
#     p2 = im.getpixel((((50 * c) + (50 - (x % 50)) ) % width, y))
#     p1 = im.getpixel((x, y))
#     p3 = im.getpixel((x, y))
#     out.putpixel((x, y), (p1[0], p2[1], p3[2]))

# out = Image.new("RGB", (width, height))
# for x in range(width):
#   for y in range(height):
#     c = x // 50
#     p2 = im.getpixel((((50 * c) + (50 - (x % 50)) ) % width, y))
#     p1 = im.getpixel((x, y))
#     p3 = im.getpixel((x, y))
#     out.putpixel((x, y), (p1[0], p2[1], p3[2]))


OFFSET = 100
out = Image.new("RGB", (width, height ))
for x in range(width ):
  for y in range(height):
    p1 = im.getpixel((x , y))
    p2 = im.getpixel(((x + OFFSET) % width, y))
    p3 = im.getpixel((x, (y + OFFSET) % height ))
    out.putpixel((x, y), (p1[0], p2[1], p3[2]))


out.show()
