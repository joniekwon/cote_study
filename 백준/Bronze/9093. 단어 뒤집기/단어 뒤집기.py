import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = list(map(lambda x: x[::-1], input().split()))
    print(' '.join(s))