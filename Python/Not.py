print('\"Not\" program\n')
string = input('Please input your binary code: ')
print('After doing not operating, the code becomes:')
for x in range(0, len(string)):
    if(string[x]=='0'):
        print('1', end='')
    else:
        print('0', end='')
