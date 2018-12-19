import numpy as np
from PIL import Image
print('Decryption program\n')
path = input('Please input the encrypted filename: ')
if path == 'exit':
    exit()
try:
    image = Image.open(path)
except IOError:
    print('\nThe image filename is incorrect or couldn\'t loaded')
    print('The program is quitting, try again!')
    exit()
arr = np.array(image)
image.close()
print('\nBelow is the secret message:\n')
cnt = 0#counting the binary code, if 7 then print the char
msg = 0#storing msg
lt_ct = 0#if it's first 14 of the bin code, store the length of the msg
length = 0
found_length = 0
#reading function: read every last digit of the image array
for h in range(0, len(arr)):
    if lt_ct == length + 2 and found_length:#if reaches the last char of the msg then quit
        break
    for w in range(0, len(arr[h])):
        if lt_ct == length + 2 and found_length:
            break
        for a in range(0, len(arr[h][w])):
            msg += (arr[h][w][a] % 2)
            if cnt == 6:
                if lt_ct == 0:
                    length = int(msg)
                elif lt_ct == 1:
                    length <<= 7
                    length += int(msg)
                    found_length = 1
                else:
                    print(chr(msg), end = '')
                if lt_ct == length + 2 and found_length:
                    break
                cnt = 0
                msg = 0
                lt_ct += 1
            else:
                msg <<= 1#left shift the msg by 1
                cnt += 1
exit()
