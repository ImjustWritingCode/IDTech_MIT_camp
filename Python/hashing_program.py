print('Hashing function\n')
while 1:
    pwd = input('Please input your password: ')
    if (len(pwd)<2):
        print('Error! Password too short! Try again!')
        continue
    if (pwd == 'exit'):
        exit()
    abt = ord(pwd[1])
    val = (abt|len(pwd))
    print('The verification code of the password is: ', '{0:07b}'.format(val), '\n')

