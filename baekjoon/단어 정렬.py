import sys
N = int(sys.stdin.readline())
d = {}
for _ in range(N):
    key = sys.stdin.readline().strip()
    d[key] = len(key)

for i in sorted(d.items(), key=lambda x: (x[1],x[0])):
    k,v = i
    print(k)