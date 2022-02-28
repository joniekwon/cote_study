import sys
sys.stdin.readline()
nums = list(map(int, sys.stdin.readline().split()))
d= {x:i for i, x in enumerate(sorted(set(nums)))}
for i in nums:
    print(d[i], end=' ')