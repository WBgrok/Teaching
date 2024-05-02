from  PIL import Image
# import matplotlib.pyplot as plt
# plt.rcParams['figure.figsize'] = [12, 8]

im = Image.open("Tim.jpg")
# im.show()
width = im.width
height = im.height

OFFSET = 5

out = Image.new("RGB", (width - OFFSET, height - OFFSET))
for x in range(width - OFFSET):
  for y in range(height - OFFSET):
    p1 = im.getpixel((x, y))
    p2 = im.getpixel((x + OFFSET, y))
    p3 = im.getpixel((x, y + OFFSET))
    out.putpixel((x, y), (p1[0], p2[1], p3[2]))

out.show()
