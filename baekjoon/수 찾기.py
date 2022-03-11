import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
d = {x:1 for x in A}
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
for x in nums:
    try:
        print(d[x])
    except:
        print(0)