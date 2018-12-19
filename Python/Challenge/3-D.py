length = int(input('Please input the length: '))
width = int(input('Please input the width: '))
graph = input('Please input the character you want to output: ')
for x in range(0, width):
    for y in range(0, length):
        print(graph, end='')
    print('')
