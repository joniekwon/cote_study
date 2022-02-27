import sys
N = int(sys.stdin.readline())
nums = [0]*N
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    nums[i] = (a,b)
for i in sorted(nums, key=lambda x: (x[0], x[1])):
    a, b =i
    print(a, b)