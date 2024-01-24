from PIL import Image

im = Image.open("image.jpg")
pixels = im.load()
x, y = im.size
color_sum = [0, 0, 0]

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        color_sum[0] += r
        color_sum[1] += g
        color_sum[2] += b

print(*[num // (x * y) for num in color_sum])