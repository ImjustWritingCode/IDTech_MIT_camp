def encode (sen, codeword):
    for x in range(0, len(sen)):
        n = x % len(codeword)
        if codeword[n].isupper:
            minus = 65
        elif codeword[n].isalpha:
            minus = 97
        else:
            print('Error! Please input alphabet!')
            return None
        sft = ord(sen[x]) + ord(codeword[n]) - minus
        print(chr(sft), end = '')
    return None
def decode (sen, codeword):
    for x in range(0, len(sen)):
        n = x % len(codeword)
        if codeword[n].isupper:
            plus = 65
        elif codeword[n].isalpha:
            plus = 97
        else:
            print('Error! Please input alphabets!')
            return None
        sft = ord(sen[x]) - ord(codeword[n]) + plus
        print(chr(sft), end = '')
    return None
while 1:
    print('Vigenere cipher program\n')
    string = input('Please input the message you want to encrypt (type \"exit\" to exit): ')
    if string == 'exit':
        exit()
    flag = 0
    for x in range(0, len(string)):
        if not string.isalpha:
            flag = 1
    if flag == 1:
        print('Please input alphabets!\n')
        continue
    eord = input('Encode (e) or decode (d): ')
    code = input('Please insert the code: ')
    if eord == 'e' or eord == 'E':
        print('The cipher text of your message is: ', end = '')
        encode(string, code)
    elif eord == 'd' or eord == 'D':
        print('The message is actually: ', end = '')
        decode(string, code)
    else:
        print('Error!, repowering the program...\n')
    print('\n')
