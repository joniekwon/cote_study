import sys
N = int(sys.stdin.readline())
q = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n==0:
        q.pop()
    else:
        q.append(n)
print(sum(q))
