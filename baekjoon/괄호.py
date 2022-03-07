import sys
T = int(sys.stdin.readline())
for _ in range(T):
    q = []
    s = sys.stdin.readline().strip()
    for c in s:
        if len(q)<1:
            q.append(c)
        elif q[-1]+c =='()':
            q.pop()
        else:
            q.append(c)
    print('NO') if len(q) else print('YES')
