import sys
import string
input = sys.stdin.readline
upper = {i:x for i, x in zip(range(26), string.ascii_uppercase)}
lower = {i:x for i, x in zip(range(26), string.ascii_lowercase)}
strings = input().rstrip()
answer = ''
for s in strings:
    if s.isdigit() or s == ' ':
        answer += s
    elif s.isupper():
        answer += upper[(ord(s) - 65 + 13) % 26]
    else:
        answer += lower[(ord(s) - 97 + 13) % 26]
print(answer)