import numpy as np
from PIL import Image
image = Image.open('mit_try.jpg')
image = image.convert('RGBA')
image.show()
arr = np.array(image)
image.close()
red, green, blue, alpha = arr.T
white_areas = (red >= 240) & (blue >= 240) & (green >= 240)
arr[..., :-1][white_areas.T] = (0, 0, 255)
img_1 = Image.fromarray(arr)
img_1.show()
img_1.close()
exit()
