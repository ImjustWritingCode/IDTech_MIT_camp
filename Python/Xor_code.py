print('Xor cipher program\n')
pln = input('Please input the message you want to encrypt: ')
code = input('Enter the code: ')
for x in range(0, len(pln)):
    num1 = (int)pln[x]
    num2 = (int)code[x]
    pln[x] = (chr)(num1+num2)
print(pln)
