import string
str = input()
for s in str:
    if s.isupper():
        print(s.lower(), end='')
    else:
        print(s.upper(), end='')