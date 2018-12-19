import numpy as np
from PIL import Image
path = input('Please enter the filename: ')
try:
    image = Image.open(path)
except IOError:
    print('Load Error!')
    exit()
print('\n')
arr = np.array(image)
print('Shape of array is: ', arr.shape)
print('Item size is: ', arr.size)
#np.set_printoptions(threshold = np.nan)
#print(arr)
