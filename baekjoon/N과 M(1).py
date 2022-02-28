import sys
from itertools import permutations

N, M = map(int,sys.stdin.readline().split())
nums = [x for x in range(1, N+1)]
for p in permutations(nums, M):
    print(' '.join(map(str, p)))
