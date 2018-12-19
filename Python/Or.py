print('\"Or\" program\n')
str1 = input('Please input the first binary code: ')
str2 = input('Please input another binary code: ')
if len(str1) != len(str2):
    print('Error! The length of two binary code is not the same!')
    exit()
print('After doing or operation, the binary code is:')
for x in range(0, len(str1)):
    if str1[x]=='1' or str2[x] == '1':
        print('1', end='')
    else:
        print('0', end='')
