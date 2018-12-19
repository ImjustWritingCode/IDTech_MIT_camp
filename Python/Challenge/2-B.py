import sys
string = input('Please input a word: ')
for x in range(0, len(string)):
    sys.stdout.write(string[x])
    sys.stdout.write('!')
