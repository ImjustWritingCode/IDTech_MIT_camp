print('Factor finding program\n')
num = int(input('Please input a number: '))
print('The factors of ', num, ' are: ', end='')
for x in range(1, num+1):
    if(not num%x):
        print(x, end=' ')
