import sys
from itertools import combinations
M = int(sys.stdin.readline().split()[1])
nums = list(map(int,sys.stdin.readline().split()))
c = list(map(sum, list(combinations(nums,3))))
min_diff = 100000
answer = -1
for i, s in enumerate(c):
    diff =  M - s
    if s <= M and diff < min_diff:
        min_diff = diff
        answer = i
print(c[answer])