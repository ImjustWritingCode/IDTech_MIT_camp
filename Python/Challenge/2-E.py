import sys
string = input("Please input any words or sentence(alphabets only): ")
for x in range(0, len(string)):
    if(string[x]!='a' and string[x]!='e' and string[x]!='i' and string[x]!='o' and string[x]!='u'):
        sys.stdout.write(string[x])
