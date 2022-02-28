import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().split())
nums = [x for x in range(1, N+1)]
for i, c in enumerate(combinations(nums, M)):
    print(' '.join(map(str, c)))