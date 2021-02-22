import os

import imglib

import matplotlib.pyplot as plt
import numpy as np

# FIRST TEST: JPEG
image = imglib.read("images/Space_187k.jpg")

for i in range(100):
    imglib.save("images/Space_187k_100.jpg", image)
    image = imglib.read("images/Space_187k_100.jpg")

initial = imglib.read("images/Space_187k.jpg")
processed = imglib.read("images/Space_187k_100.jpg")
first = np.hstack((initial, processed))

print(os.path.getsize("images/Space_187k.jpg"), os.path.getsize("images/Space_187k_100.jpg"))

plt.figure()
plt.imshow(first)
plt.axis("off")

first_comp = (initial - processed).astype(np.uint8)

plt.figure()
plt.imshow(first_comp)
plt.axis("off")

# END OF FIRST TEST: JPEG

# SECOND TEST: LUMINANCE

original_image = imglib.color_as_gray_scale(imglib.read("images/Space_187k.jpg"))
luminance_image = imglib.color_as_gray_scale(imglib.read("images/Space_187k.jpg"))

for i in range(100):
    luminance_image = imglib.color_as_gray_scale(luminance_image)

second = np.hstack((original_image, luminance_image))

plt.figure()
plt.imshow(second)
plt.axis("off")

third = original_image - luminance_image

plt.figure()
plt.imshow(third)
plt.axis("off")

# END OF SECOND TEST: LUMINANCE

plt.show()
