length = int(input('Please input the length: '))
width = int(input('Please input the width: '))
graph = input('Please input the character you want to output: ')
for x in range(0, width):
    for y in range(0, length):
        if x==0 or x==width-1:
            print(graph, end='')
        elif y==0 or y==length-1:
            print(graph, end='')
        else:
            print(' ', end='')
    print('')
