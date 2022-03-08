import re
import sys
while True:
    s = sys.stdin.readline().rstrip('\n')
    if s=='.':
        break
    s = re.sub(r'[^()\[\]]','', s)
    d=['[]', '()']
    q = []
    for x in s:
        if len(q)<1:
            q.append(x)
        elif q[-1]+x in d:
            q.pop()
        else:
            q.append(x)
    print('no') if len(q)>0 else print('yes')