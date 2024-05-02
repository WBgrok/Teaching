from  PIL import Image
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [12, 8]

im = Image.open("Tim.jpg")
# im.show()

width = im.width
height = im.height

out = Image.new("RGB", (width, height))

# min = [255, 255, 255]
# max = [0, 0, 0]
# for x in range(width):
#     for y in range(height):
#         pixel = im.getpixel((x, y))
#         for i in range(3):
#             if pixel[i] < min[i]:
#                 min[i] = pixel[i]
#             if pixel[i] > max[i]:
#                 max[i] = pixel[i]
# print(min)
# print(max)
offset = 10
for x in range(width - offset):
    for y in range(height - offset):
        p1 = im.getpixel((x, y))
        p2 = im.getpixel((x + offset, y))
        p3 = im. getpixel((x, y + offset))
        out.putpixel((x, y), (p1[0], p2[1], p3[2]))

out.show()
