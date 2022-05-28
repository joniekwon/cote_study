import sys
import string
input = sys.stdin.readline
upper = string.ascii_uppercase
lower = string.ascii_lowercase
strings = input().rstrip()
answer = ''
for s in strings:
    if s.isdigit() or s == ' ':
        answer += s
    elif s in set(upper):
        answer += upper[(ord(s) - 65 + 13) % 26]
    else:
        answer += lower[(ord(s) - 97 + 13) % 26]
print(answer)