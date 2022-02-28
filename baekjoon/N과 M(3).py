import sys
from itertools import product

N, M = map(int,sys.stdin.readline().split())
nums = [x for x in range(1, N+1)]
for i, p in enumerate(product(nums, repeat=M)):
    print(' '.join(map(str, p)))