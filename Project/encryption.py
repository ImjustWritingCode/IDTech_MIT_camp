import numpy as np
from PIL import Image
print('Image encryption program\n')
path = input('Please input the object png file: ')
if path == 'exit':#set quit value
    exit()
try:#open image
    image = Image.open(path)
except IOError:
    print('\nThe image filename is incorrect or couldn\'t loaded')
    print('The program is quitting, try again!')
    exit()
arr = np.array(image)
image.close()
code = input('\nPlease input your secret message: ')
bin_code = "{0:014b}".format(len(code))# 7 digit encrypting, first 14 digit is length
for x in range(0, len(code)):
    bin_code += "{0:07b}".format(ord(code[x]))
if len(bin_code) > 65535 or len(bin_code) > arr.size:#check if message is too long to encrypt
    print('Error! Message is too large to encrypt!')
    print('Try another message or picture!')
    print('Program is quitting...')
    exit()
fin = 0
cnt = 0
#change every LSB of the pixel into msg
for h in range(0, len(arr)):
    if fin == 1:#if encryption has finished, then quit the loop
        break
    for w in range(0, len(arr[h])):
        if fin == 1:
            break
        for a in range(0, len(arr[h][w])):
            if cnt == len(bin_code):
                fin = 1
                break
            if arr[h][w][a]%2 == 1 and bin_code[cnt] == '0':#change the binary of the LSB into msg
                arr[h][w][a] -= 1
            if arr[h][w][a]%2 == 0 and bin_code[cnt] == '1':
                arr[h][w][a] += 1
            cnt += 1
img_2 = Image.fromarray(arr)
print('Encryption finished!\n')
print('Please input the filename you want to save')
path = input('(WARNING: The file might overwrite if assigning to an existing file): ')
img_2.save(path)
img_2.close()
print('\nCongratulations! Job well done!')
