import sys
string = input('Please input a word: ')
for x in range(0, len(string)):
    sys.stdout.write(string[x])
    if x != len(string)-1:
        sys.stdout.write('!')
