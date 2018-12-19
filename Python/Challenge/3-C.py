length = int(input("Please input the length: "))
width = int(input("Please input the width: "))
for x in range(0, width):
    for y in range(0, length):
        print('*', end='')
    print('')
